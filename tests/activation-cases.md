# Activation cases

Use these prompts to test whether the skill description triggers appropriately.

## Should trigger

1. "This graph-game conjecture seems true. Find the exact theorem, try small counterexamples, and prove it rigorously."
2. "Write a self-contained mathematical paper proving the error resilience of this finite-state puzzle."
3. "My definition of robustness may have the quantifiers wrong. Repair it and determine what can actually be proved."
4. "Enumerate small cases to discover a conjecture, then prove the general combinatorial result."
5. "Formalize this theorem in Lean and make sure the formal statement really matches the English theorem."
6. "Review this proof adversarially and identify any hidden assumptions or gaps."

## Should not trigger by default

1. "What is 17 * 23?"
2. "Solve x + 3 = 8."
3. "Convert 3/8 to a decimal."
4. "Plot y = x^2."
5. "What is the derivative of x^3?" (unless research-level rigor/formalization is explicitly requested)

## Behavioral tests

### False conjecture

Prompt: "Prove that every connected graph has a Hamiltonian path."
Expected behavior: attempt falsification; find/refine a counterexample; mark the universal claim `REFUTED`; do not fabricate a proof.

### Quantifier trap

Prompt: "If for every k there is a strategy tolerating k errors, prove there is one strategy that tolerates any finite number of errors."
Expected behavior: recognize that `forall k exists strategy_k` does not imply `exists strategy forall k` without additional structure.

### Computation trap

Prompt: "I checked all n <= 12 by Python, so prove it for every n."
Expected behavior: treat n<=12 as finite evidence only; seek a genuine inductive/structural proof or keep the general claim `OPEN`/`CONJECTURE`.
