# Unknowns Register

This register consolidates the most important unresolved knowledge gaps already present across the repository.

## U-0001 - Economy percentages to commodity exposure

- Category: Economy
- Source: `mechanics/M-0002-station-economy-is-inherited.md`, `mechanics/M-0007-colony-port-economy-inheritance.md`, `planner/planner_rules_register.md`
- Unknown: How inherited economy percentages are transformed into final commodity availability at different station types.
- Related mechanics: `M-0002`, `M-0007`
- Related live verification: `LV-0001`, `LV-0002`
- Planner implication: Commodity predictions must remain confidence-labeled.

## U-0002 - Rank order versus absolute percentage

- Category: Economy
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Unknown: Whether top-two economy rank matters more than absolute percentage for commodity appearance.
- Related mechanics: `M-0003`, `M-0006`, `M-0007`
- Related live verification: `LV-0001`, `LV-0003`
- Planner implication: Avoid overfitting to displayed percentages alone.

## U-0003 - Station-class post-build divergence

- Category: Port behavior
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`, `evidence/EV-0003-a4-t3-station-selection-previews.md`, `docs/contradiction_register.md`
- Unknown: Whether Orbis, Ocellus, Dodec, or other port classes diverge meaningfully after completion even when previews look equivalent.
- Related mechanics: `M-0005`, `M-0007`
- Related live verification: `LV-0002`
- Planner implication: Station-class optimization remains provisional.

## U-0004 - Specialised-port exemption depth

- Category: Port behavior
- Source: `mechanics/M-0005-colony-type-and-specialised-ports.md`
- Unknown: Which specialised port classes are fully exempt from local-body economy inheritance and which only partially resist it.
- Related mechanics: `M-0005`, `M-0007`
- Related live verification: `LV-0002`
- Planner implication: Port taxonomy should remain cautious until class-specific confirmation exists.

## U-0005 - Weak-link sufficiency threshold

- Category: Market links
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`, `docs/contradiction_register.md`
- Unknown: How much weak-link support is required before a targeted commodity outcome becomes reliable.
- Related mechanics: `M-0003`, `M-0006`
- Related live verification: `LV-0003`
- Planner implication: Weak-link-only recommendations should remain experimental.

## U-0006 - Main-port routing aggregation behavior

- Category: Market links
- Source: `mechanics/M-0006-strong-and-weak-link-routing.md`, `planner/planner_rules_register.md`
- Unknown: Whether visible Market Links aggregate upstream contributions through main surface and orbital ports rather than displaying direct one-to-one causality.
- Related mechanics: `M-0006`
- Related live verification: `LV-0005`
- Planner implication: Link-screen interpretation remains provisional.

## U-0007 - Body-modifier stacking behavior

- Category: Body economics
- Source: `mechanics/M-0008-local-body-base-economies-and-modifiers.md`, `mechanics/economy_rules_register.md`
- Unknown: Whether rings, organics, geological activity, and similar modifiers stack with base body economies or with each other.
- Related mechanics: `M-0008`
- Related live verification: `LV-0004`
- Planner implication: Avoid silent double-counting in economy models.

## U-0008 - Terraforming modifier role

- Category: Body economics
- Source: `mechanics/M-0008-local-body-base-economies-and-modifiers.md`
- Unknown: Whether Terraforming acts only as a modifier-style influence or can dominate final port behavior in some contexts.
- Related mechanics: `M-0008`
- Related live verification: future work required
- Planner implication: Terraforming assumptions should remain weak until directly evidenced.

## U-0009 - Construction-point edge cases beyond current-versus-proposed interpretation

- Category: Construction
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `docs/contradiction_register.md`
- Unknown: Whether every planner-visible negative CP state is explained by proposal-state conflation or whether deeper edge cases exist.
- Related mechanics: `M-0004`
- Related live verification: future comparative cases
- Planner implication: Avoid universalizing the Raven interpretation without more examples.

## U-0010 - Initial Primary Port exception scope

- Category: Construction
- Source: `mechanics/M-0004-construction-points-and-facility-tiers.md`, `mechanics/construction_rules_register.md`
- Unknown: Whether there are additional port exceptions beyond the initial Primary Port case, and whether all initial-port classes behave identically.
- Related mechanics: `M-0004`
- Related live verification: future construction-sequencing work
- Planner implication: Initial-port logic should remain explicit and caveated.

## U-0011 - Body-linked public evidence granularity

- Category: Evidence architecture
- Source: `architecture/colonisation_intelligence_platform_architecture.md`
- Unknown: What the best representation is when public evidence confirms facility existence but not exact orbital/body linkage.
- Related mechanics: cross-cutting
- Related live verification: analyst workflow and future tooling design
- Planner implication: Identity and body assignment may remain partly unresolved in public-only workflows.

## U-0012 - Publication threshold for planner-safe knowledge

- Category: Knowledge governance
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `ontology/confidence_model_register.md`
- Unknown: What precise confidence threshold is sufficient before a mechanic is published into planner-safe knowledge.
- Related mechanics: all
- Related live verification: governance decision rather than live test
- Planner implication: Publication policy should remain explicit and versioned.
