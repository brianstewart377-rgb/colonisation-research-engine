# Phase 2 TRAE Execution Prompt

Work on `brianstewart377-rgb/colonisation-research-engine`.

This is `Phase 2: Complete Knowledge Extraction & Knowledge Base Construction`.

The repository is already checked out locally and is the current working repo.
If it is not present locally, stop and tell me instead of cloning or guessing.
Before making changes, verify the current branch, remotes, and working tree state.

This task is significantly larger than the Evidence Vault MVP.
Assume you have unlimited time.
Optimise for completeness, not speed.
A six-hour analysis is preferable to a thirty-minute summary.

## Mission

Turn every available reference document in the repository into structured knowledge for the Colonisation Research Engine.

This is not a summary.
This is not documentation.
This is not a report.
You are constructing the permanent knowledge base that future planners, analysers, and research tools will use.

## Repository-first scope

Read every available document in the repository, including but not limited to:

- the reference pack metadata in `evidence/EV-0004-reference-documents-pack.md`
- existing mechanics
- existing evidence
- experiments
- architecture
- ontology
- planner rules
- roadmap and governance documents
- templates if they imply canonical field structure

If a named source document from any prompt or evidence record is not actually present in the repository, do not invent it.
Instead:

1. record it as not present
2. continue with all available source material
3. include the absence in the final report

Do not use external web sources unless explicitly requested.
This phase is repository-first extraction and consolidation.

## Read everything

Read every page, paragraph, table, glossary, appendix, figure description, caption, and footnote available in the repository.
Do not skip sections because they appear introductory.

## Extraction goal

Extract everything useful, including:

- gameplay mechanics
- economy inheritance
- economy modifiers
- commodity generation or weighting clues
- body behaviour
- market-link behaviour
- strong and weak links
- construction points
- facility tiers
- unlock chains
- ports, stations, installations, and settlements
- colony development effects
- strategic planner rules
- implicit heuristics
- contradictions
- unknowns
- experiment candidates

## Classification requirements

Every extracted knowledge item must include:

- unique ID
- title
- description
- source
- page number or exact location reference
- section
- confidence
- category
- related mechanics
- planner implications
- testing status
- contradictions
- unknowns

If a source does not have reliable page numbers, do not fabricate page numbers.
Use the best exact location available instead:

- section heading
- table title
- file path
- evidence ID
- experiment ID
- figure or appendix label

## Truth model

Never convert opinion into fact.
Distinguish clearly between:

- `Confirmed`
- `Community supported`
- `Hypothesis`
- `Planner heuristic`
- `Needs verification`
- `Unknown`

## Knowledge graph requirement

Do not create isolated files.
Cross-link:

- mechanics
- glossary terms
- economy rules
- planner rules
- experiments
- evidence
- contradictions
- verification tasks
- architecture patterns

Every mechanic should know what it relates to.

If helpful, create machine-readable graph artifacts such as `nodes.csv` and `edges.csv`.

## Repository improvements

If a better folder structure becomes obvious, implement it.
If indexing is required, implement it.
If missing README or index files would improve navigation, create them.
Prefer improving canonical records over scattering near-duplicates.

## Existing mechanics rule

Review every existing mechanic document.
Merge, expand, correct, and normalize.
Do not preserve duplicate mechanic IDs.
Do not leave competing canonical versions in place.

## Contradictions

Identify contradictions:

- within documents
- between documents
- against existing mechanics
- against existing evidence
- against public-source claims already captured in the repository

Record contradictions.
Do not silently resolve them unless the repository already contains a documented resolution.

## Live verification entries

Whenever the repository evidence is insufficient, create a `Needs Live Verification` entry.
Do not invent results.
Treat uncertainty as a durable work object, not a gap to hide.

## Operating checklist

1. Inventory every repository file that may contain colonisation knowledge.
2. Build a coverage register showing what was processed and what is absent.
3. Normalize mechanic IDs and create a canonical mechanic index.
4. Extract glossary, planner rules, contradictions, and live-verification items.
5. Build graph links between evidence, mechanics, experiments, and planner rules.
6. Create logical commits, not one giant commit.

## Suggested commit split

- source inventory and repository structure
- mechanic catalogue normalization
- glossary and planner rules
- contradiction and live-verification registers
- knowledge graph and navigation improvements

## Git requirements

- commit everything logically
- push with normal `git push`
- if git credentials are unavailable, stop and tell me rather than using an alternate publish path
- do not recreate commits through another API unless explicitly asked

## Final report requirements

Report:

- number of mechanics
- number of glossary entries
- number of planner rules
- number of economy rules
- number of construction rules
- number of contradictions
- number of live experiments required
- number of source documents processed
- coverage estimate for every source document
- full commit SHAs
- any areas that still require manual research

## Quality standard

Assume every commit will be technically reviewed afterward.
The goal is not to summarise the repo.
The goal is to leave the repository materially closer to becoming the definitive research platform for Elite Dangerous Colonisation.

If in doubt:

- extract more
- cross-link more
- preserve provenance
- never lose information
