# Source Coverage Register

This register records the repository-local source material processed for Phase 2 knowledge extraction.

## Coverage method

- `100%` means the file was fully reviewed for knowledge extraction or repository-structure implications.
- `Indirect only` means the underlying source artifact is not present in the repository and is only represented by metadata or downstream interpretation.
- `Not present` means the source is named in repository evidence but the actual artifact is absent from the working tree.

## Repository-local sources processed

| Source path | Type | Coverage | Notes |
|---|---|---:|---|
| `README.md` | Repository overview | 100% | Defines project purpose, scope, and layout. |
| `constitution/project_principles.md` | Governance | 100% | Core evidence-first principles and research commitments. |
| `architecture/README.md` | Architecture index | 100% | Sets boundary for architecture documents. |
| `architecture/colonisation_intelligence_platform_architecture.md` | Architecture | 100% | Core layer model, confidence model, contradiction handling, and data entities. |
| `architecture/evidence_vault.md` | Architecture | 100% | Evidence lifecycle and evidence/observation separation. |
| `docs/community_discussions.md` | Governance | 100% | Discussion-vs-issue split and research-conversation model. |
| `docs/knowledge_versioning.md` | Governance | 100% | Knowledge-versioning rules. |
| `docs/project_roadmap.md` | Roadmap | 100% | Phase structure and repository maturity path. |
| `evidence/colonisation_ai_data_sources_review.md` | Source review | 100% | Main source hierarchy, confidence model, ingestion order, and external-source gap analysis. |
| `evidence/source_catalog.md` | Source catalog | 100% | Source families and handling rules. |
| `evidence/EV-0001-rocha-liberty-post-high-tech-build.md` | Evidence record | 100% | Post-build A4 High Tech observations. |
| `evidence/EV-0002-wregoe-raven-proposed-build-review.md` | Evidence record | 100% | Raven proposed-build interpretation and placeholder-name rules. |
| `evidence/EV-0003-a4-t3-station-selection-previews.md` | Evidence record | 100% | Station-class and layout-preview comparison evidence. |
| `evidence/EV-0004-reference-documents-pack.md` | Evidence record | 100% | Metadata for absent reference-pack artifacts and evidence hierarchy. |
| `experiments/README.md` | Process doc | 100% | Scientific workflow and required experiment fields. |
| `experiments/EXP-0000-wregoe-methodology-seed.md` | Experiment | 100% | Seed methodology, negative evidence, and first three mechanics. |
| `experiments/EXP-0001-a4-complementary-high-tech-role.md` | Experiment | 100% | Active A4 High Tech experiment definition. |
| `mechanics/README.md` | Mechanic catalogue guidance | 100% | Canonical mechanic-document expectations. |
| `mechanics/M-0001-water-worlds-have-no-surface-slots.md` | Mechanic | 100% | Confirmed Wregoe body-slot constraint. |
| `mechanics/M-0002-station-economy-is-inherited.md` | Mechanic | 100% | Confirmed planner-safety rule on economy inheritance. |
| `mechanics/M-0003-one-weak-refinery-link-is-insufficient-to-restore-metals.md` | Mechanic | 100% | Confirmed narrow negative-evidence mechanic. |
| `mechanics/M-0001-construction-points-and-facility-tiers.md` | Mechanic draft | 100% | Reviewed and marked for ID normalization into canonical catalogue. |
| `mechanics/M-0002-colony-type-and-specialised-ports.md` | Mechanic draft | 100% | Reviewed and marked for ID normalization into canonical catalogue. |
| `mechanics/M-0003-strong-and-weak-link-routing.md` | Mechanic draft | 100% | Reviewed and marked for ID normalization into canonical catalogue. |
| `mechanics/M-0004-colony-port-economy-inheritance.md` | Mechanic draft | 100% | Reviewed and marked for canonical renumbering. |
| `mechanics/M-0005-local-body-base-economies-and-modifiers.md` | Mechanic draft | 100% | Reviewed and marked for canonical renumbering. |
| `ontology/entities.md` | Ontology | 100% | Core entities. |
| `ontology/relationships.md` | Ontology | 100% | Core graph edges and relationship rules. |
| `ontology/roles_assets_strategies.md` | Ontology / planning | 100% | Role, asset, strategy, and coverage vocabulary. |
| `planner/decision_support_model.md` | Planner model | 100% | Objective-first reasoning and contextual strategy rules. |
| `planner/planner_safety.md` | Planner safety | 100% | Mandatory recommendation constraints. |
| `schemas/README.md` | Schema index | 100% | Future schema scope. |
| `schemas/evidence_vault_schema.sql` | Schema | 100% | Evidence-vault implementation schema, used mainly for evidence-layer context. |
| `templates/evidence_record_template.md` | Template | 100% | Evidence-field expectations and provenance conventions. |
| `templates/experiment_template.md` | Template | 100% | Experiment-field expectations. |
| `templates/mechanic_template.md` | Template | 100% | Canonical mechanic-document structure. |
| `tools/README.md` | Tooling scope | 100% | Confirms tooling-vs-repository boundary. |
| `tools/evidence_vault/README.md` | Tooling doc | 100% | Evidence registration workflow and managed-storage assumptions. |

## Referenced source artifacts not present locally

These artifacts are named in repository evidence but are not present as local files in the working tree.

| Named artifact | Repository reference | Working-tree status | Usable coverage |
|---|---|---|---|
| `Elite Dangerous Colonization Mega Guide v2.3.0` | `evidence/EV-0004-reference-documents-pack.md` | Not present | Indirect only via existing repository mechanics and source-review notes |
| `Colonization Construction Details (By DaftMav).xlsx` | `evidence/EV-0004-reference-documents-pack.md` | Not present | Indirect only via source-review notes and existing mechanic drafts |
| `Elite Dangerous Colonisation Strong and Weak Links Illustrated Reference` | `evidence/EV-0004-reference-documents-pack.md` | Not present | Indirect only via existing mechanic drafts and EV-0004 metadata |
| Earlier Frontier forum DOCX import | `evidence/EV-0004-reference-documents-pack.md` | Not present | Not usable beyond EV-0004 note that the parser could not read it |
| Dependency flowchart image | `evidence/EV-0004-reference-documents-pack.md` | Not present | Indirect only via EV-0004 note and source-review references |

## Extraction limitation

Phase 2 can fully consolidate repository-local knowledge.
It cannot honestly claim direct extraction from the absent reference-pack artifacts until those files are checked into the repository or reattached as evidence inputs.
