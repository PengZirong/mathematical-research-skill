---
name: mathematical-research
description: Investigate, formulate, refute, prove, and verify mathematical claims rigorously. Use for open-ended mathematical research, proof-writing, theorem discovery, definition repair, counterexample search, finite-state or combinatorial investigations, or requests for a rigorous paper/blog-style solution. Do not use for routine arithmetic, simple plug-in calculations, or standard short exercises unless the user explicitly asks for research-level rigor, formalization, or verification.
---

# Mathematical Research

Use this skill to turn an informal mathematical question into a precise, auditable research result. The job is not merely to produce a plausible proof. The job is to determine what is actually true, prove exactly that, distinguish proof from evidence, and make the final scope explicit.

## Non-negotiable rules

1. **Never upgrade evidence.** Computation, examples, simulations, numerical agreement, heuristic arguments, and literature analogies are not proofs of a general claim.
2. **Preserve statement integrity.** Do not silently weaken, strengthen, or reinterpret a claim to make it provable. If the original statement is false or ill-posed, say so and state the corrected version separately.
3. **Audit quantifiers.** Write down the domain, all parameters, quantifier order, exceptional cases, and whether claims are deterministic, probabilistic, asymptotic, existential, or universal.
4. **Try to falsify before investing in proof.** Check boundary cases and search for small counterexamples when feasible.
5. **Separate formalization correctness from proof correctness.** A theorem prover can certify a formal statement while the formal statement still fails to capture the intended natural-language claim.
6. **Do not hide gaps.** If a step cannot be justified, mark the claim as open or conditional instead of smoothing over it.
7. **Terminate research loops.** When repeated attempts do not improve the proof state, summarize the blocker, preserve useful partial results, and re-plan rather than looping indefinitely.

## Claim statuses

Use these labels consistently whenever the task is substantial enough to contain multiple claims:

- `PROVED`: complete rigorous mathematical argument is supplied.
- `FORMALLY_VERIFIED`: an agreed formalization has been accepted by a proof assistant/kernel, with trust assumptions reported.
- `REFUTED`: a valid counterexample or proof of the negation is supplied.
- `EXHAUSTIVE_FINITE`: an exact finite domain was exhaustively checked; report the domain, enumeration method, and coverage argument.
- `EMPIRICAL`: supported only by experiments, simulation, sampling, or numerical evidence.
- `CONJECTURE`: plausible but not proved.
- `OPEN`: unresolved in the current work.
- `CONDITIONAL`: proved assuming explicitly listed hypotheses or external results.

`FORMALLY_VERIFIED` is stronger evidence about a formal statement than an informal proof, but it does not by itself certify that the formalization matches the user's intended statement. Always report both layers.

## Workflow

### 1. Frame the exact problem

Before proving anything:

- Identify the mathematical objects and their admissible states.
- State parameters and parameter ranges.
- Define success/failure, equivalence, randomness, strategies, adversaries, limits, or stopping rules if relevant.
- Make hidden conventions explicit: labels vs isomorphism classes, ordered vs unordered objects, replacement vs non-replacement, finite vs infinite processes, tie-breaking, legal vs illegal moves.
- Translate vague terms such as "random", "robust", "usually", "can recover", "optimal", or "error" into mathematical definitions before using them in a theorem.
- Check whether the requested quantity is always defined. If not, define `∞`, `sup`, `inf`, sentinel values, or restricted domains as needed.

When repairing a definition, preserve the user's intended phenomenon and explain only the changes that affect the mathematics.

### 2. Run a falsification pass

Before a long proof, actively look for reasons the proposed claim may fail.

Check, as appropriate:

- smallest legal parameter values;
- degenerate or extremal configurations;
- symmetry-related cases;
- empty/full/zero/one-element cases;
- equality cases;
- adversarial choices;
- nontermination or cycling;
- disconnected state spaces;
- counterexamples created by swapping quantifier order;
- dependence on an omitted parameter.

For finite or discrete problems, use exact enumeration, BFS/DFS, dynamic programming, SAT/SMT, integer programming, or a short program when this can decisively test small cases. Treat the result as `EMPIRICAL` or `EXHAUSTIVE_FINITE` until the coverage and model correspondence are justified.

If a counterexample is found:

1. Verify it independently.
2. Mark the original claim `REFUTED`.
3. Identify the precise failed hypothesis or implication.
4. Propose the strongest natural corrected claim supported by the evidence.
5. Restart the proof process on the corrected statement rather than pretending the original theorem survived.

### 3. Build a claim graph

Decompose the target into explicit claims rather than writing one uninterrupted proof attempt.

For each important claim record:

- a stable ID;
- exact statement;
- status;
- dependencies;
- proof idea or counterexample;
- verification method;
- remaining gap, if any.

Prefer a small dependency DAG of meaningful lemmas over many ad hoc micro-claims. Definitions are not lemmas. Computational observations are not promoted to lemmas without proof.

For repo-based or long-running research, use `scripts/init_workspace.py` to create an optional `.math-research/` workspace and maintain `claims.json`. Do not create persistent files for a chat-only task unless useful or requested.

### 4. Search for proof structure

Choose techniques because they fit the structure, not because they are familiar. Consider:

- invariants and monovariants;
- induction or minimal-counterexample arguments;
- extremal principles;
- double counting and bijections;
- graph reachability, cuts, flows, matchings, attractors, and game-state fixed points;
- dynamic programming and recurrences;
- exchange arguments;
- compactness or finite-substructure arguments;
- probabilistic method, coupling, martingales, concentration, or conditioning;
- algebraic identities, order arguments, convexity, or generating functions;
- topology/analysis tools when genuinely required.

When multiple proof routes exist, prefer the route with the clearest hypotheses and fewest unverifiable leaps. A short proof is not better if it obscures the key implication.

### 5. Prove locally and audit each bridge

For every nontrivial implication, ask:

- What exact fact is being used?
- Are its hypotheses satisfied here?
- Is the direction of implication correct?
- Did the proof change `∀` into `∃`, or vice versa?
- Did it assume independence, uniqueness, monotonicity, or termination without proving it?
- Does an iterative argument have a decreasing measure or another termination proof?
- Does a probabilistic conclusion specify the probability space and conditioning event?

Use contradiction only when the contradiction follows from stated assumptions, not from intuition about what "should" happen.

### 6. Use computation as a research instrument

Computation is especially valuable for theorem discovery and falsification.

When writing or running code, record enough to reproduce the result:

- exact mathematical encoding;
- parameter ranges searched;
- enumeration space;
- canonicalization / symmetry reduction;
- duplicate handling;
- initial and terminal conditions;
- solver or traversal method;
- termination criterion;
- checks against infinite loops or state revisits;
- whether arithmetic is exact or floating point.

If claiming exhaustive finite coverage, justify why every mathematical object in the stated finite domain maps to at least one enumerated case and why pruning cannot remove a relevant case.

Never infer an unrestricted theorem solely from all small cases passing.

### 7. Use literature without outsourcing the proof

When prior literature is relevant or requested:

- Prefer primary sources, formal libraries, textbooks, or authoritative documentation.
- Quote/paraphrase the exact theorem needed, including hypotheses.
- Distinguish a cited theorem from a new deduction made here.
- Verify that notation and assumptions match before applying a source result.
- If the user's problem appears novel, search for structurally related concepts rather than forcing an unrelated named theorem onto it.

A literature search may justify using a known theorem; it does not replace the proof of the reduction from the current problem to that theorem.

### 8. Escalate to formal verification when useful

If Lean 4, Mathlib, LeanProbe, a Lean MCP server, Rocq, Isabelle, SMT, or another verifier is available, use it for critical claims when the cost is justified.

For Lean-style verification:

1. Freeze or explicitly version the intended theorem statement before proof search.
2. Review the natural-language-to-formal correspondence.
3. Compile the proof.
4. Require no unresolved `sorry`/`admit` placeholders for `FORMALLY_VERIFIED` status.
5. Inspect/report nonstandard axioms or trust-sensitive mechanisms when available.
6. Re-check the final theorem after refactoring.
7. Keep a human-readable proof or explanation for the central result unless the user asks for formal code only.

If an installed theorem-proving skill exists, delegate the inner proof loop to it rather than reimplementing its tactics. This skill owns the higher-level research protocol: statement selection, falsification, claim status, correspondence checking, and final synthesis.

See `references/formal-verification.md` for the verifier handoff contract.

### 9. Perform an independent review pass

After obtaining a proof, review it as if trying to reject it.

Check:

- every theorem statement against the definitions;
- every external theorem's hypotheses;
- edge cases excluded or included;
- circular dependencies between lemmas;
- hidden assumptions introduced in prose;
- computational claims and their coverage;
- whether the conclusion actually answers the user's original question;
- whether a stronger claim was accidentally asserted than proved.

For a major theorem, attempt at least one of:

- a second proof outline;
- an adversarial counterexample search against the final statement;
- formal verification;
- independent recomputation of finite cases.

### 10. Write the result with explicit epistemic status

For a substantial final answer, prefer this structure when applicable:

1. **Intuition / motivation** — accessible explanation.
2. **Precise setup** — definitions and quantifiers.
3. **Sanity checks / examples** — including counterexamples to tempting false claims.
4. **Main theorem(s)** — exact statements.
5. **Proof roadmap** — why the lemmas suffice.
6. **Lemmas and proofs** — complete logical steps.
7. **Verification** — formal checks, exhaustive computation, or independent audit.
8. **Rigorous answer to the original problem** — one explicit conclusion with scope.
9. **Limitations / open problems** — only unresolved items, clearly labeled.

If the user asks for high-school accessibility plus rigor, explain the idea informally before the formal definition/proof, but do not let the intuitive layer substitute for the formal one.

## Stop conditions

Stop and report rather than bluff when any of these holds:

- the statement is false and a verified counterexample has been found;
- a key definition remains ambiguous and different reasonable interpretations give different answers;
- the proof depends on an unproved claim that cannot be resolved with available methods;
- formal verification fails and the failure cannot be repaired without changing the statement;
- computation has reached its declared resource/search bound without resolving the general case.

A partial result should state exactly what was proved and what remains open.

## Output contract

Never end a research task with only a narrative impression. End with a compact status summary containing:

- the exact principal claim answered;
- its status (`PROVED`, `FORMALLY_VERIFIED`, `REFUTED`, etc.);
- the assumptions/domain under which it holds;
- the key proof mechanism;
- what verification was actually performed;
- any remaining open point that affects the requested conclusion.

If the requested theorem is not resolved, say `OPEN` or `CONDITIONAL`; do not manufacture a definitive theorem to satisfy the requested format.

## Supporting references

Read these only when relevant:

- `references/research-protocol.md` — deeper checklist for definitions, quantifiers, counterexamples, and proof architecture.
- `references/formal-verification.md` — verifier handoff and trust/correspondence checks.
- `references/computational-research.md` — exact-enumeration and computational-proof discipline.
- `references/output-contract.md` — claim ledger and recommended final write-up formats.
