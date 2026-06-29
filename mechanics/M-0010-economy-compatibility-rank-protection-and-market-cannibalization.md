# M-0010 - Economy Compatibility, Rank Protection, and Market Cannibalization

## Summary

Colonisation markets are shaped by economy rank, not just economy presence. The top two economies protect their own supply, third-and-lower economies still create overlap pressure, and Appendix D pair material becomes essential once a port moves beyond a two-economy mix.

## Status

Extracted

## Confidence

Current working confidence: 84%.

The directional rule set is strong, but tie-breaking and some community spreadsheets still need live confirmation.

## Mechanic statement

- First- and second-ranked economies protect their own supply from being netted out by other economies at the same port.
- Demand from those top-two economies is still active against non-top-two supply.
- Two-economy designs are the default high-confidence market recommendation, not a proof that every larger mix is automatically bad.
- Third-and-lower economies require overlap review because compatibility varies by pair and by commodity category.
- Economy order can matter more than raw boost size when the goal is to keep a desired economy inside the top two, especially in advanced planner-guidance scenarios.

## Planner behaviour

- Default to one- or two-dominant-economy designs in planner-safe recommendations unless a more complex mix is deliberately justified.
- Flag three-plus economy stations as requiring Appendix D review.
- Treat tie cases as uncertain until same-strength ordering is directly verified.
- Preserve commodity-location constraints such as orbital-only and planetary-only materials.

## Evidence basis

- `evidence/claim_register.csv`
- `mechanics/economy_rules_register.md`
- `mechanics/market_rules_register.md`

## Related mechanics

- `M-0002`
- `M-0003`
- `M-0006`
- `M-0007`
- `M-0008`

## Related experiments

- `LV-0001`
- `LV-0003`
- `LV-0006`
- `LV-0007`

## Open questions

- Is same-strength ordering always alphabetical?
- Which Appendix D pairings are stable across recent live patches and which have drifted?
