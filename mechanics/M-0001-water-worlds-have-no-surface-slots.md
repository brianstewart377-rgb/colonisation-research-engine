# M-0001 — Water Worlds Have No Surface Slots

## Summary

Water Worlds cannot host planetary surface facilities in Elite Dangerous Colonisation. They may provide orbital construction opportunities, but they should not be treated as candidates for ground settlements, hubs, ports, or other surface builds.

## Status

Confirmed.

## Confidence

100% for planner purposes.

## Mechanic statement

If a body is classified as a Water World, the planner must not recommend surface facilities for that body.

## Planner behaviour

- Block all surface-build recommendations on Water Worlds.
- Allow orbital recommendations only where the system/body data reports available orbital slots.
- Treat any plan requiring Water World surface slots as invalid.
- Do not attempt to infer hidden surface slots from screenshots, economy type, or player naming.

## Evidence basis

- Repeated internal Wregoe planning observations confirmed that planets 5, 6, 7, and 8 were Water Worlds with orbital slots only.
- Multiple plan revisions were required after earlier assumptions incorrectly treated Water Worlds as possible surface-build bodies.
- This mechanic is also consistent with live Architect behaviour as observed during Wregoe planning.

## Negative evidence preserved

Earlier planning assumptions that attempted to place surface facilities on Water Worlds were invalidated. These failures should remain recorded because they represent a common planning error.

## Contradictions

None currently recorded.

## Patch sensitivity

Low. This is treated as a body-slot availability mechanic, not a balance-weighting mechanic. Re-check only if Frontier changes colonisation slot rules for body classes.

## Related mechanics

- M-0002 — Station Economy Is Inherited, Not Manually Chosen

## Open questions

None for MVP planner safety.
