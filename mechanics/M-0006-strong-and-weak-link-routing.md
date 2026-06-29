# M-0006 - Strong and Weak Link Routing

## Summary

Strong and weak links do not seem to be interchangeable. The repository evidence consistently treats strong links as local body-level market-shaping tools and weak links as cross-body spillover that is useful but less dependable for targeted outcome control.

## Status

Likely

## Confidence

Current working confidence: 84%.

This mechanic is strongly represented in the repository through `FW-0001`, `MG-0001`, and Wregoe-context evidence. The routing model is reliable enough for planner heuristics, but exact commodity effects and some multi-port edge cases still need live verification.

## Mechanic statement

- Strong links are local same-body relationships and are the preferred mechanism for deliberately shaping a target market.
- Weak links are cross-body system-wide spillover and should not be treated as guaranteed market-control tools.
- A body's Main Port is the highest-tier port on that body; if tied, the first built is selected.
- Facilities on the same body route strong links to that body's Main Port rather than to every eligible local port.
- If a body has both a Main Surface Port and a Main Orbital Port, strong-link influence may route through the main surface port into the main orbital port, meaning displayed link arrows may aggregate multiple upstream contributors.
- Main Ports receive strong and weak links, but the reference-source routing model says they should not themselves generate weak links.
- Weak links are received by the highest-tier port on the other body, or the earliest built if the receiving ports are tied.
- Adding a second same-body port can change which port receives or emits the relevant weak-link behavior in the illustrated multi-port cases.

## Scope

- Body classes: colony bodies with multiple facilities and at least one qualifying port
- Facility types: ports, hubs, settlements, installations, and other economy-contributing facilities
- Economy types: any economy affected by strong or weak routing
- Patch/version: repository reference state derived from `EV-0004` and Wregoe evidence context
- Known exclusions: visible arrow count alone does not fully reveal the underlying contribution graph
- Known exclusions: the exact numerical weighting behind routed versus directly displayed influence is still not planner-safe

## Planner behaviour

- Required behaviour:
  - prefer local strong-link generation for must-have market targets
  - identify the Main Port on each relevant body before reasoning about local or cross-body link outcomes
  - inspect live Market Links before recommending demolition or architecture changes
  - model visible link arrows as potentially aggregated displays rather than one-to-one causal edges
- Required warnings:
  - one weak link is not equivalent to local strong support
  - visible arrows do not necessarily enumerate every contributing facility directly
  - adding or replacing a same-body port can change routing priority without obviously changing the visible topology
- Blocked outputs:
  - do not promise a commodity outcome purely because a weak link appeared
  - do not recommend irreversible demolition solely because a model predicts that a routed link should remain intact
- When to suggest an experiment instead:
  - when commodity availability depends on weak-link spillover rather than direct local support
  - when routing between surface and orbital main ports is inferred but not directly evidenced
  - when a main port appears to receive weak links but may also be acting as a routing intermediary

## Evidence basis

- `EV-0001` - Rocha Liberty Post High Tech Build Evidence
- `EV-0004` - Colonisation Reference Documents Pack
- `reference_sources/FW-0001-strong-weak-links/strong-and-weak-links-illustrated-reference.txt`
- `reference_sources/MG-0001-megaguide-v2-3/elite-dangerous-colonization-mega-guide-v2-3.txt`
- prior repository draft `M-0003-strong-and-weak-link-routing.md`
- `M-0003` - One Weak Refinery Link Is Insufficient To Restore Metals

## Negative evidence preserved

- `M-0003` preserves a concrete failure case where a single weak Refinery link did not restore Steel, Titanium, or Aluminium.
- Wregoe strategy notes explicitly rejected relying on remote spillover when local same-body High Tech support could be built instead.

## Contradictions

- `C-0004` - Weak-link generalisation risk versus narrow negative evidence from Wregoe

## Patch sensitivity

High. Link weighting, aggregation display, and economy effects are all vulnerable to Frontier balance changes.

## Planner-safe edge rules

- Same-body support should be treated as the deliberate-control path; cross-body support should be treated as spillover unless live evidence proves otherwise.
- Main-port priority must be resolved before interpreting either strong or weak links on a body with multiple ports.
- A visible link count is a routing display, not a complete additive proof of influence.
- Surface-to-orbital forwarding on the same body should be treated as plausible and useful, but still verified live before an irreversible architecture change.

## Related mechanics

- `M-0003` - One Weak Refinery Link Is Insufficient To Restore Metals
- `M-0005` - Colony-Type and Specialised Ports
- `M-0007` - Colony Port Economy Inheritance

## Related experiments

- `EXP-0000` - Wregoe Methodology Seed
- `LV-0003` - Refinery Threshold for Metals at Dodec
- `LV-0005` - Main Port Routing and Link Aggregation

## Open questions

- How much of commodity appearance is driven by top-two economy rank versus the precise strong/weak contribution values?
- Are there port-class-specific routing exceptions that do not appear in current repository evidence?
