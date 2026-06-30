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


def test_explain_unknown_claim_returns_none(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        assert rt.explain_claim("CL-9999") is None


def test_explain_claim_cl0010_returns_non_empty_bundle(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None
        assert bundle["claim"]["claim_id"] == "CL-0010"
        assert bundle["provenance"]
        assert bundle["trace"]["nodes"]
        assert bundle["trace"]["edges"]


def test_explain_claim_cl0010_statement_matches_canonical_fields(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None

        claim = bundle["claim"]
        statement = bundle["claim_statement"]
        assert set(statement) == {
            "claim_text",
            "status",
            "confidence",
            "claim_type",
            "category",
            "planner_implication",
            "needs_live_verification",
        }
        for key in statement:
            assert statement[key] == claim[key]


def test_explain_claim_cl0010_surfaces_mechanics_unknowns_and_contradictions(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None

        assert "M-0007" in _ids(bundle["linked_mechanics"], "mechanic_id")
        assert {"U-0003", "U-0004"}.issubset(_ids(bundle["linked_unknowns"], "unknown_id"))
        assert "C-0002" in _ids(bundle["linked_contradictions"], "contradiction_id")


def test_explain_claim_cl0010_supporting_evidence_contains_only_evidence_rows(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None

        supporting_evidence = bundle["supporting_evidence"]
        assert supporting_evidence
        for entry in supporting_evidence:
            evidence = entry["evidence"]
            assert evidence["evidence_id"].startswith("EV-")
            assert entry["provenance_relationships"] == sorted(
                entry["provenance_relationships"],
                key=lambda r: (
                    r.get("relationship") or "",
                    r.get("source_entity") or "",
                    r.get("basis_note") or "",
                ),
            )


def test_explain_claim_provenance_keeps_experiments_separate_from_supporting_evidence(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0011")
        assert bundle is not None

        evidence_ids = {entry["evidence"]["evidence_id"] for entry in bundle["supporting_evidence"]}
        assert "EXP-0001" not in evidence_ids
        assert "EXP-0001" in _ids(bundle["related_experiments"], "experiment_id")


def test_explain_claim_cl0010_surfaces_related_decisions(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None

        assert "D-0003" in _ids(bundle["related_decisions"], "decision_id")


def test_explain_claim_trace_edges_reference_existing_nodes(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None

        node_ids = {node["id"] for node in bundle["trace"]["nodes"]}
        for edge in bundle["trace"]["edges"]:
            assert edge["from_id"] in node_ids
            assert edge["to_id"] in node_ids
            assert edge["relationship"]
            assert edge["origin"]


def test_explain_claim_trace_nodes_include_registry_status(runtime_db):
    db_path, _ = runtime_db
    with Runtime(db_path) as rt:
        bundle = rt.explain_claim("CL-0010")
        assert bundle is not None

        nodes = bundle["trace"]["nodes"]
        by_id = {node["id"]: node for node in nodes}
        assert by_id["CL-0010"]["registry_status"] == "registered"
        for node in nodes:
            assert node["registry_status"] in {"registered", "missing_from_registry"}
            if node["registry_status"] == "missing_from_registry":
                assert set(node) == {"id", "registry_status"}


def test_explain_claim_is_deterministic_and_read_only(runtime_db):
    db_path, _ = runtime_db
    before = sha256(db_path.read_bytes()).hexdigest()
    with Runtime(db_path) as rt:
        first = rt.explain_claim("CL-0010")
        second = rt.explain_claim("CL-0010")
        assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
    after = sha256(db_path.read_bytes()).hexdigest()
    assert before == after
