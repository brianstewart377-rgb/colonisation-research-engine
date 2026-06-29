#!/usr/bin/env python3
"""
Deterministically assemble the release-oriented export bundle from canonical
repository registers and source files.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "exports"


@dataclass(frozen=True)
class ExportSpec:
    output_name: str
    format: str
    source: str
    builder: Callable[[Path], int]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def require_file(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"Required source file is missing: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Required source path is not a file: {path}")
    return path


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(OrderedDict((name, row.get(name, "")) for name in fieldnames))
    return len(rows)


def copy_text_file(src: Path, dest: Path) -> int:
    require_file(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    if dest.suffix == ".csv":
        return count_csv_rows(dest)
    return 0


def count_csv_rows(path: Path) -> int:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return max(sum(1 for _ in csv.reader(f)) - 1, 0)


SECTION_HEADER_RE = re.compile(r"^## ([A-Z]{1,4}-\d{4}) - (.+)$")
FIELD_RE = re.compile(r"^- ([^:]+):\s*(.*)$")


def parse_sectioned_register(path: Path, required_fields: list[str]) -> list[dict[str, str]]:
    require_file(path)
    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        header_match = SECTION_HEADER_RE.match(raw_line)
        if header_match:
            if current is not None:
                finalize_section_record(path, current, required_fields)
                records.append(current)
            current = {
                "id": header_match.group(1),
                "title": header_match.group(2),
            }
            continue

        if current is None:
            continue

        field_match = FIELD_RE.match(raw_line)
        if field_match:
            key = normalize_field_name(field_match.group(1))
            current[key] = field_match.group(2).strip()

    if current is not None:
        finalize_section_record(path, current, required_fields)
        records.append(current)

    if not records:
        raise ValueError(f"No section records were parsed from {path}")

    return records


def finalize_section_record(path: Path, record: dict[str, str], required_fields: list[str]) -> None:
    missing = [field for field in required_fields if field not in record]
    if missing:
        raise ValueError(
            f"Missing required fields in {path} for section {record.get('id', '<unknown>')}: {', '.join(missing)}"
        )


def normalize_field_name(value: str) -> str:
    lowered = value.lower().strip()
    lowered = lowered.replace("/", " ")
    lowered = re.sub(r"[^a-z0-9]+", "_", lowered)
    return lowered.strip("_")


MECHANICS_TABLE_RE = re.compile(r"^\|\s*`(M-\d{4})`\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$")


def parse_mechanics_index(path: Path) -> list[dict[str, str]]:
    require_file(path)
    rows: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = MECHANICS_TABLE_RE.match(line)
        if not match:
            continue
        rows.append(
            {
                "mechanic_id": match.group(1),
                "title": match.group(2),
                "status": match.group(3),
                "primary_category": slugify(match.group(4)),
                "source_basis": match.group(5),
                "related_evidence": clean_backticks(match.group(6)),
                "related_experiments": clean_backticks(match.group(7)),
            }
        )
    if not rows:
        raise ValueError(f"No mechanics table rows were parsed from {path}")
    return rows


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def clean_backticks(value: str) -> str:
    return value.replace("`", "")


def split_reference_field(value: str) -> list[str]:
    cleaned = clean_backticks(value).strip()
    if not cleaned or cleaned.lower() == "none":
        return []
    parts = re.split(r"[;,]\s*|\s{2,}", cleaned)
    return [part.strip() for part in parts if part.strip()]


def extract_id_from_filename(path: Path, pattern: str) -> str | None:
    match = re.match(pattern, path.name)
    return match.group(1) if match else None


def load_known_ids() -> dict[str, set[str]]:
    evidence_ids = {
        extracted
        for path in (REPO_ROOT / "evidence").glob("EV-*.md")
        for extracted in [extract_id_from_filename(path, r"^(EV-\d{4})")]
        if extracted
    }
    experiment_ids = {
        extracted
        for path in (REPO_ROOT / "experiments").glob("EXP-*.md")
        for extracted in [extract_id_from_filename(path, r"^(EXP-\d{4})")]
        if extracted
    }
    mechanic_ids = {row["mechanic_id"] for row in parse_mechanics_index(REPO_ROOT / "mechanics" / "index.md")}
    planner_rule_ids = {row["id"] for row in parse_sectioned_register(REPO_ROOT / "planner" / "planner_rules_register.md", ["category", "status", "source", "related_mechanics", "rule", "planner_implication"])}

    claim_ids: set[str] = set()
    with open(REPO_ROOT / "evidence" / "claim_register.csv", "r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            claim_id = (row.get("claim_id") or "").strip()
            if claim_id:
                claim_ids.add(claim_id)

    return {
        "evidence": evidence_ids,
        "experiment": experiment_ids,
        "mechanic": mechanic_ids,
        "planner_rule": planner_rule_ids,
        "claim": claim_ids,
    }


def validate_reference_membership(record_id: str, field_name: str, refs: list[str], known_ids: set[str], path: Path) -> None:
    missing = [ref for ref in refs if ref not in known_ids]
    if missing:
        raise ValueError(
            f"Unknown references in {path} for {record_id} field {field_name}: {', '.join(missing)}"
        )


def validate_decision_sections(path: Path, sections: list[dict[str, str]]) -> None:
    allowed_status = {"Proposed", "Accepted", "Implemented", "Superseded", "Rejected"}
    allowed_confidence = {"High", "Medium", "Low"}
    allowed_review_status = {"Draft", "Analyst reviewed", "Governance confirmed", "Needs live review", "Superseded"}
    known = load_known_ids()
    decision_ids = {section["id"] for section in sections}

    for section in sections:
        decision_id = section["id"]
        status = section.get("status", "")
        if status not in allowed_status:
            raise ValueError(f"Invalid decision status in {path} for {decision_id}: {status}")

        date = section.get("date", "")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            raise ValueError(f"Invalid decision date in {path} for {decision_id}: {date}")

        confidence = section.get("confidence", "")
        if confidence not in allowed_confidence:
            raise ValueError(f"Invalid confidence in {path} for {decision_id}: {confidence}")

        review_status = section.get("review_status", "")
        if review_status not in allowed_review_status:
            raise ValueError(f"Invalid review status in {path} for {decision_id}: {review_status}")

        validate_reference_membership(
            decision_id,
            "evidence_references",
            split_reference_field(section.get("evidence_references", "")),
            known["evidence"],
            path,
        )
        validate_reference_membership(
            decision_id,
            "claim_references",
            split_reference_field(section.get("claim_references", "")),
            known["claim"],
            path,
        )
        validate_reference_membership(
            decision_id,
            "mechanic_references",
            split_reference_field(section.get("mechanic_references", "")),
            known["mechanic"],
            path,
        )
        validate_reference_membership(
            decision_id,
            "planner_rule_references",
            split_reference_field(section.get("planner_rule_references", "")),
            known["planner_rule"],
            path,
        )
        validate_reference_membership(
            decision_id,
            "experiment_references",
            split_reference_field(section.get("experiment_references", "")),
            known["experiment"],
            path,
        )
        validate_reference_membership(
            decision_id,
            "supersedes",
            split_reference_field(section.get("supersedes", "")),
            decision_ids,
            path,
        )
        validate_reference_membership(
            decision_id,
            "superseded_by",
            split_reference_field(section.get("superseded_by", "")),
            decision_ids,
            path,
        )


def build_mechanics_csv(output_dir: Path) -> int:
    rows = parse_mechanics_index(REPO_ROOT / "mechanics" / "index.md")
    return write_csv(
        output_dir / "mechanics.csv",
        [
            "mechanic_id",
            "title",
            "status",
            "primary_category",
            "source_basis",
            "related_evidence",
            "related_experiments",
        ],
        rows,
    )


def build_register_csv(
    output_dir: Path,
    source_path: Path,
    output_name: str,
    fieldnames: list[str],
    required_fields: list[str],
    value_map: dict[str, str],
) -> int:
    sections = parse_sectioned_register(source_path, required_fields)
    rows: list[dict[str, str]] = []
    for section in sections:
        row: dict[str, str] = {}
        for out_field in fieldnames:
            src_field = value_map.get(out_field, out_field)
            row[out_field] = section.get(src_field, "")
        rows.append(row)
    return write_csv(output_dir / output_name, fieldnames, rows)


def build_planner_rules_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "planner" / "planner_rules_register.md",
        output_name="planner_rules.csv",
        fieldnames=[
            "rule_id",
            "title",
            "status",
            "category",
            "rule",
            "related_mechanics",
            "planner_implications",
            "testing_status",
            "contradictions",
            "unknowns",
            "related_decisions",
            "source",
        ],
        required_fields=["category", "status", "source", "related_mechanics", "rule", "planner_implication"],
        value_map={
            "rule_id": "id",
            "planner_implications": "planner_implication",
            "source": "source",
        },
    )


def build_economy_rules_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "mechanics" / "economy_rules_register.md",
        output_name="economy_rules.csv",
        fieldnames=[
            "rule_id",
            "title",
            "status",
            "rule",
            "related_mechanics",
            "planner_implications",
            "testing_status",
            "contradictions",
            "unknowns",
            "source",
        ],
        required_fields=["status", "source", "rule", "related_mechanics", "planner_implications", "testing_status"],
        value_map={
            "rule_id": "id",
            "source": "source",
        },
    )


def build_construction_rules_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "mechanics" / "construction_rules_register.md",
        output_name="construction_rules.csv",
        fieldnames=[
            "rule_id",
            "title",
            "status",
            "rule",
            "related_mechanics",
            "planner_implications",
            "testing_status",
            "contradictions",
            "unknowns",
            "source",
        ],
        required_fields=["status", "source", "rule", "related_mechanics", "planner_implications", "testing_status"],
        value_map={
            "rule_id": "id",
            "source": "source",
        },
    )


def build_planner_risks_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "planner" / "planner_risk_register.md",
        output_name="planner_risks.csv",
        fieldnames=[
            "risk_id",
            "title",
            "severity",
            "failure_mode",
            "why_dangerous",
            "required_mitigation",
            "source",
        ],
        required_fields=["severity", "source", "failure_mode", "why_dangerous", "required_mitigation"],
        value_map={
            "risk_id": "id",
            "source": "source",
        },
    )


def build_governance_decisions_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "docs" / "governance_decision_register.md",
        output_name="governance_decisions.csv",
        fieldnames=[
            "decision_id",
            "title",
            "status",
            "decision_to_make",
            "why_it_matters",
            "related_unknowns",
            "related_risks",
            "blocking_impact",
            "source",
        ],
        required_fields=["status", "source", "decision_to_make", "why_it_matters", "blocking_impact"],
        value_map={
            "decision_id": "id",
            "source": "source",
            "related_unknowns": "related_unknowns",
            "related_risks": "related_risks",
        },
    )


def build_decisions_csv(output_dir: Path) -> int:
    source_path = REPO_ROOT / "docs" / "decision_register.md"
    required_fields = [
        "status",
        "date",
        "context",
        "problem_statement",
        "alternatives_considered",
        "decision",
        "rationale",
        "trade_offs",
        "consequences",
        "confidence",
        "review_status",
    ]
    sections = parse_sectioned_register(source_path, required_fields)
    validate_decision_sections(source_path, sections)
    rows: list[dict[str, str]] = []
    fieldnames = [
        "decision_id",
        "title",
        "status",
        "date",
        "context",
        "problem_statement",
        "alternatives_considered",
        "decision",
        "rationale",
        "trade_offs",
        "consequences",
        "evidence_references",
        "claim_references",
        "mechanic_references",
        "planner_rule_references",
        "experiment_references",
        "supersedes",
        "superseded_by",
        "confidence",
        "review_status",
    ]
    for section in sections:
        row = {field: section.get(field, "") for field in fieldnames}
        row["decision_id"] = section["id"]
        row["title"] = section["title"]
        rows.append(row)
    return write_csv(output_dir / "decisions.csv", fieldnames, rows)


def build_unknowns_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "docs" / "unknowns_register.md",
        output_name="unknowns.csv",
        fieldnames=[
            "unknown_id",
            "title",
            "category",
            "unknown_statement",
            "related_mechanics",
            "related_live_verification",
            "planner_implications",
            "source",
        ],
        required_fields=["category", "source", "unknown", "related_mechanics", "planner_implication"],
        value_map={
            "unknown_id": "id",
            "unknown_statement": "unknown",
            "planner_implications": "planner_implication",
            "source": "source",
        },
    )


def build_contradictions_csv(output_dir: Path) -> int:
    return build_register_csv(
        output_dir=output_dir,
        source_path=REPO_ROOT / "docs" / "contradiction_register.md",
        output_name="contradictions.csv",
        fieldnames=[
            "contradiction_id",
            "title",
            "category",
            "description",
            "confidence",
            "related_mechanics",
            "planner_implications",
            "testing_status",
            "unknowns",
            "source",
        ],
        required_fields=["category", "description", "source", "confidence", "planner_implications", "testing_status"],
        value_map={
            "contradiction_id": "id",
            "source": "source",
        },
    )


def copy_observations_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "evidence" / "observation_register.csv"
    return copy_text_file(src, output_dir / "observations.csv")


def copy_claims_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "evidence" / "claim_register.csv"
    return copy_text_file(src, output_dir / "claims.csv")


def copy_claim_provenance_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "evidence" / "claim_provenance_links.csv"
    return copy_text_file(src, output_dir / "claim_provenance_links.csv")


def copy_evidence_traceability_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "evidence" / "evidence_mechanic_traceability.csv"
    return copy_text_file(src, output_dir / "evidence_traceability.csv")


def copy_live_verification_matrix_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "experiments" / "live_verification_matrix.csv"
    return copy_text_file(src, output_dir / "live_verification_matrix.csv")


def copy_graph_nodes_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "ontology" / "knowledge_graph_nodes.csv"
    return copy_text_file(src, output_dir / "graph_nodes.csv")


def copy_graph_edges_csv(output_dir: Path) -> int:
    src = REPO_ROOT / "ontology" / "knowledge_graph_edges.csv"
    return copy_text_file(src, output_dir / "graph_edges.csv")


EXPORT_SPECS: list[ExportSpec] = [
    ExportSpec("mechanics.csv", "csv", "mechanics/index.md", build_mechanics_csv),
    ExportSpec("planner_rules.csv", "csv", "planner/planner_rules_register.md", build_planner_rules_csv),
    ExportSpec("economy_rules.csv", "csv", "mechanics/economy_rules_register.md", build_economy_rules_csv),
    ExportSpec("construction_rules.csv", "csv", "mechanics/construction_rules_register.md", build_construction_rules_csv),
    ExportSpec("planner_risks.csv", "csv", "planner/planner_risk_register.md", build_planner_risks_csv),
    ExportSpec("decisions.csv", "csv", "docs/decision_register.md", build_decisions_csv),
    ExportSpec("governance_decisions.csv", "csv", "docs/governance_decision_register.md", build_governance_decisions_csv),
    ExportSpec("unknowns.csv", "csv", "docs/unknowns_register.md", build_unknowns_csv),
    ExportSpec("contradictions.csv", "csv", "docs/contradiction_register.md", build_contradictions_csv),
    ExportSpec("observations.csv", "csv", "evidence/observation_register.csv", copy_observations_csv),
    ExportSpec("claims.csv", "csv", "evidence/claim_register.csv", copy_claims_csv),
    ExportSpec("claim_provenance_links.csv", "csv", "evidence/claim_provenance_links.csv", copy_claim_provenance_csv),
    ExportSpec("evidence_traceability.csv", "csv", "evidence/evidence_mechanic_traceability.csv", copy_evidence_traceability_csv),
    ExportSpec("live_verification_matrix.csv", "csv", "experiments/live_verification_matrix.csv", copy_live_verification_matrix_csv),
    ExportSpec("graph_nodes.csv", "csv", "ontology/knowledge_graph_nodes.csv", copy_graph_nodes_csv),
    ExportSpec("graph_edges.csv", "csv", "ontology/knowledge_graph_edges.csv", copy_graph_edges_csv),
]


def assemble_exports(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    exports: list[dict[str, object]] = []
    for spec in EXPORT_SPECS:
        source_path = REPO_ROOT / spec.source
        require_file(source_path)
        record_count = spec.builder(output_dir)
        exports.append(
            OrderedDict(
                [
                    ("path", str(Path(output_dir.name) / spec.output_name) if output_dir == DEFAULT_OUTPUT else spec.output_name),
                    ("format", spec.format),
                    ("source", spec.source),
                    ("record_count", record_count),
                ]
            )
        )
        print(f"built {spec.output_name} ({record_count} rows)")

    manifest = OrderedDict(
        [
            ("export_manifest_version", "0.2.0-draft"),
            ("generated_at", utc_now_iso()),
            ("status", "assembled"),
            ("purpose", "Deterministically assembled release-oriented exports derived from canonical repository registers."),
            ("exports", exports),
            (
                "notes",
                [
                    "This manifest is generated by tools/build_release_bundle.py.",
                    "Canonical source-of-truth files remain the repository registers and indexes.",
                ],
            ),
        ]
    )

    manifest_path = output_dir / "export_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    print(f"wrote {manifest_path}")
    return manifest


def validate_exports(output_dir: Path) -> None:
    manifest_path = output_dir / "export_manifest.json"
    require_file(manifest_path)
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    if "exports" not in manifest or not isinstance(manifest["exports"], list):
        raise ValueError(f"Manifest missing exports list: {manifest_path}")

    for spec, item in zip(EXPORT_SPECS, manifest["exports"], strict=True):
        expected_path = output_dir / spec.output_name
        if not expected_path.exists():
            raise FileNotFoundError(f"Expected assembled output is missing: {expected_path}")
        if item["source"] != spec.source:
            raise ValueError(f"Manifest source mismatch for {spec.output_name}: {item['source']} != {spec.source}")
        if item["format"] != spec.format:
            raise ValueError(f"Manifest format mismatch for {spec.output_name}: {item['format']} != {spec.format}")
        if spec.format == "csv":
            actual_count = count_csv_rows(expected_path)
            if actual_count != item["record_count"]:
                raise ValueError(
                    f"Row count mismatch for {spec.output_name}: manifest={item['record_count']} actual={actual_count}"
                )
            print(f"validated {spec.output_name} ({actual_count} rows)")

    print("OK bundle validation")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Assemble the deterministic release-oriented export bundle.")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output directory for assembled exports. Defaults to the repository exports/ directory.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate an existing assembled export bundle instead of rebuilding it.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output).resolve()
    if args.validate_only:
        validate_exports(output_dir)
        return 0

    assemble_exports(output_dir)
    validate_exports(output_dir)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # fail loudly and clearly
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
