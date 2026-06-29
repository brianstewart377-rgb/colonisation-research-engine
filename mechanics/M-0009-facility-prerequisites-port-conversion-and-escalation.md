# M-0009 - Facility Prerequisites, Port Conversion, and High-Tier Port Cost Escalation

## Summary

Colonisation construction is constrained by more than raw commodity cost. High-tier ports escalate in CP cost as soon as additional ports are started, several facilities have explicit prerequisites, and same-body extra ports can convert into supporting facilities instead of remaining independent ports.

## Status

Extracted

## Confidence

Current working confidence: 88%.

The core rules are consistent across the recovered Mega Guide v2.3.0 and the DaftMav-derived reference tables.

## Mechanic statement

- T2 and T3 ports escalate in CP cost after the first counted port, with separate formulas for T2 and T3 families.
- The completed primary port is effectively permanent and is exempt from later high-tier port escalation.
- T1 ports and non-port facility families do not trigger the T2/T3 escalation mechanic.
- Several facility classes have explicit prerequisites, including orbital installations, tourism settlements, and multiple hub families.
- When multiple ports exist on one local body, lower-tier or later-built ports can convert into supporting facilities and follow routing rules instead of behaving as ordinary independent ports.

## Planner behaviour

- Separate material-cost calculations from CP-gating calculations.
- Sequence capital builds around high-tier port escalation before optimizing aesthetic or secondary facilities.
- Represent prerequisites explicitly as build-chain constraints.
- Warn when a same-body extra port will convert into a supporting-facility role.

## Evidence basis

- `evidence/claim_register.csv`
- `mechanics/construction_rules_register.md`
- `mechanics/market_rules_register.md`

## Related mechanics

- `M-0004`
- `M-0005`
- `M-0006`
- `M-0010`

## Related experiments

- `LV-0005`
- `LV-0010`

## Open questions

- How many same-body port exceptions exist beyond the guide's documented routing cases?
- Which settlement variants most often diverge from their advertised landing pad metadata?
