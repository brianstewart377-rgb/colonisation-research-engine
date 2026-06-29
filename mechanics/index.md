# Mechanics Index

This is the canonical mechanic catalogue for the current repository state.

## Normalization notes

The repository previously contained two mechanic strands with overlapping IDs:

- `M-0001` to `M-0003` from direct Wregoe live evidence
- `M-0001` to `M-0005` from reference-derived extraction drafts

Phase 2 normalizes them into one sequence:

- `M-0001` to `M-0003` remain the Wregoe live-evidence mechanics
- the reference-derived drafts are renumbered to `M-0004` to `M-0008`

This preserves the meaning of the original Wregoe seed mechanics while removing duplicate identifiers from the canonical catalogue.

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

## Category counts

- Body-constraint mechanics: `1`
- Construction mechanics: `1`
- Port-taxonomy mechanics: `1`
- Economy mechanics: `5`
- Link-routing mechanics: `1`
- Narrow negative-evidence mechanics: `1`

## Use rule

The planner and future tooling should treat this file as the canonical mechanic index.
Mechanic IDs referenced elsewhere in the repository should resolve through this catalogue rather than through filename guesswork.
