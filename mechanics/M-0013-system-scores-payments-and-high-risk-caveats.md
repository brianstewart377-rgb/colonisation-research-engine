# M-0013 - System Scores, Payments, and High-Risk Caveats

## Summary

By-facility system score values are deterministic enough to plan around, but several high-impact caveats remain live: bugged agricultural ports, suspected routing exploits, pad-size mismatches, and other issues that can make a build mechanically worse than it looks on paper.

## Status

Extracted

## Confidence

Current working confidence: 78%.

The score values themselves are strong; the caveat layer remains patch-sensitive.

## Mechanic statement

- Population does not contribute to system score.
- Weekly architect credits are driven by system score and modified by Happiness.
- Appendix C provides deterministic score values by facility class.
- The recovered sources also preserve multiple planner-relevant caveats and bugs, including agricultural zero-output cases, settlement pad-size divergence, and suspected nested-port passthrough behavior.

## Planner behaviour

- Use Appendix C score values for payout estimates instead of hand-wavy heuristics.
- Keep bug-sensitive recommendations explicitly marked as experimental or caveated.
- Elevate demolition, nested-port exploit reliance, and agriculture reliability to high-risk planner warnings.

## Evidence basis

- `evidence/claim_register.csv`
- `docs/contradiction_register.md`
- `planner/planner_risk_register.md`

## Related mechanics

- `M-0009`
- `M-0010`
- `M-0011`
- `M-0012`

## Related experiments

- `LV-0009`
- `LV-0010`

## Open questions

- Which current bugs are variant-specific and which are systemic?
- How much live drift should be tolerated before a caveat is reclassified as a contradiction or a retired issue?
