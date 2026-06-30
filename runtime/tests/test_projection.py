"""Projection-stage tests (pure, no database)."""

from runtime.config import extract_ids


def test_extract_ids_handles_backticks_and_separators():
    assert extract_ids("`M-0002`, `M-0007`") == ["M-0002", "M-0007"]
    assert extract_ids("OBS-0001; EXP-0000") == ["OBS-0001", "EXP-0000"]
    assert extract_ids("M-0007; M-0008") == ["M-0007", "M-0008"]


def test_extract_ids_ignores_sentinels_and_prose():
    assert extract_ids("None") == []
    assert extract_ids("None currently recorded") == []
    assert extract_ids("contextual rule") == []
    assert extract_ids("") == []
    assert extract_ids(None) == []
    # Tokens that look like ids but are not canonical (no dash-digit form).
    assert extract_ids("A4 High Tech build on T3 station") == []


def test_extract_ids_deduplicates_preserving_order():
    assert extract_ids("M-0001, M-0001, M-0002") == ["M-0001", "M-0002"]


def test_projection_record_counts_match_manifest(projection_result):
    assert len(projection_result.detail["mechanics"]) == 13
    assert len(projection_result.detail["planner_rules"]) == 13
    assert len(projection_result.detail["claims"]) == 343
    assert len(projection_result.detail["unknowns"]) == 20
    assert len(projection_result.detail["contradictions"]) == 9
    assert len(projection_result.claim_provenance) == 370
    assert len(projection_result.graph_edges) == 294


def test_projection_builds_identity_registry(projection_result):
    objs = projection_result.objects
    assert "M-0007" in objs and objs["M-0007"].object_type == "mechanic"
    assert "CL-0042" in objs and objs["CL-0042"].object_type == "claim"
    assert "MG-0001" in objs and objs["MG-0001"].object_type == "source"


def test_projection_normalises_inline_references(projection_result):
    refs = projection_result.references
    pr_to_m0007 = [
        r for r in refs
        if r.to_id == "M-0007" and r.relationship == "depends_on_mechanic" and r.from_id.startswith("PR-")
    ]
    assert any(r.from_id == "PR-0003" for r in pr_to_m0007)


def test_projection_is_deterministic(exports_dir):
    from runtime.projection import project
    a = project(exports_dir)
    b = project(exports_dir)
    assert a.source_fingerprint == b.source_fingerprint
    assert len(a.references) == len(b.references)
