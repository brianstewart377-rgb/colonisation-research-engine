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
    decision.schema.json
    mechanic.schema.json
    colony_state.schema.json
    planner_recommendation.schema.json
    knowledge_release_manifest.schema.json
  exports/
    mechanics.csv
    planner_rules.csv
    economy_rules.csv
    construction_rules.csv
    planner_risks.csv
    governance_decisions.csv
    decisions.csv
    unknowns.csv
    contradictions.csv
    observations.csv
    claims.csv
    claim_provenance_links.csv
    evidence_traceability.csv
    live_verification_matrix.csv
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
- `planner_risks.csv`
  Planner failure modes and mitigations.
- `governance_decisions.csv`
  Open governance gates that still affect release policy.
- `decisions.csv`
  Accepted, rejected, implemented, or superseded engineering decisions with linked evidence and planner context.
- `unknowns.csv`
  Release-visible unresolved questions.
- `contradictions.csv`
  Contradiction cases still visible to consumers.
- `observations.csv`
  Included structured observations.
- `claims.csv`
  Included structured claims.
- `claim_provenance_links.csv`
  Explicit claim provenance edges.
- `evidence_traceability.csv`
  Evidence-to-mechanic mapping.
- `live_verification_matrix.csv`
  Current machine-readable live-verification queue.
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
- `planner/planner_risk_register.md`
- `docs/governance_decision_register.md`
- `docs/decision_register.md`
- `evidence/observation_register.csv`
- `evidence/claim_register.csv`
- `evidence/claim_provenance_links.csv`
- `evidence/evidence_mechanic_traceability.csv`
- `experiments/live_verification_matrix.csv`
- `ontology/knowledge_graph_nodes.csv`
- `ontology/knowledge_graph_edges.csv`

## Current builder

The repository now includes a deterministic bundle builder:

- `tools/build_release_bundle.py`
- `docs/release_bundle_assembly.md`
