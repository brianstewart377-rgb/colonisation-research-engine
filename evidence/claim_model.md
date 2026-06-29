# Claim Model

This register explains how claims should be represented in the repository.

Claims sit between raw observations and higher-order mechanics, planner rules, or strategy patterns.

## Why claims exist

The repository already distinguishes:

- raw evidence
- structured observations
- mechanics
- planner-safe knowledge

Claims are the missing bridge when one or more observations support a meaningful statement, but that statement still needs provenance, limitations, and explicit qualification before it becomes a canonical mechanic or planner rule.

## Claim fields

Each claim should record:

- `claim_id`
- `claim_type`
- `status`
- `confidence`
- `title`
- `claim_text`
- `primary_basis`
- `linked_mechanics`
- `linked_contradictions`
- `linked_unknowns`

## Provenance links

Claim provenance should be explicit rather than compressed into one text field.

Useful relationship types include:

- `supported_by`
- `produced_by`
- `derived_from`
- `canonicalized_as`
- `qualified_by`
- `limited_by`
- `uses_baseline`
- `predicted_by`
- `informs`

## Status guidance

- `Observed`
  A direct evidence-backed claim that has not yet been elevated into a canonical mechanic.
- `Confirmed`
  A claim that is strong enough to anchor a canonical mechanic or planner rule.
- `Confirmed_Narrow`
  Strong inside a specific documented scope, but unsafe to generalize.
- `Pending`
  An experimental prediction or unresolved claim awaiting validation.

## Use rule

Future ingestion and review tooling should be able to answer:

- what exactly is being claimed
- which observations support it
- which evidence artifacts produced those observations
- what contradicts or limits it
- whether it has been canonicalized into a mechanic or remains provisional
