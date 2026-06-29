# Planner Rules Register

This register extracts planner-operational rules from the repository's mechanics, ontology, and planner documents.

## PR-0001 - Optimize objectives, not isolated facilities

- Category: Decision model
- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Related mechanics: contextual rule
- Rule: Start from player objective, constraints, current coverage, and gaps before recommending facilities.
- Planner implication: Facility lists are outputs of reasoning, not the start of reasoning.
- Testing status: Documentation-confirmed, operationally safe
- Contradictions: None currently recorded
- Unknowns: None

## PR-0002 - Block impossible builds

- Category: Safety
- Status: Confirmed
- Source: `planner/planner_safety.md`, `mechanics/M-0001-water-worlds-have-no-surface-slots.md`
- Related mechanics: `M-0001`
- Rule: Unsupported facility types and impossible body/build combinations must be blocked rather than merely soft-warned.
- Planner implication: Invalid recommendations should never reach the user as options.
- Testing status: Supported by Wregoe negative evidence
- Contradictions: None currently recorded
- Unknowns: None

## PR-0003 - Never imply direct station economy selection

- Category: Safety / economy
- Status: Confirmed
- Source: `planner/planner_safety.md`, `mechanics/M-0002-station-economy-is-inherited.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`
- Related mechanics: `M-0002`, `M-0007`
- Rule: Do not tell the user to set a colony-type station to a chosen economy.
- Planner implication: Express economy shaping as an indirect projected outcome.
- Testing status: Supported by repository live evidence
- Contradictions: None currently recorded
- Unknowns: Final percentage-to-commodity mapping remains open

## PR-0004 - Prefer local strong links for targeted market shaping

- Category: Economy strategy
- Status: Likely
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`, `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`
- Related mechanics: `M-0003`, `M-0006`
- Rule: For must-have outcomes, prefer same-body strong-link support over remote weak-link spillover.
- Planner implication: Weak-link-only plans should be labeled experimental unless corroborated.
- Testing status: Partly supported, still requires broader live verification
- Contradictions: `C-0004`
- Unknowns: Exact threshold at which weak support becomes reliable

## PR-0005 - Treat visible arrows as incomplete routing evidence

- Category: Economy analysis
- Status: Likely
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`
- Related mechanics: `M-0006`
- Rule: Do not infer full causal structure from visible Market Links arrow count alone.
- Planner implication: Require live link inspection and caution before demolition or architecture changes.
- Testing status: Reference-derived, awaiting direct routing verification
- Contradictions: None currently recorded
- Unknowns: Exact aggregation behavior between main surface and orbital ports

## PR-0006 - Distinguish current buildability from proposed-plan totals

- Category: Construction safety
- Status: Likely
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Related mechanics: `M-0004`
- Rule: A negative projected construction-point total that includes unbuilt facilities is not enough to declare the next selected build invalid.
- Planner implication: Separate `current` from `proposed full-plan` states in the UI and logic.
- Testing status: Supported by Wregoe/Raven interpretation evidence
- Contradictions: `C-0003`
- Unknowns: Additional planner-model edge cases

## PR-0007 - Preserve negative evidence and contradictions

- Category: Research safety
- Status: Confirmed
- Source: `constitution/project_principles.md`, `planner/planner_safety.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`
- Related mechanics: all mechanics
- Rule: Raw contradiction and failed predictions must remain visible instead of being flattened into a single confident answer.
- Planner implication: Confidence must fall when credible conflicting evidence exists.
- Testing status: Governance-confirmed
- Contradictions: None currently recorded
- Unknowns: None

## PR-0008 - Label every recommendation by confidence band

- Category: Safety
- Status: Confirmed
- Source: `planner/planner_safety.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Related mechanics: all mechanics
- Rule: Every recommendation must be labeled `Confirmed`, `Likely`, `Experimental`, or `Unknown`.
- Planner implication: The planner cannot output unsupported certainty.
- Testing status: Governance-confirmed
- Contradictions: None currently recorded
- Unknowns: None

## PR-0009 - Never universalize a contextual strategy

- Category: Decision model
- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Related mechanics: contextual strategy rule
- Rule: A locally good architecture must not be promoted into a universal rule without context.
- Planner implication: State the objective, gap, and trade-off that made a strategy viable.
- Testing status: Documentation-confirmed
- Contradictions: None currently recorded
- Unknowns: None

## PR-0010 - Suggest experiments when confidence is weak

- Category: Research workflow
- Status: Confirmed
- Source: `planner/planner_safety.md`, `experiments/README.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Related mechanics: all experimental or unresolved mechanics
- Rule: When confidence is insufficient, recommend a validation experiment or observation step instead of pretending certainty.
- Planner implication: Live verification entries are first-class outputs.
- Testing status: Governance-confirmed
- Contradictions: None currently recorded
- Unknowns: None
