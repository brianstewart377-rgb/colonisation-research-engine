# CRE Runtime v0 — Sprint 1 (Foundation)

A **generated, disposable, read-only** execution layer for the Colonisation
Research Engine.

> The repository is the canonical source of truth.
> The runtime is a projection of it. Deleting the runtime loses **no** knowledge —
> it is regenerated deterministically from `exports/*.csv`.

This sprint delivers the runtime *foundation only*. There is **no** web app, UI,
planner, API, user accounts, or Digital Twin here — by design.

---

## Quick start

```bash
# Build the runtime database (reads ../exports, writes runtime/cre_runtime.db)
python3 -m runtime.build_runtime

# Validate an already-built runtime
python3 -m runtime.build_runtime --validate-only

# Run the demonstration query layer
python3 -m runtime.examples.run_queries

# Run the test suite
python3 -m pytest runtime/tests -q
```

Run all commands from the repository root (`/app`).

---

## Architecture decisions

1. **Repository stays canonical; runtime is a pure function of the exports.**
   The builder reads only the deterministic *release exports*
   (`exports/*.csv` + `export_manifest.json`) and the canonical reference-source
   register. It never parses Markdown directly when an export exists, and it
   never writes back to the repository.

2. **SQLite, standard library only.** A single-file SQLite database is the ideal
   disposable runtime: zero services, trivially deletable, fast to query. The
   package depends only on the Python stdlib (`sqlite3`, `csv`, `json`); `pytest`
   is used for tests only.

3. **A master identity registry (`objects`).** Every canonical identity
   (`M-####`, `CL-####`, `PR-####`, …) is registered once in `objects`. Typed
   detail tables foreign-key into it. This makes identity validation, orphan
   detection, and provenance checks cheap and deterministic.

4. **Normalise inline cross-references; preserve canonical edges verbatim.**
   The canonical CSVs store references as backticked, comma/semicolon-separated
   lists inside cells (e.g. `` "`M-0002`, `M-0007`" ``). A single deterministic
   identity extractor (`config.extract_ids`) normalises these into the
   `object_references` edge table. Relationship exports that are *already*
   normalised (`graph_edges`, `claim_provenance_links`, `evidence_traceability`)
   are preserved row-for-row so provenance is never collapsed or rewritten.

5. **Edges are not FK-constrained on purpose.** Detail tables FK into `objects`,
   but edge tables do not — so the validator can *surface* dangling references
   rather than the database silently rejecting them. Orphans that reflect the
   state of the canonical source are reported as **warnings**, not build
   failures (the runtime is a faithful mirror, not the source of truth).

6. **Determinism by construction.** All rows are inserted in sorted order,
   surrogate keys are assigned deterministically, no wall-clock value is stored
   inside the database, and a `VACUUM` normalises the file. A `content_fingerprint`
   (sha256 over all data tables, order-independent) and a `source_fingerprint`
   (sha256 over the input files) are stored in `runtime_meta` and reported.
   Rebuilding from identical exports yields a **byte-identical** database.

---

## Schema summary

| Group | Tables |
|-------|--------|
| Metadata | `runtime_meta`, `provenance` |
| Identity registry | `objects` |
| Typed detail | `mechanics`, `planner_rules`, `economy_rules`, `construction_rules`, `planner_risks`, `decisions`, `governance_decisions`, `unknowns`, `contradictions`, `observations`, `claims`, `live_verifications`, `evidence`, `experiments`, `sources` |
| Relationships | `object_references` (derived), `graph_edges`, `claim_provenance_links`, `evidence_traceability` (verbatim) |

Full DDL with inline rationale: [`schema.sql`](schema.sql).

- `objects(object_id PK, object_type, title, status, source_ref)` — identity +
  table-agnostic provenance pointer.
- `object_references(id, from_id, to_id, relationship, origin)` — normalised
  edges; `origin` records which export/column produced each edge.
- `provenance(object_type, export_path, source_register, record_count)` —
  table-level provenance projected straight from `export_manifest.json`.

---

## Projection pipeline

```
exports/*.csv ──▶ projection.project()  (pure, no DB)
                      │
                      ├─ objects        (identity registry, deduplicated)
                      ├─ detail rows    (one list per typed table)
                      ├─ references     (normalised inline cross-refs)
                      └─ verbatim edges (graph / provenance / traceability)
                      │
build_runtime.build() ─▶ SQLite (sorted inserts, VACUUM, fingerprints)
                      │
validation.validate() ─▶ ValidationReport (errors / warnings / stats)
```

- `config.py` — declarative mapping of every export onto the schema (no logic).
- `projection.py` — pure read → normalised records (+ input fingerprint).
- `build_runtime.py` — creates the DB, loads, validates, reports, deterministic.
- `validation.py` — orphan / duplicate / provenance / required / FK checks.
- `queries.py` — read-only `Runtime` accessor with the example queries.

---

## Runtime queries

The runtime answers the Sprint-1 success-criteria questions (see
`examples/run_queries.py`):

| Question | Method |
|----------|--------|
| Which planner rules depend on M-0007? | `planner_rules_depending_on("M-0007")` → `PR-0003` |
| Which evidence supports CL-0042? | `evidence_supporting_claim("CL-0042")` → `MG-0001` |
| Which decisions reference M-0010? | `decisions_referencing("M-0010")` → `D-0001` |
| Which mechanics remain blocked by live verification? | `mechanics_blocked_by_live_verification()` → M-0007..M-0013 + more |
| Which contradictions affect this recommendation? | `contradictions_affecting("M-0005")` → `C-0002` |

Plus single-object retrieval (`get_mechanic`, `get_planner_rule`, `get_decision`,
`get_contradiction`, `get_unknown`) and the full claim provenance chain
(`get_evidence_chain`).

The accessor opens the database in SQLite read-only mode (`mode=ro`); the runtime
cannot be mutated through this interface.

---

## Statistics (current build)

- Database size: **~828 KB** (`cre_runtime.db`)
- Identities (`objects`): **604**
- Normalised references: **1,346**
- Canonical graph edges: **294**
- Claim provenance links: **370**
- Claims: 343 · Mechanics: 13 · Planner rules: 13 · Economy rules: 20 ·
  Construction rules: 23 · Planner risks: 15 · Unknowns: 20 · Contradictions: 9 ·
  Observations: 13 · Decisions: 5 · Governance decisions: 5 ·
  Live verifications: 12 · Evidence: 4 · Experiments: 2 · Sources: 4

## Validation output (current build)

```
validation       : PASS
  orphan_references            1   (warning — canonical-source gap: G-0015)
  duplicate_identities         0
  broken_provenance            0
  missing_required_objects     0
  invalid_foreign_keys         0
```

A machine-readable copy is written to `validation_output.json`. The single
orphan (`G-0015`, a glossary id referenced by a graph edge but not yet defined
in `graph_nodes.csv`) is a finding *about the canonical source* and is reported
as a warning rather than failing the build.

## Test results

```
python3 -m pytest runtime/tests -q
30 passed
```

Coverage: projection (identity extraction, counts, determinism), schema
(tables/indexes/meta/provenance), reference integrity (orphans/duplicates/FKs/
provenance), runtime generation (build + every example query), and deterministic
rebuild (stable content fingerprint + byte-identical file).

---

## Constraints honoured

Repository remains authoritative · runtime is generated, read-only & disposable ·
no runtime editing · no duplication of business logic · no planner · no API · no UI.
