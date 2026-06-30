# Planner Risk Register

This register captures recurring failure modes the planner must guard against.

## R-0001 - Fake manual economy selection

- Severity: Critical
- Source: `mechanics/M-0002-station-economy-is-inherited.md`, `planner/planner_rules_register.md`, `planner/planner_safety.md`
- Failure mode: The planner tells the user to set a colony-type station to a chosen economy as if that were a direct control.
- Why dangerous: It recommends a mechanic the repository already rejects.
- Required mitigation: Enforce inherited-economy modeling and block direct choose-economy outputs.

## R-0002 - Surface recommendations on impossible bodies

- Severity: Critical
- Source: `mechanics/M-0001-water-worlds-have-no-surface-slots.md`, `planner/planner_rules_register.md`
- Failure mode: The planner recommends surface facilities on a Water World or another unsupported body/facility combination.
- Why dangerous: It produces impossible builds.
- Required mitigation: Run hard feasibility checks before recommendation generation.

## R-0003 - Weak-link overconfidence

- Severity: High
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`, `docs/contradiction_register.md`
- Failure mode: The planner treats weak-link spillover as dependable targeted control without sufficient corroboration.
- Why dangerous: It can recommend brittle or failed market-repair strategies.
- Required mitigation: Label weak-link-only recommendations as experimental and prefer local strong support for must-have outcomes.

## R-0004 - Preview-state treated as completed-state truth

- Severity: High
- Source: `evidence/EV-0003-a4-t3-station-selection-previews.md`, `docs/anomaly_register.md`
- Failure mode: The planner treats preview equality or preview labels as proof of final completed behavior.
- Why dangerous: Preview panels can hide post-build differences.
- Required mitigation: Distinguish preview, proposed, under-construction, and completed evidence states.

## R-0005 - Proposed-build totals treated as current buildability

- Severity: High
- Source: `evidence/EV-0002-wregoe-raven-proposed-build-review.md`, `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Failure mode: The planner treats a projected negative full-plan CP state as proof that the next selected build is currently invalid.
- Why dangerous: It can incorrectly block valid progress or recommend unnecessary demolition.
- Required mitigation: Separate current buildability from projected plan totals.

## R-0006 - Identity collapse across same-name facilities or disputed architects

- Severity: High
- Source: `ontology/identity_and_provenance_rules.md`, `docs/anomaly_register.md`, `evidence/source_authority_register.md`
- Failure mode: The planner or research tooling merges records that merely share names or trusts a single public-page architect attribution as definitive.
- Why dangerous: It contaminates provenance and can attach the wrong evidence to the wrong system or builder.
- Required mitigation: Require system/body context and preserve attribution as a sourced claim.

## R-0007 - Stale or mirrored sources override better evidence

- Severity: High
- Source: `evidence/source_authority_register.md`, `docs/contradiction_register.md`, `docs/anomaly_register.md`
- Failure mode: A stale community guide, mirror, or reposted document silently overrides direct live evidence or official wording.
- Why dangerous: It reintroduces already-known source drift.
- Required mitigation: Preserve source hierarchy and explicit contradiction tracking.

## R-0008 - Demolition advice without strong direct evidence

- Severity: Critical
- Source: `planner/knowledge_projection_rules.md`, `planner/contextual_strategy_register.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Failure mode: The planner recommends irreversible demolition on the basis of weak or indirect evidence.
- Why dangerous: It creates a high-cost irreversible error.
- Required mitigation: Require stronger evidence for demolition than for additive or observational advice.

## R-0009 - Missing primary artifacts mistaken for completed extraction

- Severity: Medium
- Source: `docs/source_coverage_register.md`, `docs/manual_research_gaps.md`
- Failure mode: Future tooling assumes page-level extraction came from transient upload paths or original binaries and ignores the repository's committed canonical derivatives under `reference_sources/`.
- Why dangerous: It can either understate real extraction coverage or fabricate the wrong provenance path.
- Required mitigation: Treat `reference_sources/` as the canonical direct-extraction base and keep original-binary versus committed-derivative distinction explicit.

## R-0010 - Agricultural advice that ignores the zero-output planetary agri bug

- Severity: High
- Source: `docs/contradiction_register.md`, `evidence/claim_register.csv`
- Failure mode: The planner recommends planetary agricultural ports as if they were always reliable agricultural producers.
- Why dangerous: Some of those ports can bug out and produce no agricultural goods.
- Required mitigation: Prefer orbital agriculture in high-confidence recommendations and warn explicitly when a ground agriculture design is chosen.

## R-0011 - Nested-port passthrough bug treated as stable design doctrine

- Severity: Critical
- Source: `docs/contradiction_register.md`, `evidence/claim_register.csv`
- Failure mode: The planner treats planetary-to-orbital inherited-economy passthrough as a safe permanent mechanic.
- Why dangerous: The guide itself warns this behavior is likely a bug and could be fixed.
- Required mitigation: Label any recommendation that depends on nested-port passthrough as experimental and reversible.

## R-0012 - Population-pruning demolition advice based on anecdote

- Severity: Critical
- Source: `experiments/live_verification_register.md`, `evidence/claim_register.csv`
- Failure mode: The planner recommends demolition to reduce population or reset output without strong direct evidence that demolition actually lowers population.
- Why dangerous: It can create irreversible loss without delivering the intended population change.
- Required mitigation: Block population-pruning demolition advice until `LV-0009` is resolved.

## R-0013 - Pad-size advice that trusts advertised settlement metadata

- Severity: High
- Source: `docs/contradiction_register.md`, `evidence/claim_register.csv`
- Failure mode: The planner recommends a facility to a large hauler because the variant advertises the required pad size.
- Why dangerous: Some variants appear to expose different real landing access than their advertised pad size suggests.
- Required mitigation: Preserve pad-size uncertainty warnings and request variant-level confirmation when large-hauler access matters.

## R-0014 - Arrow-count routing overconfidence

- Severity: Critical
- Source: `docs/contradiction_register.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`, `planner/planner_rules_register.md`
- Failure mode: The planner treats visible Market Links arrow count as a direct additive proof of influence and recommends demolition or replacement based on that assumption.
- Why dangerous: Routed influence can be aggregated or forwarded in ways the visible topology does not reveal.
- Required mitigation: Block irreversible recommendations that rely only on arrow count and require live link inspection or targeted validation.

## R-0015 - Dependency-family flattening

- Severity: High
- Source: `docs/contradiction_register.md`, `mechanics/M-0009-facility-prerequisites-port-conversion-and-escalation.md`, `experiments/live_verification_register.md`
- Failure mode: The planner flattens every prerequisite into a generic family rule and ignores cases where the large or upgraded branch may be the actual requirement.
- Why dangerous: It can recommend build orders that look CP-valid but still fail live prerequisite checks.
- Required mitigation: Preserve branch-sensitive prerequisite caveats and treat unresolved chains as conditional until `LV-0012` is resolved.
