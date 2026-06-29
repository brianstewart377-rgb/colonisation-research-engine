# Contextual Strategy Register

This register captures strategy patterns that appear in the current repository.

These are not universal laws.
They are contextual patterns whose validity depends on objective, body context, existing coverage, and evidence strength.

## CS-0001 - Industrial Anchor plus High Tech Support Body

- Status: Experimental but promising
- Source: `experiments/EXP-0001-a4-complementary-high-tech-role.md`, `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`, `evidence/EV-0001-rocha-liberty-post-high-tech-build.md`
- Pattern: Keep a strong Industrial anchor on one body while using a second body to raise High Tech presence and complementary commodity coverage.
- Best-fit context:
  - one body is already a proven industrial producer
  - the second body has room to fill missing commodity coverage rather than duplicate the anchor
  - the player objective is whole-colony supply improvement rather than single-body purity
- Planner implications:
  - evaluate complementarity, not just maximize a single economy everywhere
  - protect the anchor role while testing the support role
- Related mechanics: `M-0002`, `M-0006`, `M-0007`, `M-0008`
- Related evidence: `EV-0001`, `EXP-0001`
- Unknowns: Exact material-coverage gain from the High Tech promotion

## CS-0002 - Prefer local same-body shaping before remote spillover

- Status: Likely
- Source: `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md`, `mechanics/M-0006-strong-and-weak-link-routing.md`, `planner/decision_support_model.md`
- Pattern: When a target commodity or economy gap matters, try to create local strong support on the same body before relying on remote weak-link spillover.
- Best-fit context:
  - target outcome is narrow and important
  - weak-link-only evidence is thin or contradictory
- Planner implications:
  - strong links are the default route for dependable repair
  - weak-link repairs should remain experimental until verified
- Related mechanics: `M-0003`, `M-0006`
- Related evidence: `EV-0001`, `EV-0002`
- Unknowns: Threshold at which spillover becomes sufficient

## CS-0003 - Use under-utilized bodies to fill gaps, not mirror the strongest body

- Status: Confirmed as a planning pattern
- Source: `planner/decision_support_model.md`, `ontology/roles_assets_strategies.md`, `experiments/EXP-0001-a4-complementary-high-tech-role.md`
- Pattern: When one body already carries a strong role, another body should usually be evaluated as a gap-filling complement rather than a duplicate.
- Best-fit context:
  - the colony already has a clear anchor body
  - another body has different body traits, orbit context, or remaining build options
- Planner implications:
  - ask what the body can add, not what it can imitate
  - duplication must be justified by resilience or scale needs
- Related mechanics: contextual, especially `M-0005`, `M-0007`, `M-0008`
- Related evidence: `EXP-0001`
- Unknowns: When deliberate duplication becomes superior to complementarity

## CS-0004 - Demolition is a late-stage strategy, not a first response

- Status: Confirmed as a planner-safety pattern
- Source: `planner/planner_safety.md`, `planner/decision_support_model.md`, `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Pattern: When evidence is weak or the model may be conflating current and projected states, observation and additive testing should come before demolition recommendations.
- Best-fit context:
  - projected deficits or weak-link concerns exist
  - the planner lacks direct proof that demolition improves the target outcome
- Planner implications:
  - irreversible actions need stronger evidence
  - recommend validation and local inspection first
- Related mechanics: `M-0004`, `M-0006`
- Related evidence: `EV-0002`
- Unknowns: Which demolition cases can ever be made planner-safe without direct live evidence
