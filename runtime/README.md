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

1. **Repository stays canonical; runtime is a pure function of its inputs.**
   The builder reads two explicitly-declared canonical inputs: (a) the
   deterministic *release export bundle* (`exports/*.csv` +
   `export_manifest.json`), and (b) one auxiliary canonical input — the
   reference-source register (`reference_sources/source_register.csv`). The
   register is not part of the export bundle, so it is declared as a separately
   versioned runtime input: its stable repo-relative path and a content
   fingerprint are recorded in `runtime_meta` (`source_register_path`,
   `source_register_fingerprint`). The builder never parses Markdown when an
   export exists and never writes back to the repository.

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
   (sha256 over the input files, keyed by **stable repo-relative path**) are
   stored in `runtime_meta` and reported. Rebuilding from identical inputs yields
   a **byte-identical** database.

7. **Identity-family integrity is enforced.** Validation checks that every typed
   detail-row id has a valid canonical prefix, that the prefix maps to the
   table's expected object type, and that `objects.object_type` agrees with the
   type implied by the id prefix. Malformed or cross-family ids are **errors**.

8. **Provenance has two honest models.** *Scalar-provenance* objects
   (`mechanic`, `claim`, `planner_rule`) carry a canonical `source_ref`; a
   missing one is a warning. *Structured-provenance* objects (`decision`) derive
   provenance through typed reference edges (the mechanics / claims / evidence /
   experiments they rest on) and therefore legitimately have **no** scalar
   `source_ref`. Validation confirms each decision has ≥1 structured reference
   and reports them as `info.structured_provenance_objects` rather than spurious
   "missing source" warnings. A decision with zero structured references would be
   an `unresolved_provenance_gap` warning.

---

## Schema summary

| Group | Tables |
|-------|--------|
| Metadata | `runtime_meta`, `provenance` |
| Identity registry | `objects` |
| Typed detail | `mechanics`, `planner_rules`, `economy_rules`, `construction_rules`, `planner_risks`, `decisions`, `governance_decisions`, `unknowns`, `contradictions`, `observations`, `claims`, `live_verifications`, `evidence`, `experiments`, `sources` |
| Relationships | `object_references` (derived), `graph_edges`, `claim_provenance_links`, `evidence_traceability` (verbatim) |
| Audit | `graph_node_conflicts` (graph-vs-typed metadata drift) |

Full DDL with inline rationale: [`schema.sql`](schema.sql).

- `objects(object_id PK, object_type, title, status, source_ref)` — identity +
  table-agnostic provenance pointer.
- `object_references(id, from_id, to_id, relationship, origin)` — normalised
  edges; `origin` records which export/column produced each edge.
- `provenance(export_path PK, object_type, source_register, record_count)` —
  table-level provenance keyed by canonical export path (so re-sourcing or
  splitting an export stays expressible), projected from `export_manifest.json`.
- `graph_node_conflicts(id, object_id, field, typed_value, graph_value)` —
  recorded metadata drift between a graph node and the typed canonical object.

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
| Which mechanics have pending live verification? | `mechanics_pending_live_verification()` → M-0007..M-0013 + more |
| Which contradictions affect this recommendation? | `contradictions_affecting("M-0005")` → `C-0002` |

> `mechanics_pending_live_verification()` reports mechanics whose confidence is
> gated on outstanding live testing. It deliberately does **not** assert that
> every downstream use is blocked — that judgement belongs to the (out-of-scope)
> planner. The old name `mechanics_blocked_by_live_verification()` remains as a
> thin alias for the original success-criteria phrasing.
>
> `contradictions_affecting(object_id)` resolves three labelled paths
> (`link_path`): `direct_mechanic` (object is an affected mechanic),
> `direct_rule` (object is a rule that records the contradiction), and
> `indirect_rule` (rule → `depends_on_mechanic` → mechanic ← `affects_mechanic`
> ← contradiction). E.g. `PR-0003` reaches `C-0002` only via the indirect path.

Plus single-object retrieval (`get_mechanic`, `get_planner_rule`, `get_decision`,
`get_contradiction`, `get_unknown`) and the full claim provenance chain
(`get_evidence_chain`).

The accessor opens the database in SQLite read-only mode (`mode=ro`); the runtime
cannot be mutated through this interface.

---

## Sprint 2A: Decision Explanation Slice

Sprint 2A adds one narrow, deterministic explanation capability: the runtime can
assemble a structured, inspectable evidence bundle for a single canonical
decision.

- The output is an evidence bundle, not a generated recommendation or a natural-language answer.
- The runtime reads only the generated SQLite database.
- No planner reasoning is added and no Markdown is parsed.
- Every returned supporting item is traceable via ids and explicit edges.

### API

`Runtime.explain_decision(decision_id: str) -> dict | None`

- Returns `None` if the decision id does not exist.
- Returns a deterministically ordered bundle for known ids.

### Example (D-0003, compact)

`D-0003` is a guardrail decision: it rejects any claim that Dodec is universally
superior to Orbis or Ocellus based solely on currently available evidence.

The runtime surfaces that boundary by returning:

- `decision_boundary` from the canonical `decisions` table fields (no generated prose)
- direct references (one hop):
  - decision → `EV-0003`
  - decision → `CL-0009`, `CL-0010`
  - decision → `M-0005`, `M-0007`
  - decision → `PR-0003`
- mechanic context derived from those mechanics:
  - contradictions affecting the mechanics (includes `C-0002` where present)
  - unknowns about the mechanics (includes `U-0003`, `U-0004` where present)
  - live verifications targeting the mechanics (includes `LV-0002` where present)

---

## Sprint 2B: Mechanic Explanation Slice

Sprint 2B adds a second narrow, deterministic explanation capability focused on a
single mechanic.

- The runtime returns an auditable mechanic evidence bundle, not a recommendation
  or a universal gameplay claim.
- The runtime reads only the generated SQLite database.
- Expansion stays one controlled hop from the named mechanic.
- Trace nodes retain registry-status visibility so missing referenced endpoints
  are explicit rather than silently invented.

### API

`Runtime.explain_mechanic(mechanic_id: str) -> dict | None`

- Returns `None` if the mechanic id does not exist.
- Returns a deterministically ordered bundle for known ids.

### Example (M-0007, compact)

`M-0007` returns:

- `mechanic_statement` from canonical mechanic fields only
- supporting claims linked to `M-0007`
- direct evidence traceability rows for the mechanic
- guardrails:
  - contradictions such as `C-0002`
  - unknowns such as `U-0001` and `U-0003`
  - live verifications such as `LV-0001` and `LV-0002`
- dependent planner rules such as `PR-0003`
- related decisions such as `D-0002` and `D-0003`
- related experiments where explicitly linked, such as `EXP-0001`

---

## Sprint 2C: Claim Explanation Slice

Sprint 2C adds a third narrow, deterministic explanation capability focused on a
single canonical claim.

- The runtime returns an auditable assertion-and-provenance bundle, not a
  recommendation generator.
- The runtime reads only the generated SQLite database.
- Expansion stays limited to direct provenance, direct linked mechanics,
  direct unknowns, direct contradictions, provenance-backed evidence or
  experiments, and explicit decision references.
- Evidence and experiments remain distinct ontology types in the returned
  bundle.

### API

`Runtime.explain_claim(claim_id: str) -> dict | None`

- Returns `None` if the claim id does not exist.
- Returns a deterministically ordered bundle for known ids.

### Example (CL-0010, compact)

`CL-0010` returns:

- `claim_statement` from canonical claim fields only
- direct provenance rows such as `EV-0003`, `OBS-0011`, and `C-0002`
- linked mechanics including `M-0005` and `M-0007`
- linked unknowns including `U-0003` and `U-0004`
- linked contradictions including `C-0002`
- supporting evidence derived only from provenance entities that resolve in the
  `evidence` table
- related decisions such as `D-0003`

---

## Statistics (current build)

- Database size: **~840 KB** (`cre_runtime.db`)
- Identities (`objects`): **604**
- Normalised references: **1,346**
- Canonical graph edges: **294**
- Claim provenance links: **370**
- Graph/typed metadata conflicts recorded: **3**
- Claims: 343 · Mechanics: 13 · Planner rules: 13 · Economy rules: 20 ·
  Construction rules: 23 · Planner risks: 15 · Unknowns: 20 · Contradictions: 9 ·
  Observations: 13 · Decisions: 5 · Governance decisions: 5 ·
  Live verifications: 12 · Evidence: 4 · Experiments: 2 · Sources: 4

## Validation output (current build)

The report separates **errors**, **warnings**, **info**, and **stats**:

```
validation       : PASS
  identity_integrity_errors        0
  duplicate_identities             0
  broken_provenance                0
  missing_required_objects         0
  invalid_foreign_keys             0
  missing_source_ref               0
  structured_provenance_objects    5   (info  — decisions D-0001..D-0005)
  unresolved_provenance_gaps       0
  canonical_source_orphans         1   (warn  — G-0015)
  graph_metadata_conflicts         3   (warn  — ER-0009 / ER-0010 / CR-0008 status drift)
```

A machine-readable copy is written to `validation_output.json`.

**Remaining warnings and why they remain (all are honest canonical-source findings):**

- `canonical_source_orphans` = 1 → `G-0015`, a glossary id referenced by a graph
  edge but not yet defined in `graph_nodes.csv`. A source-side fix (add the node)
  is tracked for the canonical repo; the runtime must mirror, not invent it.
- `graph_metadata_conflicts` = 3 → `ER-0009`, `ER-0010`, `CR-0008` carry a
  shortened `status` on their graph node (e.g. "Confirmed") versus the fuller
  typed register status (e.g. "Confirmed as a caution rule"). The typed value is
  authoritative and wins in `objects`; the drift is recorded for source cleanup.

## Test results

```
python3 -m pytest runtime/tests -q
40 passed
```

Coverage: projection (identity extraction, counts, determinism), schema
(tables/indexes/meta/provenance/source-register input), identity integrity
(family/type agreement + negative injections), reference integrity
(orphans/duplicates/FKs/structured-provenance/graph-conflicts), runtime
generation (build, read-only enforcement, every example query incl. direct +
indirect contradiction paths), and deterministic rebuild (stable content
fingerprint + byte-identical file).

---

## Constraints honoured

Repository remains authoritative · runtime is generated, read-only & disposable ·
no runtime editing · no duplication of business logic · no planner · no API · no UI.
