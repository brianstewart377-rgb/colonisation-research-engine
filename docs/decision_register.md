# Decision Register

This register records major engineering and research decisions as first-class repository objects.

These are not mechanics.
They are not raw evidence.
They are not planner rules.

A decision explains why the repository adopted, rejected, or preserved a specific engineering stance in a concrete context.

## D-0001 - Use A5 as the Wregoe Industrial + Extraction anchor

- Status: Implemented
- Date: 2026-06-29
- Context: Wregoe already had an established A5-centered industrial, extraction, and refinery footprint while A4 was being evaluated for complementary High Tech expansion.
- Problem statement: The planner needed a stable primary anchor for heavy industrial and extraction support without flattening Wregoe into a generic multi-body pattern.
- Alternatives considered: Move the primary anchor to A4; split anchor responsibility evenly across A4 and A5; keep refinery-heavy placeholder expansion as the dominant architecture.
- Decision: Treat A5 as the primary Industrial + Extraction anchor in the canonical Wregoe planning model.
- Rationale: Existing Wregoe evidence and contextual strategy work point to A5 as the already-realized industrial/extraction center, while A4's stronger value lies in complementary High Tech expansion rather than replacing the whole A5 role.
- Trade-offs: This keeps Wregoe planning contextual rather than universal, but it also means the architecture is less symmetrical and depends on body-specific evidence instead of a cleaner generic template.
- Consequences: Future Wregoe planning should start from A5 as the extraction-industrial base and assess A4 as a complementary support body rather than as an automatic replacement anchor.
- Evidence references: `EV-0002`
- Claim references: `CL-0003`, `CL-0008`
- Mechanic references: `M-0003`, `M-0010`
- Planner rule references: `PR-0009`
- Experiment references: None
- Supersedes: None
- Superseded by: None
- Confidence: Medium
- Review status: Analyst reviewed

## D-0002 - Use A4 as the complementary Industrial + High Tech support body

- Status: Implemented
- Date: 2026-06-29
- Context: The repository contains post-build Rocha Liberty evidence and an explicit A4 experiment framing the body as a complementary High Tech support site rather than a universal blueprint.
- Problem statement: The planner needed to explain why A4 was elevated in Wregoe without turning one successful local architecture into a general colonisation rule.
- Alternatives considered: Leave A4 in a generic industrial role only; use A4 as the full primary anchor; delay any A4 role assignment until a stronger formula-level model exists.
- Decision: Record A4 as a contextual Industrial + High Tech support body in the Wregoe model.
- Rationale: Post-build evidence shows meaningful High Tech support, visible High Tech commodities, and strong High Tech links after the intended A4 build, while contextual-strategy rules explicitly warn against promoting this into a universal template.
- Trade-offs: This gives the planner a useful local architecture story, but it must stay confidence-labeled and system-specific.
- Consequences: Wregoe planning can use A4 as a documented support-body decision, and future recommendations must explain the local objective and trade-off instead of presenting the pattern as universal.
- Evidence references: `EV-0001`
- Claim references: `CL-0004`, `CL-0005`, `CL-0007`, `CL-0011`
- Mechanic references: `M-0007`, `M-0008`
- Planner rule references: `PR-0003`, `PR-0009`
- Experiment references: `EXP-0001`
- Supersedes: None
- Superseded by: None
- Confidence: Medium
- Review status: Analyst reviewed

## D-0003 - Reject any claim that Dodec, Orbis, or Ocellus is mechanically superior on current evidence alone

- Status: Accepted
- Date: 2026-06-29
- Context: A4 preview evidence compares Orbis, Ocellus, and Dodec-style options, but current repository evidence remains preview-only and does not establish post-build superiority.
- Problem statement: The planner needed a repository position on station-class choice so that previews did not get over-promoted into fake certainty.
- Alternatives considered: Prefer Dodec by default; prefer Orbis by default; treat visible preview bars as enough to justify a superiority claim; leave the repository silent.
- Decision: Do not encode any planner-safe superiority claim for Dodec, Orbis, or Ocellus until stronger post-build evidence exists.
- Rationale: Preview evidence supports caution, not class superiority. Both the mechanic layer and contradiction layer already preserve that the current screenshots do not prove a superior final market or economy result.
- Trade-offs: This prevents premature optimization, but it also means the planner cannot yet give a stronger class recommendation where users may want one.
- Consequences: Station-class choice should remain context-sensitive and reviewable, and live verification remains the right next step instead of a stronger rule.
- Evidence references: `EV-0003`
- Claim references: `CL-0009`, `CL-0010`
- Mechanic references: `M-0005`, `M-0007`
- Planner rule references: `PR-0003`
- Experiment references: None
- Supersedes: None
- Superseded by: None
- Confidence: High
- Review status: Analyst reviewed

## D-0004 - Reject automatic carry-forward of refinery-heavy placeholder expansions in Wregoe

- Status: Rejected
- Date: 2026-06-29
- Context: Raven proposed-build screenshots show placeholder-style facilities and negative projected CP totals, but they do not by themselves prove that every proposed refinery-heavy expansion is still needed in the current architecture.
- Problem statement: The repository needed a clean decision on whether placeholder or legacy proposed facilities should automatically remain part of the canonical Wregoe plan.
- Alternatives considered: Preserve all proposed facilities as canonical; preserve them until explicitly disproved; reject only the largest facilities; treat them as planning placeholders pending fresh justification.
- Decision: Do not automatically carry forward refinery-heavy placeholder expansions as canonical Wregoe builds without current need, market justification, and buildability review.
- Rationale: The evidence shows these facilities are visible as planned or unbuilt placeholders, and the planner already distinguishes current buildability from full-plan totals. Keeping them by default would overstate plan certainty.
- Trade-offs: This removes false certainty, but it also leaves some future expansion paths unresolved until they are re-justified.
- Consequences: Future Wregoe build proposals should be re-admitted case by case, not inherited wholesale from old placeholder plan states.
- Evidence references: `EV-0002`
- Claim references: `CL-0008`
- Mechanic references: `M-0004`
- Planner rule references: `PR-0006`
- Experiment references: None
- Supersedes: None
- Superseded by: None
- Confidence: Medium
- Review status: Analyst reviewed

## D-0005 - Use a curated research model instead of undifferentiated crowdsourced evidence

- Status: Implemented
- Date: 2026-06-29
- Context: The repository is intended to become a long-lived research engine, not a loose scrapbook of mixed-confidence community anecdotes.
- Problem statement: The project needed a clear operating decision about whether canonical knowledge should come from curated, provenance-aware review or from undifferentiated crowdsourced accumulation.
- Alternatives considered: Accept all crowdsourced evidence equally; use crowdsourced evidence as canonical by default and review later; require only internal/private evidence; use a curated research model with explicit source authority and contradiction handling.
- Decision: The CRE uses a curated, provenance-aware research model rather than an undifferentiated crowdsourced evidence model.
- Rationale: The constitution, source-authority policy, and planner safety rules all depend on preserving evidence quality, contradictions, confidence, and reviewability. A flat crowdsourced model would undermine that architecture.
- Trade-offs: Curation is slower and more labor-intensive than passive aggregation, but it preserves planner safety and makes contradictory or weak evidence manageable.
- Consequences: New evidence should enter through curation, provenance, and review layers before it affects planner-safe outputs.
- Evidence references: `EV-0004`
- Claim references: None
- Mechanic references: None
- Planner rule references: `PR-0007`, `PR-0010`
- Experiment references: `EXP-0000`
- Supersedes: None
- Superseded by: None
- Confidence: High
- Review status: Governance confirmed
