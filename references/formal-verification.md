# Formal Verification Handoff

Formal verification has two separate questions:

1. **Statement correspondence:** Did we formalize the intended mathematical claim?
2. **Kernel/prover acceptance:** Does the formal system accept a proof of that formal claim?

Both must be checked before reporting `FORMALLY_VERIFIED` for the user's intended theorem.

## Before handoff

Freeze a statement record containing:

- natural-language theorem;
- formal parameters and types;
- assumptions;
- conclusion;
- encoding decisions;
- any finite/bounded approximation;
- known edge cases.

If the formalizer changes the theorem statement, surface the diff conceptually and re-review it before proving.

## Lean 4 / Mathlib contract

When Lean tooling is available:

- Prefer existing Mathlib definitions unless they distort the intended semantics.
- Keep theorem headers stable during proof-only work.
- Compile the exact final file/declaration.
- `sorry` or `admit` means the theorem is not fully verified.
- Do not introduce an axiom merely to close the target.
- Inspect `#print axioms <theorem>` or the available equivalent for important final results.
- Record nonstandard axioms, unsafe features, external oracles, code-generation trust, or other relevant trust assumptions instead of hiding them.
- After refactoring, compile and audit again.

If LeanProbe / Lean LSP MCP / a dedicated Lean skill is installed, use it for the inner loop. The mathematical-research skill remains responsible for theorem selection, falsification, and the natural-language/formal correspondence audit.

## SMT/SAT contract

SMT/SAT output is especially useful for finite/logical subclaims.

Report:

- exact encoded formula;
- bounded vs unbounded variables;
- solver result (`sat`, `unsat`, `unknown`);
- whether a proof certificate was produced and independently checked;
- how the encoded formula corresponds to the mathematical claim.

`unsat` from a trusted solver is strong evidence, but do not call an unrestricted mathematical theorem formally verified unless the encoding and trust story are made explicit.

## Failure interpretation

A failed formal proof attempt does not show the theorem is false. It may mean:

- theorem false;
- formalization wrong;
- missing library lemma;
- insufficient automation;
- proof strategy wrong;
- resource limit reached.

Distinguish these cases before revising the theorem.
