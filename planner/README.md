# Planner Layer

This directory defines how future planning tools must consume knowledge safely.

## Key files

- `decision_support_model.md`
  Objective-first reasoning model.
- `planner_safety.md`
  Mandatory safety constraints.
- `planner_rules_register.md`
  Canonical extracted planner rules.
- `knowledge_projection_rules.md`
  Rules for turning research knowledge into planner-safe projections.
- `coverage_dimensions_register.md`
  The dimensions a planner should inspect before choosing new builds.
- `contextual_strategy_register.md`
  Reusable but non-universal strategy patterns extracted from the repository.
- `planner_risk_register.md`
  Canonical planner failure modes and required mitigations.
- `role_register.md`
  Canonical role concepts for bodies, stations, and facility groups.
- `architecture_pattern_register.md`
  Reusable architecture patterns and their prerequisites.
- `recommendation_schema_register.md`
  Required fields for planner recommendations.
- `objective_register.md`
  Canonical objective types for planner reasoning.
- `asset_category_register.md`
  Canonical asset categories used in coverage analysis.

## Use rule

Future planners should use this directory as a contract:

- what the planner may assume
- what it must block
- how it should expose uncertainty
- when it must suggest validation instead of commitment
