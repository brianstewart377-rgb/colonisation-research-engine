-- Colonisation Research Engine
-- Evidence Vault SQLite Schema v0.1

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS evidence_batch (
    batch_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    source_channel TEXT,
    uploaded_by TEXT,
    uploaded_at TEXT NOT NULL,
    default_system_name TEXT,
    default_body_name TEXT,
    default_facility_name TEXT,
    default_experiment_id TEXT,
    default_phase TEXT CHECK(default_phase IN ('before', 'after', 'during', 'reference', 'unknown')) DEFAULT 'unknown',
    notes TEXT
);

CREATE TABLE IF NOT EXISTS evidence_item (
    evidence_id TEXT PRIMARY KEY,
    batch_id TEXT,
    evidence_type TEXT NOT NULL,
    title TEXT NOT NULL,
    system_name TEXT,
    body_name TEXT,
    facility_name TEXT,
    experiment_id TEXT,
    research_package_id TEXT,
    phase TEXT CHECK(phase IN ('before', 'after', 'during', 'reference', 'unknown')) DEFAULT 'unknown',
    captured_at TEXT,
    uploaded_at TEXT NOT NULL,
    captured_by TEXT,
    source_channel TEXT,
    original_filename TEXT NOT NULL,
    stored_path TEXT NOT NULL,
    sha256 TEXT NOT NULL UNIQUE,
    mime_type TEXT,
    file_size_bytes INTEGER,
    review_status TEXT CHECK(review_status IN ('unreviewed', 'analyst_reviewed', 'corroborated', 'disputed', 'superseded')) DEFAULT 'unreviewed',
    notes TEXT,
    FOREIGN KEY (batch_id) REFERENCES evidence_batch(batch_id)
);

CREATE TABLE IF NOT EXISTS research_package (
    research_package_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    experiment_id TEXT,
    system_name TEXT,
    body_name TEXT,
    facility_name TEXT,
    package_phase TEXT CHECK(package_phase IN ('before', 'after', 'comparison', 'reference', 'mixed', 'unknown')) DEFAULT 'unknown',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    review_status TEXT CHECK(review_status IN ('draft', 'analyst_reviewed', 'published', 'superseded')) DEFAULT 'draft',
    summary TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS research_package_item (
    research_package_id TEXT NOT NULL,
    evidence_id TEXT NOT NULL,
    role_in_package TEXT,
    sort_order INTEGER,
    notes TEXT,
    PRIMARY KEY (research_package_id, evidence_id),
    FOREIGN KEY (research_package_id) REFERENCES research_package(research_package_id),
    FOREIGN KEY (evidence_id) REFERENCES evidence_item(evidence_id)
);

CREATE TABLE IF NOT EXISTS observation (
    observation_id TEXT PRIMARY KEY,
    evidence_id TEXT NOT NULL,
    observation_type TEXT NOT NULL,
    subject_type TEXT,
    subject_name TEXT,
    value_text TEXT NOT NULL,
    confidence_score REAL,
    extraction_method TEXT CHECK(extraction_method IN ('manual', 'ocr', 'vision_ai', 'parser', 'imported')) DEFAULT 'manual',
    extracted_by TEXT,
    extracted_at TEXT NOT NULL,
    review_status TEXT CHECK(review_status IN ('unreviewed', 'analyst_reviewed', 'corroborated', 'disputed', 'superseded')) DEFAULT 'unreviewed',
    notes TEXT,
    FOREIGN KEY (evidence_id) REFERENCES evidence_item(evidence_id)
);

CREATE TABLE IF NOT EXISTS evidence_link (
    link_id TEXT PRIMARY KEY,
    evidence_id TEXT NOT NULL,
    target_type TEXT NOT NULL,
    target_id TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    confidence_score REAL,
    created_at TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (evidence_id) REFERENCES evidence_item(evidence_id)
);

CREATE TABLE IF NOT EXISTS tag (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS evidence_tag (
    evidence_id TEXT NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (evidence_id, tag_id),
    FOREIGN KEY (evidence_id) REFERENCES evidence_item(evidence_id),
    FOREIGN KEY (tag_id) REFERENCES tag(tag_id)
);

CREATE INDEX IF NOT EXISTS idx_evidence_item_system ON evidence_item(system_name);
CREATE INDEX IF NOT EXISTS idx_evidence_item_body ON evidence_item(body_name);
CREATE INDEX IF NOT EXISTS idx_evidence_item_facility ON evidence_item(facility_name);
CREATE INDEX IF NOT EXISTS idx_evidence_item_experiment ON evidence_item(experiment_id);
CREATE INDEX IF NOT EXISTS idx_evidence_item_package ON evidence_item(research_package_id);
CREATE INDEX IF NOT EXISTS idx_evidence_item_phase ON evidence_item(phase);
CREATE INDEX IF NOT EXISTS idx_observation_evidence ON observation(evidence_id);
CREATE INDEX IF NOT EXISTS idx_observation_type ON observation(observation_type);
CREATE INDEX IF NOT EXISTS idx_evidence_link_target ON evidence_link(target_type, target_id);
