# Coverage Dimensions Register

This register defines the coverage dimensions the planner should inspect before recommending new facilities.

## CD-0001 - Commodity coverage

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Definition: Which demanded commodities the current colony can reliably source or expose through its existing facilities and links.
- Why it matters: Material bottlenecks and missing categories often matter more than raw facility count.
- Related mechanics: `M-0003`, `M-0006`, `M-0007`, `M-0008`
- Planner use: Check missing construction materials and rare outputs before adding redundant facilities.

## CD-0002 - Service coverage

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Definition: Which player-facing services, market surfaces, and station functions are already present.
- Why it matters: A colony can be economically rich yet still operationally incomplete.
- Related mechanics: `M-0005`, `M-0007`
- Planner use: Measure what functional capability a new port or facility would actually add.

## CD-0003 - Mission and activity coverage

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`
- Definition: Which mission types, loops, or player activity patterns are currently supported by the colony.
- Why it matters: Good planning should improve viable activities, not just static infrastructure.
- Related mechanics: contextual; depends on service and economy state
- Planner use: Match recommendations to the player's actual objective.

## CD-0004 - Economy-shaping coverage

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`
- Definition: The colony's current ability to shape market outcomes through body choice, local facilities, and strong or weak links.
- Why it matters: Some bodies provide leverage rather than direct output.
- Related mechanics: `M-0006`, `M-0007`, `M-0008`
- Planner use: Identify whether a body should be treated as an anchor, support body, spillover source, or neutral site.

## CD-0005 - Construction progression coverage

- Status: Confirmed
- Source: `planner/decision_support_model.md`, `mechanics/M-0004-construction-points-and-facility-tiers.md`
- Definition: The colony's current ability to unlock future builds through construction-point generation and sequencing.
- Why it matters: The next best facility may be the one that unlocks later options rather than the one with the highest standalone value.
- Related mechanics: `M-0004`
- Planner use: Check unlock leverage, not just immediate output.

## CD-0006 - Body-role coverage

- Status: Confirmed
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Definition: Whether each body currently has a clear, non-redundant role inside the colony architecture.
- Why it matters: Colonies degrade when multiple bodies mirror the same role without filling missing gaps.
- Related mechanics: `M-0005`, `M-0006`, `M-0007`, `M-0008`
- Planner use: Prefer complementary roles over accidental duplication.

## CD-0007 - Resilience and redundancy coverage

- Status: Confirmed
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Definition: How robust the colony is if one facility, body, or weak-link dependency fails to deliver the expected outcome.
- Why it matters: Strong performance on paper can still be brittle in practice.
- Related mechanics: `M-0003`, `M-0006`
- Planner use: Flag single-point dependencies and fragile weak-link strategies.

## CD-0008 - Confidence coverage

- Status: Confirmed
- Source: `planner/planner_safety.md`, `ontology/confidence_model_register.md`
- Definition: The trust level of the knowledge supporting each recommendation.
- Why it matters: A colony may appear to have coverage, but only under weak or stale evidence.
- Related mechanics: all
- Planner use: Prefer robustly-supported architectures when player cost of error is high.
