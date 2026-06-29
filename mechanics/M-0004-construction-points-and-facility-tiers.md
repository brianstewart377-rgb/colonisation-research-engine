# M-0004 - Construction Points and Facility Tiers

## Summary

Colonisation facilities appear to be grouped into tiered construction-point relationships rather than behaving as flat build options. Tier requirements and tier generation must be modeled separately from raw material cost.

## Status

Likely

## Confidence

Current working confidence: 82%.

This mechanic is directly represented in the committed canonical source pack through `MG-0001`, with supporting repository evidence from Wregoe review material. It is good enough for planner warnings and analyst modeling, but still benefits from live corroboration on edge-case exceptions.

## Mechanic statement

- Tier 1 facilities require no construction points and generate Tier 2 construction points.
- Tier 2 facilities require Tier 2 construction points and generate Tier 3 construction points.
- Tier 3 facilities require Tier 3 construction points and do not generate further construction points.
- Primary Ports are treated as a special case because they generate applicable construction points but do not require construction points when established as the initial system port.

## Scope

- Body classes: all body classes that can host the relevant facility type
- Facility types: ports and supporting facilities with tiered construction behavior
- Economy types: not economy-specific
- Patch/version: canonical repository source state derived from `MG-0001`
- Known exclusions: live buildability in Architect remains authoritative if it disagrees with projected tier logic

## Planner behaviour

- Required behaviour:
  - model construction-point requirement, generation, and material cost as separate fields
  - distinguish current buildability from projected future buildability after planned construction
- Required warnings:
  - warn when a community planner total appears to include unbuilt proposed facilities
  - warn that negative projected CP totals are not automatically proof that the immediate next build is invalid
- Blocked outputs:
  - do not describe a facility as blocked solely because a projected full-plan total is negative
- When to suggest an experiment instead:
  - when Architect allows a build that the model marks impossible
  - when a port behaves unlike the projected tier exception

## Evidence basis

- `reference_sources/MG-0001-megaguide-v2-3/elite-dangerous-colonization-mega-guide-v2-3.txt`
- `EV-0004` - Colonisation Reference Documents Pack
- prior repository draft `M-0001-construction-points-and-facility-tiers.md`
- Wregoe notes preserved in the earlier draft regarding Raven negative CP totals versus live buildability

## Negative evidence preserved

- Raven proposed-build totals can show negative yellow/green balances while the immediate selected build remains valid in live Architect.
- Proposed-build math and currently buildable math must not be flattened into the same planner field.

## Contradictions

- `C-0003` - Raven proposed-build deficits versus live buildability interpretation

## Patch sensitivity

Medium. Construction-point logic is a core mechanic and could change through Frontier patching or planner-model drift.

## Related mechanics

- `M-0005` - Colony-Type and Specialised Ports
- `M-0006` - Strong and Weak Link Routing

## Related experiments

- `EXP-0000` - Wregoe Methodology Seed
- `LV-0005` - Main Port Routing and Link Aggregation

## Open questions

- Are there additional port exceptions beyond the initial Primary Port case?
- Does every planner-visible negative CP state fall cleanly into current-versus-proposed interpretation, or are there edge cases still unmodeled?
