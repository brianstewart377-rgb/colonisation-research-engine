"""Deterministic-rebuild tests.

Rebuilding the runtime from identical exports must produce an identical content
fingerprint and byte-identical database files. This guarantees the runtime is a
pure, reproducible projection of the canonical repository.
"""

import hashlib

from runtime.build_runtime import build
from runtime.config import DEFAULT_EXPORTS_DIR


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_content_fingerprint_is_stable(tmp_path):
    db_a = tmp_path / "a.db"
    db_b = tmp_path / "b.db"
    report_a = build(DEFAULT_EXPORTS_DIR, db_a, run_validation=False)
    report_b = build(DEFAULT_EXPORTS_DIR, db_b, run_validation=False)
    assert report_a["content_fingerprint"] == report_b["content_fingerprint"]
    assert report_a["source_fingerprint"] == report_b["source_fingerprint"]


def test_rebuild_is_byte_identical(tmp_path):
    db_a = tmp_path / "a.db"
    db_b = tmp_path / "b.db"
    build(DEFAULT_EXPORTS_DIR, db_a, run_validation=False)
    build(DEFAULT_EXPORTS_DIR, db_b, run_validation=False)
    assert _sha256(db_a) == _sha256(db_b)


def test_fingerprint_persisted_in_meta(tmp_path):
    import sqlite3
    db = tmp_path / "c.db"
    report = build(DEFAULT_EXPORTS_DIR, db, run_validation=False)
    conn = sqlite3.connect(str(db))
    meta = {k: v for k, v in conn.execute("SELECT key, value FROM runtime_meta")}
    conn.close()
    assert meta["content_fingerprint"] == report["content_fingerprint"]
