# M-0005 - Local Body Base Economies and Modifiers

## Status

Candidate mechanic, high confidence from Mega Guide reference, derived from Frontier-described mechanics as interpreted in the guide.

## Claim

Colony-type ports inherit economy tendencies from the local body type, then apply local body economy modifiers.

## Base inheritable economies from Mega Guide

| Local body type | Base inheritable economies |
|---|---|
| Black holes, neutron stars, white dwarves | High Tech, Tourism |
| Brown dwarves and all other star types | Military |
| Earth-like worlds | Agriculture, High Tech, Military, Tourism |
| Water worlds | Agriculture, Tourism |
| Ammonia worlds | High Tech, Tourism |
| Gas giants | High Tech, Industrial |
| High metal content and metal rich worlds | Extraction |
| Rocky ice worlds | Industrial, Refinery |
| Rocky worlds | Refinery |
| Icy worlds | Industrial |

## Local body economy modifiers from Mega Guide

| Local body modifier | Economy modifier |
|---|---|
| Has rings, including stars with asteroid belts | + Extraction |
| Has organics | + Agriculture, + Terraforming |
| Has geologicals | + Extraction, + Industrial |

The Mega Guide states that these local body modifiers do not stack with base planet economies and do not stack with each other.

## Source evidence

- EV-0004 - Colonisation Reference Documents Pack
- Mega Guide v2.3.0, page 47

## Planner implication

The planner should compute an initial economy hypothesis from body type and modifiers before considering strong and weak links.

The planner must preserve modifier non-stacking rules and must not double-count repeated local-body features without evidence.

## Wregoe relevance

- Water Worlds in Wregoe should be expected to resist non-Agriculture/Tourism flipping because their base inheritable economies are Agriculture and Tourism.
- A4/A5 behaviour should be assessed from their body type, geological/ring context, and facility links rather than from station type alone.

## Confidence

High as reference mechanic. Live previews and Market Links remain authoritative for specific facilities.
