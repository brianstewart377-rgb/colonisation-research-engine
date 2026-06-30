"""Runtime-generation and query-layer tests."""

from runtime.queries import Runtime


def test_build_produces_nonempty_db(runtime_db):
    db_path, report = runtime_db
    assert db_path.exists()
    assert report["db_size_bytes"] > 0
    assert report["validation"]["ok"]


def test_retrieve_single_objects(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        assert rt.get_mechanic("M-0007")["mechanic_id"] == "M-0007"
        assert rt.get_planner_rule("PR-0003")["rule_id"] == "PR-0003"
        assert rt.get_decision("D-0001")["decision_id"] == "D-0001"
        assert rt.get_contradiction("C-0002")["contradiction_id"] == "C-0002"
        assert rt.get_unknown("U-0001")["unknown_id"] == "U-0001"


def test_planner_rules_depending_on_mechanic(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        rules = rt.planner_rules_depending_on("M-0007")
        assert any(r["rule_id"] == "PR-0003" for r in rules)


def test_evidence_supporting_claim(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        chain = rt.evidence_supporting_claim("CL-0042")
        assert len(chain) >= 1
        assert all(c["source_entity"] for c in chain)


def test_decisions_referencing_mechanic(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        decisions = rt.decisions_referencing("M-0010")
        assert any(d["decision_id"] == "D-0001" for d in decisions)


def test_mechanics_pending_live_verification(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        pending = rt.mechanics_pending_live_verification()
        assert isinstance(pending, list)
        assert len(pending) >= 1
        assert all("mechanic_id" in b for b in pending)
        assert all("pending_verification_sources" in b for b in pending)


def test_contradictions_direct_mechanic(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        rows = rt.contradictions_affecting("M-0005")
        direct = [r for r in rows if r["link_path"] == "direct_mechanic"]
        assert any(r["contradiction_id"] == "C-0002" for r in direct)


def test_contradictions_direct_rule(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        rows = rt.contradictions_affecting("ER-0002")
        direct_rule = [r for r in rows if r["link_path"] == "direct_rule"]
        assert any(r["contradiction_id"] == "C-0002" for r in direct_rule)


def test_contradictions_indirect_rule_to_mechanic(runtime_db):
    # PR-0003 depends on M-0007; C-0002 affects M-0007. PR-0003 records no direct
    # contradiction, so this contradiction must be reached via the indirect path.
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        rows = rt.contradictions_affecting("PR-0003")
        indirect = [r for r in rows if r["link_path"] == "indirect_rule"]
        assert any(r["contradiction_id"] == "C-0002" for r in indirect)
        assert not any(r["link_path"] == "direct_rule" for r in rows)


def test_contradictions_no_false_positives(runtime_db):
    # M-0001 is affected by no contradiction and is not a rule, so the traversal
    # must return nothing rather than spuriously matching.
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        assert rt.contradictions_affecting("M-0001") == []


def test_evidence_chain_structure(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        chain = rt.get_evidence_chain("CL-0001")
        assert chain["claim"]["claim_id"] == "CL-0001"
        assert len(chain["provenance"]) >= 1


def test_runtime_is_read_only(runtime_db):
    import sqlite3

    import pytest

    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        before = rt.get_mechanic("M-0001")
        # A read-only connection must reject any write with OperationalError.
        with pytest.raises(sqlite3.OperationalError):
            rt._conn.execute("DELETE FROM mechanics")

    # Re-open a fresh read-only connection and confirm the data is unchanged.
    with Runtime(db_path) as rt2:
        assert rt2.get_mechanic("M-0001") == before
        count = rt2._conn.execute("SELECT COUNT(*) AS n FROM mechanics").fetchone()["n"]
        assert count == 13
