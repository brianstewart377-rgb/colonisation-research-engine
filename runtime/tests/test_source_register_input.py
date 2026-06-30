"""Source-register input-contract tests (P-final hardening).

The reference-source register is a REQUIRED, separately versioned runtime input.
A build must never silently succeed without it.
"""

import hashlib
import sqlite3

import pytest

from runtime.build_runtime import build
from runtime.config import DEFAULT_EXPORTS_DIR, SOURCE_REGISTER
from runtime.projection import project


def test_default_canonical_source_register_builds(tmp_path):
    db = tmp_path / "default.db"
    report = build(DEFAULT_EXPORTS_DIR, db, run_validation=True)
    assert report["validation"]["ok"]
    assert db.exists()


def test_missing_source_register_fails_clearly(tmp_path):
    missing = tmp_path / "does_not_exist.csv"
    db = tmp_path / "out.db"
    with pytest.raises(FileNotFoundError) as exc:
        build(DEFAULT_EXPORTS_DIR, db, run_validation=False, source_register_path=missing)
    assert "source register" in str(exc.value).lower()


def test_cli_missing_source_register_returns_nonzero(tmp_path):
    from runtime.build_runtime import main

    missing = tmp_path / "nope.csv"
    db = tmp_path / "out.db"
    rc = main([
        "--exports-dir", str(DEFAULT_EXPORTS_DIR),
        "--source-register", str(missing),
        "--output", str(db),
    ])
    assert rc == 2


def test_changed_source_register_changes_fingerprint(tmp_path):
    baseline = project(DEFAULT_EXPORTS_DIR).source_fingerprint

    # A modified copy of the register must change the source fingerprint.
    altered = tmp_path / "source_register.csv"
    altered.write_bytes(SOURCE_REGISTER.read_bytes() + b"\n# altered\n")
    changed = project(DEFAULT_EXPORTS_DIR, altered).source_fingerprint

    assert baseline != changed


def test_source_records_present_with_canonical_register(tmp_path):
    db = tmp_path / "sources.db"
    build(DEFAULT_EXPORTS_DIR, db, run_validation=False)
    conn = sqlite3.connect(str(db))
    try:
        (count,) = conn.execute("SELECT COUNT(*) FROM sources").fetchone()
    finally:
        conn.close()
    assert count == 4


def test_deterministic_rebuild_with_explicit_input_path(tmp_path):
    db_a = tmp_path / "a.db"
    db_b = tmp_path / "b.db"
    build(DEFAULT_EXPORTS_DIR, db_a, run_validation=False, source_register_path=SOURCE_REGISTER)
    build(DEFAULT_EXPORTS_DIR, db_b, run_validation=False, source_register_path=SOURCE_REGISTER)
    assert hashlib.sha256(db_a.read_bytes()).hexdigest() == hashlib.sha256(db_b.read_bytes()).hexdigest()
