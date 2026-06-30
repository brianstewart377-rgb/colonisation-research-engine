# Mechanics catalogue

Every mechanic should eventually live in its own document in this directory.

A mechanic document should contain:

- description
- evidence
- confidence
- experiments
- contradictions
- patch history

## Why this matters

Mechanics are revisable knowledge objects, not static rules. They must be traceable to evidence, vulnerable to contradiction, and anchored to patch context.

## Suggested mechanic document shape

- `Mechanic ID`
- `Name`
- `Status`
- `Description`
- `Scope`
- `Evidence supporting it`
- `Negative evidence and failed predictions`
- `Experiments run`
- `Contradictions`
- `Last verified version/date`
- `Confidence score and rationale`
- `Notes for planner-safe usage`

## Canonical navigation

Use `mechanics/index.md` as the canonical mechanic register.

The repository may contain older draft mechanic files or renumbered records as the catalogue is normalised over time. The index is the authoritative mapping for current mechanic IDs.

For rule-level consumption, use:

- `mechanics/economy_rules_register.md`
- `mechanics/construction_rules_register.md`
- `mechanics/mechanic_dependency_register.md`
