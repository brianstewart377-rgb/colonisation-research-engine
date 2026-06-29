# Confidence Model Register

This register turns the repository's confidence logic into a canonical reference for future tools and analyst review.

## Core model

Confidence must be tracked separately for:

- observations
- experiments
- mechanics
- planner knowledge

This separation is required by:

- `constitution/project_principles.md`
- `architecture/colonisation_intelligence_platform_architecture.md`
- `planner/planner_safety.md`

## Components

The repository source review defines six weighted components:

| Component | Weight | Meaning |
|---|---:|---|
| Source authority | 25 | Official and trusted sources score highest |
| Directness | 20 | Direct observation beats interpretation of observation |
| Specificity | 15 | Named system/body/facility beats generic claim |
| Exportability / reproducibility | 10 | Publicly reproducible evidence beats one-off inaccessible material |
| Freshness | 10 | Newer evidence scores better |
| Corroboration | 20 | Independent agreement increases trust |

## Bands

| Score | Band | Meaning |
|---|---|---|
| `85-100` | High confidence | Good enough to drive automation or strong planner logic |
| `70-84` | Usable with review | Good enough for planner hints and analyst use |
| `50-69` | Exploratory only | Preserve for analyst review, not automation |
| `<50` | Weak evidence | Discovery lead only |

## CM-0001 - Confidence must be explicit at every interpretation layer

- Status: Confirmed
- Source: `constitution/project_principles.md`
- Rule: Confidence must be explicit wherever interpretation occurs.
- Planner implication: Planner outputs must expose confidence instead of hiding it.

## CM-0002 - Contradictions lower confidence rather than disappearing

- Status: Confirmed
- Source: `constitution/project_principles.md`, `architecture/colonisation_intelligence_platform_architecture.md`, `planner/planner_safety.md`
- Rule: Credible contradictions must reduce mechanic or planner confidence and may unpublish planner-safe knowledge.
- Planner implication: Contradicted rules should downgrade from `Confirmed` to `Likely`, `Disputed`, or `Unknown` rather than stay silently stable.

## CM-0003 - Patch drift must decay confidence

- Status: Confirmed
- Source: `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: Major mechanics patches should cause confidence decay for patch-sensitive mechanics until they are re-verified.
- Planner implication: Stale post-patch mechanics should not remain fully trusted without renewed evidence.

## CM-0004 - Source authority alone is insufficient

- Status: Confirmed
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: A claim should not be trusted only because it comes from a respected source; specificity, freshness, corroboration, and directness still matter.
- Planner implication: Older official guidance may still need caveats after balance changes.

## CM-0005 - Negative evidence must count against confidence

- Status: Confirmed
- Source: `constitution/project_principles.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: Failed predictions, null effects, and disproved assumptions must reduce confidence rather than be treated as missing data.
- Planner implication: The planner should become more cautious after failed interventions, not ignore them.

## CM-0006 - Historical evidence must be labeled as historical

- Status: Confirmed
- Source: `planner/planner_safety.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: Historical evidence is useful, but it must be marked as historical when current state is unknown.
- Planner implication: Do not present stale state as if it were live.

## CM-0007 - Community interpretation can be high-value but remains conditional

- Status: Confirmed
- Source: `evidence/source_catalog.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: Community spreadsheets and guides can yield strong structured hypotheses, but they remain conditional until corroborated by direct evidence or repeated tests.
- Planner implication: Community-derived rules should often enter as `Likely`, `Experimental`, or `Needs verification`, not `Confirmed`.

## Mechanic-specific required fields

Per the platform architecture, each mechanic should eventually track:

- `confidence_score`
- `confidence_band`
- `last_verified_version`
- `last_verified_at`
- `contradiction_count`
- `corroborating_evidence_count`
- `negative_evidence_count`
- `patch_sensitivity`
- `confidence_decay_state`

## Operational use

Future tooling should treat this register as the canonical confidence-policy layer.
If a future implementation needs different numeric weights, the rule changes should be versioned rather than silently rewritten.
