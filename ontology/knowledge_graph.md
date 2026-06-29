# Knowledge Graph Layer

The repository now includes a lightweight graph representation for Phase 2 extraction:

- `ontology/knowledge_graph_nodes.csv`
- `ontology/knowledge_graph_edges.csv`

## Purpose

These files provide a machine-readable cross-link layer between:

- mechanics
- evidence
- experiments
- planner rules
- glossary terms
- contradiction cases
- live-verification tasks

## Node model

`knowledge_graph_nodes.csv` uses:

- `node_id`
- `node_type`
- `title`
- `status`
- `category`
- `source_ref`
- `path_or_ref`

## Edge model

`knowledge_graph_edges.csv` uses:

- `source_id`
- `relationship`
- `target_id`
- `basis`

## Intended use

- navigation and search
- future graph database import
- planner knowledge projection
- contradiction tracking
- evidence-to-mechanic traceability

This graph is intentionally conservative.
If a relationship is not supported by repository evidence, it should remain absent rather than be guessed.
