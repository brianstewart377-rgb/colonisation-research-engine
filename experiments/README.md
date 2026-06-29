# Experiment workflow

Colonisation Research Engine treats experiments as first-class records rather than informal notes.

## Scientific workflow

Observation

↓

Question

↓

Hypothesis

↓

Prediction

↓

Experiment

↓

Observation

↓

Conclusion

↓

Mechanic Update

## Required experiment fields

- hypothesis
- prediction
- system, body, and facility context
- build or change tested
- before state
- after state
- observed result
- conclusion
- confidence
- supporting evidence

## Important rules

- Failed experiments are preserved.
- Null effects are evidence.
- Repeated tests across patches should be treated as distinct evidence eras.
- Planner knowledge should only be updated after experiment review, not merely after data entry.

## Live verification assets

- `live_verification_register.md`
  Canonical queue of unresolved items that need live testing.
- `live_verification_matrix.csv`
  Machine-readable summary of the current live-verification queue.
- `verification_protocols.md`
  Concrete protocols for running the current live-verification items.
