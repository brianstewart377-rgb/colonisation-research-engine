# Population Rules Register

This register captures the population-growth and output rules extracted directly from the recovered colonisation sources.

## PR-0001 - Population grows on weekly maintenance ticks

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Population growth is applied on weekly maintenance ticks rather than continuously.
- Related mechanics: `M-0012`
- Planner implications: Use week-based population models and avoid day-to-day micromath beyond the first-tick projections.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## PR-0002 - Population follows a hybrid curve

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Population uses fixed growth for the first 14 ticks and a logistic curve thereafter.
- Related mechanics: `M-0012`
- Planner implications: Short-run and long-run population planning should be modeled separately.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: `U-0015`

## PR-0003 - Output scales with the square root of population

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Commodity supply and demand scale with the square root of facility population.
- Related mechanics: `M-0012`
- Planner implications: Population gains have diminishing returns on production.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## PR-0004 - Stations reach about twenty percent of max population after 14 full ticks

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: After roughly 15-16 days, a station reaches about 20% of max population and about 44.72% of max production.
- Related mechanics: `M-0012`
- Planner implications: Newly built stations become materially useful quickly even if they remain far from long-run maturity.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## PR-0005 - Full population maturation takes about a year

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: A station takes about a year to approach its asymptotic population and production.
- Related mechanics: `M-0012`
- Planner implications: Long-run production planning differs materially from first-month bootstrapping.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: `U-0015`

## PR-0006 - Body and facility type both change asymptotic population

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Population tables vary by both body class and facility class, and many combinations have different K populations.
- Related mechanics: `M-0012`
- Planner implications: Do not reuse one facility's population profile across different bodies or tiers.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: `U-0015`

## PR-0007 - Tier 3 ELW orbitals reach about 3.1 billion asymptotic population

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: The population table lists a Tier 3 orbital over an Earth-Like World at about 3.1 billion asymptotic population.
- Related mechanics: `M-0012`
- Planner implications: ELW T3 orbitals are population monsters and therefore major long-run output anchors.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Whether all ELW orbital subclasses match that same ceiling

## PR-0008 - Tier 1 planetary ports can outclass Coriolis on population

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Tier 1 planetary ports at suitable bodies can exceed the population profile of a Tier 2 Coriolis in the guide's cited comparison cases.
- Related mechanics: `M-0012`
- Planner implications: Cheap ground ports can be valid population drivers rather than mere stepping stones, but body choice still matters heavily.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Body-specific coverage remains incomplete

## PR-0009 - Population affects only its own facility output

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Population boosts the output of the facility it belongs to and does not automatically raise output across unrelated facilities in the same system.
- Related mechanics: `M-0012`
- Planner implications: Model facility-level output, not just system-total population.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: None currently recorded

## PR-0010 - Population affects emissions grade and BGS resistance

- Status: Extracted
- Source: `evidence/claim_register.csv`
- Rule: Higher population appears to improve emissions grade and make BGS control harder to swing.
- Related mechanics: `M-0012`
- Planner implications: Population choices likely matter beyond commodity output alone, even if the exact magnitude is still loosely quantified.
- Testing status: Extracted from Mega Guide v2.3.0
- Contradictions: None currently recorded
- Unknowns: Exact magnitude of the emissions and BGS effects

## PR-0011 - Demolition may fail to reduce population

- Status: Needs verification
- Source: `evidence/claim_register.csv`
- Rule: The guide records anecdotal evidence that demolishing facilities may not reduce system population accordingly.
- Related mechanics: `M-0012`, `M-0013`
- Planner implications: Demolition should not be recommended as a reliable population reset tactic yet.
- Testing status: Needs live verification
- Contradictions: None currently recorded
- Unknowns: `U-0016`
