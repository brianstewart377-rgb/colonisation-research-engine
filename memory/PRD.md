# CRE Runtime — PRD / Working Memory

## Original problem statement
CRE Runtime v0 — Sprint 1 (Foundation). Build ONLY the runtime foundation that
projects canonical repository knowledge into a generated, disposable, read-only
SQLite runtime database. No web app, no UI, no planner, no API, no accounts, no
Digital Twin. Repository stays canonical; runtime is regenerated from exports.

## Context / source of truth
- Canonical repo: `brianstewart377-rgb/colonisation-research-engine` (synced into /app).
- Canonical release exports: `/app/exports/*.csv` + `export_manifest.json`.
- Runtime reads exports only (never Markdown directly when exports exist).

## Architecture (Sprint 1 — DONE 2026-06-30)
- New package `/app/runtime/` (stdlib only; pytest for tests).
- `config.py` declarative export→schema mapping + deterministic id extractor.
- `projection.py` pure read → normalised records (ObjectRecord / Reference).
- `schema.sql` SQLite schema: `objects` identity registry + typed detail tables
  + `object_references` (derived edges) + verbatim `graph_edges` /
  `claim_provenance_links` / `evidence_traceability` + `provenance` + `runtime_meta`.
- `build_runtime.py` builder/CLI: create → load → validate → report; deterministic
  (sorted inserts, no wall-clock in DB, VACUUM, content+source fingerprints,
  byte-identical rebuilds).
- `validation.py` orphan / duplicate / broken-provenance / missing-required / FK checks.
- `queries.py` read-only `Runtime` accessor (success-criteria queries).
- `examples/run_queries.py` demonstration. `tests/` 30 tests (all pass).

## Status / statistics
- Build: PASS. DB ~828 KB. objects=604, references=1346, graph_edges=294,
  claim_provenance_links=370, claims=343, mechanics=13, planner_rules=13.
- Validation: PASS (1 warning: orphan `G-0015` — canonical-source gap).
- Determinism: byte-identical rebuild verified. Disposable (delete+rebuild OK).
- Tests: 30 passed.

## Success criteria — all met
planner rules depending on M-0007 (PR-0003) · evidence supporting CL-0042 (MG-0001) ·
decisions referencing M-0010 (D-0001) · mechanics blocked by live verification ·
contradictions affecting a recommendation (C-0002 for M-0005).

## Sprint 1 Hardening (DONE 2026-06-30)
- P0 read-only test fixed: `pytest.raises(sqlite3.OperationalError)` + post-write reread confirms data unchanged.
- P0 identity-family/type integrity: `validation.check_identity_integrity` enforces valid prefix, prefix→type, table family, objects.object_type agreement; cross-family/mismatch/invalid ids are errors. Negative tests added.
- P1 honest provenance model: decisions use STRUCTURED provenance (typed reference edges) → reported as info, not false missing-source warnings. Scalar types (mechanic/claim/planner_rule) keep source_ref check. Report split into errors/warnings/info/stats.
- P1 release-portable inputs: source register declared as explicit separately-versioned runtime input; `runtime_meta.source_register_path` + `source_register_fingerprint` recorded; docs corrected (not "exports only").
- P1 contradiction traversal: `contradictions_affecting` now resolves direct_mechanic / direct_rule / indirect_rule (rule→depends_on_mechanic→mechanic→contradiction). Regression tests for all paths + no-false-positive.
- P2: provenance keyed by export_path; graph_node_conflicts table records graph-vs-typed metadata drift (3 status drifts) surfaced as warnings; fingerprints use repo-relative paths; `mechanics_blocked_by_live_verification` renamed to `mechanics_pending_live_verification` (alias kept).
- Tests: 40 passed. Validation PASS. Byte-identical rebuild verified (sha 636cdb67…). Remaining warnings: G-0015 orphan (canonical gap) + 3 graph status drifts (ER-0009/ER-0010/CR-0008).

## Backlog / next (future sprints — NOT in scope)
- P1: Promote `G-0015` glossary node in canonical `graph_nodes.csv` (source-side fix).
- P1: Richer query module (transitive evidence chains, reverse dependency graphs).
- P2: CLI query tool / export of query results.
- P2: Incremental/streaming projection for large export growth (optimisation).
- Out of scope by design: planner, API, UI, Digital Twin, accounts.

## Notes
- No auth, no third-party integrations, no MongoDB used (intentional).
- Generated artifacts gitignored: `runtime/*.db`, `runtime/build_report.json`.
- Committed deliverable artifact: `runtime/validation_output.json`.
