# Computational Research Discipline

Use computation to discover mathematics, falsify conjectures, and certify finite cases without confusing those roles.

## Evidence levels

### Example / witness

One generated state or numerical example proves only an existential fact when the witness itself can be checked.

### Sampled experiment

Random sampling supports only `EMPIRICAL` conclusions. Report seed/distribution/sample count when material.

### Exhaustive finite verification

Use `EXHAUSTIVE_FINITE` only when:

1. the target domain is finite and precisely stated;
2. every object in that domain is represented by the enumeration or a justified symmetry class;
3. pruning rules are correctness-preserving;
4. the property checker corresponds to the mathematical definition;
5. traversal terminates;
6. duplicate handling cannot omit a distinct relevant case.

For graph/state-space search, report:

- state encoding;
- transition relation;
- canonicalization;
- visited-state policy;
- terminal states;
- winning/losing criterion;
- treatment of cycles;
- strategy/adversary quantifier order;
- whether the algorithm is reachability, minimax, attractor, retrograde analysis, DP, etc.

## Turning exhaustive computation into a theorem

An exhaustive run can become part of a proof only after proving the correspondence between:

- mathematical states and encoded states;
- legal mathematical moves and generated transitions;
- mathematical success/failure and algorithmic terminal labels;
- all finite cases and the enumerated search space.

The code run alone is not the correspondence proof.

## Counterexample workflow

When computation finds a counterexample:

1. Emit a human-readable witness.
2. Replay/check every defining condition.
3. Minimize parameters if possible.
4. Explain exactly which implication fails.
5. Preserve the witness in `counterexamples/` for repo-based research.
