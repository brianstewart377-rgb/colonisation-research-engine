# Colonisation AI Data Sources Review

Prepared for Brian and ChatGPT before any implementation work begins.

Date: `2026-06-28`

## Overview

This review prioritises public sources that are either official, openly downloadable, or consistently reusable for manual validation. The strongest first-ingestion stack is:

1. Frontier official colonisation mechanics sources
2. Official and community-maintained journal schemas
3. Spansh dumps
4. EDSM nightly dumps
5. EDDN live stream plus ED Galaxy Data archives
6. Inara public colony/system pages for validation and named examples

The weakest evidence class is anecdotal discussion without exports, snippet-only community posts, mirrors that disagree with official text, and tools that infer layouts from incomplete journal data.

## Method

- Only sources found during this research pass are included.
- `UNKNOWN` means the claim could not be verified from a public source during this pass.
- “Download/export/API accessed” is only marked positively where there is explicit evidence.
- Many sources fit more than one category; each source is listed once in its primary category.
- Public availability does not automatically mean redistribution rights are clear. Where no explicit licence was found, licensing is marked `UNKNOWN`.

## A. Core mechanics sources

### Frontier official System Colonisation Guide

- Source name: `Frontier official System Colonisation Guide`
- URL: <https://www.elitedangerous.com/news/system-colonisation-guide>
- Source type: Official mechanics guide
- Public/reusable status: Public web page. Reusable for rules extraction. Bulk redistribution terms `UNKNOWN`.
- Data available: Claim flow, 15 ly claim radius, primary port choices, colony build flow, facility classes, reward model, system architect role.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Web page only. No bulk export evidenced.
- Suggested ingestion method: Hand-curated mechanics rules table with version stamp.
- Trust rating: `High`
- Why it matters for the colonisation AI: Best high-level official description of the intended gameplay loop and the canonical terms Frontier uses.
- Caveats, licensing, or reliability concerns: Not machine-readable and not sufficient by itself for economy/link math.

### Frontier Trailblazers update notes `4.1.0.0`

- Source name: `Frontier Trailblazers update notes 4.1.0.0`
- URL: <https://www.elitedangerous.com/update-notes/4-1-0-0>
- Source type: Official release notes
- Public/reusable status: Public web page
- Data available: Claim registration, 24-hour claim window, primary-port construction flow, system colonisation ship, facility placement overview.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Versioned mechanics changelog source
- Trust rating: `High`
- Why it matters for the colonisation AI: Establishes the launch-state mechanics and original assumptions that some community tools still embed.
- Caveats, licensing, or reliability concerns: Some launch-state behaviour was later changed by patches.

### Frontier update notes `4.1.2.0` (`Update 3`)

- Source name: `Frontier Trailblazers Update 3 patch notes`
- URL: <https://www.elitedangerous.com/update-notes/4-1-2-0>
- Source type: Official balance and mechanics patch notes
- Public/reusable status: Public web page
- Data available: Strong links, weak links, port vs supporting facility classes, body-based overrides, economy boosts/decreases, population growth changes.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Structured mechanics reference for link rules, overrides, and patch-era assumptions
- Trust rating: `High`
- Why it matters for the colonisation AI: This is the single most important official source for market-link reasoning and economy inheritance logic.
- Caveats, licensing, or reliability concerns: Some downstream community guides still reflect pre- or post-patch interpretations differently; keep patch version attached.

### Frontier Dodec update notes `4.2.2.0`

- Source name: `Frontier Dodec update notes 4.2.2.0`
- URL: <https://www.elitedangerous.com/update-notes/4-2-2-0>
- Source type: Official late-beta / post-beta colonisation update notes
- Public/reusable status: Public web page
- Data available: Dodec construction rights, human tech broker availability, reweighting of development/security/wealth/tech effects, refinery-contact requirement, industrial economy change.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Later-mechanics delta source
- Trust rating: `High`
- Why it matters for the colonisation AI: Important for any planner that wants to avoid baking in stale assumptions about system stats, refinery contacts, or Dodec unlocks.
- Caveats, licensing, or reliability concerns: Community guides may lag this patch.

### Frontier Galnet colonisation release article

- Source name: `Frontier Galnet colonisation release article`
- URL: <https://www.elitedangerous.com/en-US/news/galnet/system-colonisation-equipment-reaches-public-market>
- Source type: Official lore/news article
- Public/reusable status: Public web page
- Data available: Public launch timing, framing of colonisation contacts and claim process, intended player-facing positioning.
- Whether it has real system names: `Yes` (`Minerva`, `Starlace Station`)
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Context-only reference, not a core data feed
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Useful for timeline context and release-state provenance.
- Caveats, licensing, or reliability concerns: Mostly narrative, not a rules source.

### Official Player Journal Manual `v32`

- Source name: `Official Player Journal Manual v32`
- URL: <https://hosting.zaonce.net/community/journal/v32/Journal_Manual-v32.pdf>
- Source type: Official file/schema documentation
- Public/reusable status: Public PDF
- Data available: Journal file format, `Market.json`, `Outfitting.json`, `Shipyard.json`, `Status.json`, journal storage location, event structure.
- Whether it has real system names: `Example only`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Downloadable PDF; game-generated files documented
- Suggested ingestion method: Source-of-truth schema reference for local evidence capture
- Trust rating: `High`
- Why it matters for the colonisation AI: Defines the official local files and event model that downstream tools read from.
- Caveats, licensing, or reliability concerns: `v32` predates colonisation-specific events and needs supplementation from newer community schemas.

### Jixxed Elite Dangerous Journal Schemas

- Source name: `Jixxed Elite Dangerous Journal Schemas`
- URL: <https://jixxed.github.io/ed-journal-schemas/>
- Source type: Community-maintained schema/documentation site
- Public/reusable status: Public website
- Data available: Modern event catalogue including `ColonisationBeaconDeployed`, `ColonisationConstructionDepot`, `ColonisationContribution`, `ColonisationSystemClaim`, `CompleteConstruction`, plus standard market and docking events.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Indirect only`
- Whether it can be downloaded/exported/API accessed: Public documentation; machine-readable schema source is public via linked project
- Suggested ingestion method: Journal parser contract and event mapping
- Trust rating: `High`
- Why it matters for the colonisation AI: Best accessible schema reference found for modern colonisation events.
- Caveats, licensing, or reliability concerns: Community-maintained, not official; should be checked against live journals during implementation.

### CMDR Mechan’s Colonization Mega Guide

- Source name: `CMDR Mechan’s Colonization Mega Guide`
- URL: <https://docs.google.com/document/d/1toXyDQglwVACFKx8umXhP8QcMSAUYPcP6k3STIV2-hE/mobilebasic>
- Source type: Community deep-dive guide
- Public/reusable status: Public Google Doc
- Data available: Terminology, advanced strategies, economy overlap notes, strong/weak link interpretations, population/system-score notes, case studies, appendix links.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public document view; exportability not verified, so `UNKNOWN`
- Suggested ingestion method: Research reference and hypothesis bank, not primary truth
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Probably the richest single community explanation of how players think the system works after months of testing.
- Caveats, licensing, or reliability concerns: Explicitly notes some content lags later patches; treat as tested community interpretation, not canonical authority.

## B. Live galaxy/system data sources

### Spansh nightly dumps

- Source name: `Spansh Data Dumps`
- URL: <https://spansh.co.uk/dumps>
- Source type: Public nightly bulk dump
- Public/reusable status: Publicly downloadable bulk data
- Data available: `galaxy.json.gz`, `galaxy_populated.json.gz`, `galaxy_stations.json.gz`, `systems.json.gz`, faction dump, schemas for systems/bodies/stations.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes` download links are explicit
- Suggested ingestion method: Primary bulk import for systems, bodies, stations, and frequent diff snapshots
- Trust rating: `High`
- Why it matters for the colonisation AI: Best confirmed bulk source for whole-galaxy bodies and stations, including populated subsets and recent-update slices.
- Caveats, licensing, or reliability concerns: Schemas are noted as early/developing; dump sizes are very large.

### EDSM nightly dumps

- Source name: `EDSM Nightly Dumps`
- URL: <https://www.edsm.net/en/nightly-dumps>
- Source type: Public nightly bulk dump
- Public/reusable status: Publicly downloadable bulk data
- Data available: `systemsWithCoordinates`, `systemsWithoutCoordinates`, `systemsPopulated`, `powerPlay`, `stations`, `codex`, `bodies7days`.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes` dump URLs are explicit
- Suggested ingestion method: Secondary bulk import and reconciliation source against Spansh
- Trust rating: `High`
- Why it matters for the colonisation AI: Strong snapshot source for populated systems and stations; especially useful for reconciliation and gap-filling.
- Caveats, licensing, or reliability concerns: Full body dump is not offered, only `bodies7days`; timestamps need to be preserved.

### EDDN live data network

- Source name: `EDDN`
- URL: <https://github.com/EDCD/EDDN/blob/master/README.md>
- Source type: Community live message broker and schema host
- Public/reusable status: Public docs and public live endpoints
- Data available: Live stream endpoints, schema references, developer docs, known downstream consumers, archive pointers.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes` live listener/upload endpoints are documented
- Suggested ingestion method: Stream consumer for fresh observations; never as sole state authority
- Trust rating: `High`
- Why it matters for the colonisation AI: Best source for near-real-time market, station, scan, and journal-driven updates entering the third-party ecosystem.
- Caveats, licensing, or reliability concerns: The README explicitly says the live service does not store an archive or current-state snapshot.

### ED Galaxy Data archives

- Source name: `ED Galaxy Data`
- URL: <https://edgalaxydata.space/>
- Source type: Public archive/index site
- Public/reusable status: Public website with archive navigation
- Data available: EDDN captures, EDSM captures, EDDB captures, Spansh captures, lookup tools, historical spreadsheets.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Archive access is evidenced; formal API status `UNKNOWN`
- Suggested ingestion method: Historical backfill and audit archive, especially for EDDN-derived change history
- Trust rating: `High`
- Why it matters for the colonisation AI: Best public evidence found for historical captures when EDDN itself does not retain archives.
- Caveats, licensing, or reliability concerns: Completeness depends on listener uptime; archive provenance should be recorded per file.

### EDSM public platform / API positioning

- Source name: `EDSM public platform`
- URL: <https://edsm.net>
- Source type: Public site and API-facing platform
- Public/reusable status: Public site
- Data available: System, body, faction, traffic, and logbook ecosystem; public statement that it is a major API used by many tools.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: API/dumps are publicly indicated; specific endpoints were not exhaustively audited here
- Suggested ingestion method: Supporting live-query and reconciliation source
- Trust rating: `High`
- Why it matters for the colonisation AI: Core ecosystem source for bodies and system metadata referenced by multiple community tools.
- Caveats, licensing, or reliability concerns: Do not assume field parity with Spansh; validate field coverage before implementation.

### EDCD CMDR’s Guide

- Source name: `EDCD CMDR’s Guide`
- URL: <https://edcd.github.io/cmdrs-guide.html>
- Source type: Community ecosystem documentation
- Public/reusable status: Public web page
- Data available: Data flow overview for journals, EDDN, CAPI, privacy boundaries, and third-party tool classes.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Indirect only`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Architecture reference, not data ingestion
- Trust rating: `High`
- Why it matters for the colonisation AI: Excellent grounding document for how the ED data ecosystem actually fits together.
- Caveats, licensing, or reliability concerns: Not a dataset.

## C. Market/station data sources

### Inara public star system and station pages

- Source name: `Inara public star system and station pages`
- URL: <https://inara.cz/elite/starsystem/?prm1=176553>
- Source type: Public galaxy/station web pages
- Public/reusable status: Public for human access. Automated bulk reuse terms `UNKNOWN`.
- Data available: System architect, economy pair, population, controlling faction, construction-site percentages, station names, station types, station counts, traffic.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public pages confirmed; official API does **not** provide this dataset
- Suggested ingestion method: Targeted validation scraper or manual evidence capture for named colony systems
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Best public named-system validation surface found for actual colonised systems and their visible build state.
- Caveats, licensing, or reliability concerns: Public pages are valuable; Inara’s official API explicitly excludes star systems, stations, markets, and similar outputs.

### Inara API developer guide

- Source name: `Inara API developer guide`
- URL: <https://inara.cz/elite/inara-api-devguide/>
- Source type: API documentation
- Public/reusable status: Public documentation
- Data available: Scope limitations, batching expectations, endpoint pattern, explicit exclusions.
- Whether it has real system names: `Example only`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: `Yes`, but not for star-system/station/market outputs
- Suggested ingestion method: Negative constraint source to prevent wrong integration path
- Trust rating: `High`
- Why it matters for the colonisation AI: Confirms that Inara is excellent for public page validation but unsuitable as a direct API source for colony-state discovery.
- Caveats, licensing, or reliability concerns: Requires whitelisting and is intentionally not a general data relay.

### EDMarketConnector

- Source name: `EDMarketConnector`
- URL: <https://github.com/EDCD/EDMarketConnector/wiki/Installation%20&%20Setup>
- Source type: Journal/CAPI client and exporter
- Public/reusable status: Public open-source project
- Data available: Journal file location handling, Frontier authentication flow, EDDN station/system/faction/scan export, EDSM and Inara integrations, market/outfitting/shipyard export.
- Whether it has real system names: `Indirect only`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes` releases and docs are public
- Suggested ingestion method: Optional local evidence collector or reference implementation
- Trust rating: `High`
- Why it matters for the colonisation AI: Confirms how much market/station data is exported from player machines into the wider ecosystem.
- Caveats, licensing, or reliability concerns: Tooling integration is useful, but not itself a canonical warehouse.

### Official journal-side market files

- Source name: `Official journal-side market and station files`
- URL: <https://hosting.zaonce.net/community/journal/v32/Journal_Manual-v32.pdf>
- Source type: Official file documentation
- Public/reusable status: Public PDF documentation
- Data available: `Market.json`, `Outfitting.json`, `Shipyard.json`, `Status.json`, `Docked` event semantics, storage path.
- Whether it has real system names: `Example only`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes` locally generated files are documented
- Suggested ingestion method: Local evidence capture contract for contributor uploads
- Trust rating: `High`
- Why it matters for the colonisation AI: Defines the most direct official local files for commodity and station-service evidence.
- Caveats, licensing, or reliability concerns: Requires player-contributed local files; not a public bulk feed by itself.

### EDDN journal schemas and developer docs

- Source name: `EDDN journal schemas and developer docs`
- URL: <https://github.com/EDCD/EDDN/blob/master/schemas/journal-README.md>
- Source type: Schema documentation
- Public/reusable status: Public repository docs
- Data available: Journal-derived field naming, normalisation rules, current-state message expectations, live-branch developer guidance.
- Whether it has real system names: `Indirect only`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes`
- Suggested ingestion method: Parser/mapping reference for stream ingestion
- Trust rating: `High`
- Why it matters for the colonisation AI: Important for correctly interpreting EDDN payloads instead of treating them as raw journal mirrors.
- Caveats, licensing, or reliability concerns: The repository warns developers not to assume `master` always matches live service behaviour.

## D. Completed colony and build-diary sources

### Inara architect pages

- Source name: `Inara architect pages`
- URL: <https://inara.cz/elite/cmdr-architect/447709/>
- Source type: Public commander/architect pages
- Public/reusable status: Public human-readable pages
- Data available: Named architect, colonised systems attached to that commander, system economy/government/allegiance/population, sometimes construction progress.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public page only; API access for this surface `UNKNOWN`
- Suggested ingestion method: Named-system evidence registry and architect attribution validation
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Useful for tying real colony systems to public commanders and confirming that a named system is not hypothetical.
- Caveats, licensing, or reliability concerns: Inara itself warns that architect attribution may be imperfect because claims are not fully stored in journals.

### Inara updates / bug reports thread

- Source name: `Inara updates, bug reports, requests thread`
- URL: <https://inara.cz/elite/board-thread/1/489033/>
- Source type: Public support/discussion thread
- Public/reusable status: Public thread
- Data available: Architect-correction workflow, screenshot requirement, named examples of colonised systems with ghost sites, renamed facilities, and completed ports.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: Public page only
- Suggested ingestion method: Manual named-system evidence queue, especially for anomaly and correction cases
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Very useful for identifying real colony systems and the failure modes of public metadata.
- Caveats, licensing, or reliability concerns: Discussion content is anecdotal and should be corroborated against system pages or screenshots.

### Raven Colonial release thread

- Source name: `Raven Colonial release thread`
- URL: <https://forums.frontier.co.uk/threads/raven-colonial.639577/>
- Source type: Frontier forum release thread
- Public/reusable status: Public thread
- Data available: Tool capabilities, public examples of named systems, planner features, current-vs-live comparison claims, limitations discussed openly by the author.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public thread only; site/API bulk access not independently verified here
- Suggested ingestion method: Research source and manual evidence surface, not first-wave ground truth
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Strong window into how advanced community planners model links, layout, and comparison against live data.
- Caveats, licensing, or reliability concerns: The thread also documents important unknowability limits from journals.

### Inara public logbooks

- Source name: `Inara public logbooks`
- URL: <https://inara.cz/elite/logbooks/>
- Source type: Public narrative diary platform
- Public/reusable status: Public posts
- Data available: Build diaries, commander narratives, screenshots, named colony systems, qualitative outcomes.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Sometimes`
- Whether it has market/economy evidence: `Sometimes`
- Whether it can be downloaded/exported/API accessed: Public pages; export/API status `UNKNOWN`
- Suggested ingestion method: Manual curation for case studies and screenshot-backed examples
- Trust rating: `Medium`
- Why it matters for the colonisation AI: One of the better sources for qualitative “what did players actually build and why?” evidence.
- Caveats, licensing, or reliability concerns: Narrative and screenshot evidence can be rich but unevenly structured.

### Inara public squadron missions and operations pages

- Source name: `Inara public squadron missions and operations pages`
- URL: <https://inara.cz/elite/squadron-missions-other/15908/?page=2>
- Source type: Public operations bulletin / mission pages
- Public/reusable status: Public pages
- Data available: Named colony build operations, target systems, rough timing, public logistics calls.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Sometimes`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: Public pages only
- Suggested ingestion method: System discovery lead source for colonies worth manual inspection
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Useful for finding real active or recently completed colony systems beyond the most famous examples.
- Caveats, licensing, or reliability concerns: Operational posts do not guarantee completion and should be cross-checked.

### Frontier System Colonization Assistance Megathread

- Source name: `Frontier System Colonization Assistance Megathread`
- URL: <https://forums.frontier.co.uk/threads/system-colonization-assistance-megathread.634106/>
- Source type: Frontier forum megathread
- Public/reusable status: Public thread
- Data available: Public requests for help, build support signals, named commander and system leads.
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `Sometimes`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: Public thread only
- Suggested ingestion method: Lead generator for manual system shortlist
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Helps identify real active colonies and communities willing to surface evidence.
- Caveats, licensing, or reliability concerns: Operational chatter is weaker evidence than system pages or structured tools.

## E. Community spreadsheets and tools

### DaftMav Colonization Construction v3

- Source name: `DaftMav Colonization Construction v3`
- URL: <https://docs.google.com/spreadsheets/d/1jsZOzNJSnPIWlU88puOc9gQXvsw-MGp8meoQ6k-Yj-Y/htmlview>
- Source type: Community planning spreadsheet
- Public/reusable status: Public sheet view
- Data available: Construction point logic, commodity lists, layout selections, colony tabs, hauling support, links to supporting resources, screenshot indexes.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public sheet view confirmed; formal export status `UNKNOWN`
- Suggested ingestion method: Heuristic and UI reference; possible structured import if permissions allow later
- Trust rating: `Medium`
- Why it matters for the colonisation AI: One of the most important community planning artefacts and a major upstream influence on later tools.
- Caveats, licensing, or reliability concerns: Spreadsheet logic is community-authored; some notes explicitly say Frontier has not fully clarified all mechanics.

### SrvSurvey colonization wiki

- Source name: `SrvSurvey colonization wiki`
- URL: <https://github.com/njthomson/SrvSurvey/wiki/Colonization>
- Source type: Tool documentation
- Public/reusable status: Public wiki
- Data available: Shopping overlay logic, project creation flow, Raven integration, fleet-carrier limitations, journal-derived constraints.
- Whether it has real system names: `Indirect only`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public wiki and public code repository
- Suggested ingestion method: UX and evidence-capture reference; contributor tooling integration candidate
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Strong source for how active players operationalise hauling and build tracking.
- Caveats, licensing, or reliability concerns: The wiki explicitly notes that journals do not reveal full fleet-carrier cargo state unless items are marked for sale.

### BGS-Tally colonisation tracking

- Source name: `BGS-Tally colonisation tracking`
- URL: <https://github.com/aussig/BGS-Tally/wiki/Usage-%E2%80%90-Colonisation-Tracking/83037c95114c5d4cf3303ed3fc46d7244720f80f>
- Source type: Tool documentation
- Public/reusable status: Public wiki and repository
- Data available: System planning grid, build rows, body features, EDSM/Spansh retrieval, Raven sync, carrier cargo, progress tracking, availability checks.
- Whether it has real system names: `Indirect only`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public wiki; tool is public
- Suggested ingestion method: Planning-feature benchmark and evidence-shape reference
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Shows what advanced community tooling already considers important enough to model explicitly.
- Caveats, licensing, or reliability concerns: Tool output depends on user-maintained plans and multiple external sources.

### RavenColonial EDMC plugin

- Source name: `RavenColonial EDMC plugin`
- URL: <https://github.com/Fenris159/ravencolonial_edmc>
- Source type: Open-source plugin
- Public/reusable status: Public repository
- Data available: Construction depot sync, build tracking overlay, plan-site refresh, fleet-carrier sync, journal/CAPI integration notes, API-shaped flows.
- Whether it has real system names: `Indirect only`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public code and releases confirmed
- Suggested ingestion method: Behavioural reference and possible future contributor connector
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Good evidence of what data active builders actually move between game, plugin, and planning site.
- Caveats, licensing, or reliability concerns: Plugin behaviour is downstream of Raven data and journal constraints.

### Raven Colonial site and EDCodex listing

- Source name: `Raven Colonial site and EDCodex listing`
- URL: <https://edcodex.info/?m=tools&entry=613>
- Source type: Tool listing and public tool site
- Public/reusable status: Public listing and public site
- Data available: Public description of teamwork support, fleet-carrier tracking, completed-project visuals, API existence claim.
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public site confirmed; API documentation was claimed in the listing but not independently verified, so API status = `UNKNOWN`
- Suggested ingestion method: Manual validation and future connector candidate
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Probably the most important dedicated colonisation planning surface in the current community ecosystem.
- Caveats, licensing, or reliability concerns: Public system data may require manual intervention because journals do not expose everything needed.

### anthonylangsworth/Colonisation

- Source name: `anthonylangsworth/Colonisation`
- URL: <https://github.com/anthonylangsworth/Colonisation>
- Source type: Open-source utility repository
- Public/reusable status: Public repository
- Data available: Candidate colonisation-system search flow using EDSM system/body lookups and JSON outputs.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public code confirmed
- Suggested ingestion method: Discovery heuristic reference
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Shows how one public tool filters and scores potential candidate systems before build planning.
- Caveats, licensing, or reliability concerns: Candidate-finding logic is narrower than a full colony planner.

## F. Screenshot and evidence-submission opportunities

### Inara screenshot-backed architect correction flow

- Source name: `Inara screenshot-backed architect correction flow`
- URL: <https://inara.cz/elite/board-thread/1/489033/>
- Source type: Public support workflow
- Public/reusable status: Public thread
- Data available: Requirement for in-game star-system-map screenshot showing architect name for correction requests.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: Public thread only
- Suggested ingestion method: Human submission pathway for disputed architect/system evidence
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Strong model for how user-submitted screenshots can correct public metadata safely.
- Caveats, licensing, or reliability concerns: Manual moderation required.

### DaftMav layout and service screenshot resources

- Source name: `DaftMav layout and service screenshot resources`
- URL: <https://docs.google.com/spreadsheets/d/1jsZOzNJSnPIWlU88puOc9gQXvsw-MGp8meoQ6k-Yj-Y/htmlview>
- Source type: Spreadsheet-linked screenshot index
- Public/reusable status: Public sheet links
- Data available: Settlement layout screenshot index, help/documentation screenshots, services unlock flowchart.
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Indirect only`
- Whether it can be downloaded/exported/API accessed: Public links present; bulk export status `UNKNOWN`
- Suggested ingestion method: Screenshot taxonomy and manual visual-reference set
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Good starting point for a future screenshot evidence workflow tied to facility types and pad sizes.
- Caveats, licensing, or reliability concerns: Community-maintained and not a structured dataset yet.

### Raven Colonial manual plan and site correction path

- Source name: `Raven Colonial manual plan and site correction path`
- URL: <https://forums.frontier.co.uk/threads/raven-colonial.639577/>
- Source type: Public tool-support thread
- Public/reusable status: Public thread
- Data available: Manual plan entry, system-page debugging, known missing fields, examples of systems that need manual intervention.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public thread only
- Suggested ingestion method: Manual review queue for disputed or partially inferable colony layouts
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Demonstrates where automation stops and human evidence submission still matters.
- Caveats, licensing, or reliability concerns: Forum discussion is not a structured API.

## G. Sources to avoid or treat as weak evidence

### Steam mirror of the colonisation guide

- Source name: `Steam mirror of the colonisation guide`
- URL: <https://steamcommunity.com/games/elitedangerous/announcements/detail/508447709615621618>
- Source type: Mirror / repost
- Public/reusable status: Public page
- Data available: Reposted guide text
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Do not ingest as primary mechanics source
- Trust rating: `Low`
- Why it matters for the colonisation AI: Useful only as a discrepancy check
- Caveats, licensing, or reliability concerns: It disagreed with Frontier official wording on claim radius (`16 ly` vs official `15 ly`), so the official site should win.

### Inara API as a colony-state source

- Source name: `Inara API as a colony-state source`
- URL: <https://inara.cz/elite/inara-api-devguide/>
- Source type: API documentation
- Public/reusable status: Public docs
- Data available: Explicit exclusions
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: `Yes`, but not for the required domain
- Suggested ingestion method: Avoid for this use case
- Trust rating: `Low` for colonisation discovery use, `High` for understanding API limits
- Why it matters for the colonisation AI: Prevents wasted implementation effort on the wrong connector.
- Caveats, licensing, or reliability concerns: The guide explicitly says it does not include markets, star systems, stations, or similar outputs.

### Raw EDDN as a canonical historical warehouse

- Source name: `Raw EDDN as a canonical historical warehouse`
- URL: <https://github.com/EDCD/EDDN/blob/master/README.md>
- Source type: Live broker docs
- Public/reusable status: Public docs and live service
- Data available: Stream transport
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes`
- Suggested ingestion method: Use only with downstream storage or archive sources
- Trust rating: `Low` if treated as historical/state truth
- Why it matters for the colonisation AI: This is a common mistake to avoid.
- Caveats, licensing, or reliability concerns: The README explicitly says the live service itself stores no archive and no current-state snapshot.

### Fandom and generic wiki pages

- Source name: `Fandom and generic wiki pages`
- URL: <https://elite-dangerous.fandom.com/wiki/Third_Party_Tools>
- Source type: Community wiki / tertiary summary
- Public/reusable status: Public
- Data available: Tool lists and historical notes
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Weak`
- Whether it can be downloaded/exported/API accessed: Web page only
- Suggested ingestion method: Last-resort orientation only
- Trust rating: `Low`
- Why it matters for the colonisation AI: Can occasionally point to tools, but should not drive mechanics or live-state claims.
- Caveats, licensing, or reliability concerns: Secondary/tertiary curation, can be stale.

### Snippet-only Reddit and forum leads without accessible body content

- Source name: `Snippet-only Reddit and inaccessible discussion leads`
- URL: `UNKNOWN`
- Source type: Search-result fragments
- Public/reusable status: Mixed
- Data available: Usually only brief anecdotal claim fragments
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `UNKNOWN`
- Whether it has market/economy evidence: `UNKNOWN`
- Whether it can be downloaded/exported/API accessed: `UNKNOWN`
- Suggested ingestion method: Do not ingest; only use as search lead to a better public source
- Trust rating: `Low`
- Why it matters for the colonisation AI: Helpful for discovery, not for evidence.
- Caveats, licensing, or reliability concerns: This review intentionally excluded these as primary support.

### Raven system pages treated as full ground truth without manual confirmation

- Source name: `Raven system pages treated as full ground truth without manual confirmation`
- URL: <https://forums.frontier.co.uk/threads/raven-colonial.639577/>
- Source type: Tool limitation warning
- Public/reusable status: Public thread
- Data available: Tool limitation discussion
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Partial`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public site exists; API status `UNKNOWN`
- Suggested ingestion method: Use with corroboration from Inara, Spansh, EDSM, or screenshots
- Trust rating: `Low` if used alone
- Why it matters for the colonisation AI: The tool author explicitly says some details are not knowable from journals alone.
- Caveats, licensing, or reliability concerns: Missing system architect, orbital-body linkage ambiguity, and incomplete finished-facility import were all publicly discussed.

## Follow-up pass additions

This section records additional sources found in the second source-only pass after the first review draft was written.

### Spansh schema repository

- Source name: `spansh/elite_dangerous_schemas`
- URL: <https://github.com/spansh/elite_dangerous_schemas>
- Source type: Open-source schema repository
- Public/reusable status: Public GitHub repository, MIT licensed
- Data available: Versioned `galaxy.schema.json` and `systems.schema.json`, version history, direct download URLs for current and versioned schemas.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Indirect only`
- Whether it can be downloaded/exported/API accessed: `Yes`
- Suggested ingestion method: Pin schema versions alongside each Spansh dump ingest
- Trust rating: `High`
- Why it matters for the colonisation AI: This turns Spansh from “large dump source” into a properly versioned ingest contract with explicit schema URLs and an MIT licence.
- Caveats, licensing, or reliability concerns: Covers Spansh dump structure, not Frontier mechanics.

### EDSM API Systems v1

- Source name: `EDSM API Systems v1`
- URL: <https://www.edsm.net/en/api-v1>
- Source type: Public API documentation
- Public/reusable status: Public documentation
- Data available: `system`, `systems`, `sphere-systems`, and `cube-systems` endpoints, JSON output shapes, date-window querying, coordinate and information flags.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: `Yes`
- Suggested ingestion method: Targeted live lookup for system metadata and local-neighbourhood candidate discovery
- Trust rating: `High`
- Why it matters for the colonisation AI: Confirms a documented API path for targeted system discovery and reconciliation, not just nightly dump consumption.
- Caveats, licensing, or reliability concerns: The documented page inspected here is focused on system endpoints, not full station-market warehousing.

### ED Commodities by Economy

- Source name: `ED Commodities by Economy`
- URL: <https://docs.google.com/spreadsheets/d/12KZHn2I3nD5ky59oZAv4HR_htpG11e91LDylUFRb6g8/htmlview>
- Source type: Community spreadsheet
- Public/reusable status: Public sheet view
- Data available: Commodity-by-economy production and consumption mapping, legality notes, colonisation commodity tab, Odyssey vs orbital distinctions, known Inara/in-game mismatches.
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public sheet view confirmed; export status `UNKNOWN`
- Suggested ingestion method: Analyst reference table and future heuristic seed dataset
- Trust rating: `Medium`
- Why it matters for the colonisation AI: One of the best structured community attempts to map actual supply and consumption relationships relevant to colony construction.
- Caveats, licensing, or reliability concerns: Community-maintained; some rows explicitly note uncertain or incorrect in-game/Inara descriptions.

### CMDR Dubior’s Supply System Guide

- Source name: `CMDR Dubior’s Supply System Guide`
- URL: <https://docs.google.com/document/d/1SL45xutvD8l5U6Flv-fEyGCLQUywXXlXhjBW99XwPJM/mobilebasic>
- Source type: Community guide
- Public/reusable status: Public Google Doc
- Data available: Same-body vs separate-body supply patterns, dedicated supply-system archetypes, haul-rate assumptions, named example systems, economy prioritisation logic.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public document view confirmed; export status `UNKNOWN`
- Suggested ingestion method: Planning-pattern reference and manual case-study source
- Trust rating: `Medium`
- Why it matters for the colonisation AI: More operational and concrete than a generic mechanics guide, especially for supply-chain design and build-order reasoning.
- Caveats, licensing, or reliability concerns: Community-authored and optimisation-oriented; not official.

### ED Colonization Economic Effects

- Source name: `ED Colonization Economic Effects`
- URL: <https://docs.google.com/spreadsheets/d/1Cu6we6PUmyRrmKr-XDgeWoRuxR9uV6L8-5afxoKvkO8/htmlview>
- Source type: Community spreadsheet/model
- Public/reusable status: Public sheet view
- Data available: Body-driven intrinsics, body-feature economies, strong-link base values and modifiers, weak-link notes, modifier edge cases, known bug references.
- Whether it has real system names: `Sometimes`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public sheet view confirmed; export status `UNKNOWN`
- Suggested ingestion method: Hypothesis/reference layer for economy reasoning, with explicit version and caveat tagging
- Trust rating: `Medium`
- Why it matters for the colonisation AI: This is close to a community rules engine for economy and link effects, and is one of the richest reusable reasoning artefacts found.
- Caveats, licensing, or reliability concerns: Explicitly derived from community testing and includes disputed or bug-dependent behaviour.

### StationEconomies EDMC plugin

- Source name: `StationEconomies`
- URL: <https://github.com/MEolh/StationEconomies>
- Source type: Open-source EDMC plugin
- Public/reusable status: Public GitHub repository, MIT licensed
- Data available: Docked-station main economy and other economy proportions shown directly from journal `Docked` event data.
- Whether it has real system names: `Indirect only`
- Whether it has completed-build evidence: `No`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: `Yes` public releases and code confirmed
- Suggested ingestion method: Contributor-side evidence capture helper and validation aid for station economy proportions
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Useful because it confirms that docked journal data can expose economy types and proportions directly enough for local evidence capture.
- Caveats, licensing, or reliability concerns: Only useful when a player docks and the relevant `Docked` data exists.

### EDMC Colonisation Plugin

- Source name: `EDMC Colonisation Plugin`
- URL: <https://github.com/karolnowacki/edmc-colonisation-plugin>
- Source type: Open-source plugin
- Public/reusable status: Public GitHub repository
- Data available: Commodity tracking for colonisation efforts, screenshots of plugin behaviour.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public repository confirmed
- Suggested ingestion method: Historical/community workflow reference only
- Trust rating: `Low-Medium`
- Why it matters for the colonisation AI: Useful as an early public example of EDMC-based colonisation tracking and as an upstream inspiration for later tools.
- Caveats, licensing, or reliability concerns: Very minimal documentation and explicitly under development.

### EliteDangerousWarboard colonisation module

- Source name: `EliteDangerousWarboard colonisation module`
- URL: <https://github.com/Mirooz/EliteDangerousWarboard/blob/master/docs/modules/colonisation.md>
- Source type: Open-source tool documentation
- Public/reusable status: Public repository
- Data available: Architect/orrery workflow, active-vs-completed tracking, optimal market search, fleet-carrier/CAPI integration, journal event list, optional Spansh body hydration.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public code/docs confirmed
- Suggested ingestion method: Workflow benchmark and future connector candidate
- Trust rating: `Medium`
- Why it matters for the colonisation AI: It is another serious public planner that treats colonisation as operations tooling, which helps triangulate what advanced users actually need surfaced.
- Caveats, licensing, or reliability concerns: Tool-centric source, not a canonical data warehouse.

### Raven Colonial building-project workflow page

- Source name: `Raven Colonial building-project workflow page`
- URL: <https://ravencolonial.com/#about=build>
- Source type: Public workflow/help page
- Public/reusable status: Public web page
- Data available: Manual delivery workflow, commander assignment, aggregated multi-project cargo view, primary-project selection, 30-second auto-refresh behaviour, notes field, progress charts.
- Whether it has real system names: `No`
- Whether it has completed-build evidence: `Indirect only`
- Whether it has market/economy evidence: `No`
- Whether it can be downloaded/exported/API accessed: Web page only; API status `UNKNOWN`
- Suggested ingestion method: Workflow reference for contributor tooling and analyst interpretation of Raven project state
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Best public description found of how Raven handles solo and group build tracking, manual delivery, and aggregated project views outside SrvSurvey.
- Caveats, licensing, or reliability concerns: This is a usage/help surface, not a structured dataset.

### Raven Colonial public system planner pages

- Source name: `Raven Colonial public system planner pages`
- URL: <https://ravencolonial.com/#sys=Col%20285%20Sector%20YU-P%20c5-13>
- Source type: Public planner/system surface
- Public/reusable status: Public web page
- Data available: Named system page, site list, system score, tier points, unlock icons, total hauled estimate, warnings for unknown bodies, missing build types, invalid primary port, and unknown architect.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Partial`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public page access confirmed; export/API status `UNKNOWN`
- Suggested ingestion method: Manual page capture and analyst-reviewed extraction for named case studies and planner-visible anomalies
- Trust rating: `Medium`
- Why it matters for the colonisation AI: This is the clearest public planner surface found for seeing how one advanced community tool exposes inferred build state, system score, and “data missing” warnings on real colonies.
- Caveats, licensing, or reliability concerns: Some systems still sit on `Loading ...`, and the author explicitly states several fields are unknowable from journals alone.

### Inara commander build diary `Colonization Log 03 - Vellix at 60%`

- Source name: `Inara commander build diary - Colonization Log 03 - Vellix at 60%`
- URL: <https://inara.cz/elite/logbook/90310/>
- Source type: Public commander logbook / build diary
- Public/reusable status: Public Inara logbook page
- Data available: Progress percentage (`~60%`), named system `Synuefe KS-J c25-12`, named station `Vellix`, supporting system `Synuefe DT-F d12-110`, named port `Cassian Industries`, supporting-economy narrative, screenshot.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public web page only
- Suggested ingestion method: Build-diary evidence row with screenshot flag and named cross-system support relationship
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Strong example of a serialized commander diary that records concrete progress percentages, named facilities, and the surrounding support-system logic.
- Caveats, licensing, or reliability concerns: Narrative source written by the architect, so claims should be corroborated against public system pages or later snapshots.

### Inara system development diary `Development Phase Three`

- Source name: `Inara system development diary - Development Phase Three`
- URL: <https://inara.cz/elite/logbook/90989/>
- Source type: Public commander logbook / build diary
- Public/reusable status: Public Inara logbook page
- Data available: Named primary system `Col 285 Sector BE-C b28-3`, named secondary system `Col 285 Sector BC-B c14-23`, named facilities `Behnken Enterprise`, `Forest Depot`, `Adarsh Astrophysics Institution`, and `Davis Depot`, plus explicit primary-secondary role assignment.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Yes`
- Whether it can be downloaded/exported/API accessed: Public web page only
- Suggested ingestion method: High-value diary evidence for build order, facility naming, and support-system design patterns
- Trust rating: `Medium`
- Why it matters for the colonisation AI: One of the best public examples found of a player documenting how a primary colony and a secondary support system are developed together over multiple phases.
- Caveats, licensing, or reliability concerns: Narrative and selective rather than exhaustive; still needs external corroboration.

### Inara commander colony diary `Wredguia OO-P b33-0`

- Source name: `Inara commander colony diary - Wredguia OO-P b33-0`
- URL: <https://inara.cz/elite/logbook/95960/>
- Source type: Public commander logbook / colony narrative
- Public/reusable status: Public Inara logbook page
- Data available: Named system `Wredguia OO-P b33-0`, initial colony plan, temporary base name `Puesto Abismo`, logistics narrative, materials narrative, construction timeline, hostile interruption narrative.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Partial`
- Whether it has market/economy evidence: `Indirect only`
- Whether it can be downloaded/exported/API accessed: Public web page only
- Suggested ingestion method: Discovery and diary source for early-phase build narrative and named-system tracking
- Trust rating: `Low-Medium`
- Why it matters for the colonisation AI: Useful as a real public diary of first-phase colony establishment in a named system, especially for tracing how players describe the logistics burden of remote builds.
- Caveats, licensing, or reliability concerns: Heavy roleplay/narrative framing means operational details are less reliable than in the more structured progress diaries.

### Frontier public colonisation project thread `Project Galtea`

- Source name: `Frontier public colonisation project thread - Project Galtea`
- URL: <https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/>
- Source type: Public multi-user project/update thread
- Public/reusable status: Public forum thread
- Data available: Long-range project goal, 200x200 LY bubble plan, tool usage (`SrvSurvey` and Raven Colonial), milestone systems such as `Bleia Eohn QT-O d7-10`, `Cat's Paw Sector OI-T c3-3`, and `Cat's Paw Sector GW-W c1-9`, named facility `Galtea's Forge`, completion updates including `60% complete`, and later build-order intentions.
- Whether it has real system names: `Yes`
- Whether it has completed-build evidence: `Yes`
- Whether it has market/economy evidence: `Partial`
- Whether it can be downloaded/exported/API accessed: Public forum pages only
- Suggested ingestion method: Analyst-reviewed project timeline source for group builds, milestone systems, and live progress updates
- Trust rating: `Medium`
- Why it matters for the colonisation AI: Best public example found of a large group openly posting colonisation milestones, system choices, build sequencing, and live percentage updates over time.
- Caveats, licensing, or reliability concerns: Forum thread quality varies by post and remains discussion-driven rather than machine-readable.

## Ranked top 20 sources

| Rank | Source | Why it belongs near the top | Recommended role |
|---|---|---|---|
| 1 | Frontier Update 3 patch notes | Best official explanation of strong/weak links and body-based economy behaviour | Mechanics truth |
| 2 | Frontier System Colonisation Guide | Best official top-level workflow and terminology source | Mechanics truth |
| 3 | Jixxed Journal Schemas | Best accessible modern schema for colonisation journal events | Event contract |
| 4 | Official Player Journal Manual v32 | Official source for local files and legacy event/file structure | Event/file contract |
| 5 | Spansh dumps | Best confirmed bulk source for systems, bodies, and stations | Primary bulk ingest |
| 6 | EDSM nightly dumps | Strong bulk snapshot and reconciliation source | Secondary bulk ingest |
| 7 | EDDN | Best live transport layer for fresh observations | Streaming ingest |
| 8 | ED Galaxy Data | Best public archive layer for EDDN/EDSM/Spansh captures | Historical backfill |
| 9 | Inara public system/station pages | Best public named-colony validation surface | Manual/targeted validation |
| 10 | Inara architect pages | Good named-system attribution source | Named evidence registry |
| 11 | EDMarketConnector | Best practical reference for what local clients export | Contributor tooling reference |
| 12 | DaftMav Colonization Construction v3 | Major community planning artefact | Heuristic reference |
| 13 | SrvSurvey colonization wiki | Strong operational view of hauling and project tracking | Workflow reference |
| 14 | BGS-Tally colonisation tracking | Strong planner model combining EDSM, Spansh, Raven, carrier state | Workflow reference |
| 15 | Raven Colonial public system/build pages | Best public planner surface for named build plans, inferred system state, and visible data gaps | Manual-review source |
| 16 | CMDR Mechan’s Colonization Mega Guide | Deep community interpretation and case studies | Research reference |
| 17 | Frontier Dodec update notes | Critical later-mechanics patch source | Mechanics delta |
| 18 | Inara commander logbooks | Best public build-diary source for named systems, facilities, and progress updates | Analyst-reviewed diary evidence |
| 19 | EDSM public platform | Important ecosystem source used by multiple tools | Live lookup/reconciliation |
| 20 | Frontier public project/update threads | Best public group-build source for milestone systems and ongoing build sequencing | Analyst-reviewed project evidence |

## Ranking changes from follow-up pass

- `EDSM API Systems v1` now strengthens the case for using EDSM not only as a dump provider but as a targeted live lookup service.
- `spansh/elite_dangerous_schemas` strengthens Spansh as a first-wave source because the schema repo is public, versioned, and MIT licensed.
- `ED Commodities by Economy` and `ED Colonization Economic Effects` are two of the best community-maintained structured artefacts found so far for economy reasoning, but they still remain below official mechanics and bulk state sources.
- `StationEconomies` is a useful contributor-side evidence tool, but not a first-wave ingest source by itself.
- `Raven Colonial public system/build pages` materially improve the case for a manual-review layer because they expose named site lists, system score, total hauled, and planner-visible warnings on real colonies.
- `Inara commander logbooks` and `Frontier public project threads` are now the strongest public sources found for serial build updates, named milestone systems, and phase-by-phase construction narratives.

## Proposed evidence schema

The storage model should separate `source truth`, `observations`, `inference`, and `confidence`.

### Core tables

| Entity | Primary key | Important fields | Typical source |
|---|---|---|---|
| `source_catalog` | `source_id` | `name`, `url`, `type`, `trust_rating`, `licence_status`, `access_mode`, `notes` | This review |
| `source_snapshot` | `snapshot_id` | `source_id`, `captured_at`, `version_label`, `raw_locator`, `checksum`, `scope` | Any ingest run |
| `system` | `system_id64` or canonical name | `name`, `coords`, `population`, `allegiance`, `government`, `security`, `economy_primary`, `economy_secondary` | Spansh, EDSM, Inara |
| `body` | `system_id64 + body_id` | `body_name`, `body_type`, `terraformable`, `organics`, `geologicals`, `rings`, `volcanism`, `tidal_flags`, `arrival_ls` | Spansh, EDSM |
| `facility` | internal UUID plus external ids | `system_name`, `body_name`, `market_id`, `facility_name`, `facility_type`, `tier`, `orbital_or_surface`, `status` | Inara, journal, Raven, EDDN |
| `construction_site` | internal UUID | `facility_name`, `system_name`, `body_name`, `progress_pct`, `architect_name`, `last_seen_at`, `source_snapshot_id` | Inara, journal |
| `economy_link_claim` | internal UUID | `from_facility`, `to_facility`, `link_type`, `claimed_strength`, `rule_source`, `observed_or_inferred` | Frontier rules, Raven, internal inference |
| `market_snapshot` | internal UUID | `market_id`, `captured_at`, `commodity_name`, `category`, `buy_price`, `sell_price`, `stock`, `demand`, `prohibited`, `source_snapshot_id` | Journal `Market.json`, EDDN, Inara page capture |
| `station_service_snapshot` | internal UUID | `market_id`, `captured_at`, `shipyard`, `outfitting`, `tech_broker`, `material_trader`, `black_market`, `service_list` | Journal, EDDN, Inara |
| `architect_claim` | internal UUID | `system_name`, `architect_name`, `evidence_type`, `evidence_url`, `reported_at`, `verified_status` | Inara architect/system pages, screenshots |
| `build_diary_item` | internal UUID | `system_name`, `author`, `date`, `source_url`, `excerpt`, `screenshot_present`, `manual_tags` | Inara logbooks, forum threads |
| `screenshot_evidence` | internal UUID | `system_name`, `facility_name`, `body_name`, `image_url`, `capture_type`, `ocr_text`, `review_status` | User submissions, public posts |
| `observation_claim` | internal UUID | `subject_type`, `subject_id`, `claim_type`, `claim_value`, `source_snapshot_id`, `is_direct_observation` | Any source |
| `claim_confidence` | `observation_claim_id` | `source_authority_score`, `specificity_score`, `freshness_score`, `corroboration_score`, `total_score`, `band` | Derived |
| `ingestion_run` | `run_id` | `source_id`, `started_at`, `completed_at`, `status`, `record_count`, `parser_version`, `notes` | Internal |

### Important schema rules

- Keep `source_snapshot` immutable. Never overwrite a prior fetch.
- Keep `observation` separate from `inference`.
- Store all body-linked economy reasoning as explicit claims, not hidden code-only decisions.
- Preserve external identifiers such as `market_id`, EDSM dump name, Spansh dump name, and source URL.
- Allow multiple contradictory claims for the same system/facility, each with separate confidence.
- Treat screenshots and diaries as first-class evidence objects, not free text attached to systems.
- Treat `facility_name` as non-unique across the galaxy. Never use name alone as a global identity key; require system context and, where possible, body or external station identity.

## Proposed confidence scoring system

Use a `0-100` score built from six components:

| Component | Weight | What it rewards |
|---|---:|---|
| Source authority | 25 | Official Frontier docs and widely trusted bulk dumps score highest |
| Directness | 20 | Direct observation beats discussion about observation |
| Specificity | 15 | Named system/body/facility beats generic guide text |
| Exportability / reproducibility | 10 | Public dump/schema/API/file evidence beats one-off screenshots |
| Freshness | 10 | Newer snapshots and later patch-era sources score better |
| Corroboration | 20 | Agreement with independent sources |

### Suggested bands

| Score | Band | Meaning |
|---|---|---|
| `85-100` | `High confidence` | Good enough to drive automation or scoring logic |
| `70-84` | `Usable with review` | Fine for planner hints or validation queues |
| `50-69` | `Exploratory only` | Keep for analyst review, not automated scoring |
| `<50` | `Weak evidence` | Discovery lead only |

### Example heuristics

- Frontier patch note about strong/weak links: likely `95+`
- Spansh or EDSM dump row for a named system: likely `85-95`
- Inara system page showing architect and live construction sites: likely `75-90`
- Raven planner inference for orbital-body mapping without screenshot corroboration: likely `55-70`
- Forum anecdote with no screenshot: likely `35-55`

## Source gaps still to solve

1. No official public bulk export of colonised-system layout state was found.
2. No official API exposing system architect, live facility graph, and completed colony layout together was found.
3. Inara public pages are strong for manual validation, but the official Inara API explicitly does not expose the needed galaxy/station/market data.
4. EDDN is live transport only; it must be paired with storage or archives.
5. Journal files do not appear to expose every finished-facility/body linkage cleanly, especially for some orbital and post-completion states.
6. Fleet-carrier cargo remains partially opaque from journals unless sale-state conditions expose it.
7. Public completed-colony screenshot archives are fragmented across forums, logbooks, and spreadsheets rather than stored in a reusable central dataset.
8. Licence terms for several community tools and spreadsheets are not explicit enough yet for unquestioned bulk redistribution.
9. A robust OCR and screenshot-review pipeline is still missing if the planner is going to rely on player-submitted evidence.
10. Patch drift is a real risk: community guides can stay useful for interpretation while still lagging late balance changes.

## 20 real colony systems worth visiting in-game

Only systems with a public source and enough evidence to justify inspection are listed here.

| System | Public source | Evidence basis | Why inspect | Confidence |
|---|---|---|---|---|
| `Col 285 Sector HD-F b13-1` | <https://inara.cz/elite/starsystem/?prm1=176553> | Public Inara system page with architect, multiple completed ports, and multiple active construction sites | Strong mixed-state example with many facilities visible | High |
| `Col 285 Sector NE-D b14-2` | <https://inara.cz/elite/starsystem/?prm1=208312> | Public Inara page snippet with architect, economy pair, population, and traffic | Good refinery/extraction validation target | Medium |
| `Col 285 Sector ID-Q b6-3` | <https://inara.cz/elite/starsystem/89290/> | Public Inara page snippet with architect and mature population | Good matured extraction/refinery example | Medium |
| `Col 285 Sector VG-H b12-0` | <https://inara.cz/elite/starsystem/441231/> | Public Inara page snippet with architect and `Tourism / Agriculture` profile | Useful non-industrial architecture case | Medium |
| `Col 285 Sector FG-T b18-10` | <https://inara.cz/elite/starsystem/273062/> | Public Inara page snippet with architect and `Extraction / Refinery` economy | Good extraction-heavy comparison case | Medium |
| `Col 285 Sector CK-X b2-3` | <https://inara.cz/elite/starsystem/480548/> | Public Inara page snippet with architect and `Industrial / Extraction` profile | Good industry/extraction mixed case | Medium |
| `Col 285 Sector NN-K c8-13` | <https://inara.cz/elite/cmdr-architect/447709/> | Public architect page linking the commander to the named colonised system | Useful architect-attribution validation case | Medium |
| `HIP 34621` | <https://inara.cz/elite/starsystem/144338/> | Public Inara page snippet with architect and `High Tech / Agriculture` pair | Good mixed-economy validation case | Medium |
| `HIP 58859` | <https://inara.cz/elite/starsystem/204094/> | Public Inara page snippet with architect and `Extraction / Refinery` pair | Good independent-system comparison outside Col 285 naming cluster | Medium |
| `Hyades Sector CQ-Y d84` | <https://inara.cz/elite/starsystem/57235/> | Public Inara system page snippet listing multiple starports and a construction site | Good visible multi-port colony example | Medium |
| `Wregoe IS-L b49-4` | <https://inara.cz/elite/starsystem/909246/> | Public Inara page snippet with architect and `Extraction / Industrial` profile | Good Wregoe-region construction-supply candidate | Medium |
| `Wregoe NA-W b57-4` | <https://inara.cz/elite/starsystem/2479407/> | Public Inara page snippet with architect and `Refinery / Industrial` profile | Good Wregoe-region comparison case | Medium |
| `Wregoe OO-P b33-0` | <https://inara.cz/elite/> | Public Inara snippet describing the system in a colony narrative context | Good named build-diary lead with narrative evidence | Low-Medium |
| `Synuefe EN-H d11-25` | <https://inara.cz/elite/starsystem/176872/> | Public Inara page snippet showing claimed architect state | Useful for inspecting lightly-developed or newer claim state | Medium |
| `Col 285 Sector JD-G b25-8` | <https://inara.cz/elite/board-thread/1/489033/> | Public Inara support thread discussing architect correction for this colonised system | Good anomaly/metadata correction case | Medium |
| `Trapezium Sector EB-W c2-10` | <https://inara.cz/elite/board-thread/1/489033/> | Public thread references ghost construction site and a long-completed surface port | Good finished-build plus stale-public-data case | Medium |
| `Synuefe FZ-D D13-80` | <https://inara.cz/elite/board-thread/1/489033/> | Public thread references incorrect architect attribution and correction workflow | Good disputed-attribution case | Medium |
| `Synuefe KF-E b45-3` | <https://inara.cz/elite/board-thread/1/489033/> | Public thread references architect correction request | Good architect-validation case | Medium |
| `Col 285 Sector YU-P c5-13` | <https://forums.frontier.co.uk/threads/raven-colonial.639577/> | Raven Colonial thread explicitly discusses this colony system loading in the planner | Good public planner-visible example | Medium |
| `Synuefai KJ-S c20-4` | <https://forums.frontier.co.uk/threads/raven-colonial.639577/> | Raven Colonial thread discusses partial data visibility for this colony system | Good test case for what public tools miss | Medium |
| `Synuefai LJ-S c20-10` | <https://forums.frontier.co.uk/threads/raven-colonial.639577/> | Raven Colonial thread confirms public loading of this un/under-colonised system page | Good boundary-case inspection target | Medium |

## Final recommendation on ingestion order

### First wave

1. `Frontier official mechanics sources`
   - System Colonisation Guide
   - Update `4.1.0.0`
   - Update `4.1.2.0`
   - Update `4.2.2.0`
2. `Journal contracts`
   - Official Player Journal Manual
   - Jixxed journal schemas
3. `Bulk galaxy data`
   - Spansh dumps
   - EDSM nightly dumps
4. `Fresh observation stream`
   - EDDN
5. `Historical archive layer`
   - ED Galaxy Data

This is enough to build a first serious evidence warehouse for systems, bodies, stations, market snapshots, and mechanically-grounded inference.

### Second wave

6. `Named-system validation layer`
   - Inara public system pages
   - Inara architect pages
   - Selected Inara station pages
7. `Community planning references`
   - DaftMav spreadsheet
   - SrvSurvey
   - BGS-Tally
   - RavenColonial EDMC plugin

This is the best layer for validating real colonies, discovering useful heuristics, and comparing planner outputs against how experienced players reason about builds.

### Third wave

8. `Manual evidence and case studies`
   - Raven Colonial public system/build pages
   - Raven Colonial forum thread
   - Inara logbooks
   - Inara update/correction threads
   - Frontier project/build threads

This wave should be treated as analyst-reviewed evidence, not automated truth.

## Build-diary and project-thread shortlist

This shortlist focuses only on public sources where commanders are posting concrete build progress, named systems, or multi-post project updates over time.

| System / project | Source | Author / group | Phase or update style | Evidence type | What is concretely visible | Confidence |
|---|---|---|---|---|---|---|
| `Synuefe KS-J c25-12` | <https://inara.cz/elite/logbook/90310/> | `CMDR Xyrellix` | Percentage-based station progress diary | Inara logbook + screenshot | `Vellix` Orbis at `~60%`, named support system `Synuefe DT-F d12-110`, named port `Cassian Industries`, supporting-economy narrative | Medium |
| `Col 285 Sector BE-C b28-3` + `Col 285 Sector BC-B c14-23` | <https://inara.cz/elite/logbook/90989/> | `Eric "Doc" Gardner` | Multi-phase development diary | Inara logbook | Named facilities `Behnken Enterprise`, `Forest Depot`, `Adarsh Astrophysics Institution`, `Davis Depot`; explicit primary/secondary-system planning | Medium-High |
| `Coalsack Sector UU-O b6-6` | <https://inara.cz/elite/logbook/96000/> | `Rhoades Cascadian` / `NQTR` | Weekly operational update | Inara logbook | Completed `Victoria Reach`, `Wedgwood Relay` in progress, shipyard/outfitting counts (`19 of 99 modules`), explicit technology-improvement goal | Medium-High |
| `Wredguia OO-P b33-0` | <https://inara.cz/elite/logbook/95960/> | `Abismo Profundo` narrative series | Serial colony narrative with later build follow-ups | Inara logbook series | Initial colony claim/build narrative, temporary base `Puesto Abismo`, later `Gutierrez's Folly` Coriolis construction and completion, expansion planning | Low-Medium |
| `Project Galtea` | <https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/> | `CMDR GFJake` and contributors | Multi-page group project thread | Frontier forum thread | Named milestones, supply-system chain, tool usage (`SrvSurvey`, Raven Colonial), `Galtea's Forge` progress, route and branch updates, named systems over weeks | Medium-High |

### Notes on use

- `Inara logbooks` are the strongest public diary source when they include percentages, named facilities, screenshots, or explicit primary/support-system roles.
- `Frontier project threads` are strongest for group sequencing, route planning, milestone systems, and repeated updates across weeks, but individual posts vary in precision.
- `Raven public system pages` are valuable as a parallel manual-review surface for checking whether these diary systems expose visible site lists, totals, or planner warnings.
- `Roleplay-heavy diary series` should stay in the evidence graph, but at a lower confidence unless corroborated by Inara system pages, Raven pages, or later build-state snapshots.

## Structured extraction shortlist

This table is a stricter extraction layer for the same diary/thread sources. It highlights what can be lifted into an evidence graph with minimal interpretation and what should be checked next.

| Source row | Primary system / project | Support system(s) | Named facilities / ports | Progress signal | Screenshot present | Best corroboration target | Recommended use |
|---|---|---|---|---|---|---|---|
| `Vellix at 60%` | `Synuefe KS-J c25-12` | `Synuefe DT-F d12-110` | `Vellix`, `Cassian Industries` | `~60% complete` for the Orbis above `Vellix` | Yes | Inara system/station pages first, Raven page if it resolves | High-value build-diary evidence |
| `Development Phase Three` | `Col 285 Sector BE-C b28-3` | `Col 285 Sector BC-B c14-23` | `Behnken Enterprise`, `Forest Depot`, `Adarsh Astrophysics Institution`, `Davis Depot` | Phase marker rather than percentage | No screenshot in fetched text | Inara system pages and later station-state snapshots | High-value architecture and support-system evidence |
| `NQTR AX FOB Coalsack - Construction Update #1` | `Coalsack Sector UU-O b6-6` | `UNKNOWN` in fetched body text | `Victoria Reach`, `Wedgwood Relay`, `Point Defiance` | One facility complete, one in progress, outfitting `19 of 99` modules | No screenshot in fetched text | Inara system/station pages and later diary entries | High-value operational progression evidence |
| `Wredguia series` | `Wredguia OO-P b33-0` | `UNKNOWN` | `Puesto Abismo`, `Gutierrez's Folly` | Serial build progression from initial establishment to Coriolis completion | `UNKNOWN` for the whole series; not consistent across entries fetched | Inara system page, later station page, or Raven if available | Discovery and chronology evidence only |
| `Project Galtea` thread | `Project Galtea` group route | Multiple supply systems and branches | `Galtea's Forge`, named mini supply hubs, named super supply systems | Repeated milestone updates including `60% complete`, completed supply hubs, distance remaining, new targets | Attachments/images appear in thread but are not consistently structured | Frontier thread itself plus any public system pages for named systems | Group-planning and route-sequencing evidence |

### Extraction guidance

- Prefer diary rows with `percentage`, `completed/in-progress state`, or `explicit primary/support-system roles` when seeding structured evidence.
- Treat `named facilities without percentages` as still valuable, because they provide strong anchors for later public-page corroboration.
- Keep `group project threads` in a separate evidence class from `single-system build diaries`; they are better at sequencing and route intent than facility-level certainty.
- When a row has `UNKNOWN` for support system or screenshot status, preserve the row but lower automation confidence until a second public source resolves the gap.

## Implementation-ready examples

The existing schema in this review is already sufficient to ingest diary and thread evidence without inventing a separate data model. The key is to split each public post into:

1. one `build_diary_item`
2. one or more `observation_claim` rows
3. optional `screenshot_evidence`
4. derived `claim_confidence`

### Claim types worth standardising

Use a small controlled vocabulary for diary-derived claims:

- `facility_progress_pct`
- `facility_status`
- `facility_exists`
- `support_system_role`
- `system_role`
- `shipyard_module_count`
- `route_milestone`
- `planned_facility_type`
- `architect_intent`

This is enough to encode nearly everything found in the public diary/thread sources above without flattening narrative nuance into brittle one-off fields.

### Example `build_diary_item`

```json
{
  "diary_item_id": "inara-logbook-90310",
  "system_name": "Synuefe KS-J c25-12",
  "author": "CMDR Xyrellix",
  "date": "2025-12-18",
  "source_url": "https://inara.cz/elite/logbook/90310/",
  "excerpt": "The Orbis above Vellix in Synuefe KS-J c25-12 is roughly 60% complete. Supporting economies in Synuefe DT-F d12-110 around Cassian Industries are feeding the project.",
  "screenshot_present": true,
  "manual_tags": [
    "build-diary",
    "percentage-progress",
    "support-system",
    "named-facility"
  ]
}
```

### Example `observation_claim` records

#### Facility progress claim

```json
{
  "claim_id": "claim-inara-90310-vellix-progress",
  "subject_type": "construction_site",
  "subject_id": "Synuefe KS-J c25-12::Vellix::orbis",
  "claim_type": "facility_progress_pct",
  "claim_value": {
    "facility_name": "Vellix",
    "facility_type": "Orbis",
    "progress_pct": 60,
    "approximate": true
  },
  "source_snapshot_id": "snapshot-inara-logbook-90310",
  "is_direct_observation": true
}
```

#### Support-system claim

```json
{
  "claim_id": "claim-inara-90310-support-system",
  "subject_type": "system",
  "subject_id": "Synuefe KS-J c25-12",
  "claim_type": "support_system_role",
  "claim_value": {
    "support_system_name": "Synuefe DT-F d12-110",
    "support_port_name": "Cassian Industries",
    "role": "industrial-support",
    "evidence_mode": "author-stated"
  },
  "source_snapshot_id": "snapshot-inara-logbook-90310",
  "is_direct_observation": false
}
```

#### Facility status claim

```json
{
  "claim_id": "claim-inara-96000-victoria-reach-status",
  "subject_type": "facility",
  "subject_id": "Coalsack Sector UU-O b6-6::Victoria Reach",
  "claim_type": "facility_status",
  "claim_value": {
    "facility_name": "Victoria Reach",
    "facility_type": "Comm Inst",
    "status": "complete"
  },
  "source_snapshot_id": "snapshot-inara-logbook-96000",
  "is_direct_observation": true
}
```

#### Counted-service claim

```json
{
  "claim_id": "claim-inara-96000-outfitting-count",
  "subject_type": "system",
  "subject_id": "Coalsack Sector UU-O b6-6",
  "claim_type": "shipyard_module_count",
  "claim_value": {
    "modules_available": 19,
    "modules_target": 99,
    "domain": "outfitting"
  },
  "source_snapshot_id": "snapshot-inara-logbook-96000",
  "is_direct_observation": true
}
```

### Example `screenshot_evidence`

```json
{
  "screenshot_evidence_id": "shot-inara-90310-1",
  "system_name": "Synuefe KS-J c25-12",
  "facility_name": "Vellix",
  "body_name": "UNKNOWN",
  "image_url": "https://wa-cdn.nyc3.digitaloceanspaces.com/.../bbae90f7246b1062f540cf34f0b7623c.png",
  "capture_type": "public-logbook-image",
  "ocr_text": "UNKNOWN",
  "review_status": "not_reviewed"
}
```

### Example `claim_confidence`

```json
{
  "observation_claim_id": "claim-inara-90310-vellix-progress",
  "source_authority_score": 14,
  "specificity_score": 15,
  "freshness_score": 8,
  "corroboration_score": 8,
  "total_score": 73,
  "band": "Usable with review"
}
```

### Normalisation rules

- Keep percentages numeric where possible, but preserve `approximate: true` when the post says `roughly`, `about`, or `~`.
- Preserve the author’s original facility name even if the facility type is inferred separately.
- Do not silently convert `supporting economies` narrative into a hard economy-link edge; store it first as a `support_system_role` claim.
- Distinguish `complete`, `operational`, `in progress`, and `planned` as separate statuses.
- For group threads, allow `subject_type: "project_route"` when the post is clearly about bridge progress rather than a single facility.
- When a public page shows the same facility name in a different system, do not automatically treat that as contradiction. First classify it as a possible name collision and require stronger identity evidence.

### Corroboration workflow

1. Ingest the public post as `build_diary_item` plus raw `observation_claim` rows.
2. Try to resolve the named system and named facilities against `Inara public system/station pages`.
3. If available, compare with `Raven public system/build pages` for site lists, planner warnings, or visible build state.
4. If the claim concerns facility type or service state, try to confirm later via station snapshots or additional diary entries.
5. Only after corroboration should diary-derived support relationships or facility states contribute to automated scoring.

### When to trust each source class

- `Inara build diary with percentage + screenshot + named support system`: good enough for review queues and analyst-facing planner hints.
- `Inara build diary with named facilities but no screenshot`: useful for evidence seeding, but wait for corroboration before automation.
- `Roleplay-heavy serial diary`: keep as chronology and discovery evidence unless corroborated.
- `Frontier project thread`: trust for route/milestone sequencing, not for precise facility state unless the post is unusually specific.

## Seed JSON claim pack

This is a first-pass extraction pack of concrete claims from the strongest public diary/thread sources found in this review. Each object below is intended to be machine-ingestable with minimal cleanup.

```json
[
  {
    "claim_id": "seed-001-vellix-progress",
    "subject_type": "construction_site",
    "subject_id": "Synuefe KS-J c25-12::Vellix::orbis",
    "claim_type": "facility_progress_pct",
    "claim_value": {
      "facility_name": "Vellix",
      "facility_type": "Orbis",
      "progress_pct": 60,
      "approximate": true
    },
    "source_url": "https://inara.cz/elite/logbook/90310/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-002-vellix-support",
    "subject_type": "system",
    "subject_id": "Synuefe KS-J c25-12",
    "claim_type": "support_system_role",
    "claim_value": {
      "support_system_name": "Synuefe DT-F d12-110",
      "support_port_name": "Cassian Industries",
      "role": "industrial-support",
      "evidence_mode": "author-stated"
    },
    "source_url": "https://inara.cz/elite/logbook/90310/",
    "is_direct_observation": false
  },
  {
    "claim_id": "seed-003-behnken-enterprise",
    "subject_type": "facility",
    "subject_id": "Col 285 Sector BE-C b28-3::Behnken Enterprise",
    "claim_type": "facility_exists",
    "claim_value": {
      "facility_name": "Behnken Enterprise",
      "facility_type": "small technical trading post",
      "location_body": "Col 285 Sector BE-C b28-3 3",
      "orbital_or_surface": "orbital"
    },
    "source_url": "https://inara.cz/elite/logbook/90989/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-004-forest-depot",
    "subject_type": "facility",
    "subject_id": "Col 285 Sector BE-C b28-3::Forest Depot",
    "claim_type": "facility_exists",
    "claim_value": {
      "facility_name": "Forest Depot",
      "facility_type": "orbital research facility",
      "location_body": "Col 285 Sector BE-C b28-3 3",
      "orbital_or_surface": "orbital"
    },
    "source_url": "https://inara.cz/elite/logbook/90989/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-005-adarsh-astrophysics",
    "subject_type": "facility",
    "subject_id": "Col 285 Sector BE-C b28-3::Adarsh Astrophysics Institution",
    "claim_type": "facility_exists",
    "claim_value": {
      "facility_name": "Adarsh Astrophysics Institution",
      "facility_type": "planetary research facility",
      "location_body": "Col 285 Sector BE-C b28-3 3 A",
      "orbital_or_surface": "surface"
    },
    "source_url": "https://inara.cz/elite/logbook/90989/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-006-secondary-agri-support",
    "subject_type": "system",
    "subject_id": "Col 285 Sector BE-C b28-3",
    "claim_type": "support_system_role",
    "claim_value": {
      "support_system_name": "Col 285 Sector BC-B c14-23",
      "role": "agricultural-support",
      "evidence_mode": "author-stated"
    },
    "source_url": "https://inara.cz/elite/logbook/90989/",
    "is_direct_observation": false
  },
  {
    "claim_id": "seed-007-davis-depot",
    "subject_type": "facility",
    "subject_id": "Col 285 Sector BC-B c14-23::Davis Depot",
    "claim_type": "facility_exists",
    "claim_value": {
      "facility_name": "Davis Depot",
      "facility_type": "specialized communications facility",
      "role": "interstellar-coordination"
    },
    "source_url": "https://inara.cz/elite/logbook/90989/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-008-victoria-reach-complete",
    "subject_type": "facility",
    "subject_id": "Coalsack Sector UU-O b6-6::Victoria Reach",
    "claim_type": "facility_status",
    "claim_value": {
      "facility_name": "Victoria Reach",
      "facility_type": "Comm Inst",
      "status": "complete"
    },
    "source_url": "https://inara.cz/elite/logbook/96000/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-009-wedgwood-relay-progress",
    "subject_type": "construction_site",
    "subject_id": "Coalsack Sector UU-O b6-6::Wedgwood Relay",
    "claim_type": "facility_status",
    "claim_value": {
      "facility_name": "Wedgwood Relay",
      "facility_type": "Satt Inst",
      "status": "in progress"
    },
    "source_url": "https://inara.cz/elite/logbook/96000/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-010-point-defiance-commissioned",
    "subject_type": "facility",
    "subject_id": "Coalsack Sector UU-O b6-6::Point Defiance",
    "claim_type": "facility_status",
    "claim_value": {
      "facility_name": "Point Defiance",
      "status": "commissioned"
    },
    "source_url": "https://inara.cz/elite/logbook/96000/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-011-coalsack-outfitting-count",
    "subject_type": "system",
    "subject_id": "Coalsack Sector UU-O b6-6",
    "claim_type": "shipyard_module_count",
    "claim_value": {
      "modules_available": 19,
      "modules_target": 99,
      "domain": "outfitting"
    },
    "source_url": "https://inara.cz/elite/logbook/96000/",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-012-galteas-forge-progress",
    "subject_type": "construction_site",
    "subject_id": "Cat's Paw Sector GW-W c1-9::Galtea's Forge",
    "claim_type": "facility_progress_pct",
    "claim_value": {
      "facility_name": "Galtea's Forge",
      "facility_type": "T3 Refinery Dodec",
      "progress_pct": 60,
      "approximate": false
    },
    "source_url": "https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/page-2",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-013-third-dodec-industrial-plan",
    "subject_type": "system",
    "subject_id": "Cat's Paw Sector GW-W c1-9",
    "claim_type": "planned_facility_type",
    "claim_value": {
      "facility_type": "Dodec starport",
      "intended_role": "industrial",
      "sequence_hint": "third dodec"
    },
    "source_url": "https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/page-2",
    "is_direct_observation": false
  },
  {
    "claim_id": "seed-014-byeia-euq-milestone",
    "subject_type": "project_route",
    "subject_id": "Project Galtea",
    "claim_type": "route_milestone",
    "claim_value": {
      "system_name": "Byeia Euq GB-F d11-139",
      "milestone_type": "mini-supply-complete",
      "distance_to_next_leg_ly": {
        "min": 450,
        "max": 500,
        "approximate": true
      }
    },
    "source_url": "https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/page-3",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-015-lysoorb-next-hub",
    "subject_type": "project_route",
    "subject_id": "Project Galtea",
    "claim_type": "route_milestone",
    "claim_value": {
      "system_name": "Lysoorb QW-W d1-10",
      "milestone_type": "next-mini-supply-hub",
      "recent_build_rate": "22+ outposts in 3 days"
    },
    "source_url": "https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/page-3",
    "is_direct_observation": true
  },
  {
    "claim_id": "seed-016-bhujerba-intent",
    "subject_type": "project_route",
    "subject_id": "Project Galtea",
    "claim_type": "architect_intent",
    "claim_value": {
      "planned_name": "Bhujerba",
      "target_kind": "ELW system",
      "intended_role": "massive Super Supply System",
      "next_region_after_target": "slengie boxel"
    },
    "source_url": "https://forums.frontier.co.uk/threads/project-galtea-long-distance-colonization-project.643888/page-3",
    "is_direct_observation": false
  }
]
```

### Notes on this seed pack

- Claims `seed-001` through `seed-011` are the best first candidates for ingestion because they are tied to named systems and facilities with specific progress or role information.
- Claims `seed-012` through `seed-016` are useful for route and project-sequencing evidence, but should remain lower-priority than system/facility claims during first implementation.
- `author-stated` support roles should not be upgraded to hard economy-link facts until a second public source corroborates them.

## Corroboration pass on seed claims

This pass checks the seed pack against current public `Inara` system/station pages and `Raven Colonial` system pages. The goal is not to overwrite the raw extracted claims, but to decide which ones can be promoted, which remain provisional, and which need identity review. A critical rule in this pass is that installation and station names are not globally unique, so same-name matches outside the claimed system must be treated as possible collisions, not automatic contradictions.

| Seed claim | Current public check | Outcome | Promotion status |
|---|---|---|---|
| `seed-001-vellix-progress` | `Synuefe KS-J c25-12` resolves publicly on Inara and lists `Vellix Orbital` as an `Orbis` starport under architect `Xyrellix` | Historical `~60%` progress is not preserved on the current system page, but facility identity/type are corroborated | `Partial corroboration` |
| `seed-002-vellix-support` | `Cassian Industries` resolves publicly in `Synuefe DT-F d12-110` as a large-pad `Surface Port` with `Industrial` as the dominant economy | The named support port and system are corroborated, but the support-role relationship remains author-stated | `Partial corroboration` |
| `seed-003-behnken-enterprise` | `Behnken Enterprise` resolves publicly in `Col 285 Sector BE-C b28-3` | Named facility existence is corroborated | `Corroborated` |
| `seed-004-forest-depot` | `Forest Depot` resolves publicly in `Col 285 Sector BE-C b28-3` | Named facility existence is corroborated, though the public station page labels it broadly as an `Installation` | `Corroborated` |
| `seed-005-adarsh-astrophysics` | `Adarsh Astrophysics Institution` resolves publicly in `Col 285 Sector BE-C b28-3` on body `3 a` as a `Surface Settlement (Odyssey)` with `High Tech (100%)` | Facility identity and body linkage are strongly corroborated | `Corroborated` |
| `seed-006-secondary-agri-support` | `Col 285 Sector BC-B c14-23` resolves publicly on Inara, but the current overview shows `High Tech` rather than an explicit agriculture-led role | The named secondary system exists, but the claimed agricultural-support role is not corroborated by the current public overview | `Keep provisional` |
| `seed-007-davis-depot` | A public `Davis Depot` page exists in `Col 285 Sector BE-C b28-3`, but facility names are not unique and that page cannot by itself prove the diary meant the same installation | This is an unresolved identity collision, not a confirmed contradiction | `Identity review needed` |
| `seed-008-victoria-reach-complete` | No direct current public station page was confirmed in this pass, but `Coalsack Sector UU-O b6-6` does resolve publicly on Inara via conflict/report pages | System existence is corroborated, facility state is still diary-only in this pass | `Keep provisional` |
| `seed-009-wedgwood-relay-progress` | Same as above | System existence is corroborated, facility progress remains diary-only | `Keep provisional` |
| `seed-010-point-defiance-commissioned` | Same as above | System existence is corroborated, commissioning state remains diary-only | `Keep provisional` |
| `seed-011-coalsack-outfitting-count` | Same as above | Numeric outfitting claim remains diary-only without a matching current public station snapshot in this pass | `Keep provisional` |
| `seed-012-galteas-forge-progress` | `Cat's Paw Sector GW-W c1-9` resolves publicly in Raven and includes `Galtea's Forge` as a `Dodec Starport` | The named facility and system are corroborated, but the historical `60%` state is not preserved on the current Raven page | `Partial corroboration` |
| `seed-013-third-dodec-industrial-plan` | The current Raven page for `Cat's Paw Sector GW-W c1-9` shows both `Galtea's Forge` and `Galtea's Orbital Factory` as `Dodec Starport` entries | The planning intent is partly supported by current visible build outcomes, but the exact “third dodec” planning step remains historical/thread-specific | `Partial corroboration` |
| `seed-014-byeia-euq-milestone` | No second public source confirmed in this pass | Still thread-only | `Keep provisional` |
| `seed-015-lysoorb-next-hub` | No second public source confirmed in this pass | Still thread-only | `Keep provisional` |
| `seed-016-bhujerba-intent` | No second public source confirmed in this pass | Still thread-only project intent | `Keep provisional` |

### Promotion rules after this pass

- Safe to promote now: `seed-003`, `seed-004`, `seed-005`
- Promote as corroborated-but-historical: `seed-001`, `seed-002`, `seed-012`, `seed-013`
- Keep analyst-reviewed only: `seed-006`, `seed-008`, `seed-009`, `seed-010`, `seed-011`, `seed-014`, `seed-015`, `seed-016`
- Identity-review before use: `seed-007`

### Identity note for `seed-007`

The raw extraction preserved the diary statement that tied `Davis Depot` to `Col 285 Sector BC-B c14-23`, but a current public station page also exists for a `Davis Depot` in `Col 285 Sector BE-C b28-3`. Because installation names are randomly generated and non-unique, the right handling is:

1. preserve the raw diary-derived claim for auditability
2. mark the claim as `identity_review_needed` rather than contradicted
3. require stronger evidence such as a matching system page, body linkage, market identity, screenshot, or later corroborating post before promoting it

## Bottom line

If only a small number of sources are ingested first, the best sequence is:

1. `Frontier mechanics docs`
2. `Jixxed + official journal documentation`
3. `Spansh dumps`
4. `EDSM dumps`
5. `EDDN`
6. `ED Galaxy Data`
7. `Inara public colony pages for validation`

That combination gives the best balance of official mechanics truth, reproducible structured data, live updates, historical recovery, and real named colony examples without overcommitting to weak or anecdotal sources.
