"""Reference-integrity and validation tests."""

from runtime.validation import validate


def test_validation_passes(conn):
    report = validate(conn)
    assert report.ok, report.as_dict()["errors"]


def test_orphan_references_are_warnings_not_errors(conn):
    report = validate(conn)
    # Orphans (if any) are canonical-source findings reported as warnings.
    assert "canonical_source_orphans" not in report.errors
    orphans = report.warnings["canonical_source_orphans"]
    # File-path provenance pointers must never be counted as orphans.
    assert all("/" not in o["id"] for o in orphans)


def test_decisions_use_structured_provenance(conn):
    report = validate(conn)
    structured = report.info["structured_provenance_objects"]
    decision_ids = {s["object_id"] for s in structured if s["object_type"] == "decision"}
    # All five decisions derive provenance through structured references.
    assert {"D-0001", "D-0002", "D-0003", "D-0004", "D-0005"}.issubset(decision_ids)
    # Decisions must not be flagged as missing a scalar source_ref.
    assert all(w["object_type"] != "decision" for w in report.warnings["missing_source_ref"])
    # And there are no unresolved provenance gaps.
    assert report.warnings["unresolved_provenance_gaps"] == []


def test_graph_metadata_conflicts_are_reported(conn):
    report = validate(conn)
    # Status drift between graph nodes and typed objects is surfaced (not lost).
    conflicts = report.warnings["graph_metadata_conflicts"]
    assert all({"object_id", "field", "typed_value", "graph_value"} <= set(c) for c in conflicts)


def test_no_duplicate_identities(conn):
    report = validate(conn)
    assert report.stats["duplicate_identities"] == 0


def test_no_invalid_foreign_keys(conn):
    assert conn.execute("PRAGMA foreign_key_check").fetchall() == []


def test_every_claim_has_provenance(conn):
    rows = conn.execute(
        """
        SELECT c.claim_id FROM claims c
        LEFT JOIN claim_provenance_links p ON p.claim_id = c.claim_id
        WHERE p.id IS NULL
        """
    ).fetchall()
    assert rows == []


def test_detail_rows_resolve_to_objects(conn):
    # Every mechanic / claim / decision detail row must exist in the registry.
    for table, pk in (("mechanics", "mechanic_id"), ("claims", "claim_id"), ("decisions", "decision_id")):
        (missing,) = conn.execute(
            f"SELECT COUNT(*) FROM {table} t WHERE t.{pk} NOT IN (SELECT object_id FROM objects)"
        ).fetchone()
        assert missing == 0
