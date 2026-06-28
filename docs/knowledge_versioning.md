# Knowledge versioning

Colonisation Research Engine should version knowledge independently from software.

## Why

Mechanics knowledge evolves through evidence, contradiction, and patch drift. A software version alone does not tell researchers what the platform believed at a given moment.

## Proposed format

Use semantic versioning for knowledge snapshots:

- `CRE Knowledge v0.1.0` – Initial ontology and constitution
- `CRE Knowledge v0.2.0` – First verified mechanics
- `CRE Knowledge v0.5.0` – Wregoe experiments incorporated
- `CRE Knowledge v1.0.0` – Community-validated mechanics catalogue

## Versioning triggers

- `MAJOR`: meaningfully changed public interpretation of mechanics or planner-safe knowledge
- `MINOR`: new mechanics, experiments, or validated evidence classes
- `PATCH`: corrections, wording fixes, or metadata improvements that do not materially change knowledge state

## Benefits

- makes the state of knowledge citable
- separates research maturity from application release cadence
- lets future tools declare which knowledge version they are using
