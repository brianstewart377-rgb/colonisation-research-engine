# Prototype Exports

This directory contains prototype machine-usable exports derived from the repository's canonical registers.

These files are not yet a final published knowledge-release bundle.
They are working export outputs that align with the release-bundle layout defined in `docs/release_bundle_layout.md`.

The deterministic assembly command is:

- `python3 tools/build_release_bundle.py --output exports`

Validation-only:

- `python3 tools/build_release_bundle.py --output exports --validate-only`

## Current exports

- `mechanics.csv`
- `planner_rules.csv`
- `economy_rules.csv`
- `construction_rules.csv`
- `planner_risks.csv`
- `governance_decisions.csv`
- `decisions.csv`
- `unknowns.csv`
- `contradictions.csv`
- `observations.csv`
- `claims.csv`
- `claim_provenance_links.csv`
- `evidence_traceability.csv`
- `live_verification_matrix.csv`
- `graph_nodes.csv`
- `graph_edges.csv`
- `export_manifest.json`
- `release_notes.md`
- `source_coverage_summary.md`
- `withheld_items.md`

## Source rule

Each export in this directory should be derivable from a canonical source register elsewhere in the repository.

This directory should not become the source of truth.
The source of truth remains the canonical registers and indexes.
