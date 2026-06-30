# Core entities

This document defines the authoritative semantic surface for the core concepts used across the Colonisation Research Engine.

It does not try to restate every mechanic or planner rule.
Its job is narrower and more important:

- define what the main concepts are
- define what they are not
- describe identity and lifecycle expectations
- reduce semantic drift between ontology, planner, projection, and future application work

## Reading rule

The ontology defines concepts.

It does not by itself prove mechanics.
It does not by itself decide planner policy.
It does not by itself define user-facing UI language.

When a future document conflicts with this ontology on what a concept means, this ontology should be treated as the semantic starting point and the conflict should be resolved explicitly.

## System

- Canonical definition: A named star system that acts as the top-level physical location for colony analysis.
- What it is: The container for stars, planets, moons, belts, rings, facilities, market behavior, evidence scope, and planner context.
- What it is not: A colony by default, a body, or a facility.
- Lifecycle: Systems are generally stable identity roots; their state may change without changing system identity.
- Identity expectations: Should use an external stable identifier such as `system_id64` when available. Display name is not enough by itself.
- Relationship to nearby concepts: A system contains bodies and facilities; a colony may occupy all or part of a system.
- Examples: `Wregoe`, `Rocha Liberty` system context.
- Common confusion risks: Treating a system as identical to its active colony state.
- Planner implications: Planner state must separate `system identity` from `current colony coverage within that system`.

## Colony

- Canonical definition: The current or historical colonisation state being analyzed within a system or system scope.
- What it is: A stateful arrangement of facilities, roles, markets, coverage, and constraints within a system.
- What it is not: A synonym for `System`, a single facility, or a permanent identity root independent of system context.
- Lifecycle: A colony evolves through planning, construction, growth, demolition, and patch-era reinterpretation.
- Identity expectations: Colony identity should usually be treated as a scoped state object, not a replacement for system identity.
- Relationship to nearby concepts: A colony is realized through facilities and market relationships on bodies within a system.
- Examples: `Current Wregoe colony state`, `post-build A4/A5 configuration`.
- Common confusion risks: Using `system` and `colony` interchangeably in planning or API design.
- Planner implications: Objectives and recommendations target colony state, not abstract system names alone.

## Body

- Canonical definition: A physical in-system celestial object or location surface that constrains colonisation behavior.
- What it is: The parent context for slots, modifiers, facility placement, and local economy inheritance behavior.
- What it is not: A facility, a role, or a market.
- Lifecycle: Body identity is stable; body interpretation and buildability assumptions may change.
- Identity expectations: Should be keyed by stable system-linked body identity, not display name alone.
- Relationship to nearby concepts: Stars, planets, moons, belts, and rings are body classes.
- Examples: `A4`, `A5`, a water world, a moon, a ring system.
- Common confusion risks: Treating body categories as interchangeable or forcing exact body linkage when only system-level evidence exists.
- Planner implications: Buildability, role assignment, link strength, and facility recommendations all depend on correct body semantics.

## Star

- Canonical definition: A stellar body within a system.
- What it is: A body class.
- What it is not: A colony, a facility, or a generic synonym for all bodies.
- Lifecycle: Stable body identity.
- Identity expectations: Uses body identity rules.
- Relationship to nearby concepts: One subtype of `Body`.
- Examples: primary star, companion star.
- Common confusion risks: Forgetting that stars are bodies but may have different colonisation constraints.
- Planner implications: Stars may constrain orbital assumptions and body hierarchy but should not be treated like planets or moons.

## Planet

- Canonical definition: A planetary body that may support surface and/or orbital colonisation behavior depending on type.
- What it is: A major subclass of `Body`.
- What it is not: A moon, ring, or built facility.
- Lifecycle: Stable body identity with changing colony state around it.
- Identity expectations: Same as body identity.
- Relationship to nearby concepts: Parent for surface slots, orbital lanes, modifiers, and facilities.
- Examples: HMC world, water world, rocky body.
- Common confusion risks: Treating all planets as equally buildable.
- Planner implications: Planet subtype and body modifiers may radically change valid recommendations.

## Moon

- Canonical definition: A natural satellite body under another body.
- What it is: A body subclass with its own buildability and placement context.
- What it is not: A secondary label for small planets or an orbital slot.
- Lifecycle: Stable body identity.
- Identity expectations: Same as body identity, including parent-body awareness.
- Relationship to nearby concepts: A moon is a body that may host its own facilities and roles.
- Examples: moonlet support body, industrial moon.
- Common confusion risks: Flattening moon and planet behavior into one undifferentiated class.
- Planner implications: Weak-link support and support-body patterns may depend on moon-specific context.

## Belt

- Canonical definition: A belt body or belt-like in-system location class.
- What it is: A body category relevant to buildability and structure assumptions when supported by evidence.
- What it is not: A generic orbital lane or ring synonym.
- Lifecycle: Stable as a body/location class.
- Identity expectations: Should remain explicitly typed as `belt`.
- Relationship to nearby concepts: Distinct from rings and orbital lanes.
- Examples: asteroid belt context.
- Common confusion risks: Treating belts, rings, and orbitals as one concept.
- Planner implications: Belt semantics should remain explicit because structure and slot assumptions may differ.

## Ring

- Canonical definition: A ring body or ring-associated location context around a parent body.
- What it is: A body-related physical structure that may constrain placement semantics.
- What it is not: A facility, a belt, or a generic orbital label.
- Lifecycle: Stable physical context.
- Identity expectations: Should remain separate from facility placement classes.
- Relationship to nearby concepts: A ring belongs to a body context but is not the same thing as an orbital facility lane.
- Examples: ringed-world context.
- Common confusion risks: Collapsing ring and orbital into one word.
- Planner implications: Any recommendation logic using ring context must keep it separate from `orbital` placement logic.

## Orbital

- Canonical definition: A facility placement or slot class above a body, not a default first-class identity root.
- What it is: A lane or location mode for a facility or slot.
- What it is not: Automatically a standalone entity, a station type, or a guarantee of inherited economy outcome.
- Lifecycle: Tied to slot or facility state, not separate identity.
- Identity expectations: Should usually be modeled as a property of a slot or facility, not its own root object.
- Relationship to nearby concepts: Distinct from `Body`, `Facility`, `Station Type`, and `Surface Slot`.
- Examples: orbital port lane, orbital slot capacity.
- Common confusion risks: Treating orbital as both a body, a facility type, and a slot entity.
- Planner implications: Orbital eligibility must constrain recommendations, but orbital status alone does not define final economy behavior.

## Surface Slot

- Canonical definition: A build-capacity unit or placement opportunity on a body's surface.
- What it is: Capacity for possible facility placement.
- What it is not: A built facility, a role, or a guarantee that something exists there now.
- Lifecycle: May move through unknown, predicted, open, occupied, blocked, or historical interpretations.
- Identity expectations: Slot identity should be scoped by body and slot class if modeled explicitly.
- Relationship to nearby concepts: A slot may host a facility; it is not the facility itself.
- Examples: `2 surface slots`, `predicted surface slot`.
- Common confusion risks: Treating slot count as facility count or treating projected slots as confirmed built state.
- Planner implications: Unsafe planners confuse capacity with realized structure.

## Facility

- Canonical definition: A concrete built, planned, observed, inferred, or historical installation in colony state.
- What it is: The root operational structure object for ports, settlements, installations, hubs, and similar built entities.
- What it is not: A body, a station type, a slot, or a final economy outcome.
- Lifecycle: Planned, under construction, built, inferred existing, demolished, historical, superseded.
- Identity expectations: Requires CRE facility identity plus system/body context and type; facility names alone are not globally unique.
- Relationship to nearby concepts: `Station`, `Port`, `Settlement`, `Hub`, and `Installation` are usually facility subtypes or labels, not competing root identities.
- Examples: main port, outpost, settlement cluster, installation.
- Common confusion risks: Treating `Facility` and `Station` as the same universal word.
- Planner implications: Recommendations should target facilities only after objective, coverage, and role logic has been established.

## Settlement

- Canonical definition: A surface facility subtype or class associated with settlement-style infrastructure.
- What it is: A kind of facility.
- What it is not: A generic synonym for any colony asset or for the entire colony.
- Lifecycle: Same lifecycle family as other facilities.
- Identity expectations: Should inherit facility identity rules.
- Relationship to nearby concepts: A settlement is a facility subtype, not a body or slot.
- Examples: ground settlement, planned support settlement.
- Common confusion risks: Treating settlement, colony, and facility as interchangeable.
- Planner implications: Settlement recommendations should remain typed because subtype may matter to services, roles, and modifiers.

## Hub

- Canonical definition: A role-bearing or informal label for a facility or facility group that acts as a concentration point for useful assets.
- What it is: Usually a role or description, sometimes a facility naming convention.
- What it is not: A canonical identity type by default.
- Lifecycle: Follows the lifecycle of the facility or group it describes.
- Identity expectations: `Hub` should not become a separate identity root unless a specific data source requires it.
- Relationship to nearby concepts: Often overlaps with role and architecture language.
- Examples: `Service Hub`, `High Tech Hub`.
- Common confusion risks: Treating hub as a facility type when it may only be a role label.
- Planner implications: Prefer expressing hub semantics as roles or architectures unless subtype evidence is explicit.

## Port

- Canonical definition: A port-class facility providing port-like services and market behavior.
- What it is: A facility subtype or facility category.
- What it is not: A synonym for all facilities or a synonym for station type.
- Lifecycle: Same lifecycle family as facilities.
- Identity expectations: Use facility identity rules plus station-type classification where relevant.
- Relationship to nearby concepts: A port may also be a station; station type further specifies its class.
- Examples: main port, orbital port, planetary port.
- Common confusion risks: Using `port`, `station`, and `facility` interchangeably.
- Planner implications: Port semantics often matter to market routing, main-port status, and economy inheritance.

## Station

- Canonical definition: A station-like facility instance.
- What it is: Usually a facility subtype or presentation label for a built installation.
- What it is not: A separate root identity that competes with `Facility`.
- Lifecycle: Same lifecycle family as facilities.
- Identity expectations: Should inherit facility identity rules.
- Relationship to nearby concepts: `Station Type` classifies a station; `Facility` remains the broader root object.
- Examples: Orbis station, Dodec station, Coriolis station.
- Common confusion risks: Letting `station_id` and `facility_id` drift into separate roots.
- Planner implications: Planner logic should reason over facilities with typed station classes, not over a split facility/station model.

## Installation

- Canonical definition: An installation-class facility.
- What it is: A subtype or classification of facility.
- What it is not: A body, slot, or station type root.
- Lifecycle: Same lifecycle family as facilities.
- Identity expectations: Uses facility identity rules.
- Relationship to nearby concepts: Distinct from settlements and ports by subtype, not by ontology root.
- Examples: orbital installation, service installation.
- Common confusion risks: Treating installation names as canonical type rules without explicit classification.
- Planner implications: Installation constraints should be modeled as facility subtype rules.

## Station Type

- Canonical definition: A canonical facility-class taxonomy describing structural class, such as Orbis, Dodec, Coriolis, outpost, installation, or settlement type.
- What it is: A type classifier.
- What it is not: A facility instance, a final economy outcome, or a body role.
- Lifecycle: Type taxonomy is stable even as facility instances change.
- Identity expectations: Station types should have stable type identifiers independent of facility instances.
- Relationship to nearby concepts: A facility uses a station type; station type does not determine every final market behavior by itself.
- Examples: `Orbis`, `Dodec`, `Ocellus`, `settlement`, `outpost`.
- Common confusion risks: Treating station type as the same thing as inherited economy or planner role.
- Planner implications: Station type can constrain mechanics and modifiers, but should not be mistaken for final colony output.

## Economy

- Canonical definition: A canonical economy category or economy mix observed, inherited, or projected in colony state.
- What it is: A market-facing or colony-behavior category such as Industrial, Extraction, Refinery, High Tech, Agriculture, Tourism, Military.
- What it is not: A role, a station type, or a recommendation by itself.
- Lifecycle: Economy state can change over time while entity identity remains stable.
- Identity expectations: Economies are taxonomy values, not unique runtime entities in the same sense as systems or facilities.
- Relationship to nearby concepts: Distinct from `Economy Role`; one is observed/projected state, the other is planning intent.
- Examples: Industrial, High Tech, Extraction.
- Common confusion risks: Treating a preview economy label as a direct user-controlled input or confusing economy exposure with role assignment.
- Planner implications: Economy semantics must remain separated from role semantics to prevent fake deterministic recommendations.

## Economy Role

- Canonical definition: A planning-oriented functional interpretation of what economic contribution a body or facility is intended to provide.
- What it is: A role or strategic framing.
- What it is not: The same thing as observed inherited economy state.
- Lifecycle: May change with objective and context.
- Identity expectations: Usually a taxonomy or assignment object, not a root identity.
- Relationship to nearby concepts: `Economy` is state or market expression; `Economy Role` is planning intent.
- Examples: `Industrial anchor`, `High Tech support`.
- Common confusion risks: Flattening intended role into observed economy outcome.
- Planner implications: The planner may recommend an economy role while remaining uncertain about exact final economy percentages or commodities.

## Market

- Canonical definition: The commodity and service exposure surface associated with a system or facility context.
- What it is: The runtime-facing output surface where commodities, services, and mission patterns become visible.
- What it is not: A commodity, an economy, or a facility identity.
- Lifecycle: Market state changes over time.
- Identity expectations: Often scoped to a facility or system context rather than treated as a root identity.
- Relationship to nearby concepts: Market is influenced by economies, links, body context, and facility mix.
- Examples: local commodity board, mission board posture, linked market outcome.
- Common confusion risks: Treating economy percentages as if they fully define market outcome.
- Planner implications: Recommendations should reason through markets cautiously and separate observed markets from projected ones.

## Commodity

- Canonical definition: A tradable item relevant to construction, market behavior, or colony support.
- What it is: A catalog item.
- What it is not: A market, an economy, or a buildability resource by default.
- Lifecycle: Commodity identity is stable; local availability is not.
- Identity expectations: Commodities should use a stable catalog key.
- Relationship to nearby concepts: Construction materials are a subset or planner-relevant slice of commodities.
- Examples: Steel, Titanium, Robotics, Auto-Fabricators.
- Common confusion risks: Treating commodity presence as guaranteed just because an economy type is present.
- Planner implications: Commodity coverage is a planner target, but commodity prediction must remain confidence-labeled.

## Construction Material

- Canonical definition: A commodity that matters directly to colony construction and build continuity.
- What it is: A planner-relevant commodity subset.
- What it is not: A separate ontology root from `Commodity`.
- Lifecycle: Follows commodity identity; relevance may vary by planning context.
- Identity expectations: Should inherit commodity identity.
- Relationship to nearby concepts: Construction materials are not the same thing as construction points.
- Examples: Steel, Titanium, Ceramic Composites, Computer Components.
- Common confusion risks: Blending material availability with non-material build gating.
- Planner implications: Material coverage and construction-point generation must remain separate in planning logic.

## Construction Points

- Canonical definition: Non-material build progression resources that gate facility tiers or buildability.
- What it is: A build-capacity metric.
- What it is not: A commodity, a market item, or a material source.
- Lifecycle: Changes with colony development.
- Identity expectations: Usually a state value, not a first-class identity root.
- Relationship to nearby concepts: Distinct from construction materials even when both affect building.
- Examples: facility-tier gating resources.
- Common confusion risks: Treating construction points as if hauling or producing commodities directly replaces them.
- Planner implications: Unsafe recommendations collapse two different build constraints if they confuse points and materials.

## Body Modifier

- Canonical definition: A body-specific modifier that changes expected facility or economy outcomes.
- What it is: A modifier on a body context.
- What it is not: A body identity, role, or facility.
- Lifecycle: Bound to body state interpretation and patch-era mechanic understanding.
- Identity expectations: Usually a typed attribute or applied modifier record, not a root identity.
- Relationship to nearby concepts: Modifiers qualify body context and may shape inherited or projected economy outcomes.
- Examples: local body economy modifiers, population/security tendencies if observed mechanically.
- Common confusion risks: Treating modifiers as direct guarantees.
- Planner implications: Body modifiers should adjust confidence and ranking, not create fake certainty.

## Strong Link

- Canonical definition: A same-body market relationship or routing effect with stronger expected economic influence.
- What it is: A relationship class between facilities or local colony components.
- What it is not: A facility, an economy, or a universal guarantee of target commodity exposure.
- Lifecycle: Relationship state may change with build configuration and mechanics understanding.
- Identity expectations: Usually a relationship object or derived relationship state.
- Relationship to nearby concepts: Distinct from weak links; often relies on main-port and local-body semantics.
- Examples: same-body industrial/high-tech support loop.
- Common confusion risks: Overstating the deterministic power of a strong link.
- Planner implications: Strong links can justify higher confidence than weak links, but still remain mechanic-sensitive.

## Weak Link

- Canonical definition: A cross-body spillover or weaker market relationship with lower targeted-control expectations.
- What it is: A relationship class between separated facilities or body contexts.
- What it is not: A guarantee of desired market repair or full commodity restoration.
- Lifecycle: Relationship state may change with colony topology and evidence.
- Identity expectations: Usually a relationship object or derived relationship state.
- Relationship to nearby concepts: Distinct from strong links in locality and expected control.
- Examples: cross-body support spillover.
- Common confusion risks: Treating a weak link as sufficient evidence for precise commodity restoration.
- Planner implications: Weak-link-driven recommendations should be caveated or experimental unless corroborated.

## Main Port

- Canonical definition: The highest-tier or otherwise dominant port on a body under the repository's current routing interpretation.
- What it is: A role or routing status assigned to a facility within local context.
- What it is not: A permanent immutable station-type property.
- Lifecycle: May change when the local facility set changes.
- Identity expectations: Main-port status attaches to a facility; it is not a separate root object.
- Relationship to nearby concepts: Important for link routing and economy influence.
- Examples: first-built highest-tier local port.
- Common confusion risks: Treating main-port status as globally stable or as a synonym for facility identity.
- Planner implications: Routing-sensitive recommendations must know which facility currently holds main-port status.

## Evidence

- Canonical definition: A source-backed artifact, record, snapshot, or linkage used to support or challenge interpretation.
- What it is: Raw or semi-raw support material for observations, claims, mechanics, and experiments.
- What it is not: A claim, a mechanic, or a planner-safe fact.
- Lifecycle: Once recorded, evidence should be immutable even if interpretations change.
- Identity expectations: Raw evidence identity and repository evidence-summary identity must remain explicit and not be silently conflated.
- Relationship to nearby concepts: Evidence informs observations, claims, experiments, decisions, and contradiction review.
- Examples: screenshot pack, source snapshot, exported page capture, repository-local artifact.
- Common confusion risks: Treating evidence titles as conclusions or equating summary evidence records with raw evidence items.
- Planner implications: The planner should consume evidence only through reviewed interpretation or projection layers.

## Research Evidence

- Canonical definition: Evidence captured for curation, interpretation, and research review.
- What it is: Part of the research layer.
- What it is not: Operational runtime state, user preference, or application telemetry.
- Lifecycle: Immutable once recorded; review status may change.
- Identity expectations: Should use evidence identity rules.
- Relationship to nearby concepts: Research evidence feeds observations and later projections.
- Examples: manual screenshots, Inara pages, Raven pages, source dumps.
- Common confusion risks: Blending research evidence with runtime operational data.
- Planner implications: Research evidence must be reviewed before it becomes planner-consumable knowledge.

## Operational Data

- Canonical definition: Generated or runtime-facing data used by projections, planner execution, APIs, or application surfaces.
- What it is: Derived, queryable, or application-consumable state.
- What it is not: Raw research evidence or user-owned private state.
- Lifecycle: Regenerated, versioned, and replaceable.
- Identity expectations: Must retain lineage to canonical research or canonical user state.
- Relationship to nearby concepts: Projections are operational data; repository evidence is not.
- Examples: planner-safe projections, denormalized planning context, API read models.
- Common confusion risks: Mistaking generated runtime objects for canonical research truth.
- Planner implications: Planner runtime should consume operational data, not raw research documents.

## User Data

- Canonical definition: Mutable user-owned application state such as preferences, saved plans, notes, tokens, or access controls.
- What it is: Application-layer private or account-scoped state.
- What it is not: Research evidence, canonical mechanics, or planner-safe published knowledge.
- Lifecycle: Mutable, user-scoped, often reversible.
- Identity expectations: Must use application/account identity, not canonical research identifiers as ownership roots.
- Relationship to nearby concepts: User data may reference systems, bodies, facilities, and recommendations without becoming canonical truth about them.
- Examples: saved plan branch, user objective preset, private note.
- Common confusion risks: Treating user preferences as if they were curated research findings.
- Planner implications: User data can shape objectives and constraints, but must not mutate canonical semantics.

## Observation

- Canonical definition: A structured statement extracted or recorded from evidence about something observed.
- What it is: An interpreted but still evidence-near statement.
- What it is not: A claim, a mechanic, or a planner-safe recommendation.
- Lifecycle: Should be preserved historically; reinterpretation should not silently erase prior observations.
- Identity expectations: Requires stable observation identity and evidence linkage.
- Relationship to nearby concepts: Evidence supports observations; claims may synthesize multiple observations.
- Examples: facility exists in system, progress percentage shown, service present, market state observed.
- Common confusion risks: Treating observation as if it already represents a generalized rule.
- Planner implications: Raw observations are too close to source detail to be planner-safe by default.

## Claim

- Canonical definition: A structured interpretive statement synthesized from one or more observations and evidence items.
- What it is: A bridge layer between observations and higher-level mechanics, decisions, or planner-safe publication.
- What it is not: Raw evidence, a universal mechanic, or a planner rule.
- Lifecycle: Claims may be supported, disputed, narrowed, superseded, or withheld.
- Identity expectations: Claims need stable IDs and provenance links.
- Relationship to nearby concepts: Claims aggregate or interpret observations; mechanics generalize or operationalize recurring claims.
- Examples: A4 build likely improved High Tech support under this context.
- Common confusion risks: Writing claims so strongly that they effectively become undocumented mechanics.
- Planner implications: Weak or disputed claims should not be promoted to planner-safe truth without publication logic.

## Mechanic

- Canonical definition: A revisable statement about how colonisation behaves under some conditions.
- What it is: Domain behavior knowledge.
- What it is not: A planner rule, a decision, or a user preference.
- Lifecycle: Confirmed, likely, experimental, disputed, disproved, patch-sensitive, superseded.
- Identity expectations: Stable mechanic identity should persist across confidence changes and patch eras where possible.
- Relationship to nearby concepts: Mechanics are supported or contradicted by observations, claims, and experiments; planner rules consume mechanics.
- Examples: link routing behavior, economy inheritance behavior, construction-point behavior.
- Common confusion risks: Conflating contextual strategy with domain mechanic.
- Planner implications: Planner logic should cite mechanics, but not flatten them into universal policy when confidence is weak.

## Planner Rule

- Canonical definition: A planner-safety or planner-policy rule describing how the planner should behave when consuming knowledge.
- What it is: Operational policy for recommendation behavior.
- What it is not: A domain mechanic or a decision record.
- Lifecycle: Confirmed, revised, superseded, or withdrawn as planner policy changes.
- Identity expectations: Stable planner rule IDs.
- Relationship to nearby concepts: Planner rules depend on mechanics and decisions, but remain separate from both.
- Examples: do not universalize contextual strategies, block invalid plans instead of just down-scoring them.
- Common confusion risks: Treating planner rules as if they were statements about game truth.
- Planner implications: Mixing mechanic and planner-rule layers creates unsafe or opaque recommendations.

## Recommendation

- Canonical definition: A planner output describing a preferred, caveated, or rejected course of action under stated objectives and constraints.
- What it is: An execution-layer output.
- What it is not: A mechanic, a decision record, or a canonical facility state.
- Lifecycle: Generated per planning context; may expire or change when context, evidence, or objectives change.
- Identity expectations: Recommendation IDs should be runtime/context scoped, not treated as canonical repository identity.
- Relationship to nearby concepts: Recommendations consume planner-safe projections, rules, decisions, and objectives.
- Examples: preserve A5 as anchor; treat A4 as complementary High Tech support under current coverage.
- Common confusion risks: Treating a recommendation as if it permanently settles domain truth.
- Planner implications: Recommendations must expose objective, trade-off, confidence, and what-would-change fields.

## Decision

- Canonical definition: A first-class engineering or research choice explaining why a contextual approach was accepted, rejected, or superseded.
- What it is: A reasoning and governance object.
- What it is not: A recommendation, a mechanic, or a user preference.
- Lifecycle: Proposed, accepted, implemented, rejected, superseded.
- Identity expectations: Stable decision identity with explicit supersession links.
- Relationship to nearby concepts: Decisions cite evidence, mechanics, planner rules, and experiments; recommendations may depend on decisions.
- Examples: A5 as Industrial + Extraction anchor; Dodec not universally superior claim rejection.
- Common confusion risks: Treating a contextual decision as permanent game truth.
- Planner implications: Decisions can constrain or contextualize recommendations, but should not replace current-state analysis.

## Experiment

- Canonical definition: A first-class test record used to validate or challenge a mechanic, strategy, or contextual hypothesis.
- What it is: Structured empirical test intent and result.
- What it is not: A raw evidence item, a planner rule, or a general mechanic by itself.
- Lifecycle: Proposed, running, completed, inconclusive, superseded, repeated.
- Identity expectations: Experiment identity should remain stable across supporting evidence additions; repeated runs may later require run-level identity.
- Relationship to nearby concepts: Experiments use evidence, produce observations, and affect mechanic confidence.
- Examples: A4 complementary High Tech role test.
- Common confusion risks: Confusing one experiment result with a fully generalized mechanic.
- Planner implications: Experiment-backed uncertainty should often produce experiment-first recommendations instead of overconfident builds.

## Unknown

- Canonical definition: A durable unresolved question or unresolved semantic/mechanic gap.
- What it is: A first-class unresolved object.
- What it is not: Missing documentation, weak evidence silently ignored, or a contradiction case.
- Lifecycle: Open, narrowed, resolved, obsolete.
- Identity expectations: Stable unknown identity even after resolution.
- Relationship to nearby concepts: Unknowns differ from contradictions because they may reflect missing knowledge rather than conflicting knowledge.
- Examples: unresolved station-class modifier impact, unresolved market effect magnitude.
- Common confusion risks: Treating unknowns as if they were merely low-confidence claims.
- Planner implications: Unknowns should either block, caveat, or trigger validation recommendations.

## Contradiction

- Canonical definition: A durable review object created when credible evidence or interpretation conflicts with an existing observation, claim, mechanic, or projection.
- What it is: A conflict-management object.
- What it is not: An unknown, a negative evidence item by itself, or a planner rule.
- Lifecycle: Open, under review, resolved, historical.
- Identity expectations: Stable contradiction case identity with explicit targets.
- Relationship to nearby concepts: Contradictions reduce trust and may unpublish planner-safe knowledge.
- Examples: evidence challenging a mechanic or prior observation.
- Common confusion risks: Resolving contradictions silently by editing downstream text without preserving the contradiction record.
- Planner implications: Contradictions must lower confidence or withhold projection publication.

## Confidence

- Canonical definition: An explicit measure of trust attached to an interpreted object or recommendation.
- What it is: A layer-specific trust assessment.
- What it is not: Certainty, truth itself, or mere rhetorical emphasis.
- Lifecycle: Can rise, decay, split by patch era, or fall after contradiction.
- Identity expectations: Usually tracked as a record or attribute tied to an object and time.
- Relationship to nearby concepts: Confidence attaches to observations, claims, mechanics, experiments, projections, and recommendations, but with different meanings.
- Examples: High confidence mechanic, medium confidence recommendation, exploratory-only claim.
- Common confusion risks: Treating one confidence label as semantically identical across all interpretation layers.
- Planner implications: Planner confidence must be explicit and should not exceed the weakest critical dependency.

## Theory

- Canonical definition: A broader explanatory model composed of multiple mechanics or mechanic assertions.
- What it is: Higher-order interpretation.
- What it is not: A single mechanic or a planner recommendation.
- Lifecycle: May strengthen, split, or collapse as mechanics change.
- Identity expectations: Stable theory identity only if the project finds theories worth formalizing separately.
- Relationship to nearby concepts: A theory contains or coordinates mechanics.
- Examples: larger routing or economy-behavior explanatory model.
- Common confusion risks: Creating theories prematurely when mechanics are still too weak.
- Planner implications: The planner should consume explicit mechanics and planner-safe projections rather than broad informal theories.

## Architecture

- Canonical definition: A reusable colony structure or system design pattern combining roles, facilities, and expected effects under prerequisites.
- What it is: A planning pattern.
- What it is not: A universal mechanic or a facility identity.
- Lifecycle: Valid, contextual, experimental, superseded, or withheld depending on evidence and prerequisites.
- Identity expectations: Architecture patterns should be typed and context-aware if made first-class.
- Relationship to nearby concepts: Architectures sit below strategy and above concrete facility selection.
- Examples: Industrial Anchor + High Tech Support Body.
- Common confusion risks: Treating an architecture as universally optimal.
- Planner implications: Architectures must remain contextual and objective-dependent.

## Source

- Canonical definition: A source family or origin class from which evidence is captured.
- What it is: Provenance origin category.
- What it is not: An evidence item or an observation.
- Lifecycle: Source families are relatively stable; individual captures are versioned snapshots.
- Identity expectations: Source family and source snapshot should remain distinguishable.
- Relationship to nearby concepts: Sources produce or host evidence.
- Examples: Frontier docs, Inara pages, Raven pages, manual logs.
- Common confusion risks: Treating source reputation as sufficient proof of specific claims.
- Planner implications: Source authority matters, but does not replace specificity or corroboration.

## Confidence Record

- Canonical definition: A time-stamped record explaining why a given interpreted object has a particular confidence state.
- What it is: Confidence provenance.
- What it is not: The object being measured.
- Lifecycle: Accumulates historically as confidence changes.
- Identity expectations: May be a first-class linked record or versioned attribute.
- Relationship to nearby concepts: Measures observations, mechanics, experiments, claims, projections, or recommendations.
- Examples: confidence update after contradiction or live verification.
- Common confusion risks: Overwriting confidence state without retaining why it changed.
- Planner implications: Recommendation confidence should be explainable, not decorative.

## Knowledge Projection

- Canonical definition: A planner-safe projection derived from reviewed mechanics, claims, observations, decisions, contradictions, and publication rules.
- What it is: A runtime-safe operational knowledge surface.
- What it is not: Raw evidence, a user plan, or canonical repository truth.
- Lifecycle: Generated, versioned, published, caveated, withheld, superseded.
- Identity expectations: Must preserve lineage to canonical upstream objects and projection version metadata.
- Relationship to nearby concepts: Future tools should consume projections rather than raw evidence.
- Examples: body feasibility projection, strategy projection, recommendation constraint projection.
- Common confusion risks: Treating projections as manually edited canonical truth.
- Planner implications: The planner should consume projections as input contract and should not bypass them.

## Non-equivalence guardrails

These distinctions are especially important for future planner and API safety.

- A `System` is not the same thing as a `Colony`.
- A `Body` is not the same thing as an `Orbital` or `Surface Slot`.
- A `Surface Slot` is not the same thing as a built `Facility`.
- A `Facility` is not the same thing as a `Station`, even though a station is usually a facility subtype.
- A `Station Type` is not the same thing as a facility instance.
- A `Station Type` is not the same thing as a final inherited `Economy`.
- An `Economy` is not the same thing as an `Economy Role`.
- A `Commodity` is not the same thing as a `Construction Point`.
- `Evidence` is not the same thing as an `Observation`.
- An `Observation` is not the same thing as a `Claim`.
- A `Claim` is not the same thing as a `Mechanic`.
- A `Mechanic` is not the same thing as a `Planner Rule`.
- A `Decision` is not the same thing as a `Recommendation`.
- `Research Evidence` is not the same thing as `Operational Data`.
- `Operational Data` is not the same thing as `User Data`.
