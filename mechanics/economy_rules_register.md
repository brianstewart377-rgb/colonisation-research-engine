# Economy Rules Register

This register decomposes the current mechanic catalogue into explicit economy-facing rules for future planners and analyzers.

## ER-0001 - Station economy is inherited, not manually chosen

- Status: Confirmed
- Source: `mechanics/M-0002-station-economy-is-inherited.md`
- Rule: A colony station's economy outcome must be planned indirectly through body, facility, and market-link context rather than direct manual selection.
- Related mechanics: `M-0002`, `M-0007`
- Planner implications: Never expose a fake choose-economy control.
- Testing status: Supported by direct Wregoe evidence
- Contradictions: None currently recorded
- Unknowns: How tied or near-tied top economies should be surfaced

## ER-0002 - Colony-type ports inherit economy behavior

- Status: Likely
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`
- Rule: Colony-type ports should be modeled as inheriting economy outcomes from local body context plus market links.
- Related mechanics: `M-0005`, `M-0007`
- Planner implications: Colony-type ports need body and link analysis, not class-only assumptions.
- Testing status: Reference-derived plus preview support
- Contradictions: `C-0002`
- Unknowns: Exact post-build formula

## ER-0003 - Specialised ports retain an inherent economy baseline

- Status: Likely
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`
- Rule: Specialised ports should not be treated as inheriting local body base economy in the same way as colony-type ports, even though links may still affect visible market behavior.
- Related mechanics: `M-0005`, `M-0007`
- Planner implications: Compare specialised ports separately from colony-type ports.
- Testing status: Reference-derived
- Contradictions: `C-0002`
- Unknowns: Which post-build effects remain class-specific

## ER-0004 - Local body type establishes base inheritable economies

- Status: Likely
- Source: `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- Rule: Body class establishes a first-pass inherited economy tendency for colony-type ports.
- Related mechanics: `M-0008`
- Planner implications: Body type must be part of economy projection.
- Testing status: Reference-derived
- Contradictions: None currently recorded
- Unknowns: Direct live confirmation coverage per body class

## ER-0005 - Local body modifiers affect inherited economy tendency

- Status: Likely
- Source: `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- Rule: Rings, organics, and geological features can modify inherited economy tendencies.
- Related mechanics: `M-0008`
- Planner implications: Planetary features should not be ignored in economy projections.
- Testing status: Reference-derived
- Contradictions: None currently recorded
- Unknowns: Full post-patch modifier behavior

## ER-0006 - Modifier stacking remains unverified

- Status: Needs verification
- Source: `mechanics/M-0008-local-body-base-economies-and-modifiers.md`, `experiments/live_verification_register.md`
- Rule: The current repository preserves a non-stacking rule for local body modifiers, but this should remain provisional until directly verified.
- Related mechanics: `M-0008`
- Planner implications: Do not double-count modifiers without evidence.
- Testing status: Needs live verification via `LV-0004`
- Contradictions: None currently recorded
- Unknowns: Whether any modifiers override, merge, or stack in edge cases

## ER-0007 - Strong links are preferred for targeted economy shaping

- Status: Likely
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`
- Rule: Same-body strong links are the preferred mechanism for deliberately shaping a target market.
- Related mechanics: `M-0006`
- Planner implications: Strong-link architectures should be preferred for must-have outcomes.
- Testing status: Strongly supported, still needs broader live verification
- Contradictions: `C-0004`
- Unknowns: Exact contribution values per facility combination

## ER-0008 - Weak links provide spillover, not guaranteed control

- Status: Likely
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`
- Rule: Weak links are useful system-wide spillover but should not be treated as guaranteed market-control tools.
- Related mechanics: `M-0006`
- Planner implications: Weak-link-only repairs should be labeled experimental.
- Testing status: Supported by routing model plus negative evidence
- Contradictions: `C-0004`
- Unknowns: Threshold where weak support becomes reliable

## ER-0009 - One weak Refinery link was insufficient in the Wregoe Dodec case

- Status: Confirmed for narrow scope
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`
- Rule: In the tested Wregoe case, one weak Refinery link did not restore Steel, Titanium, or Aluminium at the Dodec.
- Related mechanics: `M-0003`, `M-0006`
- Planner implications: Do not universalize single weak-link repair advice.
- Testing status: Directly observed
- Contradictions: `C-0004`
- Unknowns: Refinery threshold, rank order, and station-context effects

## ER-0010 - Preview equality does not prove post-build market equality

- Status: Confirmed as a caution rule
- Source: `evidence/EV-0003-a4-t3-station-selection-previews.md`, `mechanics/M-0005-colony-type-and-specialised-ports.md`
- Rule: Similar preview bars across station classes or layout variants do not prove that final services, missions, or markets are equal after construction.
- Related mechanics: `M-0005`, `M-0007`
- Planner implications: Require post-build evidence before claiming class superiority.
- Testing status: Confirmed as an uncertainty rule; final market comparison still unresolved
- Contradictions: `C-0002`
- Unknowns: Real post-build divergence

## ER-0011 - Specialised ports have fixed baseline economy strength

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Specialised ports use fixed baseline economic strength values rather than inheriting body-driven colony economies.
- Related mechanics: `M-0005`, `M-0007`, `M-0009`
- Planner implications: Compare specialised ports as fixed-economy anchors before layering strong and weak links on top.
- Testing status: Extracted from Mega Guide v2.3.0; still worth spot-checking live on edge cases
- Contradictions: None currently recorded
- Unknowns: Whether every specialised subtype still matches the guide after recent patches

## ER-0012 - Specialised ports ignore local-body inheritable economies

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Specialised ports are not affected by the local body's base inheritable economy.
- Related mechanics: `M-0005`, `M-0007`, `M-0009`
- Planner implications: Do not pick a body for a specialised port expecting body inheritance to rescue an otherwise bad economy baseline.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Whether any post-build UI still misleadingly implies body inheritance

## ER-0013 - Specialised ports ignore local-body inheritable modifiers

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Specialised ports are not affected by inheritable-economy modifiers such as rings, organics, or geologicals.
- Related mechanics: `M-0005`, `M-0008`, `M-0009`
- Planner implications: Keep ring, biological, and geological analysis out of specialised-port body projections unless live evidence says otherwise.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Whether any UI summary conflates inheritable modifiers with link modifiers

## ER-0014 - Colony-type ports recompute from body plus inheritable modifiers

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Colony-type ports acquire economies from the combination of local-body base inheritable economy and applicable inheritable modifiers.
- Related mechanics: `M-0007`, `M-0008`
- Planner implications: Treat colony-type port planning as body-first and link-second rather than station-class-first.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Exact post-build weighting when several economies tie

## ER-0015 - Inheritable modifiers do not stack with each other

- Status: Needs verification
- Source: `evidence/claim_register.csv`
- Rule: The guide states that inheritable-economy modifiers do not stack with base body economies and do not stack with one another.
- Related mechanics: `M-0008`
- Planner implications: Do not double-count rings, organics, and geologicals in inherited-economy projections.
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0007`, `U-0013`

## ER-0016 - Contraband cannot be obtained through body inheritance

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: No local body provides Contraband as an inheritable economy; contraband must come from strong/weak links or a specialised criminal outpost.
- Related mechanics: `M-0005`, `M-0006`, `M-0008`
- Planner implications: Reserve orbital planning space if contraband is a required outcome.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Whether any future patch adds new direct contraband sources

## ER-0017 - Two dominant economies are the safe planning baseline

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: The top two economies at a port protect their own supply from being netted out by the demand of the other economies present, which makes one- or two-dominant-economy designs the safest default planning baseline.
- Related mechanics: `M-0010`
- Planner implications: Default to one- or two-economy station designs for reliable commodity output.
- Testing status: Supported by guide text and appendix overlap tables
- Contradictions: None currently recorded
- Unknowns: `U-0001`, `U-0002`

## ER-0018 - Third and lower economies still create cannibalization pressure

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Demand from the top two economies and both supply and demand from lower-ranked economies continue to net against the rest of the market mix.
- Related mechanics: `M-0010`
- Planner implications: Treat any third-or-lower economy as an intentional tradeoff, not a harmless bonus.
- Testing status: Supported by guide text and appendix overlap tables
- Contradictions: None currently recorded
- Unknowns: `U-0001`, `U-0002`

## ER-0019 - Same-strength rank order is probably alphabetical but not proven

- Status: Needs verification
- Source: `evidence/claim_register.csv`
- Rule: The guide believes same-strength economy ordering is alphabetical, but marks that rule as still to be confirmed.
- Related mechanics: `M-0010`
- Planner implications: Tie cases need a warning flag instead of a hard recommendation.
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0014`

## ER-0020 - Economy order can matter more than absolute boost

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Advanced system design guidance sometimes depends more on pushing an economy into rank position one or two than on maximizing its raw value.
- Related mechanics: `M-0010`
- Planner implications: Model rank-order objectives directly when doing advanced optimization instead of optimizing only for raw percentage totals.
- Testing status: Extracted from Appendix A strategy guidance
- Contradictions: None currently recorded
- Unknowns: `U-0002`
