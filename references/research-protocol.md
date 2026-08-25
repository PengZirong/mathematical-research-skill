# Mathematical Research Protocol

Use this reference for non-routine research tasks, especially when the theorem itself is not yet obvious.

## A. Definition audit

For each central noun or process, answer:

1. What is the underlying set/class of objects?
2. Which parameters are fixed and which vary?
3. What counts as equality or equivalence?
4. Is the process deterministic, randomized, strategic, or adversarial?
5. What information is available to each actor/strategy?
6. When may choices/errors occur?
7. What is the terminal/success condition?
8. Can a process be infinite? If so, does nontermination count as failure?
9. Are labels meaningful, or should states be quotient by symmetry?
10. If a distribution is used, what is the sample space and probability measure?

### Quantifier normalization

Rewrite important claims into a visibly quantified form before proving them. In particular distinguish:

- `∀ state, ∃ strategy, ∀ adversary ...`
- `∃ strategy, ∀ state, ∀ adversary ...`
- `∀ k, ∃ strategy_k ...`
- `∃ single strategy, ∀ k ...`

These are not interchangeable.

## B. Falsification matrix

For a proposed theorem, deliberately test:

- minimum legal size;
- one step above minimum;
- maximal/degenerate concentration;
- fully symmetric configurations;
- highly asymmetric configurations;
- no-slack / one-slack / many-slack regimes;
- cases where a presumed monotone statistic stays constant;
- cases where a greedy move has a locally good but globally bad outcome;
- adversarial timing;
- loops and revisitation.

If a counterexample is discovered, first minimize it. A minimal counterexample often reveals the missing hypothesis.

## C. Claim graph discipline

Every major theorem should have a dependency DAG. Typical levels:

- Definitions / conventions
- Structural lemmas
- Local transition lemmas
- Global invariant/attractor/induction lemma
- Main theorem
- Corollaries / probabilistic consequences

Avoid using the main theorem in a lemma that is later used to prove the main theorem.

## D. Proof architecture questions

Before writing details, answer:

1. What is the proof's global progress measure?
2. Why can the bad case not persist forever?
3. Where does each hypothesis enter?
4. What is the hardest bridge in the proof?
5. Can the hardest bridge be isolated as a lemma?
6. Is there a strictly smaller counterexample after the reduction?
7. If the proof is algorithmic, why does the algorithm terminate and preserve legality?
8. If the proof is game-theoretic, whose strategy is existential and whose choices are universal?

## E. Random models

Never say "random state" without defining the distribution.

Specify:

- sample space;
- labels/quotients;
- conditioning event, especially conditioning on solvability;
- whether the generator is uniform over states or uniform over generation histories;
- whether two generation procedures induce the same distribution.

For a statistic `T`, distinguish:

- exact distribution;
- conditional distribution;
- expectation;
- high-probability bound;
- asymptotic statement;
- empirical estimate with confidence interval.

## F. Literature bridge

When a source theorem is used, create an explicit bridge:

1. Source theorem, with hypotheses.
2. Mapping from current objects to source notation.
3. Proof that current hypotheses imply source hypotheses.
4. Application.
5. Mapping conclusion back to the original problem.

If step 3 is missing, the citation is not a proof.
