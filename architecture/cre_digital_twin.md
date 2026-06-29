# CRE Digital Twin

This document defines the future-feature design for the CRE Digital Twin.

It is a backlog and architecture document only.

It does not implement the feature.
It does not modify the existing system map.
It does not add a new release system.
It does not define production UI code.

## Purpose

The CRE Digital Twin is the future interactive colony-engineering view for a single system.

Its job is to make the repository's structured research legible as a navigable engineering surface without flattening uncertainty or pretending the current knowledge base is a perfect simulation.

The Digital Twin should let a researcher or planner inspect:

- system bodies
- body hierarchy
- slot availability and lane constraints
- built, planned, under-construction, demolished, and historical facilities
- construction progress and build sequencing
- economy roles and body/facility purpose
- market links and routing confidence
- commodities and coverage state
- evidence links and claim support
- experiment links and pending verification work
- planner decisions, assumptions, and caveats
- timeline and change history
- confidence, warnings, contradictions, and unknowns

## What it is not

The Digital Twin is not:

- the existing astronomical system map
- a galaxy viewer
- a full 3D orbital simulator
- a real-time game-state mirror
- a replacement for mechanics, evidence, contradictions, or planner registers
- a production implementation plan for a full application rewrite

The Digital Twin should be treated as a future system-state and reasoning surface, not as a prettier map.

## Difference from the existing system map

The existing system map should continue to focus on orientation and body/facility visibility.

The Digital Twin is different in kind, not just in appearance.

### Existing system map

The current map is primarily a navigation and planning surface.

It should remain focused on:

- current body layout
- slot context
- facility placement context
- immediate planner interactions

### Digital Twin

The Digital Twin should be a stateful research view.

It should answer questions such as:

- What is built here now?
- What used to be built here?
- What is planned versus merely proposed?
- What evidence supports each part of the picture?
- Which links are inferred rather than directly observed?
- Which planner decisions depend on weak mechanics or unresolved unknowns?
- What changed over time?

The Digital Twin therefore needs explicit provenance, confidence, history, and caution layers that the current map should not try to absorb.

## Design principles

### Preserve uncertainty

The Digital Twin must never silently promote inferred, preview-only, or recommendation-level knowledge into confirmed live truth.

### Separate state from theory

Mechanics explain how the colony may behave.
The Digital Twin shows what is believed, observed, planned, or disputed about a specific system.

### Keep provenance visible

Every non-trivial visual element should be traceable back to evidence, claims, mechanics, experiments, planner rules, or unknowns.

### Support history, not only snapshot state

The Twin should represent both the current engineering picture and the path that produced it.

### Planner-safe by construction

Warnings, contradictions, confidence, and unresolved questions must be first-class objects in the Twin.

### Do not require a perfect simulation engine

The first versions should be explainable and inspectable before they are ambitious.

## MVP scope

The MVP should be deliberately narrow.

It should cover one system at a time and present a trustworthy engineering snapshot with visible uncertainty.

### MVP user outcomes

The MVP should let a user:

1. inspect the body tree of a system
2. see slot counts and lane availability by body
3. see facilities by state:
   - built
   - planned
   - under construction
   - demolished
4. inspect economy role labels and facility role labels
5. inspect market links with strength and confidence
6. inspect commodity coverage at a system/body/facility summary level
7. open evidence, claim, experiment, contradiction, unknown, and planner references from the affected object
8. inspect a simple timeline/history panel for major colony events and planner decisions
9. see visible confidence, warnings, and unresolved items

### MVP view boundaries

The MVP should include:

- one current twin snapshot per system
- one historical event stream for that system
- one explicit distinction between:
  - observed state
  - planned state
  - inferred state
  - projected/planner state

The MVP should not try to be a live simulation.

## Later and advanced scope

These are good future directions, but they should not be part of the MVP.

### Later scope

- compare two twin snapshots across patch dates
- filter the twin by evidence confidence or source class
- show commodity production/consumption flows at a finer level
- show explicit demolition/rebuild chains
- show planner alternatives side by side
- support body-level what-if overlays

### Advanced scope

- timeline scrubbing across many historical states
- interactive market-link tracing with hypothesis branches
- simulation overlays for predicted outcomes versus observed outcomes
- contradiction heatmaps
- patch-era replay views
- comparative multi-system twin analysis
- external API/plugin consumers of the twin object

## Required data model

This document does not create a new schema file.

Instead, it defines the required data model that a future implementation should assemble from the existing CRE layers.

The Digital Twin should likely be built on top of the current colony-state concepts plus explicit history and reasoning overlays.

### Top-level object

Recommended conceptual object:

`digital_twin_snapshot`

Suggested top-level sections:

- `twin_version`
- `knowledge_version`
- `generated_at`
- `patch_context`
- `system`
- `body_tree`
- `facilities`
- `market_links`
- `commodity_state`
- `planner_state`
- `timeline`
- `warnings`
- `unknowns`
- `contradictions`
- `supporting_refs`

### System section

The `system` section should include:

- system name and identity
- summary colony metrics where known
- overall twin confidence
- current snapshot label
- evidence and claim references for the system-level state

### Body tree section

The `body_tree` section should include, per body:

- stable body identity
- parent/child relationship
- body type and subtype
- buildability constraints
- slot summary:
  - orbital
  - surface
  - unknown
- body role labels
- body economy hypotheses or observed economy state
- body confidence
- relevant evidence, claim, unknown, and contradiction references

### Facilities section

Each facility object should include:

- stable local facility identity
- display label
- facility type and variant
- linked body id when known
- lane:
  - orbital
  - surface
  - unknown
- lifecycle state:
  - built
  - planned
  - under_construction
  - demolished
  - inferred_existing
  - projected
- build order where relevant
- construction progress
- role labels
- economy role or contribution labels
- services
- commodity contributions
- evidence/claim/experiment/planner references
- confidence and warning fields

### Market links section

Each market-link object should include:

- source facility id
- target facility id
- link type:
  - strong
  - weak
  - inferred
- directionality
- aggregation caveat
- evidence source
- confidence
- linked unknowns or contradictions where appropriate

### Commodity state section

This should include system, body, or facility-scoped commodity records with:

- commodity name
- status:
  - observed_available
  - observed_missing
  - predicted_available
  - expected_from_role
  - unknown
- source scope
- evidence and claim references
- confidence

### Planner state section

This should make the planner legible rather than hidden.

Suggested objects:

- active objective
- planner decisions
- blocked options
- recommended role architecture
- confidence band
- planner warnings
- what would change the recommendation

### Timeline section

The `timeline` should be event-based, not a full replay engine.

Each event should include:

- timestamp or patch-era label
- event type
- body/facility target
- prior state
- new state
- rationale
- evidence/experiment/planner references

Example event types:

- facility_built
- facility_planned
- facility_demolished
- facility_reclassified
- market_link_observed
- experiment_recorded
- planner_decision_recorded
- contradiction_opened

### Warning and unknown sections

Warnings and unknowns must remain visible at twin level.

The twin should support both:

- local warnings attached to objects
- system-wide warnings and unresolved questions

## Minimum object relationships

The Digital Twin must be able to join:

- body -> body
- facility -> body
- facility -> market_link -> facility
- facility -> commodity state
- system/body/facility -> evidence
- system/body/facility -> claims
- system/body/facility -> experiments
- planner decision -> claims/mechanics/unknowns
- timeline event -> evidence/planner decision/facility

## Wregoe example JSON

This is an example JSON shape for Wregoe.

It is illustrative only.

It is not a schema.
It is not a final API contract.
It is not complete enough for production use.

```json
{
  "twin_version": "draft-0.1",
  "knowledge_version": "CRE Knowledge v0.x",
  "generated_at": "2026-06-29T00:00:00Z",
  "patch_context": {
    "label": "post-colonisation launch",
    "patch_confidence": "medium"
  },
  "system": {
    "name": "Wregoe",
    "state_confidence": "medium",
    "evidence_refs": ["EV-0001", "EV-0002", "EV-0003", "EV-0004"],
    "claim_refs": ["CL-0001", "CL-0002", "CL-0003"],
    "unknown_refs": ["U-0001", "U-0002"]
  },
  "body_tree": [
    {
      "body_id": "A4",
      "parent_body_id": "A",
      "display_name": "Wregoe A4",
      "body_type": "planet",
      "subtype": "high metal content world",
      "build_constraints": ["surface_allowed", "orbital_allowed"],
      "slot_summary": {
        "orbital": { "count": 2, "confidence": "medium" },
        "surface": { "count": 2, "confidence": "medium" }
      },
      "role_labels": ["candidate high-tech support body"],
      "claim_refs": ["CL-0126", "CL-0129"],
      "unknown_refs": ["U-0004"]
    },
    {
      "body_id": "A5",
      "parent_body_id": "A",
      "display_name": "Wregoe A5",
      "body_type": "planet",
      "subtype": "rocky body",
      "build_constraints": ["surface_allowed", "orbital_allowed"],
      "slot_summary": {
        "orbital": { "count": 2, "confidence": "medium" },
        "surface": { "count": 2, "confidence": "medium" }
      },
      "role_labels": ["existing extraction-refinery-industrial anchor"],
      "evidence_refs": ["EV-0002"]
    }
  ],
  "facilities": [
    {
      "facility_id": "A5-main-port",
      "body_id": "A5",
      "display_name": "A5 Main Port",
      "lane": "orbital",
      "state": "built",
      "construction_progress": { "percent": 100, "status": "completed" },
      "economy_roles": ["industrial", "extraction", "refinery"],
      "confidence": "medium",
      "evidence_refs": ["EV-0002"],
      "claim_refs": ["CL-0002"]
    },
    {
      "facility_id": "A4-high-tech-plan",
      "body_id": "A4",
      "display_name": "A4 High Tech support build",
      "lane": "surface",
      "state": "planned",
      "construction_progress": { "percent": 0, "status": "not_started" },
      "economy_roles": ["hightech"],
      "planner_decision_refs": ["PD-0001"],
      "confidence": "medium",
      "warning_refs": ["PR-0012"],
      "unknown_refs": ["U-0004"]
    },
    {
      "facility_id": "A4-old-layout",
      "body_id": "A4",
      "display_name": "Deprecated A4 layout",
      "lane": "surface",
      "state": "demolished",
      "construction_progress": { "percent": 0, "status": "removed" },
      "timeline_refs": ["TE-0003"],
      "confidence": "low"
    }
  ],
  "market_links": [
    {
      "link_id": "ml-001",
      "source_facility_id": "A5-main-port",
      "target_facility_id": "A4-high-tech-plan",
      "link_type": "weak",
      "aggregation_caveat": true,
      "confidence": "low",
      "claim_refs": ["CL-0327", "CL-0332"],
      "unknown_refs": ["U-0007"]
    }
  ],
  "commodity_state": [
    {
      "commodity": "Computer Components",
      "scope": "system",
      "status": "predicted_available",
      "source": "planner_projection",
      "planner_decision_refs": ["PD-0001"],
      "confidence": "low"
    },
    {
      "commodity": "Titanium",
      "scope": "system",
      "status": "observed_available",
      "source": "evidence",
      "evidence_refs": ["EV-0001"],
      "confidence": "medium"
    }
  ],
  "planner_state": {
    "objective": "increase high-tech material coverage without unacceptable loss of existing extraction/refinery strength",
    "decisions": [
      {
        "decision_id": "PD-0001",
        "label": "Treat A4 as a complementary High Tech support body",
        "confidence": "medium",
        "mechanic_refs": ["M-0010", "M-0012"],
        "claim_refs": ["CL-0126", "CL-0185"],
        "unknown_refs": ["U-0004"],
        "warnings": ["Preview required before slot-committing build."]
      }
    ]
  },
  "timeline": [
    {
      "event_id": "TE-0001",
      "type": "facility_built",
      "target_id": "A5-main-port",
      "label": "A5 main port established",
      "evidence_refs": ["EV-0002"]
    },
    {
      "event_id": "TE-0002",
      "type": "planner_decision_recorded",
      "target_id": "A4-high-tech-plan",
      "label": "A4 High Tech support plan created",
      "planner_decision_refs": ["PD-0001"]
    }
  ],
  "warnings": [
    {
      "id": "TW-0001",
      "label": "Weak-link routing remains uncertain in multi-port layouts",
      "claim_refs": ["CL-0327", "CL-0332"],
      "unknown_refs": ["U-0007"],
      "severity": "high"
    }
  ],
  "unknowns": ["U-0004", "U-0007"],
  "contradictions": ["CX-0002"],
  "supporting_refs": {
    "mechanics": ["M-0006", "M-0010", "M-0012"],
    "experiments": ["EXP-0001"],
    "planner_rules": ["PR-0004", "PR-0012"]
  }
}
```

## Why this data model is enough for MVP

The MVP does not need:

- full spatial rendering
- real orbital positions
- per-frame simulation
- fully normalized event sourcing
- an external API

It only needs enough structure to represent one system honestly and let users inspect how the research layers connect.

## What must not be built yet

The following should stay explicitly out of scope for the first implementation cycle:

- a replacement for the existing system map
- a full 3D engine or animated orbital simulation
- multi-system galaxy navigation
- real-time sync against live public APIs
- a new export or release framework
- a second planner architecture parallel to the current one
- a full database migration justified only by this feature
- commodity prediction logic that outruns current evidence confidence
- speculative mechanics encoded as if already confirmed

## Dependency on existing CRE layers

The Digital Twin should consume and expose existing CRE layers rather than replacing them.

It should depend on:

- `schemas/colony_state.schema.json`
- `evidence/claim_register.csv`
- `evidence/claim_provenance_links.csv`
- `evidence/evidence_mechanic_traceability.csv`
- `docs/unknowns_register.md`
- `docs/contradiction_register.md`
- `experiments/live_verification_register.md`
- `planner/planner_rules_register.md`
- `mechanics/`

## Phased implementation posture

### Phase DT-1

Assemble a single-system twin object and render a non-destructive review surface.

### Phase DT-2

Add history/timeline and richer planner-decision inspection.

### Phase DT-3

Add comparative views, stronger queryability, and deeper experiment/evidence integration.

### Phase DT-4

Consider advanced overlays only after the underlying twin object is stable and planner-safe.

## Backlog meaning

The Digital Twin should be treated as a future major feature because it spans:

- state assembly
- planner integration
- evidence/provenance visibility
- history representation
- uncertainty handling

That is exactly why it should remain a design and backlog item first.
