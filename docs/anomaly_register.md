# Anomaly Register

This register records public-data anomalies, attribution issues, and planner-visible edge cases that future tooling should not silently normalize away.

## A-0001 - Architect attribution mismatch on public colony pages

- Category: Identity / attribution
- Status: Open
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Exact location: section discussing public Inara support-thread correction requests
- Description: Public pages can show incorrect or incomplete architect attribution for colonised systems.
- Example systems:
  - `Col 285 Sector JD-G b25-8`
  - `Synuefe FZ-D D13-80`
  - `Synuefe KF-E b45-3`
- Why it matters: Architect identity should not be treated as unquestionably correct on a single public page.
- Suggested handling: Preserve architect attribution as a claim with evidence source and correction history.

## A-0002 - Ghost construction-site visibility after completion

- Category: State visibility
- Status: Open
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Exact location: section discussing `Trapezium Sector EB-W c2-10`
- Description: Public pages may still show a construction site after a surface port is already long complete.
- Why it matters: Tooling that consumes public pages without reconciliation may misclassify colony stage.
- Suggested handling: Distinguish `public-page visible state` from `verified actual state`.

## A-0003 - Planner and public coverage can miss under-colonised systems

- Category: Source completeness
- Status: Open
- Source: `evidence/colonisation_ai_data_sources_review.md`
- Exact location: Raven Colonial thread references for `Synuefai KJ-S c20-4` and `Synuefai LJ-S c20-10`
- Description: Some under-colonised or partially visible systems appear inconsistently across public tools and planner pages.
- Why it matters: Absence from a public planner is not proof that a colony state or facility does not exist.
- Suggested handling: Treat public absence as weak evidence only.

## A-0004 - Placeholder or proposed names can resemble completed facility names

- Category: Proposal-versus-reality ambiguity
- Status: Open
- Source: `evidence/EV-0002-wregoe-raven-proposed-build-review.md`
- Exact location: `Direct observations` and `Inference`
- Description: Proposed builds or placeholder names can look concrete enough to be mistaken for finished facilities.
- Why it matters: Name parsing alone can collapse proposal state into live state.
- Suggested handling: Track proposal, preview, under-construction, and completed states separately.

## A-0005 - Preview equality can hide meaningful post-build divergence

- Category: Preview ambiguity
- Status: Open
- Source: `evidence/EV-0003-a4-t3-station-selection-previews.md`
- Exact location: `Inference` and `Caveats`
- Description: Similar preview panels across station classes may still conceal post-build service or market differences.
- Why it matters: Preview-state data is not a complete substitute for completed-state evidence.
- Suggested handling: Mark preview-derived equality as provisional until post-build validation exists.

## A-0006 - Mirror documentation can drift from official wording

- Category: Source drift
- Status: Open
- Source: `evidence/colonisation_ai_data_sources_review.md`, `docs/contradiction_register.md`
- Exact location: source-review section comparing official guide wording with Steam mirror wording
- Description: Reposted or mirrored documentation can differ materially from official text.
- Why it matters: Automated ingestion of mirrored docs can create false mechanic conflicts.
- Suggested handling: Record mirror content separately and prefer official wording when available.
