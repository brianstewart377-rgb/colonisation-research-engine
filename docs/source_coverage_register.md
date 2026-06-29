# Source Coverage Register

This register records the direct colonisation knowledge-extraction pass after the repository was supplied with a canonical local `reference_sources/` pack.

## Coverage method

- `100%` means the named page range, section, file, or sheet extract was directly reviewed and mined for mechanical content.
- `Targeted` means the source was opened and reviewed only for specific mechanically useful ranges.
- `Inventory only` means the source bundle is present locally and registered, but was not yet converted into claim-level extraction in this pass.

## Canonical source location

All direct source extraction in the rerun pass was constrained to:

- `reference_sources/`

The extraction pass no longer depended on recovered public copies or user-uploaded secondary PDFs as its active claim source base.

## Directly processed reference sources

| Source ID | Source | Format | Coverage | Notes |
|---|---|---|---:|---|
| `MG-0001` | `Elite Dangerous Colonization Mega Guide` | Local canonical text derivative | 100% targeted ranges | Primary source for construction, inheritance, links, service activation, compatibility, population, score, caveats, and appendix material. |
| `FW-0001` | `Elite Dangerous Colonisation Strong and Weak Links Illustrated Reference` | Local canonical text derivative | 100% | Direct source for main-port routing, same-body versus cross-body routing, displayed-link caveats, and planner-safety warnings. |
| `DM-0001` | `Colonization Construction Details` | Local canonical CSV sheet extracts | 100% | Direct source for facility specs, prerequisites, stat effects, CP rewards, commodity volumes, and material requirements. |
| `DD-0001` | `Colonisation Dependency Flowchart` | Local encoded diagram bundle | 100% targeted visual review | Direct corroborating source for prerequisite-edge relationships in the dependency tree. |

## Mega Guide coverage

| Source ID | Pages | Section | Coverage | Extraction outcome |
|---|---:|---|---:|---|
| `MG-0001` | `25-33` | `How To Architect A System? Construction Points, And A Tool You Will Love` through `The Value Of Space Versus Ground Slots` | 100% | Extracted CP rules, build sequencing, high-tier port escalation, slot-value rules, and commodity-location caveats. |
| `MG-0001` | `36-41` | `Station Interiors` | 100% | Extracted interior-update timing and economy tie-break caveats. |
| `MG-0001` | `47-51` | `How Do Colony-Type Ports Gain Economies? Base Inheritable Economy + Modifiers` | 100% | Extracted port-family taxonomy, body inheritance tables, body modifiers, and body-preference guidance. |
| `MG-0001` | `52-59` | `What Are Strong & Weak Links?` through `Special Case: When Ports Convert To Being Supporting Facilities` | 100% | Extracted strong/weak-link rules, modifier material, main-port routing, and converted-port caveats. |
| `MG-0001` | `60-63` | `What Do Security, Wealth, SoL, Tech Level, Dev Level, And Population Do?` | 100% | Extracted known stat effects, service thresholds, and unknown zones. |
| `MG-0001` | `68-80` | `Which Economies Are Compatible With Each Other?` and `What Does Population Affect, And How Do I Grow It?` | 100% | Extracted top-two protection, pair-overlap material, population formulas, output scaling, and score/payment rules. |
| `MG-0001` | `84-87` | `Case Study #1` and `Case Study #2` | 100% | Extracted planner-useful body recommendations and agriculture/refinery caveats. |
| `MG-0001` | `92` | `Bugs, Known Issues, And Possible Workarounds` | 100% | Extracted bug/workaround items into claims, contradictions, and planner risks. |
| `MG-0001` | `95-97` | `Appendix A: Advanced Strategies` | 100% | Extracted advanced sequencing, nesting, and rank-order tactics. |
| `MG-0001` | `99` | `Appendix C: Detailed By-Facility System Scores` | 100% | Extracted all by-facility score values. |
| `MG-0001` | `100-105` | `Appendix D: Detailed Overlap Of Economy Pairs` | 100% | Extracted all 35 economy-pair overlap entries from the appendix tables. |

## Strong/weak illustrated reference coverage

| Source ID | Section | Coverage | Extraction outcome |
|---|---|---:|---|
| `FW-0001` | `1. The one-minute model` | 100% | Extracted same-body strong-link versus cross-body weak-link baseline. |
| `FW-0001` | `2. Asset types, main ports, and body influence` | 100% | Extracted main-port priority, surface-to-orbital strong routing, and weak-link generation caveats. |
| `FW-0001` | `3. Strong links: how surface and orbital markets connect` | 100% | Extracted routing behavior for mixed surface/orbital bodies and displayed-link caveats. |
| `FW-0001` | `4. Weak links: cross-body support and its limits` | 100% | Extracted weak-link reception rules and multi-port weak-link edge cases. |
| `FW-0001` | `5-7` | 100% | Extracted visible-link-count warnings and planner-safety workflow rules. |
| `FW-0001` | `8. Source and confidence` | 100% | Extracted source-status and non-official-formula caveat. |

## DaftMav extract coverage

| Source ID | File / sheet extract | Coverage | Extraction outcome |
|---|---|---:|---|
| `DM-0001` | `DaftMav_Colonization.csv` | 100% | Extracted orbital, surface, installation, settlement, hub, port, material, and trip-count facility rows. |
| `DM-0001` | `DaftMav_Stats-only.csv` | 100% | Extracted stat-focused rows and simplified prerequisite / CP / facility-economy views. |
| `DM-0001` | `DaftMav_Shoppinglist.csv` | 100% reviewed | Used to confirm material-priority and hauling-scale patterns. |
| `DM-0001` | `DaftMav_SystemPlanner.csv` | 100% reviewed | Used as supporting planner-oriented context. |
| `DM-0001` | `DaftMav_SystemPlanner v2.csv` | 100% reviewed | Used as supporting planner-oriented context. |
| `DM-0001` | `DaftMav_v3 now available.csv` | 100% reviewed | Inventory / note only. |

## Dependency-flowchart coverage

| Source ID | Asset | Coverage | Notes |
|---|---|---:|---|
| `DD-0001` | `dependency-flowchart-v0.webp.base64.txt` | 100% | The encoded diagram bundle was decoded and visually reviewed. It was used to corroborate prerequisite edges for tourism, military, security, research, and hub chains. |

## Existing evidence rechecked during the rerun

| Evidence record | Coverage | Mechanically relevant sections reviewed |
|---|---:|---|
| `EV-0001-rocha-liberty-post-high-tech-build.md` | 100% | Post-build facilities, links, economies, and commodity observations |
| `EV-0002-wregoe-raven-proposed-build-review.md` | 100% | Current-vs-projected CP interpretation and placeholder-name caution |
| `EV-0003-a4-t3-station-selection-previews.md` | 100% | Preview-equality caveat and station-class uncertainty |
| `EV-0004-reference-documents-pack.md` | 100% | Artifact provenance and transition to committed canonical reference sources |

## Extraction note

The repository now has a committed canonical reference corpus under `reference_sources/`.
The rerun extraction pass anchors direct source claims to stable source IDs `MG-0001`, `FW-0001`, `DM-0001`, and `DD-0001` instead of relying on recovered public copies or transient upload paths.
