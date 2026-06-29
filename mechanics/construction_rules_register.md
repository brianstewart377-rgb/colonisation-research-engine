# Construction Rules Register

This register decomposes the current mechanic catalogue into explicit construction-facing rules for future planners and analyzers.

## CR-0001 - Water worlds have no surface slots

- Status: Confirmed
- Source: `mechanics/M-0001-water-worlds-have-no-surface-slots.md`
- Rule: Water Worlds do not provide surface construction slots, so surface facilities cannot be recommended on them.
- Related mechanics: `M-0001`
- Planner implications: Surface recommendations on Water Worlds must be blocked.
- Testing status: Direct Wregoe evidence
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0002 - Construction points are distinct from material cost

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Rule: Construction-point gating and material cost should be modeled as separate planning dimensions.
- Related mechanics: `M-0004`
- Planner implications: A build can be blocked by CP even when commodities are available, or appear CP-negative in projection while the immediate next build is still valid.
- Testing status: Supported by repository interpretation
- Contradictions: `C-0003`
- Unknowns: None currently recorded

## CR-0003 - Tier 1 facilities generate Tier 2 construction points

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Rule: Tier 1 facilities require no construction points and generate Tier 2 construction points.
- Related mechanics: `M-0004`
- Planner implications: Early sequencing should prioritize how T1 unlocks later options.
- Testing status: Reference-derived
- Contradictions: None currently recorded
- Unknowns: Facility-by-facility exceptions

## CR-0004 - Tier 2 facilities consume Tier 2 and generate Tier 3 construction points

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Rule: Tier 2 facilities consume Tier 2 construction points and generate Tier 3 construction points.
- Related mechanics: `M-0004`
- Planner implications: Tier 2 sequencing determines which T3 options become available.
- Testing status: Reference-derived
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0005 - Tier 3 facilities consume Tier 3 construction points and do not generate more

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Rule: Tier 3 facilities consume Tier 3 construction points and are terminal in the basic generation chain.
- Related mechanics: `M-0004`
- Planner implications: T3 commitments should be planned carefully because they do not unlock further tiers.
- Testing status: Reference-derived
- Contradictions: None currently recorded
- Unknowns: Possible port-specific exceptions

## CR-0006 - The initial Primary Port is a construction-point exception

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Rule: The first Primary Port appears to generate relevant construction points without requiring construction points to be established.
- Related mechanics: `M-0004`
- Planner implications: Initial port creation should be modeled separately from later facility builds.
- Testing status: Reference-derived
- Contradictions: None currently recorded
- Unknowns: Whether all initial-port classes behave identically

## CR-0007 - Current buildability differs from proposed full-plan totals

- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Rule: A negative projected CP state across a full future plan is not enough to conclude that the next selected build is impossible right now.
- Related mechanics: `M-0004`
- Planner implications: Separate `current buildability` from `proposed build plan`.
- Testing status: Supported by Wregoe/Raven evidence
- Contradictions: `C-0003`
- Unknowns: Additional edge cases outside Raven

## CR-0008 - Placeholder names and visible previews are not enough to infer completion state

- Status: Confirmed as a caution rule
- Source: `evidence/EV-0002-wregoe-raven-proposed-build-review.md`, `evidence/EV-0003-a4-t3-station-selection-previews.md`
- Rule: Placeholder names, proposal labels, or preview panels do not by themselves prove that a facility is completed and mechanically active.
- Related mechanics: `M-0004`, `M-0005`
- Planner implications: Distinguish proposed, under-construction, previewed, and completed states.
- Testing status: Confirmed as a repository-handling rule
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0009 - The completed primary port is effectively permanent

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Once completed, the primary port cannot be changed; it can only be cancelled or abandoned before completion.
- Related mechanics: `M-0004`, `M-0009`
- Planner implications: Primary-port selection needs stronger review than ordinary additive build decisions.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0010 - T2 and T3 port escalation begins when construction starts

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: The escalating CP cost for Tier 2 and Tier 3 ports begins as soon as construction is initiated, not when the port is completed.
- Related mechanics: `M-0004`, `M-0009`
- Planner implications: Starting a high-tier port early can make every later high-tier port more expensive immediately.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0011 - The primary port is exempt from high-tier port escalation

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: The primary port does not count toward the escalating T2/T3 port cost limit.
- Related mechanics: `M-0004`, `M-0009`
- Planner implications: A T3 primary port effectively grants a free top-tier anchor outside later CP escalation math.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0012 - T1 ports, settlements, hubs, and installations are exempt from high-tier port escalation

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: T1 ports and all non-port facility families are exempt from the escalating T2/T3 port cost mechanic.
- Related mechanics: `M-0004`, `M-0009`
- Planner implications: Use exempt facility families to expand support without inflating later T2/T3 port costs.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0013 - Construction concurrency is capped at five facilities

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: No more than five facilities can be under construction at the same time in one system.
- Related mechanics: `M-0004`, `M-0009`
- Planner implications: Build sequencing must be scheduled in waves of five or fewer.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0014 - Large settlements are the best green-CP conversion tool

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Large Tier 2 settlements convert one yellow CP into two green CP, making them uniquely efficient green-CP generators.
- Related mechanics: `M-0004`, `M-0009`
- Planner implications: Use large settlements for temporary or permanent green-CP farming in capital builds.
- Testing status: Extracted from Mega Guide v2.3.0 and DaftMav-derived tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0015 - Primary-installation material surcharges are tier-specific

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: The first installation carries a resource surcharge of +16% for Tier 1, +32% for Tier 2, and +20% for Tier 3.
- Related mechanics: `M-0009`
- Planner implications: Add primary-installation surcharges into first-wave logistics instead of using standard facility totals.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0016 - Medium settlements cost exactly double small settlements of the same type

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Medium settlements require exactly 2x the resources of small settlements of the same type.
- Related mechanics: `M-0009`
- Planner implications: Resource planning for medium settlements can be safely estimated from small-settlement baselines.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0017 - Large settlements cost exactly triple small settlements of the same type

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Large settlements require exactly 3x the resources of small settlements of the same type.
- Related mechanics: `M-0009`
- Planner implications: Large-settlement hauling estimates can be derived directly from small-settlement baselines.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0018 - Military Installations require a Military Settlement

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Military Installations require a Military Settlement as a prerequisite.
- Related mechanics: `M-0009`
- Planner implications: Military space infrastructure is a two-step chain, not a direct pick.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0019 - Security Stations require a Relay Station

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Security Stations require a Relay Station as a prerequisite.
- Related mechanics: `M-0009`
- Planner implications: Security-focused orbital chains need an earlier communications step.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0020 - Research Stations require a Bio Research Settlement

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Research Stations require a Bio Research Settlement as a prerequisite.
- Related mechanics: `M-0009`
- Planner implications: High Tech orbital research routes need matching ground science support.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0021 - Tourist Installations require a Tourism Settlement

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Tourist Installations require a Tourism Settlement as a prerequisite.
- Related mechanics: `M-0009`
- Planner implications: Tourism orbital chains start with a ground-tourism dependency.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0022 - Tourism settlements require a Satellite Installation

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Tourism settlements require a Satellite Installation as a prerequisite.
- Related mechanics: `M-0009`
- Planner implications: Tourism chains consume both an orbital support slot and a ground slot before hubs or higher tourism effects.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## CR-0023 - Multiple hub classes have facility-specific prerequisites

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Surface hubs do not share a universal prerequisite; each hub class uses a specific settlement or installation requirement.
- Related mechanics: `M-0009`
- Planner implications: Hub planning must be dependency-aware at the individual facility class level.
- Testing status: Extracted from DaftMav-derived reference tables
- Contradictions: None currently recorded
- Unknowns: None currently recorded
