# Mechanic Dependency Register

This register records how the current mechanics depend on one another.

Dependencies here are logical knowledge dependencies, not claims that the game engine necessarily computes them in the same order.

## MD-0001 - Station economy inheritance depends on rejecting manual economy choice

- Status: Confirmed
- Source: `mechanics/M-0002-station-economy-is-inherited.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`
- Dependency:
  - prerequisite mechanic: `M-0002`
  - dependent mechanic: `M-0007`
- Meaning: The richer inherited-economy model only makes sense after the planner has rejected direct manual station economy selection.
- Planner implication: `M-0002` is the safety gate; `M-0007` is the modeling layer.

## MD-0002 - Colony-type versus specialised-port reasoning depends on port taxonomy before economy modeling

- Status: Likely
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`
- Dependency:
  - prerequisite mechanic: `M-0005`
  - dependent mechanic: `M-0007`
- Meaning: Economy inheritance cannot be modeled safely until the planner knows whether the port is colony-type or specialised.
- Planner implication: Port classification should happen before economy projection.

## MD-0003 - Body-economy modeling depends on inherited-economy assumptions

- Status: Likely
- Source: `mechanics/M-0007-colony-port-economy-inheritance.md`, `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- Dependency:
  - prerequisite mechanic: `M-0007`
  - dependent mechanic: `M-0008`
- Meaning: Body type and local modifiers matter because economy is inherited rather than manually assigned.
- Planner implication: Body-modeling should be disabled or caveated if inherited-economy assumptions are under dispute.

## MD-0004 - Weak-link insufficiency is a special case inside the broader routing model

- Status: Confirmed for narrow scope
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`
- Dependency:
  - prerequisite mechanic: `M-0006`
  - dependent mechanic: `M-0003`
- Meaning: `M-0003` is best understood as a narrow negative-evidence case constraining the broader routing heuristic in `M-0006`.
- Planner implication: Use `M-0003` to limit over-generalization of `M-0006`.

## MD-0005 - Main-port routing interpretations depend on port hierarchy and construction state

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `mechanics/M-0005-colony-type-and-specialised-ports.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`
- Dependency:
  - prerequisite mechanics: `M-0004`, `M-0005`
  - dependent mechanic: `M-0006`
- Meaning: Routing interpretations involving main surface and orbital ports depend on knowing which ports exist, which are main, and what class they are.
- Planner implication: Link reasoning without state and port taxonomy is incomplete.

## MD-0006 - Construction-point planning depends on state interpretation

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Dependency:
  - prerequisite concept: proposal versus current build state
  - dependent mechanic: `M-0004`
- Meaning: Construction-point logic is unsafe if proposal, preview, and completed states are collapsed together.
- Planner implication: Build-state classification is effectively a prerequisite for construction reasoning.

## MD-0007 - Water-world slot limits constrain all downstream construction and strategy logic

- Status: Confirmed
- Source: `mechanics/M-0001-water-worlds-have-no-surface-slots.md`
- Dependency:
  - prerequisite mechanic: `M-0001`
  - dependent domains: construction, body-role planning, strategy
- Meaning: Body constraints can pre-empt all later planning choices.
- Planner implication: Body feasibility checks must occur before higher-level strategy reasoning.
