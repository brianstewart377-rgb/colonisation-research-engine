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
