# Roles, Assets, Strategies, and Coverage

This document defines the planning concepts that sit above individual facilities.

## Why this layer exists

Colonisation planning should not start with facility selection. Facility selection is the last step of a decision process that begins with objectives, constraints, and coverage gaps.

Without this layer, a planner may incorrectly claim that one economy combination is universally better than another. In practice, viability depends on what the rest of the colony already provides.

## Semantic rule

This document defines planning semantics, not physical identity.

The concepts here are usually:

- contextual
- objective-dependent
- planner-facing

They must not be silently collapsed into:

- mechanics
- facility types
- economy states
- immutable world truth

## Colony state

A colony is the current or historical planning state of a system.

For planning purposes, colony state includes:

- facilities
- slot capacity
- body modifiers
- market relationships
- services
- current roles already covered
- unresolved risks and unknowns

Colony state is not identical to system identity.

Planner implication:

- The planner optimizes a colony state under an objective, not a system name in isolation.

## Asset

An asset is something useful that a colony provides or could provide.

Assets are the planner's true optimisation targets.

An asset is not necessarily a facility.
It is often an outcome, capability, or useful property exposed through facilities, markets, or body context.

Planner implication:

- The planner should optimize for assets first and choose facilities later.

### Asset categories

- Commodity Asset
- Economy Asset
- Service Asset
- Mission Asset
- Strategic Asset
- Infrastructure Asset

### Commodity Asset

A commodity that the player wants locally available or supported through market behaviour.

Examples:

- Steel
- Titanium
- Aluminium
- CMM Composite
- Ceramic Composites
- Computer Components
- Semiconductors
- Superconductors
- Robotics
- Auto-Fabricators
- Micro Controllers

### Economy Asset

An economy type that matters because it influences commodities, missions, services, or system identity.

An economy asset is not the same thing as an economy role.

Examples:

- Industrial economy presence
- High Tech economy presence
- Extraction economy presence

Examples:

- Industrial
- Extraction
- Refinery
- High Tech
- Agriculture
- Tourism
- Military

### Service Asset

A station or facility service useful to players.

Examples:

- Shipyard
- Outfitting
- Tech broker
- Material trader
- Interstellar Factors
- Black market

### Mission Asset

A mission-board profile or useful mission type.

Examples:

- Industrial missions
- Tourism passenger missions
- High Tech delivery missions
- Extraction/source-and-return missions
- Security/Military missions

### Strategic Asset

A wider colony property.

Examples:

- Population
- Security
- Development
- Wealth
- Tech level
- BGS usefulness

## Coverage

Coverage is the set of assets already provided by the current colony state.

Coverage should be measured before recommending builds.

Coverage is not:

- total structure count
- economy labels alone
- facility count alone

Coverage is the useful asset set already exposed by the current colony state.

Questions:

- What assets are present?
- What assets are missing?
- Which missing assets matter to the player goal?
- Which assets are over-duplicated?
- Which assets are supplied by another body or companion system?

## Coverage Gap

A coverage gap is an asset that matters to the objective but is missing, weak, or unreliable.

A coverage gap is not just an empty slot.
It is an objective-relative shortage.

Example:

If A5 already supplies Extraction and Refinery coverage, then A4 does not necessarily need to duplicate Extraction. A4 may instead be valuable as High Tech support if High Tech commodity coverage is missing.

## Role

A role is the intended function of a body, station, or facility group within the colony.

Roles are assigned based on objectives and coverage gaps.

A role is not:

- a station type
- a final inherited economy
- a mechanic
- a facility identity

Identity expectations:

- Roles are usually taxonomy or assignment objects, not physical identity roots.

Relationship to nearby concepts:

- A role describes intended contribution.
- An economy describes observed or projected colony state.
- A strategy uses one or more roles.
- An architecture realizes roles through a reusable pattern.

Examples:

- Primary Metals Producer
- Primary Refinery Producer
- Industrial Anchor
- High Tech Support
- Extraction Support
- Tourism Mission Hub
- Agriculture Mission Hub
- Security Support
- Research Support
- Population Driver
- Service Hub
- Link Repair Candidate
- Experiment Testbed

Planner implication:

- Recommendations should usually select roles before selecting specific facilities.

## Economy role

An economy role is a role framed in economic contribution terms, such as:

- Industrial anchor
- High Tech support
- Extraction support
- Refinery primary producer

An economy role is not the same thing as final observed economy percentages or inherited economy ordering.

Planner implication:

- The planner may recommend an economy role even when exact economy outcomes remain caveated.

## Objective

An objective is the top-level answer to what the player is trying to optimize.

An objective is not:

- a facility
- a role
- an architecture
- a universal success criterion

Examples:

- Maximum construction-material coverage
- Maximum mission density
- Minimum demolition risk
- No cargo-hauling dependency

Planner implication:

- Objectives must be fixed before comparing architectures or facilities.

## Strategy

A strategy is a context-aware approach for achieving an objective.

A strategy includes:

- Objective
- Constraints
- Existing coverage
- Target coverage gap
- Recommended role
- Architecture pattern
- Facility candidates
- Expected gains
- Opportunity cost
- Evidence and confidence

Strategies are not universal rules.

A strategy is not:

- a mechanic
- a planner rule
- a station type
- a single facility choice

Relationship to nearby concepts:

- Objective sets the target.
- Coverage analysis identifies the gap.
- Role identifies intended contribution.
- Strategy selects a context-aware path.
- Architecture provides reusable structure.
- Facility choice realizes the strategy.

Planner implication:

- A planner should recommend strategies only in the context that made them viable.

## Architecture

An architecture is a reusable build pattern.

Examples:

- Industrial Anchor + High Tech Support Body
- Extraction/Refinery Primary Producer
- Water World Tourism Orbital Pair
- HMC Industrial Ground Cluster
- Moonlet Weak-Link Support Chain

An architecture should only be recommended when its prerequisites are met.

An architecture is not:

- a universal truth
- a body identity
- a recommendation on its own

Planner implication:

- Architecture should remain a pattern library, not a substitute for current-state analysis.

## Market

A market is the commodity, service, and mission exposure surface visible to players.

A market is influenced by:

- facility mix
- economy state
- link behavior
- body context
- station type and modifier interactions

A market is not:

- the same thing as economy
- the same thing as a commodity
- guaranteed by a role label alone

Planner implication:

- The planner should describe market outcomes as observed, projected, or uncertain rather than treating them as direct role outputs.

## Opportunity Cost

Opportunity cost is what is sacrificed by using slots, body roles, or construction effort for one option instead of another.

Opportunity cost is not just resource cost.
It also includes:

- lost alternative roles
- lost slot flexibility
- demolition risk
- confidence burden
- delayed validation opportunities

Examples:

- Two High Tech hubs consume slots that could have reinforced Industrial, Extraction, or Refinery.
- Adding another Extraction body may improve metals but may leave High Tech gaps unresolved.
- Demolishing a completed port may create theoretical optimisation gains but carries time, risk, and lost service cost.

## Research Opportunity

A research opportunity is an unresolved question that would improve mechanic confidence if tested.

A research opportunity is not automatically a build recommendation.

Examples:

- Does High Tech as second economy materially improve construction-material coverage?
- Does commodity availability depend more on top-two economy rank or absolute economy percentage?
- Does a Planetary Port influence commodity distribution at linked stations?

## Unknown

Unknown is a valid outcome.

The planner should use `Unknown` when evidence does not support a confident answer. It should then suggest either a safer alternative or a validation experiment.

Unknown is not failure.
Unknown is a valid semantic outcome when evidence is insufficient.

Planner implication:

- Unknown should trigger caveat, withholding, or experiment-first behavior rather than fake certainty.

## Recommendation

A recommendation is a planner output produced after:

1. objective selection
2. constraint filtering
3. coverage analysis
4. role and strategy comparison
5. architecture and facility ranking

A recommendation is not:

- a mechanic
- a decision record
- a universal rule
- proof that the recommended result will definitely occur

Recommendations should include:

- objective served
- gap targeted
- role selected
- architecture selected
- candidate facilities
- expected gains
- expected losses
- confidence
- unknowns
- what would change the answer

Planner implication:

- Recommendations must remain contextual, ranked, and explainable.

## Wregoe A4 framing

The A4 High Tech build should be recorded as a complementary-role experiment.

Incorrect framing:

`Industrial + High Tech is better than Industrial + Extraction.`

Correct framing:

`Given A5 already provides strong Extraction/Refinery/Industrial coverage, can A4 improve total system material coverage by taking a High Tech support role?`

This distinction is critical for future planner safety.

## Non-equivalence guardrails

- Coverage is not the same thing as slot count.
- Coverage gap is not the same thing as empty capacity.
- Role is not the same thing as economy.
- Economy role is not the same thing as final inherited economy state.
- Strategy is not the same thing as mechanic.
- Architecture is not the same thing as universal best practice.
- Recommendation is not the same thing as decision.
- Research opportunity is not the same thing as build advice.
