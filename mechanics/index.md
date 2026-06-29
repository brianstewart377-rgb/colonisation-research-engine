# Mechanics Index

This is the canonical mechanic catalogue for the current repository state.

## Normalization notes

The repository originally started with a narrow Wregoe evidence strand and later expanded with direct source extraction from the recovered public colonisation corpus.

The Wregoe-seeded mechanics remain at the front of the sequence, while the new extraction pass extends the catalogue into construction, compatibility, population, and caveat-heavy mechanics without changing the original IDs.

## Canonical catalogue

| ID | Title | Status | Primary category | Source basis | Related evidence | Related experiments |
|---|---|---|---|---|---|---|
| `M-0001` | Water Worlds Have No Surface Slots | Confirmed | Body constraints | Live Wregoe planning evidence | `EV-0002` | `EXP-0000` |
| `M-0002` | Station Economy Is Inherited, Not Manually Chosen | Confirmed | Economy / planner safety | Live Wregoe planning evidence | `EV-0002`, `EV-0003` | `EXP-0000`, `EXP-0001` |
| `M-0003` | One Weak Refinery Link Is Insufficient To Restore Metals | Confirmed | Economy / negative evidence | Narrow live Wregoe test case | `EV-0002` | `EXP-0000` |
| `M-0004` | Construction Points and Facility Tiers | Likely | Construction | Reference-derived mechanic extracted from repository evidence | `EV-0004` | `LV-0005` |
| `M-0005` | Colony-Type and Specialised Ports | Likely | Port taxonomy | Reference-derived mechanic extracted from repository evidence | `EV-0003`, `EV-0004` | `LV-0002` |
| `M-0006` | Strong and Weak Link Routing | Likely | Market links / routing | Reference-derived mechanic supported by Wregoe context | `EV-0001`, `EV-0004` | `LV-0003`, `LV-0005` |
| `M-0007` | Colony Port Economy Inheritance | Likely | Economy | Reference-derived mechanic supported by Wregoe context | `EV-0001`, `EV-0003`, `EV-0004` | `LV-0001`, `LV-0002` |
| `M-0008` | Local Body Base Economies and Modifiers | Likely | Economy / body effects | Reference-derived mechanic | `EV-0004` | `LV-0001`, `LV-0004` |
| `M-0009` | Facility Prerequisites, Port Conversion, and High-Tier Port Cost Escalation | Extracted | Construction / dependencies | Recovered Mega Guide and DaftMav-derived tables | `EV-0004` | `LV-0005`, `LV-0010` |
| `M-0010` | Economy Compatibility, Rank Protection, and Market Cannibalization | Extracted | Economy / markets | Recovered Mega Guide appendix and overlap material | `EV-0004` | `LV-0001`, `LV-0003`, `LV-0006`, `LV-0007` |
| `M-0011` | Facility Stats, Service Activation, and System Effects | Extracted | System stats / services | Recovered Mega Guide and DaftMav-derived tables | `EV-0004` | `LV-0008` |
| `M-0012` | Population Growth, Body Multipliers, and Output Scaling | Extracted | Population | Recovered Mega Guide population rewrite | `EV-0004` | `LV-0008`, `LV-0009` |
| `M-0013` | System Scores, Payments, and High-Risk Caveats | Extracted | Score / caveats | Recovered Mega Guide appendices and bug tables | `EV-0004` | `LV-0009`, `LV-0010` |

## Category counts

- Body-constraint mechanics: `1`
- Construction and dependency mechanics: `2`
- Port and routing mechanics: `3`
- Economy and market mechanics: `5`
- System-stat and population mechanics: `2`
- Score and caveat mechanics: `1`

## Use rule

The planner and export builder should treat this file as the canonical mechanic index.
Mechanic IDs referenced elsewhere in the repository should resolve through this catalogue rather than through filename guesswork.
