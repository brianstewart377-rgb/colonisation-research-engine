# M-0004 - Colony Port Economy Inheritance

## Status

Candidate mechanic, high confidence from Mega Guide reference, backed by Frontier-derived community documentation.

## Claim

Colony-type ports do not have a manually selected final economy. They acquire economy types from the local body they are built on/orbit, plus applicable local body economy modifiers, plus strong and weak market-link effects.

Specialised ports have an inherent economy baseline and do not inherit the local body's base economy or local body economy modifiers, though their market types can still be affected by strong and weak links.

## Source evidence

- EV-0004 - Colonisation Reference Documents Pack
- Mega Guide v2.3.0, pages 46-47

## Economy strength notation

The Mega Guide treats economy strength as an absolute value where 1.0 is equivalent to 100%, and notes that economy strengths can exceed 1.0 / 100%.

## Planner implication

The planner must not expose a fake `choose economy` control for colony-type ports. It should instead calculate or request evidence for:

- local body base inheritable economy
- local body economy modifiers
- strong links
- weak links
- final live Market Links / market state

## Wregoe relevance

This supports the observed behaviour that A4/A5 markets are shaped by local body and facility-link context rather than manually selected station economy.

It also supports the A4 strategy of building local High Tech strong links rather than assuming a station type alone can create High Tech coverage.

## Confidence

High as a reference mechanic. Specific final market output must be verified live after construction.
