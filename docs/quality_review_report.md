# CRE Quality Review Report

Date: 2026-06-29

Scope reviewed:

1. `mechanics/`
2. `evidence/claim_register.csv`
3. `exports/mechanics.csv`
4. `exports/planner_rules.csv`
5. `exports/unknowns.csv`
6. `exports/contradictions.csv`
7. `exports/live_verification_matrix.csv`
8. `reference_sources/source_register.csv`

Review mode:

- quality review only
- no new schema added
- no new release infrastructure added
- no new extraction performed
- no architecture expansion performed

## Executive summary

The knowledge base is now materially safer and more honest than the pre-review state.

The main quality problems found were:

- warnings and bug notes still typed as ordinary extracted rules in the claim layer;
- a few lingering prose/testing-status phrases that still implied pre-canonical provenance wording;
- several planner and mechanic summaries that were already improved in earlier passes but still needed final review against claim trust calibration;
- a stale research-gap entry that still described the canonical source pack as absent.

No new extraction defects, broken source IDs, or claim-title duplicates were found in the current reviewed state.

No separate rejected-claims schema was added. Existing contradiction records already capture the supported false or over-generalized assumptions, and adding a new schema would have gone beyond the review-only remit.

## Issues found

### QR-001 - Safety caveats typed as hard extracted rules

Problem:

- some explicit warning/bug/caveat claims were still typed as `source_extracted_rule`
- this made the claim layer flatter than the evidence warranted

Affected claims:

- `CL-0182` demolition may not reduce population
- `CL-0193` agricultural planetary ports can bug out
- `CL-0315` advertised versus actual pad sizes
- `CL-0317` Eirene variant misbuild
- `CL-0318` Ichnaea variant misbuild
- `CL-0327` displayed link count can mask routed influence
- `CL-0332` visible strong-link count is not total influence

Assessment:

- these are not new mechanics
- they are caveats, bug notes, or UI interpretation warnings
- treating them as caveats makes planner safety clearer without changing the underlying evidence

Resolution:

- reclassified the affected rows to `source_extracted_caveat`

Status:

- fixed

### QR-002 - Lingering pre-canonical provenance wording

Problem:

- a few files still used old phrases like `reference-derived` or `DaftMav-derived`
- one research-gap entry still described the reference pack as absent, even though `reference_sources/` is committed and active

Affected files:

- `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- `experiments/live_verification_register.md`
- `docs/manual_research_gaps.md`
- `mechanics/construction_rules_register.md`
- `mechanics/market_rules_register.md`

Assessment:

- this was not a knowledge error so much as a provenance honesty problem
- leaving it unfixed would encourage future misreading of the current source basis

Resolution:

- updated wording to point to canonical `MG-0001`, `DM-0001`, `FW-0001`, and `reference_sources/`
- rewrote the stale research-gap entry so it distinguishes:
  - canonical committed derivatives
  - optional original-binary archival completeness

Status:

- fixed

### QR-003 - Planner-rule testing status still used outdated wording

Problem:

- `PR-0005` still used `Reference-derived, awaiting direct routing verification`

Assessment:

- the rule is still verification-sensitive, but the source basis is now the committed canonical pack, not an older indirect reference state

Resolution:

- updated wording to `Supported by the canonical reference-source pack, still awaiting direct routing verification`

Status:

- fixed

### QR-004 - Risk of recommendations sounding like hard mechanics in prose

Problem:

- this was a real issue earlier in the cycle, especially in routing, economy-planning, and strategy prose
- by the time of this final audit, the main overstatements had already been corrected in earlier quality passes

Assessment:

- no additional mechanic-wide rewrites were needed in this last pass
- current prose is now broadly aligned with the calibrated claim layer

Status:

- previously fixed during the same review cycle; no extra change required in this final pass

### QR-005 - Duplicated claims under different names

Problem checked:

- exact duplicate titles
- near-duplicate high-volume families
- duplicated Appendix D / population / CP statements

Result:

- no exact duplicate titles remain
- the remaining near-overlaps are deliberate:
  - scenario-specific versus general routing warnings
  - facility-by-facility Appendix C score rows
  - facility-family prerequisite rows

Status:

- no action required

### QR-006 - Wregoe-specific observations generalized too far

Problem checked:

- whether Wregoe observations were being promoted into universal live mechanics

Result:

- the remaining Wregoe mechanics are constrained appropriately:
  - `M-0001`
  - `M-0002`
  - `M-0003`
- they remain limited, negative-evidence, or planner-safety mechanics rather than broad extracted community-guide mechanics

Residual caution:

- these mechanics still deserve human review when new live evidence arrives

Status:

- acceptable after prior confidence calibration; no new edit required in this final pass

### QR-007 - Community-guide claims treated as confirmed live evidence

Problem checked:

- whether `MG-0001`, `DM-0001`, `FW-0001`, or `DD-0001` claims were being mislabeled as confirmed live facts

Result:

- current labeling is acceptable:
  - extracted community-source mechanics remain `Extracted` or `Likely`
  - live-specific contradictions and verification tasks remain explicit
  - planner safety notes preserve the need for live confirmation where appropriate

Residual caution:

- human review is still needed for the mechanics listed later in this report

Status:

- no additional change required

### QR-008 - Need for a Known False / Rejected Claims register

Problem checked:

- whether the repo needs a dedicated rejected-claims register

Assessment:

- current supported false or unsafe assumptions are already captured by:
  - `docs/contradiction_register.md`
  - planner safety rules
  - caveat claims
- adding a new register would have been schema expansion and was unnecessary for the supported evidence currently present

Representative already-covered rejected assumptions:

- weak-link-only repair is not safe to universalize
- preview-only station-class superiority is not proven
- visible arrow count is not sufficient routing proof
- some agricultural planetary implementations can fail live

Status:

- no new register added

## Fixes applied in this review pass

### Fix chunk A - Caveat and provenance honesty cleanup

Files changed:

- `evidence/claim_register.csv`
- `planner/planner_rules_register.md`
- `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- `experiments/live_verification_register.md`
- `docs/manual_research_gaps.md`
- `mechanics/construction_rules_register.md`
- `mechanics/market_rules_register.md`

What changed:

- retyped seven warning/bug claims from rule to caveat
- updated one planner-rule testing-status line to canonical-source wording
- cleaned the final stale provenance wording leftovers

## Validation run

Commands:

```bash
python3 tools/build_release_bundle.py --output exports
python3 tools/build_release_bundle.py --output exports --validate-only
```

Observed output:

- `mechanics.csv` `13`
- `planner_rules.csv` `13`
- `economy_rules.csv` `20`
- `construction_rules.csv` `23`
- `planner_risks.csv` `15`
- `governance_decisions.csv` `5`
- `unknowns.csv` `20`
- `contradictions.csv` `9`
- `observations.csv` `13`
- `claims.csv` `343`
- `claim_provenance_links.csv` `370`
- `evidence_traceability.csv` `24`
- `live_verification_matrix.csv` `12`
- `graph_nodes.csv` `239`
- `graph_edges.csv` `294`
- bundle validation: `OK`

## Mechanics still needing human review

These mechanics are usable, but still deserve direct human scrutiny because their remaining uncertainty is substantive rather than editorial:

- `M-0004`
  - current-versus-proposed CP edge cases beyond the Raven example
- `M-0005`
  - specialised-port exemption depth
  - post-build station-class divergence
- `M-0006`
  - main-port aggregation behavior
  - surface-to-orbital forwarding scope
  - lower-tier/later-built weak-link exceptions
- `M-0008`
  - body-modifier stacking
  - Terraforming modifier role
- `M-0009`
  - large-branch versus family-level prerequisite strictness
- `M-0010`
  - same-strength economy ordering
  - live stability of some Appendix D expectations
- `M-0012`
  - under-sampled body multipliers
  - demolition/population behavior
  - emissions/BGS effect magnitude
- `M-0013`
  - patch-sensitive bug caveats and routing-risk drift

## Final reviewer judgment

The CRE knowledge base is now:

- materially more provenance-honest
- less overconfident
- safer for planner usage
- better separated between rules, recommendations, and caveats

The remaining weaknesses are domain uncertainties that require live confirmation, not major repository hygiene failures.
