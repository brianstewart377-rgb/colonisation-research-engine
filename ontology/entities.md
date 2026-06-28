# Core entities

This document defines the core entities that make up the future Colonisation Research Engine knowledge model.

## System

A star system that may contain bodies, facilities, factions, architecture patterns, and evidence.

## Body

A planetary, lunar, ring, belt, or other in-system body that can constrain buildability, location, and mechanic behavior.

## Facility

A concrete built or observed installation, port, outpost, settlement, or construction site. Facility names are not globally unique and must never be used alone as identity keys.

## Station Type

A canonical facility class such as Coriolis, Orbis, Dodec, outpost, installation, settlement, or surface port.

## Economy

A canonical economy category or economy mix observed or inferred for systems and facilities.

## Commodity

A tradable item relevant to construction, market behavior, or facility support.

## Observation

A structured statement extracted from evidence, such as a facility existing in a system, a progress percentage, a market state, or a service being present.

## Mechanic

A revisable statement about how colonisation behaves. Mechanics can be confirmed, likely, experimental, disputed, disproved, or patch-sensitive.

## Theory

A broader explanatory model made up of one or more mechanics or mechanic assertions. A theory is useful when a set of mechanics appears to describe a larger system behavior.

## Experiment

A first-class test record containing hypothesis, prediction, context, before state, after state, observed result, conclusion, confidence, and supporting evidence.

## Evidence

A source-backed artifact or linkage used to support or challenge an observation, mechanic, or experiment. Evidence may be positive, negative, ambiguous, or contradictory.

## Contradiction

A durable review object created when new evidence challenges an existing observation, mechanic, or planner knowledge projection.

## Planner Recommendation

A build or planning output produced from verified knowledge. Recommendations must include confidence and evidence-backed caveats.

## Architecture

A reusable colony structure or system design pattern, such as a supply architecture, high-tech cluster, or support-system pattern.

## Source

A source family such as Frontier mechanics pages, Spansh dumps, EDSM dumps, Inara system pages, Raven pages, or manual experiment logs.

## Confidence Record

A time-stamped record that explains why a given observation, mechanic, experiment, or planner knowledge item has a particular confidence level.

## Knowledge Projection

A planner-safe projection derived from verified mechanics and current system data. This is the layer downstream tools should consume rather than raw evidence.
