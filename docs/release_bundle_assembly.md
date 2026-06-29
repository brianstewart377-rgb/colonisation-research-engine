# Release Bundle Assembly

This document defines the deterministic release-bundle assembly command.

## Build command

```bash
python3 tools/build_release_bundle.py --output exports
```

This command:

- reads only canonical repository registers and source files
- writes deterministic CSV exports in a fixed order
- updates `exports/export_manifest.json`
- validates generated CSV row counts against the manifest
- fails loudly if a required source file or required register field is missing

## Validation-only command

```bash
python3 tools/build_release_bundle.py --output exports --validate-only
```

This command does not rebuild outputs.
It validates the existing assembled bundle against the manifest.

## Current generated exports

The builder currently assembles:

- `mechanics.csv`
- `planner_rules.csv`
- `economy_rules.csv`
- `construction_rules.csv`
- `planner_risks.csv`
- `governance_decisions.csv`
- `unknowns.csv`
- `contradictions.csv`
- `observations.csv`
- `claims.csv`
- `claim_provenance_links.csv`
- `evidence_traceability.csv`
- `live_verification_matrix.csv`
- `graph_nodes.csv`
- `graph_edges.csv`

## Design rule

The builder is intentionally strict.
If a canonical register changes shape and the parser no longer matches it, the command should fail rather than quietly producing damaged exports.
