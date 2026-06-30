"""Automated runtime validation.

Runs entirely against a built SQLite runtime database (read-only) so it can be
used both inside the builder and as a standalone audit of any generated runtime.

The report distinguishes four classes of finding:

  errors    - structural integrity failures (the build is not trustworthy)
  warnings  - canonical-source findings the runtime faithfully mirrors
              (orphan ids, missing scalar source refs, unresolved provenance
              gaps, graph/typed metadata drift)
  info      - expected, healthy conditions worth making explicit
              (objects that correctly use structured provenance)
  stats     - counts

Checks:
  * identity integrity     - id family / prefix / object-type agreement
  * duplicate identities   - an id declared by more than one typed detail table
  * orphan references      - id-shaped relationship endpoints absent from objects
  * provenance model       - claims chain (error) + scalar/structured provenance
  * missing required objects - required object types / counts absent
  * invalid foreign keys   - SQLite foreign_key_check violations
  * graph metadata drift   - graph node vs typed object metadata conflicts
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field

from .config import (
    IDENTITY_RE,
    PREFIX_TO_TYPE,
    SCALAR_PROVENANCE_TYPES,
    STRUCTURED_PROVENANCE_RELATIONSHIPS,
    STRUCTURED_PROVENANCE_TYPES,
    TABLE_SPECS,
    prefix_of,
)

# Detail tables and their primary-key column, used for duplicate-id detection.
DETAIL_PK = {spec.table: spec.id_col for spec in TABLE_SPECS}

# Typed table -> (pk column, expected object type). Includes the graph-derived
# detail tables so every typed family is covered by identity integrity.
TYPED_TABLE_TYPES = {spec.table: (spec.id_col, spec.object_type) for spec in TABLE_SPECS}
TYPED_TABLE_TYPES["evidence"] = ("evidence_id", "evidence")
TYPED_TABLE_TYPES["experiments"] = ("experiment_id", "experiment")
TYPED_TABLE_TYPES["sources"] = ("source_id", "source")

REQUIRED_MECHANICS = [f"M-{n:04d}" for n in range(1, 14)]  # M-0001 .. M-0013
REQUIRED_TYPES = ["mechanic", "planner_rule", "decision", "claim", "contradiction", "unknown"]


@dataclass
class ValidationReport:
    errors: dict[str, list] = field(default_factory=dict)
    warnings: dict[str, list] = field(default_factory=dict)
    info: dict[str, list] = field(default_factory=dict)
    stats: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not any(self.errors.values())

    def as_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errors": {k: v for k, v in self.errors.items() if v},
            "warnings": {k: v for k, v in self.warnings.items() if v},
            "info": {k: v for k, v in self.info.items() if v},
            "stats": self.stats,
        }


def check_identity_integrity(conn: sqlite3.Connection) -> tuple[list, list]:
    """Enforce canonical identity family / type integrity.

    Returns (errors, warnings). Errors cover invalid ids, cross-family ids in a
    typed table, and objects whose stored type disagrees with their id prefix.
    """

    errors: list[dict] = []
    warnings: list[dict] = []

    for table, (pk, expected_type) in sorted(TYPED_TABLE_TYPES.items()):
        for (oid,) in conn.execute(f"SELECT {pk} FROM {table} ORDER BY {pk}"):
            if not oid or not IDENTITY_RE.fullmatch(oid):
                errors.append({"table": table, "id": oid, "issue": "invalid_canonical_id"})
                continue
            implied = PREFIX_TO_TYPE.get(prefix_of(oid))
            if implied is None:
                errors.append({"table": table, "id": oid, "issue": "unknown_identity_family", "prefix": prefix_of(oid)})
            elif implied != expected_type:
                errors.append({
                    "table": table, "id": oid, "issue": "cross_family_id",
                    "table_expects": expected_type, "prefix_implies": implied,
                })

    for oid, otype in conn.execute("SELECT object_id, object_type FROM objects ORDER BY object_id"):
        if not oid or not IDENTITY_RE.fullmatch(oid):
            errors.append({"object_id": oid, "issue": "invalid_canonical_id_in_objects"})
            continue
        implied = PREFIX_TO_TYPE.get(prefix_of(oid))
        if implied is None:
            warnings.append({"object_id": oid, "issue": "unknown_identity_family", "prefix": prefix_of(oid)})
        elif otype != implied:
            errors.append({
                "object_id": oid, "object_type": otype, "prefix_implies": implied,
                "issue": "object_type_mismatch",
            })
    return errors, warnings


def _orphan_references(conn: sqlite3.Connection) -> list[dict]:
    """Identity-shaped relationship endpoints with no entry in `objects`.

    Document-path / prose provenance pointers are valid and intentionally
    excluded; only canonical-id-shaped endpoints are eligible to be orphans.
    """

    sql = """
        SELECT id, kind FROM (
            SELECT from_id AS id, 'object_reference.from' AS kind FROM object_references
            UNION ALL SELECT to_id, 'object_reference.to' FROM object_references
            UNION ALL SELECT claim_id, 'claim_provenance.claim' FROM claim_provenance_links
            UNION ALL SELECT source_entity, 'claim_provenance.source' FROM claim_provenance_links
            UNION ALL SELECT evidence_id, 'evidence_traceability.evidence' FROM evidence_traceability
            UNION ALL SELECT mechanic_id, 'evidence_traceability.mechanic' FROM evidence_traceability
            UNION ALL SELECT source_id, 'graph_edge.source' FROM graph_edges
            UNION ALL SELECT target_id, 'graph_edge.target' FROM graph_edges
        )
        WHERE id NOT IN (SELECT object_id FROM objects)
    """
    seen: dict[str, dict] = {}
    for oid, kind in conn.execute(sql):
        if not oid or not IDENTITY_RE.fullmatch(oid):
            continue
        entry = seen.setdefault(oid, {"id": oid, "kinds": set()})
        entry["kinds"].add(kind)
    return [{"id": e["id"], "kinds": sorted(e["kinds"])} for e in sorted(seen.values(), key=lambda x: x["id"])]


def _duplicate_identities(conn: sqlite3.Connection) -> list[dict]:
    selects = [f"SELECT {pk} AS oid, '{t}' AS tbl FROM {t}" for t, pk in DETAIL_PK.items()]
    union = " UNION ALL ".join(selects)
    sql = f"SELECT oid, GROUP_CONCAT(tbl) FROM ({union}) GROUP BY oid HAVING COUNT(*) > 1"
    return [{"id": oid, "tables": tbls.split(",")} for oid, tbls in conn.execute(sql)]


def _provenance_model(conn: sqlite3.Connection) -> dict:
    """Validate provenance per the documented model (scalar vs structured)."""

    out = {
        "broken_provenance": [],               # error: claim with no provenance chain
        "missing_source_ref": [],              # warning: scalar type lacking source_ref
        "structured_provenance_objects": [],   # info: objects using structured provenance
        "unresolved_provenance_gaps": [],      # warning: structured type with no refs
    }

    rows = conn.execute(
        """
        SELECT c.claim_id FROM claims c
        LEFT JOIN claim_provenance_links p ON p.claim_id = c.claim_id
        WHERE p.id IS NULL ORDER BY c.claim_id
        """
    ).fetchall()
    out["broken_provenance"] = [{"claim_id": r[0], "issue": "no_provenance_link"} for r in rows]

    if SCALAR_PROVENANCE_TYPES:
        placeholders = ",".join("?" for _ in SCALAR_PROVENANCE_TYPES)
        rows = conn.execute(
            f"""
            SELECT object_id, object_type FROM objects
            WHERE object_type IN ({placeholders})
              AND (source_ref IS NULL OR source_ref = '')
            ORDER BY object_id
            """,
            tuple(sorted(SCALAR_PROVENANCE_TYPES)),
        ).fetchall()
        out["missing_source_ref"] = [
            {"object_id": r[0], "object_type": r[1], "issue": "missing_source_ref"} for r in rows
        ]

    rel_placeholders = ",".join("?" for _ in STRUCTURED_PROVENANCE_RELATIONSHIPS)
    for otype in sorted(STRUCTURED_PROVENANCE_TYPES):
        for (oid,) in conn.execute(
            "SELECT object_id FROM objects WHERE object_type = ? ORDER BY object_id", (otype,)
        ):
            (count,) = conn.execute(
                f"""
                SELECT COUNT(*) FROM object_references
                WHERE from_id = ? AND relationship IN ({rel_placeholders})
                """,
                (oid, *STRUCTURED_PROVENANCE_RELATIONSHIPS),
            ).fetchone()
            if count > 0:
                out["structured_provenance_objects"].append(
                    {"object_id": oid, "object_type": otype, "structured_refs": count}
                )
            else:
                out["unresolved_provenance_gaps"].append(
                    {"object_id": oid, "object_type": otype, "issue": "no_structured_provenance"}
                )
    return out


def _missing_required(conn: sqlite3.Connection) -> list[dict]:
    missing: list[dict] = []
    present = {r[0] for r in conn.execute("SELECT object_id FROM objects")}
    for mid in REQUIRED_MECHANICS:
        if mid not in present:
            missing.append({"id": mid, "issue": "required_mechanic_absent"})
    for otype in REQUIRED_TYPES:
        (count,) = conn.execute("SELECT COUNT(*) FROM objects WHERE object_type = ?", (otype,)).fetchone()
        if count == 0:
            missing.append({"object_type": otype, "issue": "required_type_empty"})
    # Reconcile manifest-declared counts (keyed by export path) with projected rows.
    for spec in TABLE_SPECS:
        row = conn.execute(
            "SELECT record_count FROM provenance WHERE export_path = ?", (f"exports/{spec.export}",)
        ).fetchone()
        if row is None:
            continue
        (actual,) = conn.execute(f"SELECT COUNT(*) FROM {spec.table}").fetchone()
        if actual != row[0]:
            missing.append({
                "table": spec.table, "issue": "manifest_count_mismatch",
                "expected": row[0], "actual": actual,
            })
    return missing


def _invalid_foreign_keys(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute("PRAGMA foreign_key_check").fetchall()
    return [{"table": r[0], "rowid": r[1], "parent": r[2], "fkid": r[3]} for r in rows]


def _graph_metadata_conflicts(conn: sqlite3.Connection) -> list[dict]:
    rows = conn.execute(
        "SELECT object_id, field, typed_value, graph_value FROM graph_node_conflicts ORDER BY object_id, field"
    ).fetchall()
    return [{"object_id": r[0], "field": r[1], "typed_value": r[2], "graph_value": r[3]} for r in rows]


def validate(conn: sqlite3.Connection) -> ValidationReport:
    report = ValidationReport()

    id_errors, id_warnings = check_identity_integrity(conn)
    duplicates = _duplicate_identities(conn)
    orphans = _orphan_references(conn)
    prov = _provenance_model(conn)
    missing = _missing_required(conn)
    bad_fks = _invalid_foreign_keys(conn)
    conflicts = _graph_metadata_conflicts(conn)

    report.errors = {
        "identity_integrity": id_errors,
        "duplicate_identities": duplicates,
        "broken_provenance": prov["broken_provenance"],
        "missing_required_objects": missing,
        "invalid_foreign_keys": bad_fks,
    }
    report.warnings = {
        "canonical_source_orphans": orphans,
        "missing_source_ref": prov["missing_source_ref"],
        "unresolved_provenance_gaps": prov["unresolved_provenance_gaps"],
        "identity_family_warnings": id_warnings,
        "graph_metadata_conflicts": conflicts,
    }
    report.info = {
        "structured_provenance_objects": prov["structured_provenance_objects"],
    }

    report.stats = {
        "objects": conn.execute("SELECT COUNT(*) FROM objects").fetchone()[0],
        "object_references": conn.execute("SELECT COUNT(*) FROM object_references").fetchone()[0],
        "graph_edges": conn.execute("SELECT COUNT(*) FROM graph_edges").fetchone()[0],
        "claim_provenance_links": conn.execute("SELECT COUNT(*) FROM claim_provenance_links").fetchone()[0],
        "identity_integrity_errors": len(id_errors),
        "duplicate_identities": len(duplicates),
        "canonical_source_orphans": len(orphans),
        "missing_source_ref": len(prov["missing_source_ref"]),
        "structured_provenance_objects": len(prov["structured_provenance_objects"]),
        "unresolved_provenance_gaps": len(prov["unresolved_provenance_gaps"]),
        "broken_provenance": len(prov["broken_provenance"]),
        "missing_required_objects": len(missing),
        "invalid_foreign_keys": len(bad_fks),
        "graph_metadata_conflicts": len(conflicts),
    }
    return report
