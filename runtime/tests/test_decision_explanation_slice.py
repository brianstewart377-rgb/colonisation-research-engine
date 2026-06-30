import json
import shutil
import sqlite3
from hashlib import sha256
from pathlib import Path

from runtime.queries import Runtime


def _ids(rows: list[dict], key: str) -> set[str]:
    out = set()
    for r in rows:
        v = r.get(key)
        if v:
            out.add(v)
    return out


def test_explain_unknown_decision_returns_none(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        assert rt.explain_decision("D-DOES-NOT-EXIST") is None


def test_explain_decision_d0003_has_required_direct_references(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_decision("D-0003")
        assert bundle is not None

        refs = bundle["direct_references"]
        assert "EV-0003" in _ids(refs["evidence"], "evidence_id")
        assert {"CL-0009", "CL-0010"}.issubset(_ids(refs["claims"], "claim_id"))
        assert {"M-0005", "M-0007"}.issubset(_ids(refs["mechanics"], "mechanic_id"))
        assert "PR-0003" in _ids(refs["planner_rules"], "rule_id")


def test_explain_decision_d0003_planner_rule_payload_is_full_row(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_decision("D-0003")
        assert bundle is not None

        rules = bundle["direct_references"]["planner_rules"]
        pr = next(r for r in rules if r["rule_id"] == "PR-0003")
        assert set(pr) >= {
            "rule_id",
            "title",
            "status",
            "category",
            "rule",
            "planner_implications",
            "testing_status",
            "source",
        }


def test_explain_decision_d0003_surfaces_guardrails_via_mechanics(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_decision("D-0003")
        assert bundle is not None

        mech_ctx = bundle["mechanic_context"]
        contradiction_ids = set()
        unknown_ids = set()
        lv_ids = set()
        for entry in mech_ctx:
            for c in entry.get("contradictions", []):
                if c.get("contradiction_id"):
                    contradiction_ids.add(c["contradiction_id"])
            for u in entry.get("unknowns", []):
                if u.get("unknown_id"):
                    unknown_ids.add(u["unknown_id"])
            for lv in entry.get("live_verifications", []):
                if lv.get("verification_id"):
                    lv_ids.add(lv["verification_id"])

        assert "C-0002" in contradiction_ids
        assert {"U-0003", "U-0004"}.issubset(unknown_ids)
        assert "LV-0002" in lv_ids


def test_explain_decision_trace_edges_reference_existing_nodes(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_decision("D-0003")
        assert bundle is not None

        trace = bundle["trace"]
        node_ids = {n["id"] for n in trace["nodes"]}
        assert "D-0003" in node_ids

        for e in trace["edges"]:
            assert e["from_id"] in node_ids
            assert e["to_id"] in node_ids
            assert e["relationship"]
            assert e["origin"]


def test_explain_decision_trace_nodes_include_registry_status(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_decision("D-0003")
        assert bundle is not None

        nodes = bundle["trace"]["nodes"]
        by_id = {n["id"]: n for n in nodes}
        assert by_id["D-0003"]["registry_status"] == "registered"

    mutated_path = Path(str(db_path) + ".missing-node-copy")
    shutil.copyfile(db_path, mutated_path)
    try:
        conn = sqlite3.connect(mutated_path)
        conn.execute(
            """
            INSERT INTO object_references (from_id, to_id, relationship, origin)
            VALUES (?, ?, ?, ?)
            """,
            ("D-0003", "ZZ-9999", "references_rule", "test_injected_missing_endpoint"),
        )
        conn.commit()
        conn.close()

        with Runtime(mutated_path) as rt:
            bundle = rt.explain_decision("D-0003")
            assert bundle is not None

            nodes = bundle["trace"]["nodes"]
            by_id = {n["id"]: n for n in nodes}
            assert by_id["ZZ-9999"]["registry_status"] == "missing_from_registry"
            assert set(by_id["ZZ-9999"]) == {"id", "registry_status"}
    finally:
        if mutated_path.exists():
            mutated_path.unlink()


def test_explain_decision_d0003_boundary_matches_decision_fields_exactly(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_decision("D-0003")
        assert bundle is not None

        expected_keys = {
            "decision",
            "rationale",
            "trade_offs",
            "consequences",
            "confidence",
            "review_status",
        }
        boundary = bundle["decision_boundary"]
        decision = bundle["decision"]

        assert set(boundary) == expected_keys
        for key in sorted(expected_keys):
            assert boundary[key] == decision[key]
        assert "conclusion" not in boundary
        assert "generated_conclusion" not in boundary


def test_explain_decision_is_deterministic_and_read_only(runtime_db):
    db_path, _ = runtime_db
    before = sha256(db_path.read_bytes()).hexdigest()
    with Runtime(db_path) as rt:
        a = rt.explain_decision("D-0003")
        b = rt.explain_decision("D-0003")
        assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    after = sha256(db_path.read_bytes()).hexdigest()
    assert before == after
