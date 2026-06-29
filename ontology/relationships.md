# Entity relationships

This document outlines the relationship model that should form the basis of the future knowledge graph.

## Core relationships

- `System HAS_BODY Body`
- `System HAS_FACILITY Facility`
- `Facility LOCATED_ON Body`
- `Facility USES_STATION_TYPE StationType`
- `Facility EXPOSES_ECONOMY Economy`
- `Facility SELLS Commodity`
- `Facility BUYS Commodity`
- `Facility HAS_MARKET_LINK Facility`
- `Architecture APPLIES_TO System`
- `Architecture USES Facility`

## Evidence relationships

- `Source PRODUCES Evidence`
- `Evidence SUPPORTS Observation`
- `Evidence CONTRADICTS Observation`
- `Observation DERIVED_FROM Source`
- `Observation ABOUTS System`
- `Observation ABOUTS Body`
- `Observation ABOUTS Facility`
- `Evidence INFORMS Decision`

## Mechanic relationships

- `Mechanic SUPPORTED_BY Observation`
- `Mechanic CONTRADICTED_BY Observation`
- `Mechanic TESTED_BY Experiment`
- `Theory CONTAINS Mechanic`
- `Mechanic APPLIES_TO StationType`
- `Mechanic APPLIES_TO Economy`

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
- `ConfidenceRecord MEASURES Mechanic`
- `ConfidenceRecord MEASURES Experiment`
- `KnowledgeProjection DERIVED_FROM Mechanic`
- `KnowledgeProjection DERIVED_FROM Observation`
- `PlannerRecommendation USES KnowledgeProjection`
- `PlannerRecommendation AFFECTS System`
- `PlannerRecommendation AFFECTS Facility`
- `Contradiction TARGETS Observation`
- `Contradiction TARGETS Mechanic`
- `Contradiction TARGETS KnowledgeProjection`

## Relationship rules

- Facility names alone are not enough to resolve identity.
- Contradictions should coexist with supported claims until resolved.
- The planner should depend on Knowledge Projections, not directly on raw observations.
- Relationship edges should be version-aware when patch context matters.
