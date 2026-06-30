import json
from hashlib import sha256

from runtime.queries import Runtime


def _ids(rows: list[dict], key: str) -> set[str]:
    out = set()
    for row in rows:
        value = row.get(key)
        if value:
            out.add(value)
    return out


def test_explain_unknown_mechanic_returns_none(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        assert rt.explain_mechanic("M-9999") is None


def test_explain_mechanic_m0007_returns_non_empty_bundle(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_mechanic("M-0007")
        assert bundle is not None
        assert bundle["mechanic"]["mechanic_id"] == "M-0007"
        assert bundle["supporting_claims"]
        assert bundle["direct_evidence"]
        assert bundle["trace"]["nodes"]
        assert bundle["trace"]["edges"]


def test_explain_mechanic_m0007_surfaces_linked_claims(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_mechanic("M-0007")
        assert bundle is not None

        claim_ids = _ids([entry["claim"] for entry in bundle["supporting_claims"]], "claim_id")
        assert {"CL-0002", "CL-0006", "CL-0010", "CL-0011"}.issubset(claim_ids)


def test_explain_mechanic_m0007_surfaces_unknowns_contradictions_and_verifications(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_mechanic("M-0007")
        assert bundle is not None

        guardrails = bundle["guardrails"]
        assert {"U-0001", "U-0003"}.issubset(_ids(guardrails["unknowns"], "unknown_id"))
        assert "C-0002" in _ids(guardrails["contradictions"], "contradiction_id")
        assert {"LV-0001", "LV-0002"}.issubset(
            _ids(guardrails["live_verifications"], "verification_id")
        )


def test_explain_mechanic_m0007_surfaces_rule_decisions_and_experiments(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_mechanic("M-0007")
        assert bundle is not None

        assert "PR-0003" in _ids(bundle["dependent_planner_rules"], "rule_id")
        assert {"D-0002", "D-0003"}.issubset(_ids(bundle["related_decisions"], "decision_id"))
        assert "EXP-0001" in _ids(bundle["related_experiments"], "experiment_id")


def test_explain_mechanic_trace_edges_reference_existing_nodes(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_mechanic("M-0007")
        assert bundle is not None

        node_ids = {node["id"] for node in bundle["trace"]["nodes"]}
        for edge in bundle["trace"]["edges"]:
            assert edge["from_id"] in node_ids
            assert edge["to_id"] in node_ids
            assert edge["relationship"]
            assert edge["origin"]


def test_explain_mechanic_trace_nodes_include_registry_status(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_mechanic("M-0007")
        assert bundle is not None

        nodes = bundle["trace"]["nodes"]
        by_id = {node["id"]: node for node in nodes}
        assert by_id["M-0007"]["registry_status"] == "registered"
        for node in nodes:
            assert node["registry_status"] in {"registered", "missing_from_registry"}
            if node["registry_status"] == "missing_from_registry":
                assert set(node) == {"id", "registry_status"}


def test_explain_mechanic_is_deterministic_and_read_only(runtime_db):
    db_path, _ = runtime_db
    before = sha256(db_path.read_bytes()).hexdigest()
    with Runtime(db_path) as rt:
        first = rt.explain_mechanic("M-0007")
        second = rt.explain_mechanic("M-0007")
        assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
    after = sha256(db_path.read_bytes()).hexdigest()
    assert before == after

