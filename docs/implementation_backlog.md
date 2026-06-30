# Implementation Backlog

This backlog converts the repository's architecture, manual gaps, schema work, and governance dependencies into implementation-oriented work items.

## Priority guide

- `P0` foundational, blocks multiple later layers
- `P1` high-value and near-term
- `P2` important but not immediately blocking

## IB-0001 - Core repository-to-database provenance model

- Priority: `P0`
- Source: `architecture/colonisation_intelligence_platform_architecture.md`
- Goal: Implement durable tables or equivalent storage for sources, evidence, observations, claims, mechanics, contradictions, experiments, and planner-safe knowledge.
- Why now: Most later tooling depends on durable provenance objects.
- Depends on: current schema documents

## IB-0002 - Claim, observation, mechanic, and knowledge-release schemas

- Priority: `P0`
- Source: `schemas/README.md`, `schemas/colony_state_schema.md`
- Goal: Add formal draft schemas for observations, claims, mechanics, planner recommendations, and knowledge-release manifests.
- Why now: The colony-state schema is now present; the surrounding contracts are the next missing pieces.
- Depends on: `schemas/colony_state.schema.json`

## IB-0003 - Current-state ingest from bulk public sources

- Priority: `P1`
- Source: `evidence/source_priority_register.csv`, `docs/manual_research_gaps.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Goal: Design the ingestion path for Spansh and EDSM current-state warehousing, with explicit provenance and patch-era tagging.
- Why now: Future planners need real galaxy context, not only local research records.
- Depends on: `IB-0001`

## IB-0004 - Analyst-side evidence entry workflow

- Priority: `P1`
- Source: `architecture/evidence_vault.md`, `docs/governance_decision_register.md`, `docs/manual_research_gaps.md`
- Goal: Define and implement the canonical workflow for entering screenshot-backed evidence, manual observations, and linked review status while OCR remains out of scope.
- Why now: Image-backed evidence is already central to the repository.
- Depends on: `GD-0005`, `IB-0001`

## IB-0005 - Contradiction and identity review surface

- Priority: `P1`
- Source: `docs/contradiction_register.md`, `docs/anomaly_register.md`, `docs/governance_decision_register.md`
- Goal: Provide a review surface or workflow for contradiction cases, identity collisions, and public-data anomalies.
- Why now: The repository already has durable contradiction and anomaly objects that need safe review workflows.
- Depends on: `GD-0004`, `IB-0001`

## IB-0006 - Planner-safe knowledge publication pipeline

- Priority: `P1`
- Source: `planner/knowledge_projection_rules.md`, `ontology/confidence_model_register.md`, `docs/governance_decision_register.md`
- Goal: Implement the publish and unpublish path from mechanics and claims into planner-safe knowledge projections.
- Why now: The planner should consume projections, not raw evidence.
- Depends on: `GD-0001`, `GD-0002`, `IB-0001`

## IB-0007 - Planner recommendation object and validation

- Priority: `P1`
- Source: `planner/recommendation_schema_register.md`, `planner/objective_register.md`, `planner/asset_category_register.md`
- Goal: Implement a structured planner recommendation object that conforms to the repository's reasoning hierarchy and required fields.
- Why now: The schema for safe recommendation content is now explicit.
- Depends on: `IB-0002`, `IB-0006`

## IB-0008 - Body-linkage uncertainty handling

- Priority: `P1`
- Source: `docs/unknowns_register.md`, `schemas/colony_state_schema.md`, `docs/governance_decision_register.md`
- Goal: Implement a consistent representation for `resolved`, `system_only`, and `uncertain` body linkage across evidence and state records.
- Why now: Public-source incompleteness is one of the most important current data limitations.
- Depends on: `GD-0003`, `IB-0001`

## IB-0009 - Knowledge graph export and query layer

- Priority: `P2`
- Source: `ontology/knowledge_graph.md`, `ontology/knowledge_graph_nodes.csv`, `ontology/knowledge_graph_edges.csv`
- Goal: Convert the current CSV graph layer into a queryable export or graph service for future tools.
- Why now: The graph is now rich enough to support tooling, but it is not yet operational.
- Depends on: `IB-0001`

## IB-0010 - Evidence Vault binary workflow completion

- Priority: `P2`
- Source: `architecture/evidence_vault.md`, `docs/manual_research_gaps.md`
- Goal: Complete the gap between current evidence records and durable binary storage plus review metadata for screenshots and uploaded artifacts.
- Why now: The repository already references binary evidence that is not yet durably co-located with every record.
- Depends on: `IB-0004`

## IB-0011 - Direct primary-artifact re-ingestion

- Priority: `P1`
- Source: `docs/source_coverage_register.md`, `docs/manual_research_gaps.md`
- Goal: Reattach the missing Mega Guide, DaftMav spreadsheet, strong-and-weak-links reference, and dependency flowchart, then run a direct extraction pass.
- Why now: Current repository extraction is honest but still indirect for those major sources.
- Depends on: access to the source files

## IB-0012 - Live-verification result ingestion

- Priority: `P2`
- Source: `experiments/live_verification_register.md`, `experiments/verification_protocols.md`
- Goal: Provide a structured ingestion path for actual experiment results once Brian performs the live tests.
- Why now: The verification queue and protocols are now ready, but result capture is not yet formalized.
- Depends on: `IB-0001`, future test runs

## IB-0013 - CRE Digital Twin

- Priority: `P2`
- Source: `architecture/cre_digital_twin.md`, `schemas/colony_state_schema.md`, `planner/decision_support_model.md`
- Goal: Design and later implement a single-system Digital Twin that exposes body hierarchy, slots, facilities, lifecycle state, construction progress, economy roles, market links, commodities, evidence links, experiment links, planner decisions, history, confidence, warnings, and unknowns as one planner-safe engineering surface.
- Why now: The repository now has enough evidence, planner, contradiction, unknown, and colony-state structure to define the future feature clearly without building it yet.
- Depends on: `IB-0001`, `IB-0003`, `IB-0006`, `IB-0012`, `schemas/colony_state.schema.json`
