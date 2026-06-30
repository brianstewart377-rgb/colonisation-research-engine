# Colony State Schema

This document explains the documentation-first colony-state schema in `schemas/colony_state.schema.json`.

## Purpose

The repository already contains:

- evidence
- observations
- claims
- mechanics
- planner rules
- unknowns

The colony-state schema is the future structured contract that ties those layers to an actual system snapshot.

It is designed for:

- current-state ingestion
- analyst review
- planner-safe state loading
- later database implementation

It is not a production database schema yet.

## Design rules

### Separate state from theory

The colony-state object should say what is currently observed or projected about a colony, not silently collapse those facts into mechanic truth.

### Preserve uncertainty

Fields such as `location_resolution`, `snapshot_kind`, `confidence`, `review_status`, and `unknown_refs` exist so the schema can represent partial knowledge honestly.

### Keep provenance attached

Most state-bearing objects include `source_refs`, while the top-level object can also carry `evidence_refs`, `claim_refs`, and `unknown_refs`.

### Respect planner safety

`planner_constraints` is part of the state object because unsupported actions and hard feasibility limits should be loaded together with state, not invented later by the planner.

## Main sections

### Top level

- `schema_version`
- `knowledge_version`
- `state_timestamp`
- `patch_context`
- `system`
- `bodies`
- `facilities`

These fields make the object version-aware and patch-aware.

### System

The `system` object captures overall colony state such as:

- architect attribution
- population
- security
- wealth
- development
- technology
- living standards

It also includes `state_confidence` and `source_refs`.

### Bodies

Each body includes:

- identity
- body class
- orbital-only or surface-build constraints
- slot summary
- body-economy hypotheses
- body modifiers
- role references

This matches the repository's view that body type strongly constrains valid planning.

Semantic note:

- A `Body` is a physical context.
- An `Orbital` is usually a placement or capacity class on or above a body.
- A `slot` is capacity, not proof of a built facility.

### Facilities

Each facility includes:

- identity
- facility or station type
- body linkage when known
- `location_resolution`
- state such as `preview`, `planned`, `under_construction`, or `completed`
- role, service, and economy references

This explicitly prevents the repository from confusing preview state, proposal state, and finished state.

Semantic notes:

- `facility_type` describes the facility class or family.
- `station_type` is a subtype or taxonomy label such as Orbis or Dodec when relevant.
- `station_type` is not the same thing as final inherited economy state.
- `economy_refs` should be interpreted as observed or projected economy state references, not as economy-role labels.

### Market links

`market_links` captures:

- source and target facility references
- link economy
- strong or weak strength
- link count
- whether the visible link may be aggregated rather than direct

This is intentionally compatible with current unresolved routing questions.

Semantic note:

- A market link is a relationship object, not a facility attribute and not an economy by itself.

### Economy snapshots

`economy_snapshots` stores observed, preview, or predicted economy values by system, body, or facility.

This makes it possible to preserve:

- preview values
- live observed values
- analyst predictions

without flattening them into one truth state.

Semantic note:

- Economy snapshots record state or hypothesis about economy exposure.
- They do not directly encode planner roles such as `Industrial Anchor` or `High Tech Support`.

### Commodity observations

These records preserve whether a commodity was:

- visible for sale
- visible for purchase
- missing
- predicted
- unknown

This fits the repository's current commodity-evidence style.

### Planner constraints

This section exists because the planner must load:

- hard blocks
- strong warnings
- softer caveats

from the knowledge base rather than reconstructing them ad hoc.

## Wregoe-friendly features

This schema deliberately includes support for the repository's hardest current cases:

- Water World orbital-only constraints
- uncertain body linkage on public evidence
- placeholder and planned facility states
- weak versus strong link representation
- preview versus observed versus predicted economy state
- explicit unknown references

## Recommended next schemas

After this colony-state schema, the most useful follow-up schemas would be:

- observation schema
- claim schema
- mechanic schema
- planner recommendation schema
- knowledge release manifest schema
