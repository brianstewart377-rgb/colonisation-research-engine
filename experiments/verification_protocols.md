# Live Verification Protocols

This file converts the current `Needs Live Verification` queue into explicit test protocols.

These protocols do not invent expected results.
They define what to hold constant, what to change, and what to record.

## VP-0001 - A4 High Tech threshold and commodity coverage

- Linked verification item: `LV-0001`
- Objective:
  Determine whether raising High Tech on A4 materially improves real construction-material coverage for the colony.
- Hold constant:
  - the rest of the colony architecture
  - the Industrial anchor body role
  - observation method and market capture workflow
- Change:
  - only the intended A4 High Tech-support intervention
- Record:
  - before and after economy shares
  - before and after commodity lists
  - whether missing construction materials return
  - relevant Market Links view
- Minimum useful outcome:
  A clear before/after comparison showing whether material coverage improved, stayed flat, or changed in a different direction than expected.
- Failure mode to watch:
  High Tech share changes without meaningful commodity improvement.

## VP-0002 - Post-build station-class market differences

- Linked verification item: `LV-0002`
- Objective:
  Determine whether Orbis, Ocellus, and Dodec diverge after construction even when preview panels look similar.
- Hold constant:
  - body type where possible
  - surrounding support architecture
  - observation timing and market capture method
- Change:
  - station class only
- Record:
  - final services
  - commodity categories and notable specific commodities
  - mission-board differences if visible
  - Market Links and visible economy behavior
- Minimum useful outcome:
  A repeated difference or a repeated lack of difference across comparable builds.
- Failure mode to watch:
  Treating preview similarity as proof of final similarity without post-build evidence.

## VP-0003 - Refinery threshold for metals at the Dodec

- Linked verification item: `LV-0003`
- Objective:
  Identify what level or pattern of Refinery support is required before Steel, Titanium, and Aluminium return.
- Hold constant:
  - the target Dodec body and existing non-Refinery support
  - observation method
- Change:
  - Refinery support in stepwise increments
  - prefer one change at a time
- Record:
  - Market Links after each intervention
  - economy shares after each intervention
  - presence or absence of Steel, Titanium, and Aluminium
- Minimum useful outcome:
  The first intervention step where the missing metals return, or a clean record that they still do not return.
- Failure mode to watch:
  Making multiple simultaneous changes and losing threshold visibility.

## VP-0004 - Local body modifier non-stacking

- Linked verification item: `LV-0004`
- Objective:
  Determine whether rings, organics, and geological activity stack with body base economies and with each other.
- Hold constant:
  - station class where possible
  - surrounding support architecture where possible
- Change:
  - one local body modifier variable at a time
- Record:
  - body type
  - modifier presence
  - preview economy shifts
  - final observed economy behavior if build completion is available
- Minimum useful outcome:
  Enough isolated comparisons to tell whether modifiers stack, override, or remain single-application.
- Failure mode to watch:
  Comparing bodies that differ in multiple hidden ways at once.

## VP-0005 - Main Port routing and link aggregation

- Linked verification item: `LV-0005`
- Objective:
  Determine whether visible Market Links aggregate upstream contributors through a main surface or orbital port path.
- Hold constant:
  - the colony body
  - the main port candidates
  - observation method
- Change:
  - one upstream support facility or one port-order condition at a time
- Record:
  - which port is main
  - visible arrow changes
  - whether downstream commodity or economy behavior changes
  - screenshots before and after each isolated change
- Minimum useful outcome:
  A reproducible case where visible routing behavior can only be explained by aggregation through a main-port path, or strong evidence that arrows are direct after all.
- Failure mode to watch:
  Inferring graph structure from a single unchanged screenshot without controlled edits.
