# Manual Research Gaps

This register converts the repository's identified source gaps into a durable manual-research backlog.

## Gap severity guide

- `Critical`: blocks strong automation or canonical interpretation
- `High`: materially limits confidence or planner safety
- `Medium`: important, but does not block current structured knowledge work

## MRG-0001 - No official public bulk export of full colonised-system layout state

- Severity: Critical
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: No official public export was found that exposes full colonised-system layout state in one authoritative package.
- Why it matters: Future system-state tooling must reconcile multiple sources instead of trusting one canonical feed.
- Suggested response: Keep manual-review layers and explicit provenance.

## MRG-0002 - No official API exposing architect, live facility graph, and completed layout together

- Severity: Critical
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: The repository source review found no official API that exposes system architect, live facility graph, and completed colony layout together.
- Why it matters: Identity resolution and layout truth remain partly indirect.
- Suggested response: Preserve architect claims, screenshot evidence, and anomaly queues separately.

## MRG-0003 - Inara pages are strong for validation but not a full machine-ingest layer

- Severity: High
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: Inara public pages are valuable, but the official API explicitly excludes the needed galaxy, station, and market outputs.
- Why it matters: Tools must separate human-validation workflows from automated ingestion.
- Suggested response: Maintain manual-validation registers and named-system shortlists.

## MRG-0004 - EDDN requires archive pairing

- Severity: High
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: EDDN is live transport only and cannot act as a historical warehouse by itself.
- Why it matters: Replayable evidence and contradiction review need stored snapshots or archive sources.
- Suggested response: Pair future EDDN ingestion with downstream storage or ED Galaxy Data-style archives.

## MRG-0005 - Journal files do not cleanly expose every finished-facility and body linkage

- Severity: High
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: Journal files appear incomplete for some finished-facility/body linkage cases, especially orbital and post-completion states.
- Why it matters: Automated layout graphs may remain partially inferential.
- Suggested response: Preserve uncertainty and support screenshot-backed correction workflows.

## MRG-0006 - Fleet-carrier cargo visibility is incomplete

- Severity: Medium
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: Fleet-carrier cargo remains partially opaque in journals unless sale-state conditions expose it.
- Why it matters: Hauling-state tooling may be incomplete.
- Suggested response: Treat cargo logistics as a partial-evidence workflow.

## MRG-0007 - Public screenshot archives are fragmented

- Severity: High
- Source: `evidence/colonisation_ai_data_sources_review.md`, `architecture/evidence_vault.md`
- Problem: Completed-colony screenshot archives are fragmented across forums, logbooks, spreadsheets, and chat uploads rather than stored centrally.
- Why it matters: High-value evidence remains easy to lose without deliberate registration.
- Suggested response: Continue building the Evidence Vault and preserve screenshot-backed evidence as first-class objects.

## MRG-0008 - Licensing for some community tools and spreadsheets remains unclear

- Severity: Medium
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Problem: Several community tools and spreadsheets do not have sufficiently explicit redistribution terms for unquestioned bulk reuse.
- Why it matters: Future ingestion or redistribution work may need case-by-case review.
- Suggested response: Keep source-family metadata and licence status explicit.

## MRG-0009 - OCR and screenshot-review pipeline remains unbuilt

- Severity: High
- Source: `evidence/colonisation_ai_data_sources_review.md`, `architecture/evidence_vault.md`
- Problem: A robust OCR and screenshot-review pipeline is still missing.
- Why it matters: Player-submitted image evidence cannot yet be scaled reliably.
- Suggested response: Preserve image evidence now; automate later without rewriting the evidence trail.

## MRG-0010 - Patch drift threatens community guides

- Severity: High
- Source: `evidence/colonisation_ai_data_sources_review.md`, `constitution/project_principles.md`
- Problem: Community guides can remain useful for interpretation while drifting behind later balance changes.
- Why it matters: Secondary references can become silently stale.
- Suggested response: Keep patch-era context attached to mechanics and confidence.

## MRG-0011 - Original binaries are not committed alongside the canonical source pack

- Severity: Critical
- Source: `docs/source_coverage_register.md`, `evidence/EV-0004-reference-documents-pack.md`
- Problem: The repository now contains committed canonical derivatives in `reference_sources/`, but not every original binary source artifact is committed alongside them.
- Why it matters: Provenance is now workable for extraction, but binary-level archival completeness is still weaker than canonical-derivative completeness.
- Suggested response: Keep `reference_sources/` as the operational source base and optionally add original binaries later if archival completeness becomes important.
