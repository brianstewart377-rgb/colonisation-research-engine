#!/usr/bin/env python3
"""build_runtime.py - CRE Runtime builder.

Creates the generated, read-only SQLite runtime from the canonical repository
inputs. The runtime is disposable: deleting ``cre_runtime.db`` loses no
knowledge because it is a deterministic function of its explicitly declared
canonical inputs: the release export bundle plus the separately versioned source
register.

Responsibilities:
  * create database (from schema.sql)
  * load the declared canonical inputs (via the projection pipeline)
  * validate identities and references
  * preserve provenance and references
  * report statistics
  * deterministic output (stable content fingerprint across rebuilds)

Usage:
  python3 -m runtime.build_runtime                 # build with defaults
  python3 -m runtime.build_runtime --validate-only # validate an existing db
  python3 -m runtime.build_runtime --source-register PATH
  python3 -m runtime.build_runtime --output /tmp/cre.db --report /tmp/report.json
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from . import config
from .config import DATA_TABLES, DEFAULT_EXPORTS_DIR, DEFAULT_OUTPUT_DB, SCHEMA_PATH, SCHEMA_VERSION, TABLE_SPECS
from .projection import ProjectionResult, ReleaseContractError, project
from .validation import ValidationReport, validate


class RuntimeValidationError(RuntimeError):
    """Raised when a built runtime database fails validation."""

    def __init__(self, report: ValidationReport):
        super().__init__("runtime validation failed")
        self.report = report


def _create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def _insert_objects(conn: sqlite3.Connection, result: ProjectionResult) -> None:
    rows = sorted(result.objects.values(), key=lambda o: o.object_id)
    conn.executemany(
        "INSERT INTO objects (object_id, object_type, title, status, source_ref) VALUES (?,?,?,?,?)",
        [(o.object_id, o.object_type, o.title, o.status, o.source_ref) for o in rows],
    )


def _insert_detail(conn: sqlite3.Connection, result: ProjectionResult) -> None:
    # Typed exports.
    for spec in TABLE_SPECS:
        rows = result.detail.get(spec.table, [])
        rows = sorted(rows, key=lambda r: r[spec.id_col] or "")
        cols = spec.columns
        placeholders = ",".join("?" for _ in cols)
        conn.executemany(
            f"INSERT INTO {spec.table} ({','.join(cols)}) VALUES ({placeholders})",
            [tuple(r[c] for c in cols) for r in rows],
        )
    # Graph-derived detail tables.
    for table, cols, key in (
        ("evidence", ["evidence_id", "title", "status", "category", "source_ref"], "evidence_id"),
        ("experiments", ["experiment_id", "title", "status", "category", "source_ref"], "experiment_id"),
        ("sources", ["source_id", "title", "type", "version", "source_tier", "repo_path", "status"], "source_id"),
    ):
        rows = sorted(result.detail.get(table, []), key=lambda r: r[key] or "")
        placeholders = ",".join("?" for _ in cols)
        conn.executemany(
            f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})",
            [tuple(r[c] for c in cols) for r in rows],
        )


def _insert_relationships(conn: sqlite3.Connection, result: ProjectionResult) -> None:
    refs = sorted(result.references, key=lambda r: (r.from_id, r.relationship, r.to_id, r.origin))
    conn.executemany(
        "INSERT INTO object_references (id, from_id, to_id, relationship, origin) VALUES (?,?,?,?,?)",
        [(i, r.from_id, r.to_id, r.relationship, r.origin) for i, r in enumerate(refs, 1)],
    )

    cpl = sorted(result.claim_provenance, key=lambda r: (r["claim_id"] or "", r["source_entity"] or "", r["relationship"] or ""))
    conn.executemany(
        "INSERT INTO claim_provenance_links (id, claim_id, source_entity, relationship, basis_note) VALUES (?,?,?,?,?)",
        [(i, r["claim_id"], r["source_entity"], r["relationship"], r["basis_note"]) for i, r in enumerate(cpl, 1)],
    )

    et = sorted(result.evidence_traceability, key=lambda r: (r["evidence_id"] or "", r["mechanic_id"] or "", r["relationship"] or ""))
    conn.executemany(
        "INSERT INTO evidence_traceability (id, evidence_id, mechanic_id, relationship, strength, basis, notes) VALUES (?,?,?,?,?,?,?)",
        [(i, r["evidence_id"], r["mechanic_id"], r["relationship"], r["strength"], r["basis"], r["notes"]) for i, r in enumerate(et, 1)],
    )

    ge = sorted(result.graph_edges, key=lambda r: (r["source_id"] or "", r["relationship"] or "", r["target_id"] or ""))
    conn.executemany(
        "INSERT INTO graph_edges (id, source_id, relationship, target_id, basis) VALUES (?,?,?,?,?)",
        [(i, r["source_id"], r["relationship"], r["target_id"], r["basis"]) for i, r in enumerate(ge, 1)],
    )


def _insert_provenance(conn: sqlite3.Connection, result: ProjectionResult) -> None:
    rows = sorted(result.provenance, key=lambda r: r["export_path"])
    conn.executemany(
        "INSERT INTO provenance (export_path, object_type, source_register, record_count) VALUES (?,?,?,?)",
        [(r["export_path"], r["object_type"], r["source_register"], r["record_count"]) for r in rows],
    )


def _insert_conflicts(conn: sqlite3.Connection, result: ProjectionResult) -> None:
    rows = sorted(result.graph_conflicts, key=lambda r: (r["object_id"], r["field"]))
    conn.executemany(
        "INSERT INTO graph_node_conflicts (id, object_id, field, typed_value, graph_value) VALUES (?,?,?,?,?)",
        [(i, r["object_id"], r["field"], r["typed_value"], r["graph_value"]) for i, r in enumerate(rows, 1)],
    )


def content_fingerprint(conn: sqlite3.Connection) -> str:
    """Deterministic hash of all data tables (order-independent, meta excluded)."""

    h = hashlib.sha256()
    for table in sorted(DATA_TABLES):
        cur = conn.execute(f"SELECT * FROM {table}")
        cols = [d[0] for d in cur.description]
        serialised_rows = sorted(
            json.dumps(
                {col: row[idx] for idx, col in enumerate(cols)},
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            )
            for row in cur.fetchall()
        )
        envelope = {
            "columns": cols,
            "rows": serialised_rows,
            "table": table,
        }
        h.update(
            json.dumps(
                envelope,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode("utf-8")
        )
    return h.hexdigest()


def _insert_meta(conn: sqlite3.Connection, result: ProjectionResult, fingerprint: str) -> None:
    # Record the exact declared source-register input: stable repo-relative path
    # plus content fingerprint.
    sr_path = result.source_register_path or config.SOURCE_REGISTER
    try:
        sr_rel = Path(sr_path).resolve().relative_to(config.REPO_ROOT).as_posix()
    except ValueError:
        sr_rel = str(sr_path)
    source_register_fp = hashlib.sha256(Path(sr_path).read_bytes()).hexdigest()
    meta = {
        "schema_version": SCHEMA_VERSION,
        "manifest_version": result.manifest.get("export_manifest_version", ""),
        "manifest_generated_at": result.manifest.get("generated_at", ""),
        "source_fingerprint": result.source_fingerprint,
        "content_fingerprint": fingerprint,
        "object_count": str(len(result.objects)),
        "reference_count": str(len(result.references)),
        # Explicitly-declared, required auxiliary runtime input (not in the export bundle).
        "source_register_path": sr_rel,
        "source_register_fingerprint": source_register_fp,
    }
    conn.executemany(
        "INSERT INTO runtime_meta (key, value) VALUES (?,?)",
        sorted(meta.items()),
    )


def _sqlite_artifact_paths(db_path: Path) -> list[Path]:
    return [
        db_path,
        Path(f"{db_path}-journal"),
        Path(f"{db_path}-wal"),
        Path(f"{db_path}-shm"),
    ]


def _cleanup_sqlite_artifacts(db_path: Path) -> None:
    for path in _sqlite_artifact_paths(db_path):
        try:
            path.unlink()
        except FileNotFoundError:
            continue


def _make_temp_output_path(output_path: Path) -> Path:
    fd, raw_path = tempfile.mkstemp(
        prefix=f".{output_path.name}.tmp-",
        suffix=".sqlite",
        dir=str(output_path.parent),
    )
    os.close(fd)
    return Path(raw_path)


def _validate_db_file(db_path: Path) -> ValidationReport:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        return validate(conn)
    finally:
        conn.close()


def build(exports_dir: Path = DEFAULT_EXPORTS_DIR, output_path: Path = DEFAULT_OUTPUT_DB,
          run_validation: bool = True, report_path: Path | None = None,
          source_register_path: Path | None = None) -> dict:
    exports_dir = Path(exports_dir)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = project(exports_dir, source_register_path)
    temp_db_path = _make_temp_output_path(output_path)
    _cleanup_sqlite_artifacts(temp_db_path)

    try:
        table_stats = {}
        conn = sqlite3.connect(str(temp_db_path))
        try:
            conn.execute("PRAGMA page_size = 4096")
            conn.execute("PRAGMA foreign_keys = ON")
            _create_schema(conn)
            _insert_objects(conn, result)
            _insert_detail(conn, result)
            _insert_relationships(conn, result)
            _insert_provenance(conn, result)
            _insert_conflicts(conn, result)
            fingerprint = content_fingerprint(conn)
            _insert_meta(conn, result, fingerprint)
            conn.commit()
            conn.execute("VACUUM")
            conn.commit()
            for table in DATA_TABLES:
                table_stats[table] = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        finally:
            conn.close()

        validation = _validate_db_file(temp_db_path)
        if not validation.ok:
            raise RuntimeValidationError(validation)

        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "exports_dir": str(exports_dir),
            "output_db": str(output_path),
            "db_size_bytes": temp_db_path.stat().st_size,
            "schema_version": SCHEMA_VERSION,
            "source_fingerprint": result.source_fingerprint,
            "content_fingerprint": fingerprint,
            "object_count": len(result.objects),
            "reference_count": len(result.references),
            "duplicate_identities_detected": result.duplicate_identities,
            "table_stats": table_stats,
            "validation": validation.as_dict() if run_validation else None,
        }

        os.replace(temp_db_path, output_path)
        _cleanup_sqlite_artifacts(temp_db_path)
        if report_path:
            Path(report_path).write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
        return report
    except Exception:
        _cleanup_sqlite_artifacts(temp_db_path)
        raise


def _print_report(report: dict) -> None:
    print("=" * 64)
    print("CRE Runtime build report")
    print("=" * 64)
    print(f"output db        : {report['output_db']}")
    print(f"db size          : {report['db_size_bytes']:,} bytes")
    print(f"schema version   : {report['schema_version']}")
    print(f"source f/print   : {report['source_fingerprint'][:16]}…")
    print(f"content f/print  : {report['content_fingerprint'][:16]}…")
    print(f"objects          : {report['object_count']}")
    print(f"references        : {report['reference_count']}")
    print("-" * 64)
    print("table statistics:")
    for table, count in report["table_stats"].items():
        print(f"  {table:<24} {count:>6}")
    val = report["validation"]
    if val is not None:
        print("-" * 64)
        print(f"validation       : {'PASS' if val['ok'] else 'FAIL'}")
        for name, count in val["stats"].items():
            print(f"  {name:<32} {count}")
        if not val["ok"]:
            print("  ERRORS:")
            for name, items in val["errors"].items():
                print(f"    {name}: {len(items)}")
    print("=" * 64)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the CRE runtime SQLite database.")
    parser.add_argument("--exports-dir", default=str(DEFAULT_EXPORTS_DIR), help="canonical exports directory")
    parser.add_argument("--source-register", default=str(config.SOURCE_REGISTER),
                        help="required reference-source register input (separately versioned canonical input)")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_DB), help="runtime database output path")
    parser.add_argument("--report", default=None, help="optional path to write a JSON build report")
    parser.add_argument("--validate-only", action="store_true", help="validate an existing runtime db and exit")
    args = parser.parse_args(argv)

    if args.validate_only:
        db_path = Path(args.output)
        if not db_path.exists():
            print(f"error: runtime db not found: {db_path}", file=sys.stderr)
            return 2
        try:
            conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        except sqlite3.Error as exc:
            print(f"error: could not open runtime db read-only: {db_path} ({exc})", file=sys.stderr)
            return 2
        try:
            report = validate(conn).as_dict()
        finally:
            conn.close()
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0 if report["ok"] else 1

    try:
        report = build(Path(args.exports_dir), Path(args.output), run_validation=True,
                       report_path=Path(args.report) if args.report else None,
                       source_register_path=Path(args.source_register))
    except RuntimeValidationError as exc:
        print(json.dumps(exc.report.as_dict(), indent=2, sort_keys=True), file=sys.stderr)
        return 1
    except (FileNotFoundError, OSError, csv.Error, ReleaseContractError, json.JSONDecodeError) as exc:
        print(f"error: runtime build failed - {exc}", file=sys.stderr)
        return 2
    _print_report(report)
    val = report["validation"]
    return 0 if (val is None or val["ok"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
