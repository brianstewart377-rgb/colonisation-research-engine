# Review Workflow Backlog

This file collects the human-review workflow needs that sit between repository research and future automation.

## RW-0001 - Contradiction triage workflow

- Goal: Review, classify, and disposition contradiction cases without prematurely deleting either side.
- Inputs:
  - `docs/contradiction_register.md`
  - `evidence/claim_register.csv`
  - `evidence/evidence_mechanic_traceability.csv`
- Why it matters: Contradictions are a core knowledge-improving object, not a cleanup nuisance.

## RW-0002 - Identity collision workflow

- Goal: Review same-name facilities, disputed architect attribution, and public correction threads before records are merged or corrected.
- Inputs:
  - `docs/anomaly_register.md`
  - `ontology/identity_and_provenance_rules.md`
  - `evidence/public_anomaly_shortlist.csv`
- Why it matters: Identity collapse is a high-severity planner and provenance risk.

## RW-0003 - Image-backed evidence attachment workflow

- Goal: Attach uploaded screenshots, evidence records, review status, and later binary storage in a repeatable analyst workflow.
- Inputs:
  - `architecture/evidence_vault.md`
  - `docs/governance_decision_register.md`
  - `experiments/README.md`
- Why it matters: The repository already relies on screenshot-backed evidence for several key mechanics.

## RW-0004 - Claim publication review

- Goal: Decide when a claim is ready to be canonicalized into a mechanic, planner rule, or planner-safe projection.
- Inputs:
  - `evidence/claim_register.csv`
  - `evidence/claim_provenance_links.csv`
  - `ontology/confidence_model_register.md`
- Why it matters: The claim layer now exists, but promotion criteria still need operational review.
