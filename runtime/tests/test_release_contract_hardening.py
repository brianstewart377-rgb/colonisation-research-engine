import csv
import hashlib
import json
import shutil
import sqlite3
from pathlib import Path

import pytest

from runtime.build_runtime import RuntimeValidationError, build, content_fingerprint, main
from runtime.config import DEFAULT_EXPORTS_DIR, MANIFEST_EXPORT
from runtime.projection import ReleaseContractError, project


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _copy_exports(tmp_path: Path) -> Path:
    dst = tmp_path / "exports_copy"
    shutil.copytree(DEFAULT_EXPORTS_DIR, dst)
    return dst


def _manifest_path(exports_dir: Path) -> Path:
    return exports_dir / MANIFEST_EXPORT


def _load_manifest(exports_dir: Path) -> dict:
    return json.loads(_manifest_path(exports_dir).read_text(encoding="utf-8"))


def _write_manifest(exports_dir: Path, manifest: dict) -> None:
    _manifest_path(exports_dir).write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def _manifest_entry(manifest: dict, export_name: str) -> dict:
    target = f"exports/{export_name}"
    for entry in manifest["exports"]:
        if entry["path"] == target:
            return entry
    raise AssertionError(f"missing manifest entry for {target}")


def _rewrite_csv(csv_path: Path, rows: list[list[str]]) -> None:
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def _read_csv_rows(csv_path: Path) -> list[list[str]]:
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def _temp_artifacts_for(output_path: Path) -> list[Path]:
    artifacts = []
    for path in output_path.parent.iterdir():
        if path.name.startswith(f".{output_path.name}.tmp-"):
            artifacts.append(path)
    for suffix in ("-journal", "-wal", "-shm"):
        sidecar = output_path.parent / f"{output_path.name}{suffix}"
        if sidecar.exists():
            artifacts.append(sidecar)
    return sorted(artifacts)


def _mutate_mechanic_id(exports_dir: Path, old_id: str, new_id: str) -> None:
    csv_path = exports_dir / "mechanics.csv"
    rows = _read_csv_rows(csv_path)
    header, data = rows[0], rows[1:]
    mutated = []
    for row in data:
        if row and row[0] == old_id:
            row = [new_id, *row[1:]]
        mutated.append(row)
    _rewrite_csv(csv_path, [header, *mutated])


def test_current_release_bundle_passes_preflight(exports_dir):
    result = project(exports_dir)
    assert result.manifest["status"] == "assembled"
    assert result.manifest["export_manifest_version"]


def test_preflight_rejects_missing_required_manifest_export(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    manifest = _load_manifest(exports_dir)
    manifest["exports"] = [entry for entry in manifest["exports"] if entry["path"] != "exports/claims.csv"]
    _write_manifest(exports_dir, manifest)

    with pytest.raises(ReleaseContractError, match="missing required export paths"):
        project(exports_dir)


def test_preflight_rejects_duplicate_manifest_path(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    manifest = _load_manifest(exports_dir)
    manifest["exports"].append(dict(manifest["exports"][0]))
    _write_manifest(exports_dir, manifest)

    with pytest.raises(ReleaseContractError, match="duplicate export path"):
        project(exports_dir)


def test_preflight_rejects_extra_unknown_manifest_export(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    manifest = _load_manifest(exports_dir)
    manifest["exports"].append(
        {
            "path": "exports/unknown_extra.csv",
            "format": "csv",
            "source": "tests/unknown.csv",
            "record_count": 0,
        }
    )
    _write_manifest(exports_dir, manifest)

    with pytest.raises(ReleaseContractError, match="unknown export path"):
        project(exports_dir)


def test_preflight_rejects_incorrect_format(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    manifest = _load_manifest(exports_dir)
    _manifest_entry(manifest, "mechanics.csv")["format"] = "json"
    _write_manifest(exports_dir, manifest)

    with pytest.raises(ReleaseContractError, match="format='csv'"):
        project(exports_dir)


def test_preflight_rejects_record_count_mismatch(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    manifest = _load_manifest(exports_dir)
    _manifest_entry(manifest, "mechanics.csv")["record_count"] = 999
    _write_manifest(exports_dir, manifest)

    with pytest.raises(ReleaseContractError, match="record_count mismatch"):
        project(exports_dir)


def test_preflight_rejects_missing_required_csv_column(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    csv_path = exports_dir / "mechanics.csv"
    rows = _read_csv_rows(csv_path)
    bad_header = rows[0][:-1]
    bad_rows = [bad_header] + [row[:-1] for row in rows[1:]]
    _rewrite_csv(csv_path, bad_rows)

    with pytest.raises(ReleaseContractError, match="header contract mismatch"):
        project(exports_dir)


def test_preflight_rejects_reordered_header(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    csv_path = exports_dir / "planner_rules.csv"
    rows = _read_csv_rows(csv_path)
    header = list(rows[0])
    header[0], header[1] = header[1], header[0]
    _rewrite_csv(csv_path, [header, *rows[1:]])

    with pytest.raises(ReleaseContractError, match="header contract mismatch"):
        project(exports_dir)


def test_preflight_rejects_extra_header_column(tmp_path):
    exports_dir = _copy_exports(tmp_path)
    csv_path = exports_dir / "claims.csv"
    rows = _read_csv_rows(csv_path)
    header = list(rows[0]) + ["unexpected_extra"]
    data = [row + [""] for row in rows[1:]]
    _rewrite_csv(csv_path, [header, *data])

    with pytest.raises(ReleaseContractError, match="header contract mismatch"):
        project(exports_dir)


def test_atomic_replacement_preserves_existing_db_on_preflight_failure(tmp_path):
    output_db = tmp_path / "cre_runtime.db"
    build(DEFAULT_EXPORTS_DIR, output_db, run_validation=True)
    before = _sha256(output_db)

    bad_exports = _copy_exports(tmp_path)
    manifest = _load_manifest(bad_exports)
    manifest["exports"].append(dict(manifest["exports"][0]))
    _write_manifest(bad_exports, manifest)

    with pytest.raises(ReleaseContractError):
        build(bad_exports, output_db, run_validation=True)

    assert _sha256(output_db) == before
    assert _temp_artifacts_for(output_db) == []


def test_atomic_replacement_preserves_existing_db_on_validation_failure_even_when_validation_hidden(tmp_path):
    output_db = tmp_path / "cre_runtime.db"
    build(DEFAULT_EXPORTS_DIR, output_db, run_validation=True)
    before = _sha256(output_db)

    bad_exports = _copy_exports(tmp_path)
    _mutate_mechanic_id(bad_exports, "M-0001", "CL-9999")

    with pytest.raises(RuntimeValidationError):
        build(bad_exports, output_db, run_validation=False)

    assert _sha256(output_db) == before
    assert _temp_artifacts_for(output_db) == []


def test_cli_returns_one_for_validation_failure(tmp_path):
    output_db = tmp_path / "cre_runtime.db"
    bad_exports = _copy_exports(tmp_path)
    _mutate_mechanic_id(bad_exports, "M-0001", "CL-9999")

    rc = main(["--exports-dir", str(bad_exports), "--output", str(output_db)])
    assert rc == 1


def test_canonical_json_content_fingerprint_distinguishes_separator_boundary_text(tmp_path):
    db_a = tmp_path / "a.db"
    db_b = tmp_path / "b.db"
    build(DEFAULT_EXPORTS_DIR, db_a, run_validation=False)
    build(DEFAULT_EXPORTS_DIR, db_b, run_validation=False)

    conn = sqlite3.connect(str(db_a))
    conn.execute(
        "UPDATE claims SET title = ?, claim_text = ? WHERE claim_id = ?",
        ("A\x1fB", "C", "CL-0001"),
    )
    conn.commit()
    conn.close()

    conn = sqlite3.connect(str(db_b))
    conn.execute(
        "UPDATE claims SET title = ?, claim_text = ? WHERE claim_id = ?",
        ("A", "B\x1fC", "CL-0001"),
    )
    conn.commit()
    conn.close()

    conn = sqlite3.connect(str(db_a))
    fp_a = content_fingerprint(conn)
    conn.close()

    conn = sqlite3.connect(str(db_b))
    fp_b = content_fingerprint(conn)
    conn.close()

    assert fp_a != fp_b


def test_validate_only_is_truly_read_only(tmp_path):
    output_db = tmp_path / "cre_runtime.db"
    build(DEFAULT_EXPORTS_DIR, output_db, run_validation=True)
    before_hash = _sha256(output_db)
    before_listing = sorted((p.name, p.stat().st_size) for p in tmp_path.iterdir())

    rc = main(["--output", str(output_db), "--validate-only"])

    after_hash = _sha256(output_db)
    after_listing = sorted((p.name, p.stat().st_size) for p in tmp_path.iterdir())
    assert rc == 0
    assert after_hash == before_hash
    assert after_listing == before_listing
