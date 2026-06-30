# Evidence Vault Architecture

## Purpose

The Evidence Vault is the permanent source of truth for raw research evidence in the Colonisation Research Engine.

Its purpose is simple:

> No evidence is ever analysed without first being registered.

This prevents screenshots, logs, spreadsheets, notes, and uploads from being lost in chat history or informal folders.

## Problem this solves

During early Wregoe research, pre-build Rocha Liberty screenshots were remembered by the researcher but could not be reliably retrieved later from chat history. That failure exposed a core requirement:

The CRE must store evidence independently of ChatGPT, conversation history, or any single AI model.

## Core principles

1. Evidence is immutable.
2. Every evidence item gets a stable ID.
3. Files are stored before interpretation.
4. Metadata is searchable.
5. Observations are derived from evidence, not mixed into raw evidence.
6. Research Packages are derived groupings, not the raw source of truth.
7. Binary files must be backed up and hash-verified.

## Evidence IDs

Evidence items use IDs such as:

- EV-000001
- EV-000002
- EV-000003

Research packages use IDs such as:

- RP-000001
- RP-000002

Experiments use IDs such as:

- EXP-0001

## Evidence Vault workflow

1. Upload or import files.
2. Create an Evidence Batch.
3. Copy raw files into managed storage.
4. Compute SHA-256 hashes.
5. Record metadata in SQLite.
6. Assign evidence IDs.
7. Optionally link evidence to an experiment.
8. Extract observations.
9. Create or update a Research Package.
10. Publish analyst-reviewed evidence summaries to GitHub.

## Storage layout

Local development layout:

```text
cre-vault/
  vault.db
  raw/
    EV-000001/
      original.png
      metadata.json
    EV-000002/
      original.png
      metadata.json
  packages/
    RP-000001/
      package.json
      README.md
      evidence_register.csv
```

The GitHub repository should store knowledge and metadata, not necessarily all binary evidence files.

## Evidence item metadata

Minimum metadata:

- evidence_id
- evidence_type
- title
- system_name
- body_name
- facility_name
- experiment_id
- research_package_id
- phase: before / after / during / reference / unknown
- captured_at
- uploaded_at
- captured_by
- source_channel
- original_filename
- stored_path
- sha256
- mime_type
- file_size_bytes
- review_status
- notes

## Evidence batch

An evidence batch represents a group of files uploaded together.

Examples:

- 8 post-build Rocha Liberty screenshots
- 1 ZIP of pre-build A4 screenshots
- A journal file plus Market.json

A batch can later be split into multiple evidence items.

## Research Package

A Research Package is a curated grouping of evidence items related to an experiment or research question.

Example:

`RP-000001 - A4 High Tech Promotion After Pack`

A package may contain:

- before evidence
- after evidence
- notes
- extracted observations
- comparison tables
- analyst summary

Packages are derived from Evidence Vault items. They should never be the only location of raw evidence.

## Observation separation

The Evidence Vault stores raw evidence and metadata.

Observation extraction creates separate records such as:

- `Rocha Liberty shows High Tech x2 strong links`
- `Computer Components visible in commodity list`
- `Coats City High Tech Hub complete`

Observations must link back to the evidence item that supports them.

## Immediate MVP

The first implementation should be local and simple:

- SQLite database
- local file storage
- command line import tool
- SHA-256 hashing
- manual metadata fields
- simple search by system/body/facility/experiment
- export evidence summary Markdown to GitHub

## Later phases

- OCR/image extraction
- commodity list extraction
- before/after comparator
- web upload UI
- ed-finder integration
- semantic search
- automated Research Package generation
- analyst review dashboard

## Non-goals for MVP

- Public community uploads
- Full OCR automation
- AI classification without review
- Replacing GitHub knowledge documents
- Storing only file IDs from chat without binary preservation

## Hard rule

When Brian provides screenshots or other evidence, the first system action should be evidence registration, not analysis.

Expected response format:

```text
Evidence registered.
Batch: EB-000001
Evidence items: EV-000001 to EV-000008
Linked experiment: EXP-0001
Phase: after
Ready for analysis.
```
