# Source Authority Register

This register defines how source classes should be treated inside the Colonisation Research Engine.

## SA-0001 - Official mechanics sources are primary for intended rules

- Status: Confirmed
- Source: `evidence/source_catalog.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: Frontier official mechanics pages, patch notes, and official journal documentation are the strongest sources for intended mechanics, terminology, patch drift, and official constraints.
- Planner implication: When community interpretation disagrees with official wording, the official source wins unless direct live evidence disproves implementation behavior.
- Confidence: High

## SA-0002 - Community guides are interpretation, not canonical truth

- Status: Confirmed
- Source: `evidence/source_catalog.md`, `evidence/EV-0004-reference-documents-pack.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: The Mega Guide, DaftMav spreadsheet, Raven references, and similar community artefacts are valuable for heuristics, hypotheses, workflow understanding, and structured reasoning, but they are not canonical truth by themselves.
- Planner implication: Community artefacts can seed mechanics and planner heuristics, but should not override direct live evidence.
- Confidence: High

## SA-0003 - Live in-game evidence outranks secondary references

- Status: Confirmed
- Source: `evidence/EV-0004-reference-documents-pack.md`, `constitution/project_principles.md`
- Rule: Architect previews, live Market Links, commodity market observations, and other direct in-game evidence take priority over reference packs when they conflict.
- Planner implication: The planner must prefer direct current evidence over stale or indirect interpretation.
- Confidence: High

## SA-0004 - Raw source data must remain separate from parsed observations

- Status: Confirmed
- Source: `evidence/source_catalog.md`, `architecture/colonisation_intelligence_platform_architecture.md`, `architecture/evidence_vault.md`
- Rule: Raw source artifacts, parsed observations, inferred mechanics, and planner-safe knowledge must remain separate layers.
- Planner implication: Downstream tools must consume verified projections, not raw contradictory evidence.
- Confidence: High

## SA-0005 - Narrative evidence is allowed but must be confidence-labeled

- Status: Confirmed
- Source: `evidence/source_catalog.md`, `evidence/colonisation_ai_data_sources_review.md`
- Rule: Diaries, forum threads, and narrative reports are useful evidence classes, but their claims must carry confidence and should be corroborated where possible.
- Planner implication: Narrative evidence can support discovery and case studies but should not silently drive automation.
- Confidence: High

## SA-0006 - Facility names are not unique identifiers

- Status: Confirmed
- Source: `evidence/source_catalog.md`, `ontology/entities.md`, `architecture/colonisation_intelligence_platform_architecture.md`
- Rule: Same-name facilities across systems must be treated as possible collisions rather than automatic identity matches.
- Planner implication: System context, body context, and external identifiers matter for resolution.
- Confidence: High

## SA-0007 - EDDN is transport, not a historical warehouse

- Status: Confirmed
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Rule: Raw EDDN should not be treated as a canonical historical store because the live service itself does not provide archive or current-state guarantees.
- Planner implication: EDDN-derived observations require downstream storage or archive pairing.
- Confidence: High

## SA-0008 - Inara public pages are strong manual-validation surfaces, but not a full API source

- Status: Confirmed
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Rule: Inara public system, station, architect, and logbook pages are valuable for manual validation and named examples, but the official Inara API does not expose the full colony-state data needed here.
- Planner implication: Treat Inara as a human-facing validation layer, not the main machine-ingest route.
- Confidence: High

## SA-0009 - Bulk dumps are the strongest public current-state warehouse layer

- Status: Confirmed
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Rule: Spansh dumps and EDSM nightly dumps are the best repository-referenced public bulk sources for systems, bodies, and stations.
- Planner implication: Future system-state warehousing should anchor there before community planner pages.
- Confidence: High

## SA-0010 - Absent artifacts cannot be treated as directly extracted

- Status: Confirmed
- Source: `docs/source_coverage_register.md`, `evidence/EV-0004-reference-documents-pack.md`
- Rule: If a named source artifact is not present in the repository, it may only be represented indirectly via existing notes, derived mechanics, or evidence metadata.
- Planner implication: Do not pretend page-perfect extraction happened from files that are not in the working tree.
- Confidence: High
