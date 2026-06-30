"""Schema-stage tests."""

EXPECTED_TABLES = {
    "runtime_meta", "provenance", "objects",
    "mechanics", "planner_rules", "economy_rules", "construction_rules",
    "planner_risks", "decisions", "governance_decisions", "unknowns",
    "contradictions", "observations", "claims", "live_verifications",
    "evidence", "experiments", "sources",
    "object_references", "claim_provenance_links", "evidence_traceability", "graph_edges",
}


def test_all_expected_tables_exist(conn):
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    names = {r[0] for r in rows}
    assert EXPECTED_TABLES.issubset(names)


def test_indexes_present(conn):
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='index'").fetchall()
    names = {r[0] for r in rows}
    assert "idx_objref_to" in names
    assert "idx_cpl_claim" in names
    assert "idx_ge_target" in names


def test_runtime_meta_populated(conn):
    meta = {k: v for k, v in conn.execute("SELECT key, value FROM runtime_meta")}
    assert meta["schema_version"] == "0.1.0"
    assert len(meta["content_fingerprint"]) == 64
    assert len(meta["source_fingerprint"]) == 64
    assert int(meta["object_count"]) > 0


def test_provenance_table_records_sources(conn):
    rows = conn.execute("SELECT object_type, source_register, record_count FROM provenance").fetchall()
    by_type = {r[0]: (r[1], r[2]) for r in rows}
    assert by_type["mechanic"][0] == "mechanics/index.md"
    assert by_type["claim"][1] == 343


def test_objects_are_typed(conn):
    (untyped,) = conn.execute("SELECT COUNT(*) FROM objects WHERE object_type IS NULL OR object_type = ''").fetchone()
    assert untyped == 0
