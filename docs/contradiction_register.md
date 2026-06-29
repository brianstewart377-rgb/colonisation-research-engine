# Contradiction Register

This register records durable contradictions and unresolved conflicts discovered in the current repository knowledge base.

## C-0001 - Official claim radius versus Steam mirror wording

- Category: Source conflict
- Description: The repository source review records that a Steam mirror of the colonisation guide states a `16 ly` claim radius while the official Frontier guide states `15 ly`.
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Exact location: `Steam mirror of the colonisation guide` section
- Confidence: High that the wording conflict exists
- Related mechanics: none directly yet
- Planner implications: Never use mirrored or reposted wording when an official source conflicts with it.
- Testing status: No live test needed; source-selection conflict only
- Contradictions: Official Frontier wording versus mirror wording
- Unknowns: Whether other mirrors contain the same drift

## C-0002 - Station-class superiority remains unproven

- Category: Community assumption versus evidence
- Description: The repository contains preview evidence showing no reliable visible mechanical superiority between Orbis, Ocellus, Dodec, or Apollo/Artemis layout variants, yet community planning discourse often implies meaningful class superiority.
- Source: `evidence/EV-0003-a4-t3-station-selection-previews.md`, `mechanics/M-0005-colony-type-and-specialised-ports.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`
- Exact location: EV-0003 `Direct observations` and `Inference`
- Confidence: Medium-high
- Related mechanics: `M-0005`, `M-0007`
- Planner implications: Do not recommend a station class as automatically superior without post-build evidence.
- Testing status: Needs live verification
- Contradictions: Community expectation of class superiority versus current preview evidence
- Unknowns: Whether post-build services or markets diverge despite equal previews

## C-0003 - Raven proposed-build deficits versus live buildability

- Category: Model interpretation conflict
- Description: Raven proposed-build totals can show negative construction-point deficits while live Architect still allows the immediate next build.
- Source: `evidence/EV-0002-wregoe-raven-proposed-build-review.md`, `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Exact location: EV-0002 `Direct observations`; M-0004 `Negative evidence preserved`
- Confidence: Medium
- Related mechanics: `M-0004`
- Planner implications: Separate `current buildability` from `full-plan projection`.
- Testing status: More live comparison examples would improve confidence
- Contradictions: Planner-model projected deficit versus actual buildable state
- Unknowns: Whether the conflict is always caused by proposed-build inclusion or sometimes by deeper modeling differences

## C-0004 - Weak-link generalisation versus Wregoe narrow failure

- Category: Heuristic conflict
- Description: Community-style reasoning often treats weak links as meaningful repair tools, but the repository's Wregoe case shows that one weak Refinery link was insufficient to restore key metals.
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`
- Exact location: M-0003 `Mechanic statement`; M-0006 `Negative evidence preserved`
- Confidence: High for the narrow contradiction, low for universalisation
- Related mechanics: `M-0003`, `M-0006`
- Planner implications: Weak-link recommendations must be labeled experimental unless corroborated.
- Testing status: Needs broader live verification across additional cases
- Contradictions: General weak-link optimism versus narrow negative evidence
- Unknowns: Threshold, ranking, and station-context conditions required for weak links to become sufficient
