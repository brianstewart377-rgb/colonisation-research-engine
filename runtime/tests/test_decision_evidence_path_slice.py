import json
import shutil
import sqlite3
from hashlib import sha256
from pathlib import Path

from runtime.queries import Runtime


def _ids(rows: list[dict], key: str) -> set[str]:
    out = set()
    for row in rows:
        value = row.get(key)
        if value:
            out.add(value)
    return out


def test_decision_evidence_path_unknown_decision_returns_none(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        assert rt.decision_evidence_path("D-9999") is None


def test_decision_evidence_path_d0003_returns_non_empty_bundle(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None
        assert bundle["decision"]["decision_id"] == "D-0003"
        assert bundle["direct_claim_paths"]
        assert bundle["direct_mechanic_paths"]
        assert bundle["trace"]["nodes"]
        assert bundle["trace"]["edges"]


def test_decision_evidence_path_d0003_direct_claim_ids_match_direct_references(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None

        expected = {
            edge["to_id"]
            for edge in bundle["trace"]["edges"]
            if edge["from_id"] == "D-0003" and edge["relationship"] == "references_claim"
        }
        actual = {entry["decision_reference"]["to_id"] for entry in bundle["direct_claim_paths"]}
        assert actual == expected
        assert {"CL-0009", "CL-0010"}.issubset(actual)


def test_decision_evidence_path_d0003_direct_mechanic_ids_match_direct_references(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None

        expected = {
            edge["to_id"]
            for edge in bundle["trace"]["edges"]
            if edge["from_id"] == "D-0003" and edge["relationship"] == "references_mechanic"
        }
        actual = {entry["decision_reference"]["to_id"] for entry in bundle["direct_mechanic_paths"]}
        assert actual == expected
        assert {"M-0005", "M-0007"}.issubset(actual)


def test_decision_evidence_path_registered_claim_paths_equal_claim_explanations(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None

        for entry in bundle["direct_claim_paths"]:
            target_id = entry["decision_reference"]["to_id"]
            if entry["target"]["registry_status"] == "registered":
                assert entry["claim_explanation"] == rt.explain_claim(target_id)
            else:
                assert entry["claim_explanation"] is None


def test_decision_evidence_path_registered_mechanic_paths_equal_mechanic_explanations(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None

        for entry in bundle["direct_mechanic_paths"]:
            target_id = entry["decision_reference"]["to_id"]
            if entry["target"]["registry_status"] == "registered":
                assert entry["mechanic_explanation"] == rt.explain_mechanic(target_id)
            else:
                assert entry["mechanic_explanation"] is None


def test_decision_evidence_path_does_not_promote_indirect_claim_mechanics(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None

        direct_mechanic_ids = {entry["decision_reference"]["to_id"] for entry in bundle["direct_mechanic_paths"]}
        claim_linked_mechanics = set()
        for entry in bundle["direct_claim_paths"]:
            claim_explanation = entry["claim_explanation"]
            if claim_explanation is None:
                continue
            claim_linked_mechanics.update(_ids(claim_explanation["linked_mechanics"], "mechanic_id"))

        indirect_only = claim_linked_mechanics - direct_mechanic_ids
        assert "M-0007" not in indirect_only
        assert direct_mechanic_ids == {"M-0005", "M-0007"}


def test_decision_evidence_path_paths_reference_trace_edges_and_targets(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.decision_evidence_path("D-0003")
        assert bundle is not None

        trace_edges = {
            (edge["from_id"], edge["to_id"], edge["relationship"], edge["origin"])
            for edge in bundle["trace"]["edges"]
        }
        nodes_by_id = {node["id"]: node for node in bundle["trace"]["nodes"]}

        for entry in bundle["direct_claim_paths"]:
            ref = entry["decision_reference"]
            assert (ref["from_id"], ref["to_id"], ref["relationship"], ref["origin"]) in trace_edges
            assert entry["target"] == nodes_by_id[ref["to_id"]]

        for entry in bundle["direct_mechanic_paths"]:
            ref = entry["decision_reference"]
            assert (ref["from_id"], ref["to_id"], ref["relationship"], ref["origin"]) in trace_edges
            assert entry["target"] == nodes_by_id[ref["to_id"]]


def test_decision_evidence_path_preserves_missing_direct_claim_references(runtime_db):
    db_path, _ = runtime_db
    mutated_path = Path(str(db_path) + ".missing-direct-claim-copy")
    shutil.copyfile(db_path, mutated_path)
    try:
        conn = sqlite3.connect(mutated_path)
        conn.execute(
            """
            INSERT INTO object_references (from_id, to_id, relationship, origin)
            VALUES (?, ?, ?, ?)
            """,
            ("D-0003", "CL-9999", "references_claim", "test_missing_direct_claim"),
        )
        conn.commit()
        conn.close()

        with Runtime(mutated_path) as rt:
            bundle = rt.decision_evidence_path("D-0003")
            assert bundle is not None

            by_id = {entry["decision_reference"]["to_id"]: entry for entry in bundle["direct_claim_paths"]}
            assert {"CL-0009", "CL-0010"}.issubset(set(by_id))
            assert "CL-9999" in by_id
            assert by_id["CL-9999"]["target"] == {"id": "CL-9999", "registry_status": "missing_from_registry"}
            assert by_id["CL-9999"]["target"]["registry_status"] == "missing_from_registry"
            assert by_id["CL-9999"]["claim_explanation"] is None
    finally:
        if mutated_path.exists():
            mutated_path.unlink()


def test_decision_evidence_path_is_deterministic_and_read_only(runtime_db):
    db_path, _ = runtime_db
    before = sha256(db_path.read_bytes()).hexdigest()
    with Runtime(db_path) as rt:
        first = rt.decision_evidence_path("D-0003")
        second = rt.decision_evidence_path("D-0003")
        assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
    after = sha256(db_path.read_bytes()).hexdigest()
    assert before == after
