# Decision Support Model

The Colonisation Research Engine is not designed to produce bare build instructions. It is designed to support decisions by explaining objectives, constraints, viable options, trade-offs, evidence, confidence, and conditions that would change the recommendation.

## Core principle

The planner should not optimise a planet in isolation. It should optimise a player objective within the current colony context.

Facilities are implementation details. They are near the bottom of the reasoning chain, not the beginning.

## Reasoning hierarchy

The planner should reason in this order:

1. Player objective
2. Constraints
3. Current colony state
4. Coverage analysis
5. Coverage gaps
6. Candidate roles
7. Candidate architectures
8. Candidate facilities
9. Expected outcomes
10. Confidence and caveats

## Objectives

An objective describes what the player is trying to achieve.

Examples:

- Maximum construction-material coverage
- Maximum mission density
- Maximum local production for bootstrapping
- Maximum High Tech coverage
- Maximum Refinery coverage
- Maximum tourism/agriculture missions
- Minimum demolition risk
- No cargo-hauling dependency

Objectives are not facilities. The same objective may be achieved by different architectures depending on context.

## Constraints

Constraints remove invalid or undesirable plans before the planner begins recommending facilities.

Examples:

- Body slot counts
- Surface/orbital availability
- Existing completed facilities
- Facilities the player refuses to demolish
- Body class restrictions
- Patch-era mechanics
- Player preference against hauling
- Known missing market coverage
- Current system roles already covered elsewhere

A plan that violates constraints should be blocked, not merely given low confidence.

## Coverage analysis

Coverage means the useful assets the colony already provides.

Coverage can include:

- Commodity coverage
- Economy coverage
- Facility role coverage
- Market-link coverage
- Mission-type coverage
- Service coverage
- Strategic/BGS coverage

The planner should ask:

- What assets are already covered?
- What assets are missing?
- What assets are duplicated too heavily?
- Which missing assets matter to the player's stated objective?

## Assets

An asset is anything useful the colony can provide.

### Commodity assets

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

### Economy assets

Examples:

- Industrial
- Extraction
- Refinery
- High Tech
- Agriculture
- Tourism
- Military
- Security

### Service assets

Examples:

- Shipyard
- Outfitting
- Material trader
- Tech broker
- Interstellar Factors
- Black market

### Mission assets

Examples:

- Industrial missions
- Extraction missions
- Tourism missions
- Agriculture missions
- High Tech missions
- Security/Military missions

## Roles

A role describes what a body, facility group, station, or system is intended to contribute to the wider colony.

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

Roles are context-dependent. A role can be valid in one system and wasteful in another.

## Architectures

An architecture is a reusable pattern of bodies, facilities, economies, and roles.

Example:

`Industrial Anchor + High Tech Support Body`

This architecture is not universally better than `Industrial + Extraction`. It is viable when Extraction/Refinery coverage is already supplied elsewhere and the current gap is High Tech-related asset coverage.

## Trade-offs

Every recommendation should state what is gained and what is sacrificed.

Examples:

- Building High Tech hubs may gain electronics-related commodity coverage while consuming slots that could reinforce Industrial, Extraction, or Refinery.
- Reinforcing Extraction may strengthen metals availability but may fail to address missing High Tech commodities.
- Duplicating an already-covered role may improve resilience but reduce total material diversity.

## Recommendation standard

Every recommendation should answer:

1. Why this?
2. Why not the obvious alternative?
3. What evidence supports it?
4. What would change this recommendation?

## Planner output shape

A planner recommendation should include:

- Objective being served
- Current coverage summary
- Coverage gap being targeted
- Recommended role
- Recommended architecture
- Candidate facilities
- Expected gains
- Expected losses or opportunity cost
- Mechanics used
- Evidence used
- Confidence band
- Unknowns
- What would change the recommendation

## Wregoe A4 example

The A4 High Tech experiment is not testing whether Industrial + High Tech is universally better than Industrial + Extraction.

It is testing whether A4 can serve as a complementary High Tech support body in a system where A5 already provides strong Extraction/Refinery/Industrial material coverage.

The better research question is:

Can promoting High Tech to second place on A4 improve Wregoe's total construction-material coverage without unacceptable loss of other useful assets?

## Safety rule

The planner must never flatten a contextual strategy into a universal rule. A strategy is only valid under the constraints, coverage state, and objective that made it viable.
