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


def test_mechanics_blocked_by_live_verification(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        blocked = rt.mechanics_blocked_by_live_verification()
        assert isinstance(blocked, list)
        assert len(blocked) >= 1
        assert all("mechanic_id" in b for b in blocked)


def test_contradictions_affecting_recommendation(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        contradictions = rt.contradictions_affecting("M-0005")
        assert any(c["contradiction_id"] == "C-0002" for c in contradictions)


def test_evidence_chain_structure(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        chain = rt.get_evidence_chain("CL-0001")
        assert chain["claim"]["claim_id"] == "CL-0001"
        assert len(chain["provenance"]) >= 1


def test_runtime_is_read_only(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        try:
            rt._conn.execute("DELETE FROM mechanics")
            assert False, "runtime must be read-only"
        except Exception:
            pass
