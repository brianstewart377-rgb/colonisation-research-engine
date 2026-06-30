"""Automated runtime validation.

Runs entirely against a built SQLite runtime database (read-only) so it can be
used both inside the builder and as a standalone audit of any generated runtime.

Checks:
  * orphan references      - relationship endpoints with no entry in `objects`
  * duplicate identities   - an id declared by more than one typed detail table
  * broken provenance      - claims with no provenance chain / missing source_ref
  * missing required objects - required object types / counts absent
  * invalid foreign keys   - SQLite foreign_key_check violations
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field

from .config import IDENTITY_RE, TABLE_SPECS

# Detail tables and their primary-key column, used for duplicate-id detection
# and manifest count reconciliation.
DETAIL_PK = {spec.table: spec.id_col for spec in TABLE_SPECS}

REQUIRED_MECHANICS = [f"M-{n:04d}" for n in range(1, 14)]  # M-0001 .. M-0013
REQUIRED_TYPES = [
    "mechanic", "planner_rule", "decision", "claim", "contradiction", "unknown",
]


@dataclass
class ValidationReport:
    errors: dict[str, list] = field(default_factory=dict)
    warnings: dict[str, list] = field(default_factory=dict)
    stats: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not any(self.errors.values())

    def as_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errors": {k: v for k, v in self.errors.items() if v},
            "warnings": {k: v for k, v in self.warnings.items() if v},
            "stats": self.stats,
        }


def _orphan_references(conn: sqlite3.Connection) -> list[dict]:
    """Identity-shaped relationship endpoints with no entry in `objects`.

    Provenance pointers that are document paths or prose (e.g.
    ``docs/source_coverage_register.md``) are valid and intentionally excluded;
    only canonical-id-shaped endpoints are eligible to be orphans.
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
            continue  # document-path / prose provenance is not an orphan
        entry = seen.setdefault(oid, {"id": oid, "kinds": set()})
        entry["kinds"].add(kind)
    return [{"id": e["id"], "kinds": sorted(e["kinds"])} for e in sorted(seen.values(), key=lambda x: x["id"])]


def _duplicate_identities(conn: sqlite3.Connection) -> list[dict]:
    selects = [f"SELECT {pk} AS oid, '{t}' AS tbl FROM {t}" for t, pk in DETAIL_PK.items()]
    union = " UNION ALL ".join(selects)
    sql = f"""
        SELECT oid, GROUP_CONCAT(tbl) FROM ({union})
        GROUP BY oid HAVING COUNT(*) > 1
    """
    return [{"id": oid, "tables": tbls.split(",")} for oid, tbls in conn.execute(sql)]


def _broken_provenance(conn: sqlite3.Connection) -> tuple[list, list]:
    errors: list[dict] = []
    warnings: list[dict] = []
    # Claims must retain a provenance chain.
    rows = conn.execute(
        """
        SELECT c.claim_id FROM claims c
        LEFT JOIN claim_provenance_links p ON p.claim_id = c.claim_id
        WHERE p.id IS NULL ORDER BY c.claim_id
        """
    ).fetchall()
    errors.extend({"claim_id": r[0], "issue": "no_provenance_link"} for r in rows)
    # Provenance-bearing objects should carry a canonical source reference.
    rows = conn.execute(
        """
        SELECT object_id, object_type FROM objects
        WHERE object_type IN ('mechanic','claim','decision','planner_rule')
          AND (source_ref IS NULL OR source_ref = '')
        ORDER BY object_id
        """
    ).fetchall()
    warnings.extend({"object_id": r[0], "object_type": r[1], "issue": "missing_source_ref"} for r in rows)
    return errors, warnings


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
    # Reconcile manifest-declared counts with actually projected detail rows.
    for spec in TABLE_SPECS:
        row = conn.execute(
            "SELECT record_count FROM provenance WHERE object_type = ?", (spec.object_type,)
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


def validate(conn: sqlite3.Connection) -> ValidationReport:
    report = ValidationReport()

    orphans = _orphan_references(conn)
    duplicates = _duplicate_identities(conn)
    prov_errors, prov_warnings = _broken_provenance(conn)
    missing = _missing_required(conn)
    bad_fks = _invalid_foreign_keys(conn)

    report.errors = {
        "duplicate_identities": duplicates,
        "broken_provenance": prov_errors,
        "missing_required_objects": missing,
        "invalid_foreign_keys": bad_fks,
    }
    # Orphan references reflect the state of the canonical source (e.g. an id
    # referenced by an edge but not yet defined). They are reported but do not
    # fail the build, since the runtime is a faithful projection, not the source.
    report.warnings = {
        "orphan_references": orphans,
        "provenance_warnings": prov_warnings,
    }

    report.stats = {
        "objects": conn.execute("SELECT COUNT(*) FROM objects").fetchone()[0],
        "object_references": conn.execute("SELECT COUNT(*) FROM object_references").fetchone()[0],
        "graph_edges": conn.execute("SELECT COUNT(*) FROM graph_edges").fetchone()[0],
        "claim_provenance_links": conn.execute("SELECT COUNT(*) FROM claim_provenance_links").fetchone()[0],
        "orphan_references": len(orphans),
        "duplicate_identities": len(duplicates),
        "broken_provenance": len(prov_errors),
        "missing_required_objects": len(missing),
        "invalid_foreign_keys": len(bad_fks),
    }
    return report
