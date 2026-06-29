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

Originally registered as source evidence with the expectation of direct local access to the Mega Guide, DaftMav spreadsheet, Strong/Weak illustrated reference, and dependency flowchart image.

### 2026-06-29 extraction update

During the later direct-extraction pass, the originally referenced `/mnt/data` copies were no longer present.

Direct extraction therefore proceeded from:

- recovered public copies of the Mega Guide;
- recovered DaftMav-derived reference tables;
- repository-local evidence already in this directory;
- user-uploaded secondary PDFs and routing graphics that were actually present in `/workspace/.uploads`.

### Files actually present in `/workspace/.uploads` during the pass

The following uploaded items were confirmed present and readable:

- `631ba045-3366-4fe0-8322-a320166fa5cb_Colonisation_ Economy and Expansion _ AetherWave Research Portal.pdf`
- `097d94a8-b373-485b-9b76-885677eeaa7c_Colonisation_ Advanced Strategies _ AetherWave Research Portal.pdf`
- `d42e5790-820c-42c4-af47-494900e81212_Colonisation_ Building Your Colony _ AetherWave Research Portal.pdf`
- `cd596385-d3b5-4cb1-9175-df2456fbbb4f_Colonisation_ Construction Process _ AetherWave Research Portal.pdf`
- `cb056bcd-0425-4ab9-8999-a20170cb08d2_System Colonisation _ Elite Dangerous Wiki _ Fandom.pdf`
- `1793dec9-81d5-470e-8bd4-1d7c4df4858a_Strong Graphic.png`
- `7898eff8-45bf-4e31-94a3-0aece981739f_Strong and Weak Graphic Diag B.png`
- `177b682e-5d30-43f9-a736-fc2a2e861cc2_Strong and Weak Graphic Diag H1.png`
- `cee6281f-d631-4c17-9501-f7d779b6d706_Strong and Weak Graphic Diag F1.png`
- `6d391ece-4a35-4846-8316-ead5d4d4540a_Strong and Weak Graphic Diag E.png`
- `319fc635-3ec8-4cf0-88b5-21fb8a8e200d_Strong and Weak Graphic Diag D-3.png`
- `aa2a469a-2c1c-4ef3-a247-c76360ac4ee2_Strong and Weak Graphic Diag C.png`
- `47bcbd7d-f5da-4dd9-adbb-5511922350f1_Strong and Weak Graphic Diag A.png`
- `894df128-7f77-4aea-aad4-5acea3ff2844_Colonisation Linking Infographic 1.jpg`

### Uploaded items named by the host but not materialized on disk

The following files were named in the upload notice for the session, but were not present in `/workspace/.uploads` when checked programmatically:

- `Elite Dangerous Colonization Mega Guide.docx`
- `Copy of Colonization Construction v3 (By DaftMav)(2).xlsx`
- `Colonisation_ Understanding Strong And Weak Links _ Frontier Forums.pdf`
- `OASIS Guide for Bootstrapping a Bubble.docx`

These should not be treated as direct local sources for this pass unless they are re-uploaded successfully in a later session.
