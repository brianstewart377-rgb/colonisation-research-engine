# Colonisation Research Engine

Colonisation Research Engine is a long-term evidence-backed research platform for understanding Elite Dangerous Colonisation mechanics, experiments, contradictions, and future AI planning.

This repository is not simply an AI planner. It exists to preserve raw evidence, structure observations, test mechanics, retain failed experiments, and publish planner-safe knowledge only after it has survived scrutiny.

## Philosophy

- Evidence first
- Mechanics evolve
- Failed experiments matter
- Contradictions improve knowledge
- Planners consume verified knowledge only

## What this repository is

- A knowledge foundation for colonisation research
- A home for mechanics documents, experiments, ontology design, and evidence governance
- A future source of truth for planners, research dashboards, and AI-assisted tools

## What this repository is not

- Not the `ed-finder.app` repository
- Not a production application
- Not a database implementation
- Not a Docker or deployment project
- Not a prompt collection

## Research stance

Colonisation behaviour should be treated as mechanics under observation, not fixed rules. Mechanics can be confirmed, disputed, experimental, disproved, or patch-sensitive. Unknown is an acceptable answer when evidence is weak.

## Knowledge versioning

This project should version knowledge independently of any future software implementation.

Examples:

- `CRE Knowledge v0.1.0` – Initial ontology and constitution
- `CRE Knowledge v0.2.0` – First verified mechanics
- `CRE Knowledge v0.5.0` – Wregoe experiments incorporated
- `CRE Knowledge v1.0.0` – Community-validated mechanics catalogue

This makes the state of knowledge citable even when multiple tools or applications eventually consume it.

## Discussions and issues

Issues are for work items.
Discussions should eventually be enabled for open research, mechanic challenges, contradictory evidence, and community submissions such as:

- “I think I found a new mechanic.”
- “This contradicts Mechanic M-014.”
- “Here is an experiment result from a recent patch.”

If GitHub Discussions are not enabled yet, this repository is still structured so that they can become part of the research workflow later.

## Initial foundation

The repository begins with:

- project constitution
- ontology and relationship model
- evidence source catalog
- experiment workflow
- planner safety rules
- platform architecture
- knowledge roadmap

## Knowledge base entry point

Use `docs/knowledge_base_index.md` as the main index for the current structured knowledge base, counts, canonical registers, and navigation into mechanics, evidence, planner rules, ontology, contradictions, and live-verification work.

## Repository layout

- `constitution/` – project principles and research governance
- `architecture/` – platform architecture and system design documents
- `ontology/` – entities and relationship model
- `mechanics/` – one document per mechanic over time
- `experiments/` – scientific workflow and experiment records
- `evidence/` – source catalog and evidence strategy
- `planner/` – planner safety and knowledge-consumption constraints
- `schemas/` – future schema contracts and structured formats
- `tools/` – supporting research-tooling documentation
- `docs/` – roadmap and supporting project docs
