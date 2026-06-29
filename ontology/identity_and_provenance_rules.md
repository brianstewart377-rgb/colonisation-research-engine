# Identity and Provenance Rules

This register captures the repository's canonical identity and provenance constraints.

## IP-0001 - Facility names are not globally unique

- Status: Confirmed
- Source: `constitution/project_principles.md`, `ontology/entities.md`, `evidence/source_catalog.md`
- Rule: A facility name alone must never be treated as a global identity key.
- Required identity context:
  - system
  - body when known
  - facility type
  - external identifier when available
- Planner implication: Same-name collisions must not silently merge evidence.

## IP-0002 - Identity must be explicit

- Status: Confirmed
- Source: `constitution/project_principles.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: Shared names, narrative references, and shorthand labels do not imply shared identity.
- Planner implication: Uncertain identity resolution should remain unresolved rather than guessed.

## IP-0003 - Evidence is immutable once recorded

- Status: Confirmed
- Source: `constitution/project_principles.md`, `architecture/evidence_vault.md`
- Rule: Observations may be reinterpreted, but raw evidence and source artifacts should not be rewritten.
- Planner implication: Corrections belong in interpretation layers, not by silently overwriting the original trail.

## IP-0004 - Source snapshots should be immutable

- Status: Confirmed
- Source: `architecture/colonisation_intelligence_platform_architecture.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: Each source capture should be stored as an immutable snapshot rather than mutating prior fetches.
- Planner implication: Historical reasoning and contradiction review depend on preserved snapshots.

## IP-0005 - Observations and inferences must remain separate

- Status: Confirmed
- Source: `architecture/evidence_vault.md`, `architecture/colonisation_intelligence_platform_architecture.md`, `constitution/project_principles.md`
- Rule: Direct observation, parsed claim, inferred mechanic, and planner-safe knowledge are different layers and must not be collapsed.
- Planner implication: A tool that consumes raw observations as if they were confirmed mechanics is unsafe by design.

## IP-0006 - Patch era is part of identity for mechanics

- Status: Confirmed
- Source: `constitution/project_principles.md`, `architecture/colonisation_intelligence_platform_architecture.md`, `experiments/README.md`
- Rule: Frontier patches create new evidence eras rather than rewriting history.
- Planner implication: A mechanic can be true in one patch era and unsafe in another.

## IP-0007 - Negative evidence is a first-class provenance object

- Status: Confirmed
- Source: `constitution/project_principles.md`, `experiments/EXP-0000-wregoe-methodology-seed.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: Failed predictions and null effects must remain attached to the mechanic or experiment they challenged.
- Planner implication: Provenance must include why a recommendation became less trusted, not only why it was once supported.

## IP-0008 - Absent primary artifacts must be marked as absent

- Status: Confirmed
- Source: `docs/source_coverage_register.md`, `evidence/EV-0004-reference-documents-pack.md`
- Rule: If a source is represented only by metadata and not by the underlying file, that absence must remain explicit.
- Planner implication: Page-level or table-level extraction claims must not be fabricated from absent artifacts.

## IP-0009 - Review status belongs with evidence objects

- Status: Confirmed
- Source: `templates/evidence_record_template.md`, `architecture/evidence_vault.md`
- Rule: Evidence records should carry review status such as `Unreviewed`, `Analyst reviewed`, `Corroborated`, `Disputed`, or `Superseded`.
- Planner implication: Review maturity should inform downstream trust.
