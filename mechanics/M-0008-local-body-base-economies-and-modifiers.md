# M-0008 - Local Body Base Economies and Modifiers

## Summary

Local body type appears to establish baseline inheritable economy tendencies for colony-type ports, and body features then apply a limited set of modifiers that should be modeled explicitly rather than guessed from station class.

## Status

Likely

## Confidence

Current working confidence: 79%.

The rule set is directly preserved in the committed canonical source pack through `MG-0001`, with compatible supporting structure from `DM-0001`. This is best treated as a structured hypothesis layer with strong planner usefulness and clear live-verification needs.

## Mechanic statement

The canonical repository source set says colony-type ports inherit economy tendencies from local body type and then apply local body modifiers.

### Base inheritable economies

| Local body type | Base inheritable economies |
|---|---|
| Black holes, neutron stars, white dwarves | High Tech, Tourism |
| Brown dwarves and all other star types | Military |
| Earth-like worlds | Agriculture, High Tech, Military, Tourism |
| Water worlds | Agriculture, Tourism |
| Ammonia worlds | High Tech, Tourism |
| Gas giants | High Tech, Industrial |
| High metal content and metal rich worlds | Extraction |
| Rocky ice worlds | Industrial, Refinery |
| Rocky worlds | Refinery |
| Icy worlds | Industrial |

### Local body modifiers

| Local body modifier | Economy modifier |
|---|---|
| Rings, including stars with asteroid belts | + Extraction |
| Organics | + Agriculture, + Terraforming |
| Geologically active body | + Extraction, + Industrial |

The repository draft also records a non-stacking claim:

- local body modifiers do not stack with base planet economies
- local body modifiers do not stack with each other

## Scope

- Body classes: stars, planets, moons, and ring-bearing bodies used for colony placement
- Facility types: colony-type ports whose economy is inherited rather than inherently fixed
- Economy types: Agriculture, Tourism, High Tech, Military, Industrial, Extraction, Refinery, Terraforming
- Patch/version: canonical repository source state derived from `MG-0001`
- Known exclusions: final market output still depends on link effects and post-build verification

## Planner behaviour

- Required behaviour:
  - compute a first-pass economy hypothesis from body type before applying link effects
  - keep body modifiers explicit rather than buried in narrative text
  - preserve the draft non-stacking rule as a caveated assumption
- Required warnings:
  - body-driven economy expectations are hypotheses until confirmed by live preview or market evidence
  - water-world bias and other strong body tendencies may overwhelm naive station-type assumptions
- Blocked outputs:
  - do not double-count rings, organics, or geological features without direct evidence that stacking occurs
- When to suggest an experiment instead:
  - when a body appears to violate the draft non-stacking rule
  - when preview or final market evidence conflicts with the expected inherited baseline

## Evidence basis

- `reference_sources/MG-0001-megaguide-v2-3/elite-dangerous-colonization-mega-guide-v2-3.txt`
- `reference_sources/DM-0001-daftmav-construction-details/DaftMav_Colonization.csv`
- `EV-0004` - Colonisation Reference Documents Pack
- prior repository draft `M-0005-local-body-base-economies-and-modifiers.md`
- `M-0001` - Water Worlds Have No Surface Slots
- `M-0007` - Colony Port Economy Inheritance

## Negative evidence preserved

- Water Worlds in Wregoe repeatedly resisted assumptions that station class alone could override their body-driven tendencies.
- The repository does not yet contain direct live confirmation for every body class in the table above.

## Contradictions

None currently recorded, but several rows remain under live-verification pressure because the stacking and Terraforming behaviors are not yet fully live-confirmed.

## Patch sensitivity

High. Body-economy and modifier interactions are prime candidates for post-patch drift.

## Related mechanics

- `M-0001` - Water Worlds Have No Surface Slots
- `M-0002` - Station Economy Is Inherited, Not Manually Chosen
- `M-0007` - Colony Port Economy Inheritance

## Related experiments

- `EXP-0001` - A4 Complementary High Tech Role
- `LV-0001` - A4 High Tech Threshold and Commodity Coverage
- `LV-0004` - Local Body Modifier Non-Stacking

## Open questions

- Which rows in the body table have direct in-repository live corroboration versus only canonical-source support?
- Does Terraforming appear only as a modifier-style effect, or can it dominate final port behavior in some contexts?
