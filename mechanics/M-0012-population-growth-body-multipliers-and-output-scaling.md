# M-0012 - Population Growth, Body Multipliers, and Output Scaling

## Summary

Population is one of the clearest long-run scaling mechanics in colonisation. It grows on a weekly hybrid curve, scales commodity output by square root rather than linearly, and depends heavily on both facility class and local body type.

## Status

Extracted

## Confidence

Current working confidence: 82%.

The global shape of the rule is strong, while some body-specific multipliers remain under-sampled.

## Mechanic statement

- Population grows on weekly maintenance ticks.
- Early growth uses fixed values for 14 ticks, then transitions into a logistic curve.
- Output scales with the square root of facility population.
- Population is attached to individual facilities, not automatically spread across the whole system.
- Body class and facility class both materially change asymptotic population and therefore long-run output.
- Population also affects emissions grade and the effort needed to swing BGS control.

## Planner behaviour

- Distinguish first-month output from year-scale mature output.
- Prefer body-specific population baselines when comparing similar facilities.
- Treat demolition-based population corrections as unsafe until directly tested.

## Evidence basis

- `evidence/claim_register.csv`
- `mechanics/population_rules_register.md`

## Related mechanics

- `M-0008`
- `M-0010`
- `M-0011`

## Related experiments

- `LV-0008`
- `LV-0009`

## Open questions

- What are the missing body multipliers for under-sampled facilities?
- Does demolition reliably remove the population associated with demolished assets?
