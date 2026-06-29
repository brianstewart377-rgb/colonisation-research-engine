# Evidence Layer

This directory stores evidence records, source-analysis outputs, and evidence governance artifacts.

## Key files

- `EV-*.md`
  Canonical evidence records tied to screenshots, previews, reference packs, or other source-backed artifacts.
- `source_catalog.md`
  High-level catalogue of important source families.
- `source_authority_register.md`
  Canonical rules for how different source classes should be treated.
- `source_priority_register.csv`
  Ranked first-wave and second-wave source priority list for future tooling.
- `real_colony_shortlist.csv`
  Named real-colony inspection targets extracted from the source review.
- `build_diary_shortlist.csv`
  High-value public build-diary and project-thread shortlist.
- `colonisation_ai_data_sources_review.md`
  Deep source review and ingestion-order analysis.

## Evidence rules

- Raw source data must remain separate from parsed observations.
- Narrative evidence is allowed, but it must be confidence-labeled.
- Same-name facilities across systems must be treated as potential collisions.
- Direct live evidence outranks secondary interpretation when they conflict.

## Navigation rule

When a planner, analyst, or future tool wants to know whether a claim comes from live evidence, source-review policy, or community interpretation, start in this directory first.
