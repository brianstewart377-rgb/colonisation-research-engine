# Knowledge Release Workflow

This document defines the repository's intended workflow for producing a versioned knowledge release.

It assumes the repository remains documentation-first and evidence-first.

## Purpose

A knowledge release is the versioned package that future planners, dashboards, or external tools should cite and consume.

It is not the same thing as:

- a software release
- a Git commit
- a raw research dump

## Release stages

## Stage 1 - Evidence and observation readiness

Before a release, the repository should have:

- the relevant evidence records entered
- observations extracted from that evidence
- claims linked to observations and limitations
- contradictions and unknowns updated

Minimum artifacts:

- `evidence/observation_register.csv`
- `evidence/claim_register.csv`
- `docs/contradiction_register.md`
- `docs/unknowns_register.md`

## Stage 2 - Mechanic and rule review

Mechanics and planner rules should be reviewed against current claims and contradictions.

This stage asks:

- which mechanics are stable enough to include
- which should remain withheld
- which should be downgraded
- which are still only experimental

Minimum artifacts:

- `mechanics/index.md`
- `mechanics/economy_rules_register.md`
- `mechanics/construction_rules_register.md`
- `planner/planner_rules_register.md`

## Stage 3 - Governance gate

The release should check the open governance decisions that affect publication quality.

Especially:

- `GD-0001` patch partitioning strategy
- `GD-0002` publication threshold
- `GD-0003` body-linkage representation policy

If these are still unresolved, the release can still happen, but the manifest must say what assumptions were used.

## Stage 4 - Version bump decision

Use the knowledge-versioning rules in `docs/knowledge_versioning.md`.

- `MAJOR`
  materially changed public interpretation of mechanics or planner-safe knowledge
- `MINOR`
  new mechanics, experiments, or validated evidence classes
- `PATCH`
  corrections, wording fixes, metadata, or structure improvements that do not materially change the knowledge state

## Stage 5 - Build release manifest

Create a manifest matching:

- `schemas/knowledge_release_manifest.schema.json`

The manifest should record:

- included mechanics
- included rules
- included unknowns
- withheld items
- source coverage summary
- decision and risk references
- release notes

## Stage 6 - Build export bundle

Assemble a machine-usable release bundle using the structure defined in:

- `docs/release_bundle_layout.md`

The bundle should include:

- the manifest
- canonical exported registers
- graph files
- schema references

## Stage 7 - Validate bundle

Validation should check:

- manifest is valid JSON and matches the schema contract
- referenced export files exist
- withheld items have reasons
- included items have consistent status and confidence labels
- source coverage notes are present when primary artifacts remain absent

## Stage 8 - Publish and cite

Once validated, publish the release as a citable knowledge snapshot.

Future tools should say:

- which `knowledge_version` they use
- which patch family or release window they rely on
- whether they consume only included items or also local working-state artifacts

## Release principles

- Releases should prefer honesty over completeness.
- Unknown items may be included as unknowns rather than hidden.
- Weak or disputed mechanics may be withheld rather than silently published.
- Primary-artifact absence must remain explicit.
- Contradictions should remain visible even when a release chooses one planner-safe default.
