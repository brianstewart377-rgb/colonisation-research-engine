"""Identity-family / object-type integrity tests, including negative cases."""

import sqlite3

import pytest

from runtime.config import SCHEMA_PATH
from runtime.validation import check_identity_integrity


def _fresh_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _add_object(conn, oid, otype):
    conn.execute(
        "INSERT INTO objects (object_id, object_type, title) VALUES (?,?,?)",
        (oid, otype, "x"),
    )


def test_clean_minimal_db_has_no_identity_errors():
    conn = _fresh_db()
    _add_object(conn, "M-0001", "mechanic")
    conn.execute("INSERT INTO mechanics (mechanic_id, title) VALUES ('M-0001','x')")
    errors, _ = check_identity_integrity(conn)
    assert errors == []


def test_claim_id_in_mechanic_row_is_cross_family_error():
    conn = _fresh_db()
    # A claim id wrongly placed in the mechanics table.
    _add_object(conn, "CL-9999", "mechanic")  # also type-mismatched in objects
    conn.execute("INSERT INTO mechanics (mechanic_id, title) VALUES ('CL-9999','x')")
    errors, _ = check_identity_integrity(conn)
    cross = [e for e in errors if e.get("issue") == "cross_family_id" and e.get("table") == "mechanics"]
    assert cross and cross[0]["table_expects"] == "mechanic" and cross[0]["prefix_implies"] == "claim"


def test_object_type_mismatch_is_error():
    conn = _fresh_db()
    _add_object(conn, "M-9999", "planner_rule")  # M-prefix but typed as planner_rule
    errors, _ = check_identity_integrity(conn)
    assert any(
        e.get("issue") == "object_type_mismatch" and e.get("object_id") == "M-9999"
        and e.get("prefix_implies") == "mechanic"
        for e in errors
    )


def test_invalid_canonical_id_is_error():
    conn = _fresh_db()
    _add_object(conn, "BADID", "mechanic")
    conn.execute("INSERT INTO mechanics (mechanic_id, title) VALUES ('BADID','x')")
    errors, _ = check_identity_integrity(conn)
    assert any(e.get("issue") == "invalid_canonical_id" and e.get("table") == "mechanics" for e in errors)
    assert any(e.get("issue") == "invalid_canonical_id_in_objects" for e in errors)


def test_real_runtime_has_clean_identity_integrity(conn):
    errors, _ = check_identity_integrity(conn)
    assert errors == [], errors
