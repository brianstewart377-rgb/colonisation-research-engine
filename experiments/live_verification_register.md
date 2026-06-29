# Needs Live Verification Register

This register captures unresolved items that should become real in-game experiments or observation tasks.

## LV-0001 - A4 High Tech threshold and commodity coverage

- Category: Economy / commodities
- Title: Does High Tech reaching second place on A4 materially improve construction-material coverage?
- Description: Validate whether the A4 High Tech promotion changes real commodity availability in a way that benefits whole-system material coverage rather than just changing percentages.
- Source: `experiments/EXP-0001-a4-complementary-high-tech-role.md`, `evidence/EV-0001-rocha-liberty-post-high-tech-build.md`
- Exact location: EXP-0001 `Prediction`, `After state`, and `Follow-up experiments`
- Confidence: Medium that the question is well framed; low that the answer is currently known
- Category tags: `economy`, `commodities`, `strategy`
- Related mechanics: `M-0002`, `M-0007`, `M-0008`
- Planner implications: High-value because it affects whether A4 should be recommended as a High Tech support body
- Testing status: Needs live verification
- Contradictions: Potentially intersects `C-0002`
- Unknowns: Top-two rank effect versus absolute percentage effect

## LV-0002 - Post-build station-class market differences

- Category: Port comparison
- Title: Do Orbis, Ocellus, and Dodec diverge after construction even when previews look equivalent?
- Description: Compare final market, services, and economy behavior across station classes whose previews currently appear similar.
- Source: `evidence/EV-0003-a4-t3-station-selection-previews.md`
- Exact location: EV-0003 `Inference` and `Caveats`
- Confidence: High that the question is unresolved
- Category tags: `ports`, `economy`, `services`
- Related mechanics: `M-0005`, `M-0007`
- Planner implications: Prevents unsupported station-class optimisation claims
- Testing status: Needs live verification
- Contradictions: `C-0002`
- Unknowns: Service differences, final commodity differences, mission-board differences

## LV-0003 - Refinery threshold for metals at the Dodec

- Category: Economy / links
- Title: What Refinery weighting is required before Steel, Titanium, and Aluminium return?
- Description: Extend the narrow Wregoe failure case into a threshold-seeking experiment instead of a binary weak-link assumption.
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`
- Exact location: M-0003 `Open questions`
- Confidence: High that the gap is real
- Category tags: `refinery`, `commodities`, `weak_links`
- Related mechanics: `M-0003`, `M-0006`
- Planner implications: Important for any metal-repair recommendation
- Testing status: Needs live verification
- Contradictions: `C-0004`
- Unknowns: Threshold, rank-order effects, station-context effects

## LV-0004 - Local body modifier non-stacking

- Category: Body economics
- Title: Do body modifiers truly fail to stack with base body economies and with each other?
- Description: Directly test the non-stacking rule currently preserved only through reference-derived material.
- Source: `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- Exact location: M-0008 `Mechanic statement`
- Confidence: Medium that the rule is worth preserving; low that it is fully confirmed locally
- Category tags: `body_type`, `economy_modifiers`
- Related mechanics: `M-0008`, `M-0007`
- Planner implications: Prevents hidden double-counting in future economy projections
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: Which modifiers override, merge, or stack in post-patch behavior

## LV-0005 - Main Port routing and link aggregation

- Category: Routing
- Title: How do main surface and main orbital ports aggregate strong-link routing?
- Description: Verify whether visible link counts are aggregating upstream facilities through main-port routing rather than showing each facility directly.
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`
- Exact location: M-0006 `Mechanic statement`
- Confidence: Medium
- Category tags: `routing`, `market_links`, `main_port`
- Related mechanics: `M-0004`, `M-0006`
- Planner implications: Affects how link screens should be interpreted and when demolitions are considered safe
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: Tie cases, mixed surface-orbital hierarchies, display rules versus actual effect rules

## LV-0006 - Strong-link modifier exact values and additive stacking

- Category: Routing / modifiers
- Title: Are strong-link boosts and penalties applied as additive ±0.4 changes with a 0.1 floor?
- Description: Validate the guide's numeric claim for boosted and penalized strong-link values across several body conditions.
- Source: `evidence/claim_register.csv`
- Exact location: Mega Guide `Strong Links`
- Confidence: Medium that the rule is approximately correct; low that the exact live numbers are fully nailed down
- Category tags: `routing`, `link_modifiers`, `economy`
- Related mechanics: `M-0006`, `M-0010`
- Planner implications: Needed before publishing numeric link-strength calculators as planner-safe output
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0013`

## LV-0007 - Same-strength economy tie ordering

- Category: Economy ranking
- Title: Do same-strength economy ties always resolve alphabetically?
- Description: Build or inspect tied economy cases and verify whether rank order follows alphabetical ordering consistently.
- Source: `evidence/claim_register.csv`
- Exact location: Mega Guide `Which Economies Are Compatible With Each Other?`
- Confidence: High that the uncertainty exists
- Category tags: `economy`, `ranking`, `ties`
- Related mechanics: `M-0010`
- Planner implications: Affects whether the planner can make hard statements in tie cases
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0014`

## LV-0008 - Body-specific population multipliers

- Category: Population
- Title: What are the missing population multipliers for under-sampled body and facility combinations?
- Description: Extend the population table with additional live observations for body classes that still show TBD values.
- Source: `evidence/claim_register.csv`
- Exact location: Mega Guide `What Does Population Affect, And How Do I Grow It?`
- Confidence: High that the gap is real
- Category tags: `population`, `body_type`, `output`
- Related mechanics: `M-0012`
- Planner implications: Needed for better long-run output forecasts
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0015`

## LV-0009 - Demolition and population decay

- Category: Population / demolition
- Title: Does demolishing a facility reduce the population associated with it?
- Description: Test the anecdotal guide claim that demolition may leave population behind instead of removing it.
- Source: `evidence/claim_register.csv`
- Exact location: Mega Guide `What Does Population Affect, And How Do I Grow It?`
- Confidence: Medium
- Category tags: `population`, `demolition`, `state_change`
- Related mechanics: `M-0012`, `M-0013`
- Planner implications: Important before recommending population-correction demolitions
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0016`

## LV-0010 - Settlement pad-size divergence by variant

- Category: Facility metadata
- Title: Which settlement variants misreport their landing pad sizes?
- Description: Compare architect previews and in-game landing availability for settlement variants reported to diverge from their advertised pad sizes.
- Source: `evidence/claim_register.csv`
- Exact location: AetherWave `Important Construction Notes`
- Confidence: Medium-high that the caveat is real
- Category tags: `landing_pads`, `settlements`, `hauling`
- Related mechanics: `M-0009`, `M-0013`
- Planner implications: Needed before pad-restricted hauling advice can be treated as reliable
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0017`
