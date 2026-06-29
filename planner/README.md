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

## Use rule

Future planners should use this directory as a contract:

- what the planner may assume
- what it must block
- how it should expose uncertainty
- when it must suggest validation instead of commitment
