# Knowledge Projection Rules

This register defines what must happen before raw research material becomes planner-safe knowledge.

## KP-0001 - The planner consumes projections, not raw evidence

- Status: Confirmed
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `ontology/relationships.md`, `ontology/entities.md`
- Rule: The planner should depend on Knowledge Projections derived from verified mechanics and current observations, not directly on raw contradictory evidence.
- Planner implication: A future implementation should have a distinct publication layer between mechanics research and planner runtime.

## KP-0002 - Experimental and disputed mechanics are not silent defaults

- Status: Confirmed
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `planner/planner_safety.md`
- Rule: Experimental or disputed mechanics must not be consumed as if they were confirmed defaults.
- Planner implication: If used at all, they must be explicitly labeled and caveated.

## KP-0003 - Unsupported requests should be blocked, not softened

- Status: Confirmed
- Source: `planner/planner_safety.md`, `planner/decision_support_model.md`
- Rule: A planner should block unsupported facility types, invalid body recommendations, and unsafe demolitions instead of disguising them as low-confidence suggestions.
- Planner implication: Safety filters come before recommendation phrasing.

## KP-0004 - Recommendations must show what would change them

- Status: Confirmed
- Source: `planner/decision_support_model.md`
- Rule: Every recommendation should explain the evidence basis, the obvious alternative, and the conditions that would change the answer.
- Planner implication: Recommendations are decision objects, not one-line commands.

## KP-0005 - Unknown is a valid published state

- Status: Confirmed
- Source: `constitution/project_principles.md`, `ontology/roles_assets_strategies.md`, `planner/planner_safety.md`
- Rule: If the evidence does not support a confident answer, the knowledge projection should remain `Unknown` or recommend live verification.
- Planner implication: Uncertainty is safer than invented precision.

## KP-0006 - Historical evidence should not masquerade as current state

- Status: Confirmed
- Source: `planner/planner_safety.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: Historical observations must be explicitly marked as historical when current live state is unknown.
- Planner implication: The planner should separate current-state knowledge from historical case-study evidence.

## KP-0007 - Contradiction cases can block publication

- Status: Confirmed
- Source: `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: High-severity contradiction cases should remove or downgrade planner-safe publication until reviewed.
- Planner implication: Publication is conditional on unresolved-conflict severity.

## KP-0008 - Planner-safe knowledge is version-aware

- Status: Confirmed
- Source: `docs/knowledge_versioning.md`, `constitution/project_principles.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: Planner-safe knowledge should be tied to knowledge version and patch era where relevant.
- Planner implication: Future planners should declare which knowledge version they consume.

## KP-0009 - Demolition advice requires stronger evidence than additive advice

- Status: Confirmed
- Source: `planner/planner_safety.md`, `planner/decision_support_model.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Rule: Irreversible demolition recommendations require stronger and more direct evidence than additive or observational advice.
- Planner implication: If direct evidence is weak, recommend observation or incremental testing first.

## KP-0010 - Complementary-role strategies must remain contextual

- Status: Confirmed
- Source: `experiments/EXP-0001-a4-complementary-high-tech-role.md`, `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Rule: Strategies such as `Industrial Anchor + High Tech Support Body` are context-dependent knowledge projections, not universal laws.
- Planner implication: Future projections should encode objective, constraints, and coverage assumptions alongside the strategy.
