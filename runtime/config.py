"""Static configuration for the CRE runtime projection.

This module describes *what* canonical exports exist and *how* their columns map
onto the runtime schema. It intentionally contains no business logic: the runtime
must never duplicate planner reasoning, it only projects repository knowledge.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

SCHEMA_VERSION = "0.1.0"

# Repository layout. The runtime package lives at <repo>/runtime, so the
# canonical exports directory is a sibling of the package parent.
REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPORTS_DIR = REPO_ROOT / "exports"
DEFAULT_OUTPUT_DB = Path(__file__).resolve().parent / "cre_runtime.db"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"

# Canonical identity pattern: 1-4 uppercase letters, a dash, then 3-4 digits.
# Examples: M-0007, CL-0042, PR-0003, OBS-0001, EXP-0000, MG-0001.
IDENTITY_RE = re.compile(r"\b([A-Z]{1,4}-\d{3,4})\b")

# Prefix -> canonical object type. Used for identity-format validation and to
# classify graph-only nodes that have no dedicated detail table.
PREFIX_TO_TYPE = {
    "M": "mechanic",
    "PR": "planner_rule",
    "ER": "economy_rule",
    "CR": "construction_rule",
    "R": "planner_risk",
    "D": "decision",
    "GD": "governance_decision",
    "U": "unknown",
    "C": "contradiction",
    "OBS": "observation",
    "CL": "claim",
    "EV": "evidence",
    "EXP": "experiment",
    "LV": "live_verification",
    # Graph-only / supporting node families (no detail table in v0).
    "AC": "asset_category",
    "AP": "architecture_pattern",
    "CD": "coverage_dimension",
    "CS": "contextual_strategy",
    "G": "glossary",
    "IB": "implementation_backlog",
    "KP": "knowledge_projection_rule",
    "MD": "mechanic_dependency",
    "MRG": "manual_research_gap",
    "OBJ": "objective",
    "RL": "role",
    "RS": "recommendation_field",
    # Reference-source families.
    "DD": "source",
    "DM": "source",
    "FW": "source",
    "MG": "source",
}


@dataclass(frozen=True)
class TableSpec:
    """Maps a single canonical export CSV onto a typed runtime table."""

    table: str
    export: str
    id_col: str
    object_type: str
    columns: list[str]  # scalar csv columns persisted verbatim (includes id_col)
    title_col: str
    status_col: str | None = None
    source_col: str | None = None
    refs: dict[str, str] = field(default_factory=dict)  # csv_col -> relationship


# Order matters only for readability; objects are always inserted before detail
# rows by the builder regardless of this ordering.
TABLE_SPECS: list[TableSpec] = [
    TableSpec(
        table="mechanics",
        export="mechanics.csv",
        id_col="mechanic_id",
        object_type="mechanic",
        columns=["mechanic_id", "title", "status", "primary_category", "source_basis"],
        title_col="title",
        status_col="status",
        source_col="source_basis",
        refs={"related_evidence": "references_evidence", "related_experiments": "references_experiment"},
    ),
    TableSpec(
        table="planner_rules",
        export="planner_rules.csv",
        id_col="rule_id",
        object_type="planner_rule",
        columns=["rule_id", "title", "status", "category", "rule", "planner_implications", "testing_status", "source"],
        title_col="title",
        status_col="status",
        source_col="source",
        refs={
            "related_mechanics": "depends_on_mechanic",
            "contradictions": "has_contradiction",
            "unknowns": "has_unknown",
            "related_decisions": "related_decision",
        },
    ),
    TableSpec(
        table="economy_rules",
        export="economy_rules.csv",
        id_col="rule_id",
        object_type="economy_rule",
        columns=["rule_id", "title", "status", "rule", "planner_implications", "testing_status", "source"],
        title_col="title",
        status_col="status",
        source_col="source",
        refs={
            "related_mechanics": "depends_on_mechanic",
            "contradictions": "has_contradiction",
            "unknowns": "has_unknown",
        },
    ),
    TableSpec(
        table="construction_rules",
        export="construction_rules.csv",
        id_col="rule_id",
        object_type="construction_rule",
        columns=["rule_id", "title", "status", "rule", "planner_implications", "testing_status", "source"],
        title_col="title",
        status_col="status",
        source_col="source",
        refs={
            "related_mechanics": "depends_on_mechanic",
            "contradictions": "has_contradiction",
            "unknowns": "has_unknown",
        },
    ),
    TableSpec(
        table="planner_risks",
        export="planner_risks.csv",
        id_col="risk_id",
        object_type="planner_risk",
        columns=["risk_id", "title", "severity", "failure_mode", "why_dangerous", "required_mitigation", "source"],
        title_col="title",
        status_col=None,
        source_col="source",
        refs={"source": "references_source"},
    ),
    TableSpec(
        table="decisions",
        export="decisions.csv",
        id_col="decision_id",
        object_type="decision",
        columns=[
            "decision_id", "title", "status", "date", "context", "problem_statement",
            "decision", "rationale", "trade_offs", "consequences", "confidence", "review_status",
        ],
        title_col="title",
        status_col="status",
        refs={
            "mechanic_references": "references_mechanic",
            "planner_rule_references": "references_rule",
            "evidence_references": "references_evidence",
            "claim_references": "references_claim",
            "experiment_references": "references_experiment",
            "supersedes": "supersedes",
            "superseded_by": "superseded_by",
        },
    ),
    TableSpec(
        table="governance_decisions",
        export="governance_decisions.csv",
        id_col="decision_id",
        object_type="governance_decision",
        columns=["decision_id", "title", "status", "decision_to_make", "why_it_matters", "blocking_impact", "source"],
        title_col="title",
        status_col="status",
        source_col="source",
        refs={"related_unknowns": "related_unknown", "related_risks": "related_risk"},
    ),
    TableSpec(
        table="unknowns",
        export="unknowns.csv",
        id_col="unknown_id",
        object_type="unknown",
        columns=["unknown_id", "title", "category", "unknown_statement", "planner_implications", "source"],
        title_col="title",
        status_col=None,
        source_col="source",
        refs={"related_mechanics": "about_mechanic", "related_live_verification": "verified_by"},
    ),
    TableSpec(
        table="contradictions",
        export="contradictions.csv",
        id_col="contradiction_id",
        object_type="contradiction",
        columns=["contradiction_id", "title", "category", "description", "confidence", "planner_implications", "testing_status", "source"],
        title_col="title",
        status_col=None,
        source_col="source",
        refs={"related_mechanics": "affects_mechanic", "unknowns": "related_unknown"},
    ),
    TableSpec(
        table="observations",
        export="observations.csv",
        id_col="observation_id",
        object_type="observation",
        columns=["observation_id", "source_id", "context", "observation_type", "statement", "confidence", "planner_relevance"],
        title_col="statement",
        status_col=None,
        refs={"source_id": "observed_in", "related_mechanics": "supports_mechanic"},
    ),
    TableSpec(
        table="claims",
        export="claims.csv",
        id_col="claim_id",
        object_type="claim",
        columns=[
            "claim_id", "claim_type", "status", "confidence", "title", "claim_text",
            "primary_basis", "source_document", "page_or_sheet", "section_heading",
            "category", "evidence_type", "planner_implication", "needs_live_verification",
        ],
        title_col="title",
        status_col="status",
        source_col="source_document",
        refs={
            "linked_mechanics": "supports_mechanic",
            "linked_contradictions": "relates_contradiction",
            "linked_unknowns": "relates_unknown",
            "primary_basis": "derived_from",
        },
    ),
    TableSpec(
        table="live_verifications",
        export="live_verification_matrix.csv",
        id_col="verification_id",
        object_type="live_verification",
        columns=["verification_id", "title", "primary_target", "method_type", "required_state", "primary_observations", "success_condition"],
        title_col="title",
        status_col=None,
        refs={"linked_mechanics": "verifies_mechanic"},
    ),
]

# Explicit relationship exports loaded verbatim (already normalised at source).
GRAPH_NODES_EXPORT = "graph_nodes.csv"
GRAPH_EDGES_EXPORT = "graph_edges.csv"
CLAIM_PROVENANCE_EXPORT = "claim_provenance_links.csv"
EVIDENCE_TRACEABILITY_EXPORT = "evidence_traceability.csv"
MANIFEST_EXPORT = "export_manifest.json"

# The reference-source register is a canonical input that is *not* part of the
# release export bundle. It is therefore declared as an explicit, separately
# versioned runtime input: its stable repo-relative path and a content
# fingerprint are recorded in runtime_meta (see build_runtime), so the runtime's
# input surface is fully documented rather than implicitly "exports only".
SOURCE_REGISTER_REL = "reference_sources/source_register.csv"
SOURCE_REGISTER = REPO_ROOT / SOURCE_REGISTER_REL

# Provenance model per object family.
#   * scalar:     provenance is a canonical source pointer on the object itself
#                 (objects.source_ref); a missing pointer is a warning.
#   * structured: provenance is expressed through typed reference edges (e.g. a
#                 decision references the mechanics/claims/evidence it rests on);
#                 these objects legitimately have no scalar source_ref.
SCALAR_PROVENANCE_TYPES = {"mechanic", "claim", "planner_rule"}
STRUCTURED_PROVENANCE_TYPES = {"decision"}
STRUCTURED_PROVENANCE_RELATIONSHIPS = (
    "references_mechanic", "references_rule", "references_evidence",
    "references_claim", "references_experiment",
)


def prefix_of(object_id: str | None) -> str | None:
    """Return the identity family prefix of a canonical id (e.g. ``M-0007`` -> ``M``)."""

    if not object_id or "-" not in object_id:
        return None
    return object_id.split("-", 1)[0]


def type_for_id(object_id: str | None) -> str | None:
    """Return the object type implied by an id's family prefix, if known."""

    return PREFIX_TO_TYPE.get(prefix_of(object_id))

# Every table that carries projected data (used for the content fingerprint).
DATA_TABLES = [
    "objects", "provenance",
    "mechanics", "planner_rules", "economy_rules", "construction_rules",
    "planner_risks", "decisions", "governance_decisions", "unknowns",
    "contradictions", "observations", "claims", "live_verifications",
    "evidence", "experiments", "sources",
    "object_references", "claim_provenance_links", "evidence_traceability", "graph_edges",
    "graph_node_conflicts",
]


def extract_ids(text: str | None) -> list[str]:
    """Deterministically extract canonical identities from any cell value.

    Handles backticked, comma-separated, semicolon-separated and prose forms
    (e.g. ``"`M-0002`, `M-0007`"`` or ``"OBS-0001; EXP-0000"``). Sentinels such
    as ``None`` / ``None currently recorded`` yield no identities.
    """

    if not text:
        return []
    seen: list[str] = []
    for match in IDENTITY_RE.findall(text):
        if match not in seen:
            seen.append(match)
    return seen
