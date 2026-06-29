# Release Bundle Layout

This document defines the intended machine-usable export structure for a knowledge release bundle.

## Goals

- make knowledge releases reproducible
- keep provenance visible
- separate included planner-safe artifacts from working-state repository files
- give future tools a stable file layout

## Proposed bundle tree

```text
cre-knowledge-release/
  manifest.json
  release_notes.md
  schemas/
    observation.schema.json
    claim.schema.json
    mechanic.schema.json
    colony_state.schema.json
    planner_recommendation.schema.json
    knowledge_release_manifest.schema.json
  exports/
    mechanics.csv
    planner_rules.csv
    economy_rules.csv
    construction_rules.csv
    unknowns.csv
    contradictions.csv
    observations.csv
    claims.csv
    evidence_traceability.csv
    graph_nodes.csv
    graph_edges.csv
  docs/
    source_coverage_summary.md
    withheld_items.md
```

## File roles

### `manifest.json`

The top-level release manifest.
This is the entry point for machines.

### `release_notes.md`

Human-readable explanation of what changed in the release.

### `schemas/`

The exact schema contracts used by the release.
Future consumers should store these alongside the bundle so validation remains version-aware.

### `exports/`

Machine-usable flattened datasets derived from canonical repository registers.

Recommended exports:

- `mechanics.csv`
  Canonical mechanic catalogue and statuses.
- `planner_rules.csv`
  Planner-operational rules.
- `economy_rules.csv`
  Economy-facing rules.
- `construction_rules.csv`
  Construction-facing rules.
- `unknowns.csv`
  Release-visible unresolved questions.
- `contradictions.csv`
  Contradiction cases still visible to consumers.
- `observations.csv`
  Included structured observations.
- `claims.csv`
  Included structured claims.
- `evidence_traceability.csv`
  Evidence-to-mechanic mapping.
- `graph_nodes.csv`
  Graph nodes for the included release.
- `graph_edges.csv`
  Graph edges for the included release.

### `docs/`

Supporting human-readable release notes that are too verbose for the manifest.

## Inclusion rule

The bundle should include only the items explicitly listed by the manifest as included.

Working-state repository files may contain:

- draft material
- unresolved exploration
- future backlog items
- documentation not meant for planner consumption

Those should not automatically enter the release bundle.

## Withheld-items rule

If a mechanic, rule, or claim is intentionally withheld:

- keep it out of the exported planner-safe files
- mention it in `manifest.json`
- explain the reason in `docs/withheld_items.md`

## Current repository mapping

The current repository can already supply most bundle inputs from:

- `mechanics/index.md`
- `planner/planner_rules_register.md`
- `mechanics/economy_rules_register.md`
- `mechanics/construction_rules_register.md`
- `docs/unknowns_register.md`
- `docs/contradiction_register.md`
- `evidence/observation_register.csv`
- `evidence/claim_register.csv`
- `evidence/evidence_mechanic_traceability.csv`
- `ontology/knowledge_graph_nodes.csv`
- `ontology/knowledge_graph_edges.csv`

## Next step

The next useful implementation step after this layout is a bundle-building script or workflow that maps repository files into this structure deterministically.
