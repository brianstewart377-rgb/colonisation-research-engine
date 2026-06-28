# Roles, Assets, Strategies, and Coverage

This document defines the planning concepts that sit above individual facilities.

## Why this layer exists

Colonisation planning should not start with facility selection. Facility selection is the last step of a decision process that begins with objectives, constraints, and coverage gaps.

Without this layer, a planner may incorrectly claim that one economy combination is universally better than another. In practice, viability depends on what the rest of the colony already provides.

## Asset

An asset is something useful that a colony provides or could provide.

Assets are the planner's true optimisation targets.

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

Questions:

- What assets are present?
- What assets are missing?
- Which missing assets matter to the player goal?
- Which assets are over-duplicated?
- Which assets are supplied by another body or companion system?

## Coverage Gap

A coverage gap is an asset that matters to the objective but is missing, weak, or unreliable.

Example:

If A5 already supplies Extraction and Refinery coverage, then A4 does not necessarily need to duplicate Extraction. A4 may instead be valuable as High Tech support if High Tech commodity coverage is missing.

## Role

A role is the intended function of a body, station, or facility group within the colony.

Roles are assigned based on objectives and coverage gaps.

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

## Architecture

An architecture is a reusable build pattern.

Examples:

- Industrial Anchor + High Tech Support Body
- Extraction/Refinery Primary Producer
- Water World Tourism Orbital Pair
- HMC Industrial Ground Cluster
- Moonlet Weak-Link Support Chain

An architecture should only be recommended when its prerequisites are met.

## Opportunity Cost

Opportunity cost is what is sacrificed by using slots, body roles, or construction effort for one option instead of another.

Examples:

- Two High Tech hubs consume slots that could have reinforced Industrial, Extraction, or Refinery.
- Adding another Extraction body may improve metals but may leave High Tech gaps unresolved.
- Demolishing a completed port may create theoretical optimisation gains but carries time, risk, and lost service cost.

## Research Opportunity

A research opportunity is an unresolved question that would improve mechanic confidence if tested.

Examples:

- Does High Tech as second economy materially improve construction-material coverage?
- Does commodity availability depend more on top-two economy rank or absolute economy percentage?
- Does a Planetary Port influence commodity distribution at linked stations?

## Unknown

Unknown is a valid outcome.

The planner should use `Unknown` when evidence does not support a confident answer. It should then suggest either a safer alternative or a validation experiment.

## Wregoe A4 framing

The A4 High Tech build should be recorded as a complementary-role experiment.

Incorrect framing:

`Industrial + High Tech is better than Industrial + Extraction.`

Correct framing:

`Given A5 already provides strong Extraction/Refinery/Industrial coverage, can A4 improve total system material coverage by taking a High Tech support role?`

This distinction is critical for future planner safety.
