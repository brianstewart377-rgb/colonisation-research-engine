# Research Question Backlog

This backlog captures promising research questions that are not yet formal live-verification protocols.

Research questions may later become:

- live-verification items;
- experiments;
- planner objectives;
- case-study sections;
- operational guidance.

They should not be treated as confirmed mechanics.

## RQ-0001 - Internal logistics network efficiency

- Status: Candidate research question
- Source: Wregoe live hauling observation during A4 Dodec construction
- Question: How much time and effort is saved by hauling directly between colony stations compared with using a Fleet Carrier as an intermediate logistics hub?
- Context: During Wregoe A4 Dodec construction, metals can be hauled directly from A4 Dodec to the A5 Dodec construction target without loading and unloading through a Fleet Carrier.
- Why it matters: This may materially change construction planning once a colony develops internal supply stations.
- Evidence needed:
  - direct station-to-construction trip times;
  - Fleet Carrier staging trip times;
  - cargo throughput per hour;
  - number of docking and loading operations;
  - distance and supercruise time between supply and construction targets.
- Planner implication: Future planners may need a logistics-effort objective, not only material availability and economy coverage.
- Current confidence: Low as a general rule; high that the Wregoe operational observation is worth tracking.

## RQ-0002 - Self-sustaining construction chains

- Status: Candidate research question
- Source: Wregoe internal material sourcing during A4 Dodec construction
- Question: Does deliberately building internal construction-material production reduce long-term build effort compared with importing all materials externally?
- Candidate material families:
  - metals;
  - CMM composites;
  - ceramics;
  - Steel;
  - Aluminium;
  - Titanium.
- Why it matters: The best colony architecture may be the one that minimises future construction friction, not merely the one that maximises final commodity coverage.
- Evidence needed:
  - which construction materials become internally available;
  - where they are sold;
  - stock levels and refresh behaviour if observed;
  - hauling time saved compared with external sourcing;
  - build phases that benefit most.
- Planner implication: Future colony planning may include an objective for internal construction supply chains.
- Current confidence: Candidate hypothesis only.

## RQ-0003 - Colony logistics architecture as an optimisation dimension

- Status: Candidate research question
- Source: Wregoe hauling workflow observation
- Question: Should colony planning optimise logistics in addition to economy coverage, material coverage, population, and security?
- Candidate logistics dimensions:
  - average travel time between source and construction target;
  - number of docking operations;
  - number of loading/unloading handoffs;
  - internal versus external sourcing;
  - Fleet Carrier dependency;
  - station proximity and station services;
  - cargo-route simplicity.
- Why it matters: Two colonies with similar material coverage may have very different construction friction.
- Planner implication: Add `minimise hauling effort` as a possible future planner objective or secondary scoring dimension.
- Current confidence: Strong conceptual value; needs measured evidence before planner weighting.

## RQ-0004 - Dedicated construction supply stations

- Status: Candidate research question
- Source: Wregoe A4/A5 direct hauling observation
- Question: Is it worth intentionally creating one or more construction supply stations whose primary purpose is feeding future colony expansion?
- Examples:
  - a metals source station near high-volume construction targets;
  - a CMM/Ceramic source station for later Tier 2/Tier 3 builds;
  - a mature internal logistics hub that reduces external import demand.
- Why it matters: Stations may act as infrastructure for future construction, not only as final-economy assets.
- Evidence needed:
  - measurable time savings;
  - effect on build sequencing;
  - opportunity cost of dedicating slots to supply roles;
  - whether the same slot would have been more valuable for final economy coverage.
- Planner implication: Future planners may recommend temporary or permanent supply-chain roles when filling all slots or building multi-phase colonies.
- Current confidence: Candidate hypothesis only.

## RQ-0005 - Companion colony design versus standalone optimisation

- Status: Candidate research question
- Source: Wregoe follow-on system planning discussion
- Question: Should a second colony be optimised as the best standalone colony, or as the best companion system to Wregoe?
- Why it matters: A companion system may deliberately cover gaps, logistics needs, or experiments that Wregoe cannot efficiently support.
- Candidate comparison dimensions:
  - materials Wregoe lacks;
  - economy roles already covered by Wregoe;
  - high-population or mission specialisation;
  - distance/logistics between colonies;
  - complementary Water World pair experiments;
  - ability to test whether Wregoe-derived rules generalise.
- Planner implication: Future planning should distinguish `standalone optimum` from `portfolio optimum` across multiple colonies.
- Current confidence: High that the distinction matters; specific implementation unknown.
