# Ontology Layer

This directory defines the knowledge model used by the Colonisation Research Engine.

## Key files

- `entities.md`
  Core entities such as System, Body, Facility, Mechanic, Experiment, Evidence, and Knowledge Projection.
- `relationships.md`
  Canonical graph edges between those entities.
- `roles_assets_strategies.md`
  Planning vocabulary above individual facilities.
- `glossary.md`
  Canonical term register for Phase 2 extraction.
- `confidence_model_register.md`
  Confidence components, bands, and confidence-handling rules.
- `identity_and_provenance_rules.md`
  Canonical identity, snapshot, and provenance rules.
- `knowledge_graph.md`
  Machine-readable graph layer overview.
- `knowledge_graph_nodes.csv`
  Current graph nodes.
- `knowledge_graph_edges.csv`
  Current graph edges.

## Use rule

Future tooling should treat this directory as the canonical conceptual model of the repository, not just as supporting prose.
