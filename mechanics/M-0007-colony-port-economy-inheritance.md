# M-0007 - Colony Port Economy Inheritance

## Summary

Colony-type ports should be modeled as inheriting economy outcomes from local body context and market-link effects rather than from a direct player-selected final economy.

Semantic guardrail:

- `station type` or `port class` constrains behavior, but it is not the same thing as final inherited economy state.
- `economy outcome` is not the same thing as `economy role`.
- `market output` is downstream from inherited economy behavior and should not be treated as a synonym for preview labels.

## Status

Likely

## Confidence

Current working confidence: 83%.

The repository contains both strong planner-safety evidence and direct canonical-source support for this mechanic, especially through `MG-0001`. It is not yet fully confirmed at formula level, but it is robust enough to block incorrect planner behavior.

## Mechanic statement

- Colony-type ports do not expose a free manual economy-selection mechanic.
- Their economy outcome is shaped by:
  - the local body's base inheritable economy tendencies
  - local body economy modifiers
  - strong links
  - weak links
- Specialised ports retain an inherent economy baseline, though visible market behavior may still be affected by links.

## Scope

- Body classes: any body that can host a colony-type port
- Facility types: colony-type ports and specialised ports used for comparison
- Economy types: inherited economy mixes and link-driven market outcomes
- Patch/version: repository reference state; relevant to post-launch colonisation patches
- Known exclusions: exact percentage-to-commodity conversion remains unresolved in the repository

## Planner behaviour

- Required behaviour:
  - never offer a fake `choose economy` control for colony-type ports
  - estimate economy outcome indirectly through body context and link structure
  - label projected economy outcomes by confidence
- Required warnings:
  - preview labels and inferred economy mixes are not equivalent to final post-build commodity certainty
  - inherited-economy behavior may drift across patches
- Blocked outputs:
  - do not instruct the user to manually set a colony-type station to a chosen economy
- When to suggest an experiment instead:
  - when final market output matters more than preview economy mix
  - when two port classes appear equivalent in preview but may diverge after completion

## Evidence basis

- `M-0002` - Station Economy Is Inherited, Not Manually Chosen
- `reference_sources/MG-0001-megaguide-v2-3/elite-dangerous-colonization-mega-guide-v2-3.txt`
- `EV-0001` - Rocha Liberty Post High Tech Build Evidence
- `EV-0003` - A4 T3 Station Selection Preview Evidence
- `EV-0004` - Colonisation Reference Documents Pack
- prior repository draft `M-0004-colony-port-economy-inheritance.md`

## Negative evidence preserved

- Early planner language that implied a user could directly choose a station economy has already been invalidated inside the repository.
- Current preview evidence does not prove that station class alone bypasses inherited-economy behavior.

## Contradictions

- `C-0002` - Station-class superiority remains unproven in current preview evidence

## Patch sensitivity

High. This mechanic depends on economy inheritance and link math, both of which are sensitive to patch drift.

## Related mechanics

- `M-0002` - Station Economy Is Inherited, Not Manually Chosen
- `M-0005` - Colony-Type and Specialised Ports
- `M-0006` - Strong and Weak Link Routing
- `M-0008` - Local Body Base Economies and Modifiers

## Related experiments

- `EXP-0001` - A4 Complementary High Tech Role
- `LV-0001` - A4 High Tech Threshold and Commodity Coverage
- `LV-0002` - Post-Build Station Class Market Differences

## Related decisions

- `D-0002` - Use A4 as the complementary Industrial + High Tech support body
- `D-0003` - Reject any claim that Dodec is universally superior to Orbis or Ocellus based solely on the currently available evidence

## Open questions

- How are inherited economy percentages translated into final commodity exposure?
- When top-two economies are close, does rank order matter more than absolute value?
