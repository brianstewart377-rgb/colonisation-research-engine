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
