# M-0011 - Facility Stats, Service Activation, and System Effects

## Summary

Facility classes modify system-level stats in distinct ways, and those stats affect services and market behavior unevenly. Tech Level has a known shipyard threshold, Development affects commodity volumes, and Security changes both system security state and some service availability.

## Status

Extracted

## Confidence

Current working confidence: 80%.

The service thresholds are firmer than the deeper systemic meaning of Wealth and Standard of Living.

## Mechanic statement

- Tech Level 35 is the known shipyard threshold.
- T2 and T3 ports grant Tech Level 35 immediately; T1 space outposts cannot host shipyards at all.
- Development affects commodity volume and appears to soft-cap around 20.
- Low security enables Interstellar Factors.
- Individual facilities have distinct Security, Tech, Wealth, Standard of Living, Development, Pop, and Max Pop effects according to the canonical `DM-0001` facility-stat extracts.
- Wealth and Standard of Living remain only partially understood.

## Planner behaviour

- Expose TL35 as a concrete service threshold.
- Keep Development visible in market-output reasoning.
- Treat Wealth and Standard of Living as tracked but not over-explained inputs.
- Preserve system-stat deltas by facility class rather than collapsing them into one generic quality score.

## Evidence basis

- `evidence/claim_register.csv`
- `mechanics/population_rules_register.md`
- `mechanics/market_rules_register.md`
- `reference_sources/MG-0001-megaguide-v2-3/elite-dangerous-colonization-mega-guide-v2-3.txt`
- `reference_sources/DM-0001-daftmav-construction-details/DaftMav_Stats-only.csv`

## Related mechanics

- `M-0005`
- `M-0009`
- `M-0012`
- `M-0013`

## Related experiments

- `LV-0008`

## Open questions

- What exact downstream gameplay effects do Wealth and Standard of Living have?
- Are there additional service thresholds beyond TL35 that can be planner-safe today?
