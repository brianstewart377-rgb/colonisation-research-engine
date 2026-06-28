# Planner safety

Future planners built on this repository must consume verified knowledge, not raw speculation.

## Required recommendation labels

Every recommendation must be marked as one of:

- `Confirmed`
- `Likely`
- `Experimental`
- `Unknown`

## Mandatory planner rules

The planner must:

- distinguish `Confirmed`, `Likely`, `Experimental`, and `Unknown`
- never invent unsupported mechanics
- never recommend impossible facilities
- avoid irreversible demolitions without evidence
- recommend experiments when confidence is insufficient

## Additional constraints

- Raw contradictory evidence must not be silently flattened into a single answer.
- Unsupported facility types must be blocked, not merely phrased as soft suggestions.
- Historical evidence must be labeled as historical when current state is unknown.
- Author-stated support relationships must not be promoted into hard economy-link facts without corroboration.
- If planner confidence is weak, the planner should suggest observation or experiment steps before suggesting commitment.
