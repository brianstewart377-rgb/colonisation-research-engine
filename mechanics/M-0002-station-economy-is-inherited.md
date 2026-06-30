# M-0002 — Station Economy Is Inherited, Not Manually Chosen

## Summary

Colonisation station economy is not selected manually as a free choice by the builder. Economy outcome is inherited from the relevant system/body/facility/economy-link context and therefore must be planned indirectly.

## Status

Confirmed.

## Confidence

High for planner purposes. Current working confidence: 98%.

## Mechanic statement

The planner must not tell a user to choose a station economy directly. It may recommend facility/body architecture intended to influence economy weighting, but must label the expected economy outcome by confidence.

## Planner behaviour

- Never output instructions such as “set the station to Refinery” or “choose High Tech economy”.
- Express economy shaping as a projected result of body type, facilities, and market links.
- Warn when the available evidence only supports a likely or experimental economy outcome.
- Preserve uncertainty where body bias or market-link behaviour may override the desired economy.

## Evidence basis

- Internal Wregoe planning confirmed that station economy could not be manually selected in Architect.
- Water World station outcomes repeatedly demonstrated strong Tourism/Agriculture bias despite attempts to influence surrounding economy mix.
- Dodec and other station outcomes required analysis through Raven/Market Links rather than direct economy selection.

## Negative evidence preserved

Early planning language that implied station type or direct station selection could set the economy was corrected. That correction should remain visible because it is a high-risk planner hallucination pattern.

## Contradictions

None currently recorded.

## Patch sensitivity

Medium. Frontier economy/link rebalancing could change how inherited economy is calculated, but the absence of direct manual economy selection is currently treated as stable.

## Related mechanics

- M-0001 — Water Worlds Have No Surface Slots
- Future mechanic: Body Intrinsic Economy Bias
- Future mechanic: Strong and Weak Market Links

## Open questions

- How exactly are economy percentages transformed into commodity availability at different station types?
- How should tied or near-tied top economies be represented in planner output?
