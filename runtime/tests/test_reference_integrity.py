"""Reference-integrity and validation tests."""

from runtime.validation import validate


def test_validation_passes(conn):
    report = validate(conn)
    assert report.ok, report.as_dict()["errors"]


def test_orphan_references_are_warnings_not_errors(conn):
    report = validate(conn)
    # Orphans (if any) are canonical-source findings reported as warnings.
    assert "orphan_references" not in report.errors
    orphans = report.warnings["orphan_references"]
    # File-path provenance pointers must never be counted as orphans.
    assert all("/" not in o["id"] for o in orphans)


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
