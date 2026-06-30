# Governance Decision Register

This register turns the repository's open governance questions into explicit decisions-to-be-made.

These are not resolved decisions yet.
They are canonical governance work items.

## GD-0001 - Patch partitioning strategy for planner knowledge

- Status: Open
- Source: `architecture/colonisation_intelligence_platform_architecture.md`
- Decision to make: Should planner-safe knowledge be version-partitioned primarily by patch family, by time window, or by a hybrid model?
- Why it matters: Mechanics can stay historically true while becoming unsafe for current planning after a patch.
- Related unknowns: `U-0012`
- Blocking impact: High

## GD-0002 - Publication threshold for planner-safe knowledge

- Status: Open
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `ontology/confidence_model_register.md`
- Decision to make: What confidence threshold or evidence pattern is sufficient before a mechanic can be published into planner-safe knowledge?
- Why it matters: The repository currently has confidence bands, but not a final publication gate.
- Related unknowns: `U-0012`
- Blocking impact: High

## GD-0003 - Body-linkage representation policy

- Status: Open
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `docs/unknowns_register.md`
- Decision to make: How should the system represent outcomes when public evidence confirms facility existence but not exact orbital or body linkage?
- Why it matters: Identity and body assignment can remain partly unresolved in public-only workflows.
- Related unknowns: `U-0011`
- Blocking impact: High

## GD-0004 - Human review surface for contradictions and identity collisions

- Status: Open
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `docs/anomaly_register.md`
- Decision to make: What is the best human-facing review surface for contradiction cases, identity collisions, and correction workflows?
- Why it matters: The repository already accumulates contradiction and anomaly objects that future tooling will need to review safely.
- Related risks: `R-0006`, `R-0007`
- Blocking impact: Medium-High

## GD-0005 - Analyst-side workflow for image-backed evidence before production screenshot ingestion

- Status: Open
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `docs/manual_research_gaps.md`, `architecture/evidence_vault.md`
- Decision to make: What is the canonical analyst workflow for attaching screenshots and image-backed evidence while production OCR and screenshot ingestion remain unbuilt?
- Why it matters: High-value evidence is already arriving in screenshots, but the repository still lacks a final operating workflow.
- Related risks: `R-0009`
- Blocking impact: High
