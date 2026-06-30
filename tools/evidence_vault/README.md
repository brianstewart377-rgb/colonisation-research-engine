# Evidence Vault Tool

The first Evidence Vault implementation is a local command-line import tool.

It registers evidence before analysis by:

- creating the SQLite database automatically
- applying `schemas/evidence_vault_schema.sql`
- creating Evidence Batch and Evidence Item records
- copying raw files into managed storage
- hashing files with SHA-256
- detecting duplicates by SHA-256
- exporting a Markdown summary for the repository `evidence/` directory

## Location

The executable lives at `bin/cre-vault`.

Run it from the repository root with either:

```bash
./bin/cre-vault --help
```

or, if you want `cre-vault` on your shell path for the current terminal session:

```bash
export PATH="$PWD/bin:$PATH"
cre-vault --help
```

The tool uses Python 3 and only depends on the standard library.

## Import command

Example command:

```bash
./bin/cre-vault import ./incoming/rocha-liberty-after \
  --title "Rocha Liberty post High Tech build" \
  --system "Wregoe" \
  --body "A4" \
  --facility "Rocha Liberty" \
  --experiment "EXP-0001" \
  --phase after \
  --captured-by Brian
```

Equivalent command if `bin/` has been added to `PATH`:

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

## Stored outputs

The tool creates a managed local vault in the repository root:

```text
cre-vault/
  vault.db
  raw/
    EV-000001/
      screenshot-01.png
      metadata.json
    EV-000002/
      screenshot-02.png
      metadata.json
```

Each imported file is copied into its own `raw/EV-XXXXXX/` directory and keeps its original filename.

The Markdown batch summary is exported into `evidence/` using a filename such as:

```text
evidence/eb-000001-rocha-liberty-post-high-tech-build.md
```

## Supported metadata

The import command stores:

- `system`
- `body`
- `facility`
- `experiment`
- `phase`
- `captured_by`
- `uploaded_at`
- `source_channel`

Additional options:

- `--description`
- `--captured-at`
- `--uploaded-by`
- `--notes`

## Duplicate handling

Duplicate detection is based on SHA-256.

If a file hash already exists in the Evidence Vault:

- no new `evidence_item` row is created for that file
- no second raw copy is written
- the CLI prints the existing `EV-XXXXXX` identifier
- the Markdown summary records the duplicate mapping

If every file in the supplied folder is already known, the tool reports that no new evidence was registered and points to the existing evidence IDs instead.

## Command reference

```bash
./bin/cre-vault import SOURCE_DIR \
  --title "Batch title" \
  [--description "Batch description"] \
  [--system "System"] \
  [--body "Body"] \
  [--facility "Facility"] \
  [--experiment "EXP-0001"] \
  [--phase before|after|during|reference|unknown] \
  [--captured-by "Brian"] \
  [--captured-at "2026-06-29T12:00:00Z"] \
  [--source-channel "local_cli_import"] \
  [--uploaded-by "local-user"] \
  [--notes "Optional notes"]
```

## Non-goals for this MVP

- OCR
- AI classification
- web UI
- public uploads
- ed-finder integration
- automatic mechanic updates

This version only guarantees durable local registration of raw evidence before analysis.
