# Entity relationships

This document outlines the relationship model that should form the basis of the future knowledge graph.

It also records semantic guardrails where relationship confusion would create unsafe planner or runtime behavior.

## Core relationships

- `System HAS_BODY Body`
- `System HAS_COLONY_STATE Colony`
- `System HAS_FACILITY Facility`
- `System HAS_MARKET Market`
- `Facility LOCATED_ON Body`
- `Facility OCCUPIES Slot`
- `Facility USES_STATION_TYPE StationType`
- `Facility EXPOSES_ECONOMY Economy`
- `Facility PLAYS_ROLE Role`
- `Facility SELLS Commodity`
- `Facility BUYS Commodity`
- `Facility HAS_MARKET_LINK Facility`
- `Body HAS_SURFACE_SLOT SurfaceSlot`
- `Body HAS_ORBITAL_CAPACITY Orbital`
- `Body HAS_MODIFIER BodyModifier`
- `Market EXPOSES Commodity`
- `Market INFLUENCED_BY Economy`
- `Market INFLUENCED_BY Facility`
- `Architecture APPLIES_TO System`
- `Architecture USES Facility`
- `Strategy TARGETS CoverageGap`
- `Strategy USES Role`
- `Recommendation SELECTS Strategy`
- `Recommendation SELECTS Architecture`
- `Recommendation MAY_BUILD Facility`

## Evidence relationships

- `Source PRODUCES Evidence`
- `Evidence SUPPORTS Observation`
- `Evidence SUPPORTS Claim`
- `Evidence CONTRADICTS Observation`
- `Evidence LIMITS Claim`
- `Observation DERIVED_FROM Source`
- `Observation ABOUTS System`
- `Observation ABOUTS Body`
- `Observation ABOUTS Facility`
- `Claim SYNTHESIZES Observation`
- `Claim ABOUTS System`
- `Claim ABOUTS Body`
- `Claim ABOUTS Facility`
- `Evidence INFORMS Decision`

## Mechanic relationships

- `Mechanic SUPPORTED_BY Observation`
- `Mechanic SUPPORTED_BY Claim`
- `Mechanic CONTRADICTED_BY Observation`
- `Mechanic TESTED_BY Experiment`
- `Theory CONTAINS Mechanic`
- `Mechanic APPLIES_TO StationType`
- `Mechanic APPLIES_TO Economy`
- `PlannerRule DEPENDS_ON Mechanic`
- `PlannerRule QUALIFIED_BY Decision`

## Experiment relationships

- `Experiment TESTS Mechanic`
- `Experiment USES Evidence`
- `Experiment CHANGES Facility`
- `Experiment OBSERVES System`
- `Experiment OBSERVES Body`
- `Experiment OBSERVES Facility`
- `Experiment PRODUCES Observation`
- `Decision CITES Evidence`
- `Decision CITES Mechanic`
- `Decision CITES PlannerRule`
- `Decision CITES Experiment`
- `Decision AFFECTS System`
- `Decision AFFECTS Body`
- `Decision AFFECTS Facility`

## Trust and planning relationships

- `ConfidenceRecord MEASURES Observation`
- `ConfidenceRecord MEASURES Claim`
- `ConfidenceRecord MEASURES Mechanic`
- `ConfidenceRecord MEASURES Experiment`
- `ConfidenceRecord MEASURES Recommendation`
- `KnowledgeProjection DERIVED_FROM Mechanic`
- `KnowledgeProjection DERIVED_FROM Observation`
- `KnowledgeProjection DERIVED_FROM Claim`
- `KnowledgeProjection DERIVED_FROM Decision`
- `PlannerRecommendation USES KnowledgeProjection`
- `PlannerRecommendation AFFECTS System`
- `PlannerRecommendation AFFECTS Facility`
- `Contradiction TARGETS Observation`
- `Contradiction TARGETS Claim`
- `Contradiction TARGETS Mechanic`
- `Contradiction TARGETS KnowledgeProjection`

## Data-boundary relationships

- `ResearchEvidence FEEDS Observation`
- `OperationalData PRESENTS KnowledgeProjection`
- `UserData REFERENCES System`
- `UserData REFERENCES Body`
- `UserData REFERENCES Facility`
- `UserData STORES PlannerPreference`
- `UserData STORES SavedPlan`

## Relationship rules

- Facility names alone are not enough to resolve identity.
- Contradictions should coexist with supported claims until resolved.
- The planner should depend on Knowledge Projections, not directly on raw observations.
- Relationship edges should be version-aware when patch context matters.

## Non-equivalence and semantic guardrails

- `Facility LOCATED_ON Body` does not mean `Facility == Body`.
- `Facility OCCUPIES Slot` does not mean `Slot == Facility`.
- `Facility USES_STATION_TYPE StationType` does not mean `Facility == StationType`.
- `Facility EXPOSES_ECONOMY Economy` does not mean `Economy == Role`.
- `Evidence SUPPORTS Observation` does not mean `Evidence == Observation`.
- `Claim SYNTHESIZES Observation` does not mean `Claim == Mechanic`.
- `PlannerRule DEPENDS_ON Mechanic` does not mean `PlannerRule == Mechanic`.
- `Decision CITES Evidence` does not mean `Decision == Recommendation`.
- `KnowledgeProjection DERIVED_FROM Observation` does not mean raw observations are planner-safe by default.
- `UserData REFERENCES Facility` does not mean user-owned state may redefine canonical facility semantics.

## Planner-safety rules

- Empty or predicted slot capacity must not be treated as built facility state.
- Station type should constrain planner reasoning, but should not be mistaken for final inherited economy outcome.
- Strong and weak links should remain relationship classes, not substitute facility attributes.
- Market outcomes should be modeled as influenced by economy, links, and body context rather than as direct synonyms for any single upstream concept.
