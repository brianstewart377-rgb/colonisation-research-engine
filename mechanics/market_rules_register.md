# Market and Material Rules Register

This register captures market-behavior, commodity-location, and overlap rules extracted from the recovered colonisation sources.

Semantic rule:

- `market` means the exposure surface for commodities, services, and demand or supply behavior.
- `economy` influences market behavior but is not identical to market outcome.
- `construction material` is a planner-relevant commodity subset, not a separate non-commodity resource family like construction points.

## MR-0001 - Top-two economies protect their own supply

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: The first and second-ranked economies at a port protect their supply from being netted out by other economies present there.
- Related mechanics: `M-0010`
- Planner implications: Keep must-have producer economies in the top two positions.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: `U-0002`

## MR-0002 - Top-two economies do not protect their demand

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Demand from the top two economies can still net against the supply of non-top-two economies.
- Related mechanics: `M-0010`
- Planner implications: Protected-supply status is not the same as full market immunity.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: `U-0001`

## MR-0003 - Two-economy mixes are the default safe design

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Two dominant economies can coexist without negative supply cannibalization, making two-economy mixes the default safe design recommendation.
- Related mechanics: `M-0010`
- Planner implications: Default to one or two dominant economies in high-confidence planner outputs unless a larger mix is deliberately justified.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## MR-0004 - Third-and-lower economies need pair-overlap review

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Once a third economy is present, Appendix D overlap details become mechanically relevant.
- Related mechanics: `M-0010`
- Planner implications: Do not greenlight a three-plus economy station without checking pair-overlap material.
- Testing status: Supported by 35 extracted Appendix D entries
- Contradictions: None currently recorded
- Unknowns: `U-0001`, `U-0002`

## MR-0005 - Contraband shaping is orbital-only

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Contraband strong links can only be created using orbital facilities.
- Related mechanics: `M-0006`, `M-0010`
- Planner implications: Contraband plans must reserve orbital slots.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## MR-0006 - Insulating Membranes are orbital-only

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Insulating Membranes are restricted to orbital starports.
- Related mechanics: `M-0010`
- Planner implications: A pure-ground system cannot fully cover that material.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Exact full product set of orbital-only materials

## MR-0007 - CMM Composites are planetary-only

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: CMM Composites are restricted to planetary sites.
- Related mechanics: `M-0010`
- Planner implications: A pure-orbital system cannot fully cover that material.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Exact full product set of surface-only materials

## MR-0008 - Refinery specialization requires the ground-only Refinery Hub

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Refinery markets can only be specialised directly through the ground-exclusive Refinery Hub.
- Related mechanics: `M-0006`, `M-0009`, `M-0010`
- Planner implications: Serious refinery systems need viable ground slots.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## MR-0009 - Development level affects commodity volume and seems to soft-cap near 20

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Development level affects commodity supply and demand volume and appears to soft-cap around level 20.
- Related mechanics: `M-0011`
- Planner implications: Development is a market-volume lever, not just decorative system flavor.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Exact formula beyond the soft-cap observation

## MR-0010 - Steel is the dominant construction material

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Steel is required for all installations and often represents roughly 25-30% of total mass.
- Related mechanics: `M-0010`
- Planner implications: Steel coverage should be one of the first material checks in any construction-oriented planner.
- Testing status: Extracted from canonical `DM-0001` source material
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## MR-0011 - CMM Composite, Aluminium, and Titanium are next-tier strategic materials

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: CMM Composite, Aluminium, and Titanium are all called out as major construction materials with substantial share of facility mass requirements.
- Related mechanics: `M-0010`
- Planner implications: Material-completeness scoring should not stop at steel.
- Testing status: Extracted from canonical `DM-0001` source material
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## MR-0012 - Planetary agriculture is mechanically valuable but reliability-limited

- Status: Needs verification
- Source: `evidence/claim_register.csv`, `docs/contradiction_register.md`
- Rule: Planetary agriculture can be a strong market source on paper, but bugged live behavior means some agricultural ports may produce no agri goods.
- Related mechanics: `M-0010`, `M-0013`
- Planner implications: Prefer orbital agriculture when recommendation confidence matters more than slot purity.
- Testing status: Needs live verification
- Contradictions: `C-0005`
- Unknowns: Which variants or systems are affected
