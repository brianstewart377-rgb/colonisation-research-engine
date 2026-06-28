# M-0003 — One Weak Refinery Link Is Insufficient To Restore Metals

## Summary

In the Wregoe A5/A7D test case, adding one weak Refinery link from an A7D Silenus Refinery Hub to the A5 Dodec did not restore Steel, Titanium, or Aluminium availability at the Dodec.

This is a negative-evidence mechanic. It does not prove that weak Refinery links are useless. It proves that this specific weak-link intervention was insufficient in that context.

## Status

Confirmed for the tested case. Not universalised.

## Confidence

High for the narrow claim. Current working confidence: 95%.

## Mechanic statement

The planner must not assume that a single weak Refinery link is enough to restore metal commodities at a Dodec-style station when the broader economy mix remains dominated by other effects.

## Planner behaviour

- Do not recommend “add one weak Refinery link” as a guaranteed repair for missing Steel, Titanium, or Aluminium.
- If recommending weak links, label the recommendation as experimental unless corroborated by stronger evidence.
- Prefer staged validation: preview links, record Raven percentages, then verify final market output.
- Preserve the distinction between “link appeared” and “commodity returned”.

## Tested context

- System context: Wregoe colony project.
- Target station: A5 Dodec, known in project notes as Mike Kilo Dodec.
- Intervention: A7D Silenus Refinery Hub.
- Observed effect: one weak Refinery link appeared.
- Market result: Steel, Titanium, and Aluminium remained absent.

## Evidence basis

- Internal Wregoe before/after observation.
- Raven/Market Links evidence showed the weak link appeared.
- Final market check showed metals still absent.

## Negative evidence preserved

This mechanic exists specifically to prevent the planner from repeating a plausible but failed repair strategy.

## Contradictions

None for the narrow claim.

## Patch sensitivity

Medium-high. Commodity availability and link weighting may change after Frontier patches. Re-test if economy or market-link rules are patched.

## Related experiments

- EXP-0000 — Wregoe Methodology Seed
- Future experiment: A5 refinery-dominance retest after replacing one Mining Settlement with a third Silenus Refinery Hub

## Open questions

- How strong must Refinery weighting become before Steel, Titanium, and Aluminium appear?
- Does the top-two economy order matter more than absolute percentage?
- Does Dodec station type, body context, or nearby Planetary Port state influence commodity presence?
