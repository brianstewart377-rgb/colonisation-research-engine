# Colonisation Intelligence Platform Architecture

Date: `2026-06-28`

## Executive summary

The Colonisation Intelligence Platform is an evidence system for Elite Dangerous colonisation, not a chatbot with opinions. Its job is to ingest public and private evidence, preserve contradictory observations, model colonisation mechanics as revisable knowledge, run experiments against those mechanics, and expose only planner-safe knowledge to planning workflows.

The platform separates five layers that should never be collapsed into one another: raw source data, parsed observations, inferred mechanics, decision records, and verified planner knowledge. This separation is what allows the platform to store failed predictions, disputed assumptions, patch drift, contradictory evidence, and contextual engineering choices without poisoning the planner.

The MVP does not require model fine-tuning, screenshot ingestion in the production app, or unavailable APIs. It can start with official mechanics documents, Spansh and EDSM system data, manual experiment entry, and a basic build-plan generator that uses verified mechanics plus current system facts.

## System overview

The platform has five logical subsystems:

1. `Source intake`
   Official Frontier pages, schema references, Spansh dumps, EDSM dumps, EDDN streams, manual analyst uploads, and curated public pages such as Inara or Raven captures.
2. `Observation extraction`
   Converts source artifacts into structured observations, preserving provenance and ambiguity.
3. `Mechanics lab`
   Maintains candidate mechanics, experiment records, contradiction tracking, and confidence history.
4. `Planner knowledge service`
   Publishes only planner-safe knowledge: verified mechanics, current system data, allowed facility types, and caveats.
5. `Planner runtime`
   Produces build plans for a target system and goal set, with recommendation confidence and explicit warnings.

The platform should be built around an evidence-first feedback loop:

`source -> observation -> mechanic claim -> experiment -> contradiction/reinforcement -> verified planner knowledge -> plan -> new observation`

This loop is the core product. The planner is only one consumer of that loop.

### Design principles

- Mechanics are hypotheses under observation, not immortal truths.
- Negative evidence is as valuable as positive evidence.
- Contradictions are normal and should create work, not be hidden.
- Identity must be explicit. Facility names are not globally unique.
- The planner is downstream of evidence quality and should never invent certainty.

### Logical layers

| Layer | Purpose | Allowed outputs | Must not contain |
|---|---|---|---|
| `Raw source data` | Immutable capture of inputs | Snapshots, files, URLs, checksums, timestamps | Inferred meaning |
| `Parsed observations` | Structured facts and claims extracted from sources | Named systems, facilities, progress states, market snapshots, screenshots, diary claims | Planner assumptions |
| `Inferred mechanics` | Candidate or verified explanations of how colonisation behaves | Mechanic definitions, statuses, evidence links, contradiction counts | Hidden source rewrites |
| `Verified planner knowledge` | Planner-safe operational knowledge | Allowed facility types, confidence-labeled mechanic projections, current system state | Raw contradictory noise |
| `Planner outputs` | Evidence-backed plans and caveats | Build options, warnings, confidence bands, experiment suggestions | Unsupported certainty |

### Mechanic states

The platform uses `Mechanic` instead of `Rule`. A mechanic is a belief about how the game behaves, backed by evidence and subject to revision.

| Mechanic status | Meaning | Planner behavior |
|---|---|---|
| `Confirmed` | Strongly corroborated across current evidence | Safe to use directly |
| `Likely` | Good support, but not fully resolved | Use with caveats |
| `Experimental` | Actively being tested | Show only when explicitly requested |
| `Disputed` | Credible contradictory evidence exists | Do not rely on without warning |
| `Disproved` | Repeated evidence contradicts it | Do not use for planning |
| `Patch-sensitive` | Previously supported, but recent patch drift may invalidate it | Require version/date warnings |

## Data model

The platform needs both a relational store and a graph-style relationship model. The relational side gives integrity and queryability. The graph side gives reasoning about systems, facilities, market links, mechanics, and experiments.

### Core entities

| Entity | Purpose | Key fields |
|---|---|---|
| `source_catalog` | Registry of source families | `source_id`, `name`, `type`, `access_mode`, `trust_rating`, `license_status` |
| `source_snapshot` | Immutable captured source artifact | `snapshot_id`, `source_id`, `captured_at`, `version_label`, `raw_locator`, `checksum` |
| `system` | Canonical star system identity | `system_id64`, `name`, `coords`, `economy_primary`, `economy_secondary`, `population`, `allegiance`, `government`, `security` |
| `body` | Canonical body identity within system | `system_id64`, `body_id`, `body_name`, `body_type`, `arrival_ls`, `terraformable`, `rings`, `volcanism` |
| `facility` | Canonical facility identity | `facility_id`, `system_id64`, `body_id_nullable`, `market_id_nullable`, `facility_name`, `facility_type`, `orbital_or_surface`, `status` |
| `commodity` | Commodity catalog | `commodity_id`, `name`, `category`, `legal_flags` |
| `station_type` | Canonical station/facility taxonomy | `station_type_id`, `name`, `class_family`, `landing_pad_profile` |
| `economy` | Economy taxonomy | `economy_id`, `name`, `is_surface_supported`, `is_orbital_supported` |
| `market_snapshot` | Time-stamped market/service evidence | `market_snapshot_id`, `facility_id`, `captured_at`, `commodity_id`, `buy_price`, `sell_price`, `stock`, `demand` |
| `observation` | Parsed evidence assertion | `observation_id`, `subject_type`, `subject_id`, `observation_type`, `value`, `source_snapshot_id`, `is_direct_observation` |
| `mechanic` | Candidate or verified mechanic | `mechanic_id`, `name`, `description`, `status`, `scope`, `first_seen_version`, `last_verified_version`, `last_verified_at` |
| `mechanic_assertion` | Formal statement of a mechanic | `mechanic_assertion_id`, `mechanic_id`, `assertion_text`, `subject_scope`, `expected_effect` |
| `experiment` | First-class test record | `experiment_id`, `hypothesis`, `prediction`, `context`, `change_tested`, `before_state`, `after_state`, `observed_result`, `conclusion`, `confidence` |
| `decision_record` | First-class engineering or research decision | `decision_id`, `title`, `status`, `context`, `problem_statement`, `decision`, `rationale`, `confidence`, `review_status` |
| `evidence_link` | Join table between evidence and mechanics/experiments/decisions | `evidence_link_id`, `from_entity`, `to_entity`, `relationship_type` |
| `confidence_record` | Time-series confidence record | `confidence_record_id`, `entity_type`, `entity_id`, `score`, `band`, `reason`, `measured_at` |
| `contradiction_case` | Review object for conflicting evidence | `contradiction_case_id`, `target_type`, `target_id`, `opened_at`, `severity`, `status`, `summary` |
| `planner_knowledge_view` | Published planner-safe projection | `knowledge_id`, `subject_type`, `subject_id`, `knowledge_type`, `value`, `planner_confidence`, `generated_at` |

### Experiment record

Each experiment must be a first-class row, not a note attached to a system. The minimum structure is:

| Field | Meaning |
|---|---|
| `hypothesis` | The mechanic being tested |
| `prediction` | What should happen if the mechanic is true |
| `system/body/facility context` | Where the test is happening |
| `build or change tested` | What was built, removed, activated, or altered |
| `before state` | Snapshot of the prior system state |
| `after state` | Snapshot after the change |
| `observed result` | What actually happened |
| `conclusion` | Confirmed, disputed, disproved, inconclusive |
| `confidence` | Confidence in the experiment outcome |
| `supporting evidence` | Links to screenshots, journals, snapshots, logs, and analyst notes |

### Negative evidence

Negative evidence must be modeled explicitly, not inferred from silence.

Examples:

- A predicted economy uplift did not appear after a build.
- A suspected strong market link produced no observed effect.
- A facility type assumed to be valid for a body was rejected by actual build evidence.
- A planner recommendation was executed and the observed result contradicted the expected outcome.

Recommended negative-evidence types:

- `failed_prediction`
- `null_effect_observed`
- `mechanic_disproved`
- `unsupported_facility_type`
- `identity_collision`

### Relationship model

The graph should model relationships such as:

- `system HAS_BODY body`
- `system HAS_FACILITY facility`
- `facility LOCATED_ON body`
- `facility USES_STATION_TYPE station_type`
- `facility EXPOSES_ECONOMY economy`
- `facility SELLS commodity`
- `facility BUYS commodity`
- `facility HAS_MARKET_LINK facility`
- `mechanic SUPPORTED_BY observation`
- `mechanic TESTED_BY experiment`
- `mechanic CONTRADICTED_BY observation`
- `experiment USES_EVIDENCE source_snapshot`
- `planner_knowledge DERIVED_FROM mechanic`
- `planner_knowledge DERIVED_FROM current_state_snapshot`

This model matters because the planner should reason across linked evidence, not just retrieve isolated rows.

## AI roles

The platform has three separate AI roles. They must not be merged into one undifferentiated “assistant”.

### Evidence Extractor AI

Purpose: turn evidence into structured observations.

Inputs:

- public pages
- official mechanics pages
- journal files
- bulk dumps
- forum posts
- logbooks
- screenshots
- analyst-entered notes

Outputs:

- structured observations
- source metadata
- candidate identities
- unresolved fields marked `UNKNOWN`
- extraction confidence

Constraints:

- must preserve ambiguity
- must never promote an observation into a mechanic
- must not assume screenshots are available to the production app

### Mechanics Researcher AI

Purpose: analyze observations and experiments to discover patterns, contradictions, and candidate mechanics.

Outputs:

- candidate mechanics
- confidence updates
- patch drift warnings
- contradiction cases
- proposals for new experiments

Constraints:

- may use disputed and experimental evidence
- must keep negative evidence
- must produce rationale and linked evidence
- must not directly generate planner output

### Planner AI

Purpose: generate build plans from verified mechanics, current system state, and user goals.

Inputs:

- verified planner knowledge
- current system/body/facility data
- user objectives
- allowed facility catalog

Outputs:

- build options
- projected outcomes
- confidence labels
- evidence-backed caveats
- suggested experiments when confidence is weak

Constraints:

- must not use raw disputed mechanics as if confirmed
- must avoid unsupported facility types
- must avoid irreversible demolition advice without evidence
- must distinguish `Confirmed`, `Likely`, `Experimental`, and `Unknown`

## Evidence lifecycle

The evidence lifecycle should be explicit and auditable.

1. `Capture`
   A source artifact is captured into `source_snapshot`.
2. `Extract`
   Evidence Extractor AI and deterministic parsers create structured observations.
3. `Normalize`
   Systems, bodies, facilities, commodities, and station types are identity-matched where possible.
4. `Review`
   Ambiguous identities, name collisions, and low-confidence extractions enter analyst review.
5. `Relate`
   Observations are linked to systems, facilities, experiments, and candidate mechanics.
6. `Publish`
   Only planner-safe knowledge is projected into planner views.

### Source separation

The platform should preserve four distinct evidence classes:

- `Raw source data`
  Immutable files, pages, dumps, snapshots, screenshots, and logs.
- `Parsed observations`
  Statements such as “Vellix Orbital exists”, “facility progress was ~60%”, or “system architect was X”.
- `Inferred mechanics`
  Explanations such as “body feature X appears to boost economy Y” or “facility pair Z tends to create market link Q”.
- `Verified planner knowledge`
  Planner-safe outputs like “for this patch window and confidence range, facility type A is supported on body class B”.

Collapsing these layers would make contradiction handling impossible.

## Experiment lifecycle

Experiments are the backbone of mechanic verification.

1. `Create hypothesis`
   Example: “Building a communications facility in the support system increases effective coordination or unlock behavior for the primary system.”
2. `Record prediction`
   Define the expected observable change.
3. `Snapshot before state`
   Store relevant system, body, facility, market, and mechanic context.
4. `Apply change`
   Build, activate, complete, or otherwise alter the tested structure.
5. `Snapshot after state`
   Capture the resulting state.
6. `Compare outcome`
   Determine whether the prediction matched the observation.
7. `Conclude`
   Mark `confirmed`, `disputed`, `disproved`, or `inconclusive`.
8. `Update mechanics`
   Adjust mechanic confidence and planner knowledge only after review.

### Experiment classes

| Experiment class | Example |
|---|---|
| `Mechanic verification` | Test whether a predicted market link appears |
| `Planner validation` | Compare predicted plan outcome against real result |
| `Patch drift check` | Re-run a previously trusted mechanic after a Frontier patch |
| `Identity validation` | Resolve whether two same-name facilities are actually distinct |

## Confidence model

Confidence should be attached to observations, experiments, mechanics, and planner knowledge separately.

### Confidence components

| Component | What it measures |
|---|---|
| `Source authority` | Official source vs community interpretation |
| `Directness` | Direct observation vs second-order narrative |
| `Specificity` | Named system/body/facility vs generic claim |
| `Reproducibility` | Can the claim be rechecked from public or local evidence |
| `Freshness` | How recent the evidence is |
| `Corroboration` | How many independent sources support it |
| `Patch relevance` | Whether the evidence predates major mechanical changes |

### Mechanic confidence fields

Each mechanic should track at least:

- `confidence_score`
- `confidence_band`
- `last_verified_version`
- `last_verified_at`
- `contradiction_count`
- `corroborating_evidence_count`
- `negative_evidence_count`
- `patch_sensitivity`
- `confidence_decay_state`

### Patch drift

After Frontier patches, confidence should not remain static.

Recommended behavior:

- major mechanics patch: immediate decay against all patch-sensitive mechanics
- new post-patch confirming experiment: restores confidence
- no post-patch verification after defined time window: downgrade mechanic from `Confirmed` to `Likely` or `Experimental`

Confidence decay must be version-aware, not just date-aware.

## Contradiction handling

Contradictions should generate durable work objects, not ad hoc notes.

### Contradiction queue

When a new observation conflicts with an existing mechanic or planner knowledge item:

1. create a `contradiction_case`
2. attach the conflicting observations and evidence links
3. reduce the target mechanic confidence
4. mark the mechanic `Disputed` or `Patch-sensitive` if thresholds are crossed
5. create a review task for Mechanics Researcher AI or analyst review
6. block unsafe planner promotion until the case is resolved

### Contradiction severity

| Severity | Trigger | Planner impact |
|---|---|---|
| `Low` | One weak conflicting observation | Add caveat only |
| `Medium` | Credible conflict from public evidence | Downgrade to `Likely` or `Disputed` |
| `High` | Contradiction from strong post-patch evidence or failed experiment | Remove from verified planner knowledge |

### Negative evidence flow

Failed predictions and disproved assumptions must count against a mechanic. This means:

- the mechanic’s `contradiction_count` increases
- a new `confidence_record` is written
- an experiment may conclude `Disproved`
- planner knowledge derived from the mechanic may be unpublished or downgraded

## Planner workflow

The Planner AI should run on verified knowledge only.

1. receive user goals
2. load current system/body/facility state
3. load verified mechanics valid for the current patch window
4. generate candidate build plans using only supported facility types
5. label each recommendation by confidence
6. attach caveats and evidence notes
7. suppress unsafe actions

### Planner safety constraints

- recommendations must be labeled `Confirmed`, `Likely`, `Experimental`, or `Unknown`
- irreversible demolitions require explicit evidence and must never be implied by heuristic convenience
- unsupported facility types must be blocked, not merely warned
- planner outputs must include evidence-backed caveats when dependent on `Likely` or `Experimental` mechanics
- when confidence is weak, the planner should suggest an experiment instead of pretending certainty

### Planner output structure

Recommended output fields:

- `plan_id`
- `goal_summary`
- `candidate_builds`
- `expected_effects`
- `recommendation_confidence`
- `mechanics_used`
- `caveats`
- `unsupported_requests`
- `suggested_validation_experiments`

## MVP build order

The first milestone should deliberately avoid fine-tuning, screenshot-dependent product flows, and unavailable APIs.

### MVP scope

1. `Database schema`
   Create the source, observation, mechanic, experiment, contradiction, and planner-knowledge tables.
2. `Official mechanics ingestion`
   Ingest Frontier mechanics sources as manually curated mechanic records with version stamps.
3. `Spansh and EDSM ingest`
   Load system, body, and station data as current-state reference.
4. `Manual evidence entry`
   Allow analyst/manual entry of experiments and observations from internal tests.
5. `Basic default build-plan generation`
   Generate simple plans using current system data plus only confirmed or likely mechanics.

### Suggested MVP sequence

| Step | Deliverable | Why first |
|---|---|---|
| `1` | Core schema and provenance model | Everything depends on durable evidence objects |
| `2` | Official mechanics registry | Gives a trustworthy initial mechanic layer |
| `3` | Spansh and EDSM current-state ingest | Gives the planner real galaxy context |
| `4` | Manual experiment and contradiction entry | Lets the team build private evidence before automation |
| `5` | Planner-safe knowledge projection | Creates the contract the planner consumes |
| `6` | Basic build-plan generation | First useful product slice without fine-tuning |

### What is deliberately out of MVP

- fine-tuning
- automatic screenshot ingestion into production
- OCR-dependent production flows
- unsupported private APIs
- full forum/logbook scraping automation
- irreversible planner actions based on weak evidence

## Risks and open questions

### Risks

- `Patch drift`
  Strong mechanics can go stale after Frontier changes.
- `Identity collisions`
  Same-name facilities can exist across the galaxy.
- `Source incompleteness`
  No public source fully exposes architect, body linkage, facility graph, and market state together.
- `Observation bias`
  Community guides and diaries often overrepresent successful experiments.
- `Narrative contamination`
  Roleplay and storytelling can look like structured evidence if extraction is careless.

### Open questions

- How much of planner knowledge should be version-partitioned by patch family rather than time window alone?
- What confidence threshold is sufficient to publish a mechanic to planner-safe knowledge?
- How should the system represent body-linked outcomes when public evidence can confirm facility existence but not exact orbital/body linkage?
- What is the best human review surface for contradiction cases and name collisions?
- When screenshot ingestion remains `UNKNOWN` for production, what is the best analyst-side workflow for attaching image-backed evidence?

## Helpful additions

Two companion artifacts already created from the source review are especially useful for this architecture:

- `corrected_seed_claim_pack.json`
  A cleaned evidence seed pack with corroboration flags.
- `seed_claim_triage_manifest.json`
  A machine-readable split between safe, historical, provisional, and identity-review claims.

These are not implementation code, but they provide a concrete bridge from architecture to later schema and ingestion work.
