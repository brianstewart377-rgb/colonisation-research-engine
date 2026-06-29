# Source Coverage Register

This register records the source material processed during the direct colonisation knowledge-extraction pass.

## Coverage method

- `100%` means the named page range, section, table, or evidence record was directly reviewed and mined for mechanical content.
- `Targeted` means the source was opened and reviewed only for specific mechanically useful sections.
- `Indirect only` means the underlying source artifact was still not recovered directly and is represented only through downstream interpretation.

## Directly processed source documents

| Source | Format | Coverage | Notes |
|---|---|---:|---|
| `Elite Dangerous Colonization Mega Guide v2.3.0` | Recovered public `docx` + `txt` export | Targeted | Used as the primary extraction source for construction, economy inheritance, link routing, stats, population, bugs, Appendix C, and Appendix D. |
| `AetherWave Colonisation Reference Tables` | HTML page quoting DaftMav-derived data | 100% | Used as the structured substitute for the absent local DaftMav spreadsheet artifact. |
| `EV-0001-rocha-liberty-post-high-tech-build.md` | Evidence record | 100% | Rechecked as the current live Wregoe-style post-build evidence anchor. |
| `EV-0002-wregoe-raven-proposed-build-review.md` | Evidence record | 100% | Rechecked for CP, placeholder, and weak-link caveats. |
| `EV-0003-a4-t3-station-selection-previews.md` | Evidence record | 100% | Rechecked for station-class and preview-equality caveats. |
| `EV-0004-reference-documents-pack.md` | Evidence record | 100% | Rechecked for artifact provenance and absence status. |

## Mega Guide page and section coverage

| Pages | Section | Coverage | Extraction outcome |
|---:|---|---:|---|
| `25-33` | `How To Architect A System? Construction Points, And A Tool You Will Love` through `The Value Of Space Versus Ground Slots` | 100% | Extracted CP rules, build sequencing, high-tier port escalation, slot-value rules, and commodity-location caveats. |
| `36-41` | `Station Interiors` | 100% | Extracted interior-update timing and economy tie-break caveats. |
| `47-51` | `How Do Colony-Type Ports Gain Economies? Base Inheritable Economy + Modifiers` | 100% | Extracted port-family taxonomy, body inheritance tables, body modifiers, and body-preference guidance. |
| `52-59` | `What Are Strong & Weak Links?` through `Special Case: When Ports Convert To Being Supporting Facilities` | 100% | Extracted strong/weak-link rules, modifier material, main-port routing, and converted-port caveats. |
| `60-63` | `What Do Security, Wealth, SoL, Tech Level, Dev Level, And Population Do?` | 100% | Extracted known stat effects, service thresholds, and unknown zones. |
| `68-80` | `Which Economies Are Compatible With Each Other?` and `What Does Population Affect, And How Do I Grow It?` | 100% | Extracted top-two protection, pair-overlap material, population formulas, output scaling, and score/payment rules. |
| `84-87` | `Case Study #1` and `Case Study #2` | 100% | Extracted planner-useful body recommendations and agriculture/refinery caveats. |
| `92` | `Bugs, Known Issues, And Possible Workarounds` | 100% | Extracted bug/workaround items into claims, contradictions, and planner risks. |
| `95-97` | `Appendix A: Advanced Strategies` | 100% | Extracted advanced sequencing, nesting, and rank-order tactics. |
| `99` | `Appendix C: Detailed By-Facility System Scores` | 100% | Extracted all by-facility score values. |
| `100-105` | `Appendix D: Detailed Overlap Of Economy Pairs` | 100% | Extracted all 35 economy-pair overlap entries from the appendix tables. |

## DaftMav-derived table coverage

| Section / sheet surrogate | Coverage | Extraction outcome |
|---|---:|---|
| `Orbital Station Information` | 100% | Extracted all orbital station tier, cost, reward, pad, and commodity totals. |
| `Orbital Outpost Information` | 100% | Extracted all orbital outpost specifications. |
| `System Effects by Installation Type` | 100% | Extracted all listed system-stat effect rows. |
| `Orbital Installation Information` | 100% | Extracted all installation prerequisites, costs, rewards, and economy influence rows. |
| `Surface Port Information` | 100% | Extracted all surface-port specification rows. |
| `Surface Settlement Information` | 100% | Extracted all settlement size, prerequisite, reward, pad, and commodity rows. |
| `Surface Hub Information` | 100% | Extracted all hub prerequisite and stat rows. |
| `Resource Requirements for Major Materials` | 100% | Extracted steel, CMM Composite, aluminium, titanium, and surface-material priority notes plus exact 2x/3x scaling rules. |
| `Important Construction Notes` | 100% | Extracted first-installation surcharge, landing-pad caveat, CP strategy note, and variant bug notes. |

## Existing evidence rechecked during this pass

| Evidence record | Coverage | Mechanically relevant sections reviewed |
|---|---:|---|
| `EV-0001-rocha-liberty-post-high-tech-build.md` | 100% | Post-build facilities, links, economies, and commodity observations |
| `EV-0002-wregoe-raven-proposed-build-review.md` | 100% | Current-vs-projected CP interpretation and placeholder-name caution |
| `EV-0003-a4-t3-station-selection-previews.md` | 100% | Preview-equality caveat and station-class uncertainty |
| `EV-0004-reference-documents-pack.md` | 100% | Artifact provenance, missing-source tracking, and recovery context |

## Still not directly recovered as local primary artifacts

| Named artifact | Direct status | Current usable coverage |
|---|---|---|
| `Elite Dangerous Colonisation Strong and Weak Links Illustrated Reference` | Not directly recovered as a standalone local artifact | Substantive link-routing content recovered through the Mega Guide strong/weak-link sections |
| `Colonization Construction Details (By DaftMav).xlsx` | Not directly recovered as a standalone local spreadsheet file | Structured table coverage recovered through the AetherWave DaftMav-derived reference tables |
| `Dependency flowchart image` | Not directly recovered as a standalone local artifact | Prerequisite and dependency content recovered through Mega Guide and DaftMav-derived prerequisite tables |

## Extraction note

This pass now contains direct source extraction from recovered public copies and structured mirrors.
It is no longer limited to indirect repository-only interpretation, but it still distinguishes between directly recovered artifacts and still-missing standalone originals.
