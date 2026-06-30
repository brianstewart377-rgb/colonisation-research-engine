-- CRE Runtime v0 schema (SQLite).
--
-- Design notes:
--   * The repository is canonical; this database is a generated, read-only
--     projection. It is safe to delete and regenerate from exports/*.csv.
--   * `objects` is the master identity registry. Every typed detail row and
--     every relationship endpoint must resolve to an entry here. This is what
--     makes orphan / broken-provenance detection cheap and deterministic.
--   * Inline cross-reference columns from the canonical CSVs (which store ids
--     as backticked, comma/semicolon separated lists) are normalised into the
--     `object_references` edge table, one row per (from, to, relationship).
--   * Already-normalised canonical relationship exports are preserved verbatim
--     in their own tables (graph_edges, claim_provenance_links,
--     evidence_traceability) so provenance is never collapsed or rewritten.
--   * Detail tables FK into `objects`; edge tables intentionally do NOT, so the
--     validator can surface dangling references instead of rejecting them.

PRAGMA foreign_keys = ON;

-- Deterministic build metadata (excluded from the content fingerprint).
CREATE TABLE runtime_meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Table-level provenance: where each projected table came from. Keyed by the
-- canonical export path (the stable release-bundle artifact identity) rather
-- than by object type, so re-sourcing or splitting an export stays expressible.
CREATE TABLE provenance (
    export_path     TEXT PRIMARY KEY,
    object_type     TEXT NOT NULL,
    source_register TEXT NOT NULL,
    record_count    INTEGER NOT NULL
);

-- Master identity registry.
CREATE TABLE objects (
    object_id   TEXT PRIMARY KEY,
    object_type TEXT NOT NULL,
    title       TEXT,
    status      TEXT,
    source_ref  TEXT
);
CREATE INDEX idx_objects_type ON objects(object_type);

-- ---------------------------------------------------------------------------
-- Typed detail tables (subset of objects with rich attributes).
-- ---------------------------------------------------------------------------
CREATE TABLE mechanics (
    mechanic_id      TEXT PRIMARY KEY REFERENCES objects(object_id),
    title            TEXT NOT NULL,
    status           TEXT,
    primary_category TEXT,
    source_basis     TEXT
);

CREATE TABLE planner_rules (
    rule_id              TEXT PRIMARY KEY REFERENCES objects(object_id),
    title                TEXT NOT NULL,
    status               TEXT,
    category             TEXT,
    rule                 TEXT,
    planner_implications TEXT,
    testing_status       TEXT,
    source               TEXT
);

CREATE TABLE economy_rules (
    rule_id              TEXT PRIMARY KEY REFERENCES objects(object_id),
    title                TEXT NOT NULL,
    status               TEXT,
    rule                 TEXT,
    planner_implications TEXT,
    testing_status       TEXT,
    source               TEXT
);

CREATE TABLE construction_rules (
    rule_id              TEXT PRIMARY KEY REFERENCES objects(object_id),
    title                TEXT NOT NULL,
    status               TEXT,
    rule                 TEXT,
    planner_implications TEXT,
    testing_status       TEXT,
    source               TEXT
);

CREATE TABLE planner_risks (
    risk_id             TEXT PRIMARY KEY REFERENCES objects(object_id),
    title               TEXT NOT NULL,
    severity            TEXT,
    failure_mode        TEXT,
    why_dangerous       TEXT,
    required_mitigation TEXT,
    source              TEXT
);

CREATE TABLE decisions (
    decision_id       TEXT PRIMARY KEY REFERENCES objects(object_id),
    title             TEXT NOT NULL,
    status            TEXT,
    date              TEXT,
    context           TEXT,
    problem_statement TEXT,
    decision          TEXT,
    rationale         TEXT,
    trade_offs        TEXT,
    consequences      TEXT,
    confidence        TEXT,
    review_status     TEXT
);

CREATE TABLE governance_decisions (
    decision_id     TEXT PRIMARY KEY REFERENCES objects(object_id),
    title           TEXT NOT NULL,
    status          TEXT,
    decision_to_make TEXT,
    why_it_matters  TEXT,
    blocking_impact TEXT,
    source          TEXT
);

CREATE TABLE unknowns (
    unknown_id           TEXT PRIMARY KEY REFERENCES objects(object_id),
    title                TEXT NOT NULL,
    category             TEXT,
    unknown_statement    TEXT,
    planner_implications TEXT,
    source               TEXT
);

CREATE TABLE contradictions (
    contradiction_id     TEXT PRIMARY KEY REFERENCES objects(object_id),
    title                TEXT NOT NULL,
    category             TEXT,
    description          TEXT,
    confidence           TEXT,
    planner_implications TEXT,
    testing_status       TEXT,
    source               TEXT
);

CREATE TABLE observations (
    observation_id   TEXT PRIMARY KEY REFERENCES objects(object_id),
    source_id        TEXT,
    context          TEXT,
    observation_type TEXT,
    statement        TEXT,
    confidence       TEXT,
    planner_relevance TEXT
);

CREATE TABLE claims (
    claim_id               TEXT PRIMARY KEY REFERENCES objects(object_id),
    claim_type             TEXT,
    status                 TEXT,
    confidence             TEXT,
    title                  TEXT,
    claim_text             TEXT,
    primary_basis          TEXT,
    source_document        TEXT,
    page_or_sheet          TEXT,
    section_heading        TEXT,
    category               TEXT,
    evidence_type          TEXT,
    planner_implication    TEXT,
    needs_live_verification TEXT
);

CREATE TABLE live_verifications (
    verification_id     TEXT PRIMARY KEY REFERENCES objects(object_id),
    title               TEXT NOT NULL,
    primary_target      TEXT,
    method_type         TEXT,
    required_state      TEXT,
    primary_observations TEXT,
    success_condition   TEXT
);

CREATE TABLE evidence (
    evidence_id TEXT PRIMARY KEY REFERENCES objects(object_id),
    title       TEXT,
    status      TEXT,
    category    TEXT,
    source_ref  TEXT
);

CREATE TABLE experiments (
    experiment_id TEXT PRIMARY KEY REFERENCES objects(object_id),
    title         TEXT,
    status        TEXT,
    category      TEXT,
    source_ref    TEXT
);

CREATE TABLE sources (
    source_id   TEXT PRIMARY KEY REFERENCES objects(object_id),
    title       TEXT,
    type        TEXT,
    version     TEXT,
    source_tier TEXT,
    repo_path   TEXT,
    status      TEXT
);

-- ---------------------------------------------------------------------------
-- Relationship tables.
-- ---------------------------------------------------------------------------

-- Normalised edges derived from inline reference columns in the typed exports.
CREATE TABLE object_references (
    id           INTEGER PRIMARY KEY,
    from_id      TEXT NOT NULL,
    to_id        TEXT NOT NULL,
    relationship TEXT NOT NULL,
    origin       TEXT NOT NULL
);
CREATE INDEX idx_objref_from ON object_references(from_id);
CREATE INDEX idx_objref_to   ON object_references(to_id);
CREATE INDEX idx_objref_rel  ON object_references(relationship);

-- Canonical claim provenance chain (preserved verbatim).
CREATE TABLE claim_provenance_links (
    id            INTEGER PRIMARY KEY,
    claim_id      TEXT NOT NULL,
    source_entity TEXT NOT NULL,
    relationship  TEXT NOT NULL,
    basis_note    TEXT
);
CREATE INDEX idx_cpl_claim ON claim_provenance_links(claim_id);

-- Canonical evidence -> mechanic traceability (preserved verbatim).
CREATE TABLE evidence_traceability (
    id           INTEGER PRIMARY KEY,
    evidence_id  TEXT NOT NULL,
    mechanic_id  TEXT NOT NULL,
    relationship TEXT,
    strength     TEXT,
    basis        TEXT,
    notes        TEXT
);
CREATE INDEX idx_et_evidence ON evidence_traceability(evidence_id);
CREATE INDEX idx_et_mechanic ON evidence_traceability(mechanic_id);

-- Canonical knowledge graph edges (preserved verbatim).
CREATE TABLE graph_edges (
    id           INTEGER PRIMARY KEY,
    source_id    TEXT NOT NULL,
    relationship TEXT NOT NULL,
    target_id    TEXT NOT NULL,
    basis        TEXT
);
CREATE INDEX idx_ge_source ON graph_edges(source_id);
CREATE INDEX idx_ge_target ON graph_edges(target_id);

-- Metadata drift between a graph node and the typed canonical object of the
-- same identity (e.g. an abbreviated status on the graph node). Recorded so the
-- conflict is surfaced as a validation warning instead of silently lost when
-- the typed (authoritative) value wins in the `objects` registry.
CREATE TABLE graph_node_conflicts (
    id          INTEGER PRIMARY KEY,
    object_id   TEXT NOT NULL,
    field       TEXT NOT NULL,
    typed_value TEXT,
    graph_value TEXT
);
CREATE INDEX idx_gnc_object ON graph_node_conflicts(object_id);
