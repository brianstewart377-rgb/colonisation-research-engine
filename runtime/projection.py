"""Projection pipeline: read canonical inputs -> normalised in-memory records.

This stage is pure (no database writes). It reads the release export bundle
(``exports/*.csv`` + ``export_manifest.json``) plus the separately versioned
reference-source register, and produces ``ProjectionResult`` dataclasses that the
builder serialises into SQLite. Keeping projection pure makes it trivially
testable and guarantees the runtime is a deterministic function of its
explicitly declared canonical inputs: the release export bundle plus the
separately versioned source register.
"""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path

from . import config
from .config import TABLE_SPECS, TableSpec, extract_ids


def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    return value or None


def _read_csv(path: Path) -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


@dataclass
class ObjectRecord:
    object_id: str
    object_type: str
    title: str | None
    status: str | None
    source_ref: str | None
    origin: str  # which export/register first declared this identity


@dataclass
class Reference:
    from_id: str
    to_id: str
    relationship: str
    origin: str


@dataclass
class ProjectionResult:
    # objects keyed by id (first declaration wins; collisions tracked separately)
    objects: dict[str, ObjectRecord] = field(default_factory=dict)
    duplicate_identities: list[tuple[str, str, str]] = field(default_factory=list)
    # typed detail rows: table name -> list of row dicts (scalar columns only)
    detail: dict[str, list[dict]] = field(default_factory=dict)
    references: list[Reference] = field(default_factory=list)
    claim_provenance: list[dict] = field(default_factory=list)
    evidence_traceability: list[dict] = field(default_factory=list)
    graph_edges: list[dict] = field(default_factory=list)
    graph_conflicts: list[dict] = field(default_factory=list)
    provenance: list[dict] = field(default_factory=list)
    manifest: dict = field(default_factory=dict)
    source_fingerprint: str = ""
    source_register_path: Path | None = None

    def reference_endpoints(self) -> set[str]:
        ids: set[str] = set()
        for ref in self.references:
            ids.add(ref.from_id)
            ids.add(ref.to_id)
        for row in self.claim_provenance:
            ids.add(row["claim_id"])
            ids.add(row["source_entity"])
        for row in self.evidence_traceability:
            ids.add(row["evidence_id"])
            ids.add(row["mechanic_id"])
        for row in self.graph_edges:
            ids.add(row["source_id"])
            ids.add(row["target_id"])
        return ids


def _add_object(result: ProjectionResult, rec: ObjectRecord) -> None:
    existing = result.objects.get(rec.object_id)
    if existing is None:
        result.objects[rec.object_id] = rec
        return
    # Identity already declared. Only flag as a duplicate when two *typed* detail
    # sources claim the same id (graph_nodes / register backfill is expected).
    detail_origins = {s.export for s in TABLE_SPECS} | {"source_register"}
    if existing.origin in detail_origins and rec.origin in detail_origins:
        result.duplicate_identities.append((rec.object_id, existing.origin, rec.origin))


def _project_table(result: ProjectionResult, spec: TableSpec, rows: list[dict]) -> None:
    detail_rows: list[dict] = []
    for raw in rows:
        oid = _clean(raw.get(spec.id_col))
        if oid is None:
            continue
        detail_rows.append({col: _clean(raw.get(col)) for col in spec.columns})
        _add_object(
            result,
            ObjectRecord(
                object_id=oid,
                object_type=spec.object_type,
                title=_clean(raw.get(spec.title_col)),
                status=_clean(raw.get(spec.status_col)) if spec.status_col else None,
                source_ref=_clean(raw.get(spec.source_col)) if spec.source_col else None,
                origin=spec.export,
            ),
        )
        for csv_col, relationship in spec.refs.items():
            for target in extract_ids(raw.get(csv_col)):
                if target == oid:
                    continue
                result.references.append(
                    Reference(from_id=oid, to_id=target, relationship=relationship, origin=spec.export)
                )
    result.detail[spec.table] = detail_rows


def _project_graph_nodes(result: ProjectionResult, rows: list[dict]) -> None:
    """Backfill the identity registry and evidence/experiment detail tables."""

    evidence: list[dict] = []
    experiments: list[dict] = []
    detail_origins = {s.export for s in TABLE_SPECS} | {"source_register"}
    for raw in rows:
        nid = _clean(raw.get("node_id"))
        if nid is None:
            continue
        ntype = _clean(raw.get("node_type")) or "unknown_type"
        node_status = _clean(raw.get("status"))
        node_title = _clean(raw.get("title"))
        # If a typed canonical object already declared this identity, compare the
        # graph node's metadata against it and record any drift before the
        # authoritative typed value wins in the registry.
        existing = result.objects.get(nid)
        if existing is not None and existing.origin in detail_origins:
            if ntype != "unknown_type" and ntype != existing.object_type:
                result.graph_conflicts.append({
                    "object_id": nid, "field": "object_type",
                    "typed_value": existing.object_type, "graph_value": ntype,
                })
            if node_status and existing.status and node_status != existing.status:
                result.graph_conflicts.append({
                    "object_id": nid, "field": "status",
                    "typed_value": existing.status, "graph_value": node_status,
                })
        _add_object(
            result,
            ObjectRecord(
                object_id=nid,
                object_type=ntype,
                title=node_title,
                status=node_status,
                source_ref=_clean(raw.get("path_or_ref")) or _clean(raw.get("source_ref")),
                origin=config.GRAPH_NODES_EXPORT,
            ),
        )
        if ntype == "evidence":
            evidence.append({
                "evidence_id": nid,
                "title": _clean(raw.get("title")),
                "status": _clean(raw.get("status")),
                "category": _clean(raw.get("category")),
                "source_ref": _clean(raw.get("path_or_ref")),
            })
        elif ntype == "experiment":
            experiments.append({
                "experiment_id": nid,
                "title": _clean(raw.get("title")),
                "status": _clean(raw.get("status")),
                "category": _clean(raw.get("category")),
                "source_ref": _clean(raw.get("path_or_ref")),
            })
    result.detail["evidence"] = evidence
    result.detail["experiments"] = experiments


def _project_sources(result: ProjectionResult, rows: list[dict]) -> None:
    sources: list[dict] = []
    for raw in rows:
        sid = _clean(raw.get("source_id"))
        if sid is None:
            continue
        sources.append({
            "source_id": sid,
            "title": _clean(raw.get("title")),
            "type": _clean(raw.get("type")),
            "version": _clean(raw.get("version")),
            "source_tier": _clean(raw.get("source_tier")),
            "repo_path": _clean(raw.get("repo_path")),
            "status": _clean(raw.get("status")),
        })
        _add_object(
            result,
            ObjectRecord(
                object_id=sid,
                object_type="source",
                title=_clean(raw.get("title")),
                status=_clean(raw.get("status")),
                source_ref=_clean(raw.get("repo_path")),
                origin="source_register",
            ),
        )
    result.detail["sources"] = sources


def _fingerprint_inputs(paths: list[Path]) -> str:
    """Fingerprint inputs using stable repo-relative paths (not just basenames).

    Including the path means two distinct inputs that happen to share a basename
    can never collide, and the fingerprint is stable across checkouts.
    """

    def rel(path: Path) -> str:
        try:
            return path.resolve().relative_to(config.REPO_ROOT).as_posix()
        except ValueError:
            return path.name

    h = hashlib.sha256()
    for path in sorted(paths, key=rel):
        h.update(rel(path).encode())
        h.update(b"\x00")
        h.update(path.read_bytes())
        h.update(b"\x00")
    return h.hexdigest()


def project(exports_dir: Path, source_register_path: Path | None = None) -> ProjectionResult:
    exports_dir = Path(exports_dir)
    source_register_path = Path(source_register_path) if source_register_path else config.SOURCE_REGISTER
    result = ProjectionResult()
    result.source_register_path = source_register_path
    input_paths: list[Path] = []

    # Typed detail tables.
    for spec in TABLE_SPECS:
        path = exports_dir / spec.export
        input_paths.append(path)
        _project_table(result, spec, _read_csv(path))

    # Graph nodes: identity backfill + evidence/experiment detail.
    nodes_path = exports_dir / config.GRAPH_NODES_EXPORT
    input_paths.append(nodes_path)
    _project_graph_nodes(result, _read_csv(nodes_path))

    # Reference source register: a REQUIRED, separately versioned runtime input
    # (it is not part of the export bundle). It must never be silently skipped -
    # doing so would produce a different/incomplete runtime that still looks valid.
    if not source_register_path.is_file():
        raise FileNotFoundError(
            f"Required runtime input (source register) is missing or unreadable: {source_register_path}"
        )
    input_paths.append(source_register_path)
    _project_sources(result, _read_csv(source_register_path))

    # Verbatim relationship exports.
    for raw in _read_csv(exports_dir / config.CLAIM_PROVENANCE_EXPORT):
        result.claim_provenance.append({
            "claim_id": _clean(raw.get("claim_id")),
            "source_entity": _clean(raw.get("source_entity")),
            "relationship": _clean(raw.get("relationship")),
            "basis_note": _clean(raw.get("basis_note")),
        })
    input_paths.append(exports_dir / config.CLAIM_PROVENANCE_EXPORT)

    for raw in _read_csv(exports_dir / config.EVIDENCE_TRACEABILITY_EXPORT):
        result.evidence_traceability.append({
            "evidence_id": _clean(raw.get("evidence_id")),
            "mechanic_id": _clean(raw.get("mechanic_id")),
            "relationship": _clean(raw.get("relationship")),
            "strength": _clean(raw.get("strength")),
            "basis": _clean(raw.get("basis")),
            "notes": _clean(raw.get("notes")),
        })
    input_paths.append(exports_dir / config.EVIDENCE_TRACEABILITY_EXPORT)

    for raw in _read_csv(exports_dir / config.GRAPH_EDGES_EXPORT):
        result.graph_edges.append({
            "source_id": _clean(raw.get("source_id")),
            "relationship": _clean(raw.get("relationship")),
            "target_id": _clean(raw.get("target_id")),
            "basis": _clean(raw.get("basis")),
        })
    input_paths.append(exports_dir / config.GRAPH_EDGES_EXPORT)

    # Manifest + table-level provenance.
    manifest_path = exports_dir / config.MANIFEST_EXPORT
    result.manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    input_paths.append(manifest_path)
    spec_by_export = {s.export: s for s in TABLE_SPECS}
    for entry in result.manifest.get("exports", []):
        export_name = Path(entry["path"]).name
        spec = spec_by_export.get(export_name)
        object_type = spec.object_type if spec else Path(export_name).stem
        result.provenance.append({
            "object_type": object_type,
            "export_path": entry["path"],
            "source_register": entry.get("source", ""),
            "record_count": int(entry.get("record_count", 0)),
        })

    result.source_fingerprint = _fingerprint_inputs(input_paths)
    return result
