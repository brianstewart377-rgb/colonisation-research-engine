# CRE Glossary Register

This glossary records canonical terms used across the Colonisation Research Engine.

## G-0001 - Construction Points

- Category: Construction
- Definition: Non-material build progression resources that gate which facility tiers are currently buildable.
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Related mechanics: `M-0004`
- Planner implication: Always model separately from commodity cost.

## G-0002 - Facility Tier

- Category: Construction
- Definition: A facility class level whose build requirements and construction-point generation differ from other levels.
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Related mechanics: `M-0004`
- Planner implication: Tier logic must be explicit in build sequencing.

## G-0003 - Colony-Type Port

- Category: Port taxonomy
- Definition: A port whose preview economy is `Colony` and whose final economy behavior is treated as inherited from body and link context.
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`, `evidence/EV-0003-a4-t3-station-selection-previews.md`
- Related mechanics: `M-0005`, `M-0007`
- Planner implication: Do not treat as a direct economy-choice surface.

## G-0004 - Specialised Port

- Category: Port taxonomy
- Definition: A port class with an inherent economy baseline rather than the same inheritance behavior used by colony-type ports.
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`
- Related mechanics: `M-0005`, `M-0007`
- Planner implication: Compare separately from colony-type ports.

## G-0005 - Main Port

- Category: Link routing
- Definition: The highest-tier port on a body, with first-built order breaking ties in the repository's current routing model.
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`
- Related mechanics: `M-0006`
- Planner implication: Link-routing analysis must know which port is main.

## G-0006 - Strong Link

- Category: Economy / routing
- Definition: A same-body market relationship used for deliberate local market shaping.
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`, `evidence/EV-0001-rocha-liberty-post-high-tech-build.md`
- Related mechanics: `M-0006`
- Planner implication: Prefer for target-economy or target-commodity control.

## G-0007 - Weak Link

- Category: Economy / routing
- Definition: A cross-body spillover link that may support a market but should not be treated as guaranteed targeted control.
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`, `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`
- Related mechanics: `M-0003`, `M-0006`
- Planner implication: Label recommendations based on weak links as experimental unless corroborated.

## G-0008 - Coverage

- Category: Planning
- Definition: The total useful assets a colony already provides across commodities, economies, services, missions, and strategic properties.
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Related mechanics: contextual concept rather than a single mechanic
- Planner implication: Analyze before recommending facilities.

## G-0009 - Coverage Gap

- Category: Planning
- Definition: A missing, weak, or unreliable asset that matters to the current objective.
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Related mechanics: contextual concept
- Planner implication: Facility choice should target a gap, not just add more structures.

## G-0010 - Role

- Category: Planning
- Definition: The intended function of a body, station, or facility group inside the wider colony.
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Related mechanics: contextual concept
- Planner implication: Recommendations should be role-first, not facility-first.

## G-0011 - Architecture

- Category: Planning
- Definition: A reusable build pattern combining roles, facilities, and expected effects under specific prerequisites.
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Related mechanics: `M-0006`, `M-0007`, `M-0008`
- Planner implication: Never universalize an architecture outside its context.

## G-0012 - Negative Evidence

- Category: Research method
- Definition: A failed prediction, null effect, or disproved assumption preserved as first-class knowledge.
- Source: `constitution/project_principles.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`
- Related mechanics: `M-0003`
- Planner implication: Prevents the planner from repeating plausible but failed strategies.

## G-0013 - Contradiction Case

- Category: Research method
- Definition: A durable record that captures conflicts between documents, evidence, mechanics, or planner assumptions without forcing premature resolution.
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `constitution/project_principles.md`
- Related mechanics: all contested mechanics
- Planner implication: Contradictions must lower confidence, not disappear.

## G-0014 - Knowledge Projection

- Category: Knowledge system
- Definition: A planner-safe projection derived from verified mechanics and current evidence rather than from raw contradictory material.
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `ontology/entities.md`
- Related mechanics: all planner-consumable mechanics
- Planner implication: Future tooling should consume projections, not raw evidence directly.

## G-0015 - Needs Live Verification

- Category: Research workflow
- Definition: A durable unresolved item created when repository evidence is insufficient and a live in-game experiment or observation is required.
- Source: `planner/planner_safety.md`, `experiments/README.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Related mechanics: `M-0003`, `M-0006`, `M-0007`, `M-0008`
- Planner implication: Suggest validation instead of fake certainty.

## G-0016 - Colony

- Category: Colony state
- Definition: The current or historical colonisation state being analyzed within a system, including facilities, roles, coverage, links, and constraints.
- Source: `ontology/entities.md`, `planner/decision_support_model.md`
- Related mechanics: contextual concept
- Planner implication: Optimize colony state under an objective, not the system name in isolation.

## G-0017 - Orbital

- Category: Placement / slots
- Definition: A placement or slot class above a body, usually modeled as lane or capacity rather than as an independent identity root.
- Source: `ontology/entities.md`, `schemas/colony_state_schema.md`
- Related mechanics: `M-0005`, `M-0007`
- Planner implication: Orbital eligibility constrains placement, but `orbital` is not automatically a facility type or a final economy outcome.

## G-0018 - Surface Slot

- Category: Placement / slots
- Definition: A build-capacity unit on a body surface. A slot is capacity for possible placement, not proof of a built facility.
- Source: `ontology/entities.md`, `planner/decision_support_model.md`, `schemas/colony_state_schema.md`
- Related mechanics: contextual concept
- Planner implication: Never treat slot count or projected occupancy as realized infrastructure.

## G-0019 - Economy Role

- Category: Planning
- Definition: A planning-oriented economic function such as `Industrial anchor` or `High Tech support`.
- Source: `ontology/entities.md`, `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Related mechanics: contextual concept
- Planner implication: Economy role is not the same thing as final inherited economy state and should remain confidence-labeled.

## G-0020 - Market

- Category: Economy / planning
- Definition: The commodity, service, and mission exposure surface visible to players in a system or facility context.
- Source: `ontology/entities.md`, `planner/decision_support_model.md`
- Related mechanics: `M-0006`, `M-0007`, `M-0008`
- Planner implication: Market outcomes should be described as observed or projected; they are not direct synonyms for economy labels.

## G-0021 - Construction Material

- Category: Construction
- Definition: A commodity that matters directly to colony construction and build continuity.
- Source: `ontology/entities.md`, `planner/decision_support_model.md`
- Related mechanics: contextual concept
- Planner implication: Construction materials are a commodity subset and must remain separate from construction points.

## G-0022 - Body Modifier

- Category: Body context
- Definition: A body-specific modifier that changes expected facility, market, or economy behavior under current mechanic interpretation.
- Source: `ontology/entities.md`, `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- Related mechanics: `M-0008`
- Planner implication: Modifiers should adjust ranking and confidence, not create fake deterministic guarantees.

## G-0023 - Research Evidence

- Category: Knowledge system
- Definition: Evidence captured for curation and interpretation in the research layer.
- Source: `ontology/entities.md`, `architecture/runtime_boundary_design.md`, `architecture/evidence_vault.md`
- Related mechanics: all evidence-backed mechanics indirectly
- Planner implication: Research evidence must be reviewed before it becomes planner-safe knowledge.

## G-0024 - Operational Data

- Category: Knowledge system
- Definition: Generated runtime-facing data such as projections, denormalized query views, and planner input objects.
- Source: `ontology/entities.md`, `architecture/knowledge_projection_design.md`, `architecture/runtime_boundary_design.md`
- Related mechanics: all planner-consumable mechanics indirectly
- Planner implication: Future planner and API layers should consume operational data rather than raw repository documents.

## G-0025 - User Data

- Category: Application boundary
- Definition: Mutable user-owned state such as saved plans, private notes, preferences, credentials, or account settings.
- Source: `ontology/entities.md`, `architecture/runtime_boundary_design.md`
- Related mechanics: none directly
- Planner implication: User data may shape objectives and constraints, but must not redefine canonical research truth.
