# EXP-0000 — Wregoe Methodology Seed

## Purpose

This is the seed experiment record for the Colonisation Research Engine. It records the research method developed during the Wregoe colony project rather than a single isolated build.

Wregoe is treated as Experiment Zero because it established the working discipline of the project:

- separate observation from inference
- preserve failed predictions
- test mechanics in live systems
- record before/after states
- revise conclusions when evidence changes
- prefer `Unknown` over unsupported certainty

## Status

Active methodology seed.

## System context

- Project: Wregoe colony planning and construction.
- Main focus: Dodec economy/material availability, Water World orbital planning, A4/A5/A7 body interactions, Refinery/Industrial/Extraction weighting, and mission/material build strategy.
- Key bodies mentioned in project notes:
  - A4: secondary ground body with 1 orbital and 5 ground slots.
  - A5: primary production body with Dodec, Industrial Installation, Kvitka View Planetary Port, and completed ground production.
  - A7D: one-slot moonlet used for a Silenus Refinery Hub test.
  - Water Worlds P5-P8: orbital-only bodies, no surface slots.

## Research questions established

1. How do body slots constrain valid facility recommendations?
2. How does station economy inheritance work in practice?
3. How do weak and strong market links affect economy percentages?
4. What economy mix is needed for key construction materials such as Steel, Titanium, Aluminium, CMM, and Ceramic?
5. Which recommendations are safe for automated planning, and which require live validation?

## Key observations preserved

### Observation 1 — Water Worlds are orbital-only

Water Worlds in the Wregoe project could not receive surface facilities. This invalidated earlier planning assumptions and became seed mechanic M-0001.

### Observation 2 — Station economy is inherited

Station economy could not be manually selected. The planner must reason through body/facility/economy-link context rather than direct station economy choice. This became seed mechanic M-0002.

### Observation 3 — One weak Refinery link was insufficient

A7D Silenus Refinery Hub produced a weak Refinery link to the A5 Dodec, but Steel, Titanium, and Aluminium remained absent. This became seed mechanic M-0003.

## Hypotheses generated

- Refinery weighting may need to become a top-two economy before metals appear reliably.
- Absolute economy percentage may be less important than rank order and facility/body context.
- Planetary Port completion may alter or redistribute market output in ways not yet fully understood.
- Water World Tourism/Agriculture bias is strong enough that station type alone cannot overcome it.

## Negative evidence generated

- Do not assume Water Worlds have hidden ground slots.
- Do not assume station economy can be chosen directly.
- Do not assume one weak Refinery link repairs missing metals.
- Do not infer build completion from placeholder-style names alone.

## Planner lessons

The planner should:

- block impossible builds before asking the AI to generate text
- label every recommendation by confidence
- avoid irreversible demolition advice without direct evidence
- suggest validation experiments when confidence is weak
- keep screenshots, Raven outputs, Architect previews, and market checks as evidence rather than conversational notes

## Confidence impact

This experiment seed creates the first three mechanics in the repository:

- M-0001 — Water Worlds Have No Surface Slots
- M-0002 — Station Economy Is Inherited, Not Manually Chosen
- M-0003 — One Weak Refinery Link Is Insufficient To Restore Metals

## Required follow-up work

- Split Wregoe into individual experiment records.
- Add evidence IDs for screenshots and Raven/Architect observations.
- Record the A5 third-Silenus refinery retest once the build completes and markets recalculate.
- Create a Wregoe architecture record to support future similarity matching.

## Notes

This document is intentionally conservative. It records what the project methodology established, not every claim discussed during planning.
