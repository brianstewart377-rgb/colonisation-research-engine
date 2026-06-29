# Role Register

This register extracts canonical planner roles from the repository's ontology and decision model.

Roles are contextual.
They are not universal prescriptions.

## RL-0001 - Primary Metals Producer

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Provide strong metals-oriented commodity coverage for the wider colony.
- Typical asset focus: Steel, Titanium, Aluminium, Extraction, Refinery, Industrial support
- Best-fit context: When metals remain a live coverage gap.
- Risks: Can over-duplicate already-covered Extraction or Refinery roles.

## RL-0002 - Primary Refinery Producer

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Provide strong Refinery-oriented coverage for processed material availability.
- Typical asset focus: Refinery weighting, metal-processing commodities, related mission support
- Best-fit context: When processed materials remain weak and local support is needed.
- Risks: Weak-link assumptions may overstate actual commodity recovery.

## RL-0003 - Industrial Anchor

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/contextual_strategy_register.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Purpose: Act as the colony's stable Industrial-heavy anchor body.
- Typical asset focus: Industrial coverage, construction-material support, broad production usefulness
- Best-fit context: When one body already has a proven central production role.
- Risks: Can crowd out complementary diversification if copied thoughtlessly.

## RL-0004 - High Tech Support

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/contextual_strategy_register.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Purpose: Complement another body's existing production by adding High Tech-oriented commodity coverage.
- Typical asset focus: Computer Components, Robotics, Auto-Fabricators, Micro Controllers, related market presence
- Best-fit context: When the colony already has strong Extraction, Refinery, or Industrial coverage elsewhere.
- Risks: May fail if High Tech rank changes without meaningful commodity gains.

## RL-0005 - Extraction Support

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Add or reinforce Extraction-related output without making the body the sole colony anchor.
- Typical asset focus: Extraction weighting, support links, commodity recovery
- Best-fit context: When the colony has a targeted metals gap but another body already handles primary production.
- Risks: Can duplicate assets already covered by the primary producer.

## RL-0006 - Tourism Mission Hub

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Improve tourism-oriented missions, services, and economy identity.
- Typical asset focus: Tourism economy, passenger activity, mission mix
- Best-fit context: When player objective prioritizes missions over material coverage.
- Risks: May sacrifice construction-material roles if misapplied.

## RL-0007 - Agriculture Mission Hub

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Improve agriculture-oriented missions and related economy support.
- Typical asset focus: Agriculture economy, mission mix, possible food-related coverage
- Best-fit context: Mission-focused planning contexts.
- Risks: May not align with construction-material objectives.

## RL-0008 - Security Support

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Improve security-related outcomes and supporting mission context.
- Typical asset focus: Security, Military support, strategic colony properties
- Best-fit context: When the colony has a security gap or mission goal requiring it.
- Risks: Can consume slots without helping the current material objective.

## RL-0009 - Research Support

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Support experimentation, mechanic discovery, or uncertain build paths.
- Typical asset focus: Testable differentiation, controlled comparisons, evidence generation
- Best-fit context: When the objective is mechanic discovery rather than direct optimization.
- Risks: May be suboptimal for immediate productivity.

## RL-0010 - Population Driver

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Increase population or related strategic colony properties.
- Typical asset focus: Population, development, wealth, broader strategic growth
- Best-fit context: When strategic colony growth is part of the objective.
- Risks: Can conflict with targeted commodity optimization.

## RL-0011 - Service Hub

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `planner/decision_support_model.md`
- Purpose: Concentrate valuable player-facing services in one location.
- Typical asset focus: Shipyard, Outfitting, Tech Broker, Material Trader, Interstellar Factors, Black Market
- Best-fit context: When the objective is usability or travel convenience.
- Risks: Service concentration may not improve material diversity.

## RL-0012 - Link Repair Candidate

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`
- Purpose: A body or facility group chosen mainly to repair or strengthen market-link behavior elsewhere.
- Typical asset focus: Strong-link creation, weak-link supplementation, spillover shaping
- Best-fit context: When a specific commodity or economy gap appears link-driven.
- Risks: High sensitivity to unresolved routing and threshold mechanics.

## RL-0013 - Experiment Testbed

- Status: Confirmed role concept
- Source: `ontology/roles_assets_strategies.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`
- Purpose: A body or system deliberately used to test mechanics rather than maximize immediate output.
- Typical asset focus: controlled change, clean before/after observation, reproducibility
- Best-fit context: High-uncertainty mechanics needing live verification.
- Risks: Can spend slots on knowledge generation instead of direct utility.
