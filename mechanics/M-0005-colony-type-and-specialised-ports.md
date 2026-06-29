# M-0005 - Colony-Type and Specialised Ports

## Summary

Ports do not appear to belong to a single shared behavior class. The repository evidence distinguishes colony-type ports from specialised ports, with different economy-baseline behavior and different planner assumptions.

## Status

Likely

## Confidence

Current working confidence: 80%.

This mechanic is directly supported by the committed canonical source pack, especially `MG-0001`, and remains compatible with current A4 preview evidence.

## Mechanic statement

- Colony-type ports have `Colony` as their facility economy in preview and acquire effective economy behavior from local body context plus market-link effects.
- Specialised ports have an inherent economy baseline and should not be treated as inheriting the local body's base economy in the same way.
- Strong and weak links may still affect what a specialised port exposes even if its baseline economy is inherent.

## Scope

- Body classes: any body capable of hosting the relevant port
- Facility types:
  - colony-type examples: Civilian space outpost, Commercial space outpost, Coriolis, Orbis, Ocellus, Civilian planetary outpost, Tier 3 Planetary Port
  - specialised ports: any non-colony-type port with inherent economy behavior
- Economy types: colony, inherited economy mixes, inherent port economies
- Patch/version: canonical repository source state derived from `MG-0001`
- Known exclusions: post-build live market output is still more authoritative than preview labels

## Planner behaviour

- Required behaviour:
  - distinguish colony-type ports from specialised ports in planner logic
  - avoid treating all large-pad ports as mechanically identical
- Required warnings:
  - preview equality does not prove post-build market equality
  - visible `Facility Economy: Colony` does not mean the player can choose the final market economy manually
- Blocked outputs:
  - do not assume station class alone determines final economy outcome
- When to suggest an experiment instead:
  - when comparing Orbis, Ocellus, Dodec, or layout variants for final market/service differences

## Evidence basis

- `reference_sources/MG-0001-megaguide-v2-3/elite-dangerous-colonization-mega-guide-v2-3.txt`
- `EV-0003` - A4 T3 Station Selection Preview Evidence
- `EV-0004` - Colonisation Reference Documents Pack
- prior repository draft `M-0002-colony-type-and-specialised-ports.md`

## Negative evidence preserved

- No repository evidence currently proves that Orbis, Ocellus, or Dodec automatically yield a superior final economy outcome purely from station class.
- No repository evidence currently proves that Apollo and Artemis Orbis variants differ mechanically in preview behavior.

## Contradictions

- `C-0002` - Station-class superiority remains unproven against current preview evidence

## Patch sensitivity

Medium. Port taxonomy may remain stable while downstream economy weighting changes across patches.

## Related mechanics

- `M-0002` - Station Economy Is Inherited, Not Manually Chosen
- `M-0007` - Colony Port Economy Inheritance
- `M-0008` - Local Body Base Economies and Modifiers

## Related experiments

- `EXP-0001` - A4 Complementary High Tech Role
- `LV-0002` - Post-Build Station Class Market Differences

## Open questions

- Which specialised port classes are fully exempt from local-body economy inheritance, and which only partially resist it?
- Do any port classes diverge only after completion, services unlock, or mission-board population?
