# CRE Review Handoff

This note is for the next human reviewer.

The repository is now structurally clean enough that the highest remaining risks are no longer editorial. They are live-game uncertainty, patch sensitivity, and edge-case routing behavior.

## Review goal

Prioritize tests that would most improve planner safety.

The most valuable outcomes are:

- confirming or rejecting multi-port routing assumptions;
- confirming or rejecting branch-specific prerequisite strictness;
- confirming or rejecting same-strength economy ordering;
- reducing uncertainty around population side effects and demolition behavior.

## Priority order

### Priority 1

These directly affect unsafe planner recommendations if left unresolved.

1. `LV-0011` Multi-port weak-link generation and forwarding
2. `LV-0012` Large-branch prerequisite strictness
3. `LV-0010` Settlement pad-size divergence by variant
4. `LV-0005` Main Port routing and link aggregation

Why first:

- they gate demolition safety, routing interpretation, hub dependency logic, and hauling recommendations
- they affect whether the planner can safely recommend irreversible or slot-sensitive actions

## Priority 2

These materially affect economy-planning confidence.

1. `LV-0007` Same-strength economy tie ordering
2. `LV-0006` Strong-link modifier exact values and additive stacking
3. `LV-0003` Refinery threshold for metals at the Dodec
4. `LV-0004` Local body modifier non-stacking

Why next:

- they determine whether economy models can be treated as directional only or numerically meaningful
- they affect how much confidence to place in rank-order optimization and body-selection guidance

## Priority 3

These improve long-run output and population modeling.

1. `LV-0008` Body-specific population multipliers
2. `LV-0009` Demolition and population decay
3. `LV-0001` A4 High Tech threshold and commodity coverage
4. `LV-0002` Post-build station-class market differences

Why later:

- these are important, but less immediately dangerous than routing and prerequisite errors
- they mostly improve forecast precision rather than preventing hard planner mistakes

## Mechanics to review first

If reviewer time is limited, start with these mechanics:

1. `M-0006` Strong and Weak Link Routing
2. `M-0009` Facility Prerequisites, Port Conversion, and High-Tier Port Cost Escalation
3. `M-0010` Economy Compatibility, Rank Protection, and Market Cannibalization
4. `M-0012` Population Growth, Body Multipliers, and Output Scaling
5. `M-0013` System Scores, Payments, and High-Risk Caveats

## What to challenge aggressively

The next reviewer should actively look for evidence that would overturn or narrow these assumptions:

- visible Market Links topology reflects routed influence only imperfectly
- main-port priority controls more routing behavior than raw topology suggests
- some hub branches may require the large upgraded settlement branch, not merely any family member
- same-strength economy ordering may not always be alphabetical
- demolition may fail to reduce population as expected
- some planetary agriculture implementations may remain unreliable even when theory says they should work

## Safe reviewer stance

When in doubt:

- prefer contradiction or caveat over forced certainty
- prefer recommendation-level wording over rule-level wording
- prefer a live-verification task over a speculative mechanic
- avoid promoting a Wregoe-specific observation into a universal mechanic without broader evidence

## Most important files

- `docs/quality_review_report.md`
- `docs/contradiction_register.md`
- `docs/unknowns_register.md`
- `experiments/live_verification_register.md`
- `planner/planner_rules_register.md`
- `mechanics/M-0006-strong-and-weak-link-routing.md`
- `mechanics/M-0009-facility-prerequisites-port-conversion-and-escalation.md`
- `mechanics/M-0010-economy-compatibility-rank-protection-and-market-cannibalization.md`
- `mechanics/M-0012-population-growth-body-multipliers-and-output-scaling.md`
- `evidence/claim_register.csv`

## Definition of success

The next human review cycle should ideally produce at least one of:

- a confirmed rejection of a current routing assumption;
- a narrowed prerequisite rule for a specific hub or installation family;
- a resolved same-strength ordering rule;
- a resolved demolition/population behavior rule;
- a tighter contradiction or caveat that prevents a misleading planner recommendation.
