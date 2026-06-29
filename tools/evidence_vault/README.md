# Evidence Vault Tool

This directory will contain the first local Evidence Vault tooling.

The initial tool should be deliberately simple: a local command-line utility that imports files into a managed folder, records metadata in SQLite, hashes files, and exports Markdown summaries for analyst review.

## MVP command shape

Example command:

```bash
cre-vault import ./incoming/rocha-liberty-after \
  --title "Rocha Liberty post High Tech build" \
  --system "Wregoe" \
  --body "A4" \
  --facility "Rocha Liberty" \
  --experiment "EXP-0001" \
  --phase after \
  --captured-by Brian
```

Expected result:

```text
Evidence registered.
Batch: EB-000001
Evidence items: EV-000001 to EV-000008
Linked experiment: EXP-0001
Phase: after
Ready for analysis.
```

## Required MVP behaviour

- Create the SQLite database if missing.
- Apply `schemas/evidence_vault_schema.sql`.
- Create a batch ID.
- Create one evidence ID per file.
- Copy files into managed storage.
- Preserve the original filename.
- Compute SHA-256 for every file.
- Store metadata.
- Detect duplicate files by SHA-256.
- Export a Markdown evidence summary.

## Suggested local storage

```text
cre-vault/
  vault.db
  raw/
    EV-000001/
      original.png
      metadata.json
  packages/
    RP-000001/
      README.md
      evidence_register.csv
```

## Search commands

Future command examples:

```bash
cre-vault find --system Wregoe --facility "Rocha Liberty"
cre-vault find --experiment EXP-0001
cre-vault find --tag HighTech
```

## Export command

```bash
cre-vault export-summary EV-000001
cre-vault export-package RP-000001
```

The exported Markdown can then be committed into the GitHub repository under `evidence/` or `research_packages/`.

## Non-goals for the first version

- OCR
- image recognition
- web UI
- public uploads
- AI classification
- automatic mechanic changes

The first version only guarantees that evidence cannot be lost.
