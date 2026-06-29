# Recommendation Schema Register

This register turns the decision model's expected planner output into an explicit reusable schema.

## Required recommendation fields

Every planner recommendation should include the following fields.

## RS-0001 - Objective being served

- Status: Confirmed
- Source: `planner/decision_support_model.md`
- Requirement: State the player objective explicitly.
- Why it matters: Recommendations cannot be judged without knowing what they optimize.

## RS-0002 - Constraints summary

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `planner/planner_safety.md`
- Requirement: State the constraints that removed invalid or undesirable plans.
- Why it matters: Constraints explain why obvious alternatives were not chosen.

## RS-0003 - Current coverage summary

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `planner/coverage_dimensions_register.md`
- Requirement: Summarize what the colony already provides.
- Why it matters: Planner logic is context-dependent.

## RS-0004 - Coverage gap being targeted

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Requirement: Identify the missing, weak, or unreliable asset the recommendation is trying to improve.
- Why it matters: Prevents random facility selection.

## RS-0005 - Recommended role

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `planner/role_register.md`
- Requirement: State the intended role of the body, station, or facility group.
- Why it matters: Roles sit above individual facilities and explain purpose.

## RS-0006 - Recommended architecture

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `planner/architecture_pattern_register.md`
- Requirement: State the reusable architecture pattern, if any.
- Why it matters: Makes strategy patterns explicit and reviewable.

## RS-0007 - Candidate facilities

- Status: Confirmed
- Source: `planner/decision_support_model.md`
- Requirement: List the actual facility options only after objective, constraints, coverage, role, and architecture are clear.
- Why it matters: Facilities are implementation details, not the reasoning start-point.

## RS-0008 - Expected gains

- Status: Confirmed
- Source: `planner/decision_support_model.md`
- Requirement: State what the recommendation is expected to improve.
- Why it matters: Makes the decision testable.

## RS-0009 - Expected losses or opportunity cost

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Requirement: State what is sacrificed, crowded out, or delayed.
- Why it matters: Prevents one-sided recommendations.

## RS-0010 - Mechanics used

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `mechanics/index.md`
- Requirement: Cite the mechanics the recommendation relies on.
- Why it matters: Lets reviewers challenge specific assumptions.

## RS-0011 - Evidence used

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `evidence/evidence_mechanic_traceability.csv`
- Requirement: Cite the evidence records or observations supporting the recommendation.
- Why it matters: Makes provenance inspectable.

## RS-0012 - Confidence band

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `planner/planner_rules_register.md`, `ontology/confidence_model_register.md`
- Requirement: Label confidence explicitly.
- Why it matters: Uncertainty must be visible to the user.

## RS-0013 - Unknowns

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `docs/unknowns_register.md`
- Requirement: State the unresolved questions that still matter to the recommendation.
- Why it matters: Unknown is safer than false precision.

## RS-0014 - What would change the recommendation

- Status: Confirmed
- Source: `planner/decision_support_model.md`
- Requirement: Explain what new evidence, changed objective, or changed colony state would alter the answer.
- Why it matters: Turns the recommendation into a reviewable decision object.
