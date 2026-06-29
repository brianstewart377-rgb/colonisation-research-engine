# Objective Register

This register extracts canonical objective types from the decision model.

Objectives are not facilities.
They are the top-level answer to what the player is actually trying to optimize.

## OBJ-0001 - Maximum construction-material coverage

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`
- Description: Maximize the range and usefulness of construction-relevant commodities available across the colony.
- Typical related assets: commodity coverage, economy-shaping coverage, resilience
- Common risks: over-duplicating already-covered production roles

## OBJ-0002 - Maximum mission density

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`
- Description: Maximize mission availability or useful mission mix rather than pure material output.
- Typical related assets: mission coverage, service coverage, population, security
- Common risks: sacrificing construction-material optimization for mission posture

## OBJ-0003 - Maximum local production for bootstrapping

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`
- Description: Maximize early local self-sufficiency for colony growth and build continuity.
- Typical related assets: commodity coverage, construction progression coverage, resilience
- Common risks: overinvesting in self-sufficiency when a complementary architecture would be stronger

## OBJ-0004 - Maximum High Tech coverage

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Description: Maximize High Tech presence or related commodities.
- Typical related assets: High Tech commodities, economy-shaping coverage
- Common risks: High Tech percentage gains may not translate cleanly into missing commodity gains

## OBJ-0005 - Maximum Refinery coverage

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`
- Description: Maximize Refinery-related support where refined-material coverage is weak.
- Typical related assets: Refinery economy support, relevant processed commodities
- Common risks: weak-link assumptions or rank-order uncertainty may overstate expected gains

## OBJ-0006 - Maximum tourism or agriculture missions

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`
- Description: Prioritize tourism- or agriculture-oriented mission usefulness rather than material diversity.
- Typical related assets: mission coverage, service coverage, relevant economy identity
- Common risks: can conflict with metals, industrial, or build-sequencing goals

## OBJ-0007 - Minimum demolition risk

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`, `planner/planner_risk_register.md`
- Description: Avoid irreversible actions unless strongly justified.
- Typical related assets: confidence coverage, resilience, state-certainty
- Common risks: slower optimization or persistence of suboptimal structures

## OBJ-0008 - No cargo-hauling dependency

- Status: Confirmed objective type
- Source: `planner/decision_support_model.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Description: Prefer architectures that do not rely on player cargo hauling.
- Typical related assets: local production, service convenience, resilient coverage
- Common risks: can constrain otherwise powerful strategies
