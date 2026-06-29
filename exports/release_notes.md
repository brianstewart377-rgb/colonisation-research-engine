# Prototype Release Notes

This is a prototype release-oriented export snapshot, not a final public knowledge release.

## Included export groups

- canonical mechanics
- planner rules
- unknowns
- contradictions
- observations
- claims
- evidence traceability
- knowledge graph nodes and edges

## Important limitations

- absent primary artifacts remain absent and are not silently reconstructed
- graph exports are copied from the current repository graph layer, not from a separate release-only graph build
- planner-safe publication policy is still partially governed by open decisions in `docs/governance_decision_register.md`

## Current purpose

This prototype export folder exists to prove that the repository can already emit a structured release-shaped bundle before a dedicated build pipeline is implemented.
