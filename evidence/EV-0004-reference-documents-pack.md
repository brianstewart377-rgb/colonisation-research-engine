# EV-0004 - Colonisation Reference Documents Pack

## Evidence type

Reference document pack / secondary-source mechanics evidence.

## Source

- Source name: Brian upload in ChatGPT conversation
- Captured/uploaded at: 2026-06-29 conversation session
- Captured by: Brian
- Scope: Elite Dangerous Colonisation mechanics references

## Uploaded files

| Item | File ID | Local path | Notes |
|---|---|---|---|
| Mega Guide | file_00000000076871fdb85d5314524f1502 | /mnt/data/Elite Dangerous Colonization Mega Guide(5).docx | Elite Dangerous Colonization Mega Guide v2.3.0, parsed successfully |
| DaftMav spreadsheet | file_000000008d7c71f89dbcd816bfb2c243 | /mnt/data/Colonization Construction Details (By DaftMav).xlsx | Construction details spreadsheet |
| Strong/Weak Links illustrated reference | file_00000000c0a871fd99b1f72478adeb08 | /mnt/data/Elite_Dangerous_Colonisation_Strong_and_Weak_Links_Illustrated_Reference(2).docx | Parsed successfully; based on Frontier Forums discussion and Brian-supplied screenshots |
| Earlier Frontier forum DOCX | file_00000000f68871fdaef637327be0e280 | /mnt/data/https_forums_frontier_co_uk_threads_colonisation_understanding_s.docx | Imported but text was not readable in parser |
| Dependency flowchart image | file_0000000098d471fd91516087e03bafec | /mnt/data/colonisation-dependency-flowchart-v0-3e1gne4rz0me1.webp | Construction dependency flowchart, March 2025 |

## Evidence role

This pack should be used to extract candidate mechanics, glossary definitions, dependency rules, and planner safety rules.

It should not override live in-game evidence where screenshots, Architect previews, Market Links, or live markets contradict it.

## Recommended evidence hierarchy

1. Live in-game Architect preview.
2. Live in-game Market Links.
3. Live in-game commodity market observations.
4. Direct Frontier source material / in-game Codex / patch notes.
5. Mega Guide and community research references.
6. DaftMav spreadsheet / Raven model.
7. Analyst inference.

## Extraction targets

Initial extraction should focus on:

- Terminology definitions.
- Facility tiers and construction point behaviour.
- Colony-type versus specialised ports.
- Strong and weak link rules.
- Main surface port and main orbital port routing.
- Construction prerequisites.
- Economy inheritance and modifiers.
- Station-class claims that can be compared against live previews.
- Planner safety rules.

## Current status

Originally registered as a reference-document pack record when the repository only had indirect references to the main colonisation source documents.

### Canonical-source update

The repository now contains a committed local `reference_sources/` corpus that serves as the canonical extraction base for this pack:

- `reference_sources/MG-0001-megaguide-v2-3/`
- `reference_sources/FW-0001-strong-weak-links/`
- `reference_sources/DM-0001-daftmav-construction-details/`
- `reference_sources/DD-0001-dependency-flowchart/`

These committed derivatives supersede earlier reliance on transient `/mnt/data` paths, recovered public copies, or partially materialized uploads.

### How this evidence record should be used now

- Use `EV-0004` to explain provenance, source hierarchy, and why these source families matter.
- Use `reference_sources/` as the actual direct extraction base for page, section, file, and sheet-level claim work.
- Continue to treat live in-game evidence as higher authority than these references when conflicts arise.

### Source-family mapping

| Source ID | Meaning | Current repository form |
|---|---|---|
| `MG-0001` | Mega Guide | committed text derivative |
| `FW-0001` | Strong/Weak illustrated reference | committed text derivative |
| `DM-0001` | DaftMav construction details | committed CSV sheet extracts |
| `DD-0001` | Dependency flowchart | committed encoded diagram bundle |
