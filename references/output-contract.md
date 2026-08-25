# Research Output Contract

## Claim ledger

For substantial work, maintain claims with this conceptual schema:

```json
{
  "id": "T1",
  "statement": "Exact mathematical statement",
  "status": "PROVED",
  "dependencies": ["L1", "L2"],
  "evidence": ["proof:proofs/T1.md"],
  "verification": ["independent-review"],
  "notes": "Scope or remaining caveat"
}
```

Allowed statuses are defined in `SKILL.md`.

A claim should change status only when new evidence justifies the transition. Typical transitions:

- `CONJECTURE -> PROVED`
- `CONJECTURE -> REFUTED`
- `PROVED -> FORMALLY_VERIFIED`
- `EMPIRICAL -> EXHAUSTIVE_FINITE`

Do not silently change a statement under the same claim ID. If the theorem changes materially, create a new version/ID and mark the old one refuted, superseded, or open in notes.

## Compact final status block

End substantial work with something like:

- **Principal claim:** exact one-sentence theorem/answer.
- **Status:** `PROVED` / `FORMALLY_VERIFIED` / `REFUTED` / ...
- **Domain:** parameter range and assumptions.
- **Core argument:** one or two sentences.
- **Verification:** what was actually checked.
- **Remaining gap:** `none affecting the conclusion` or an exact unresolved point.

## Long-form paper/blog mode

When the user asks for a paper, article, or technical blog:

- Start with the phenomenon in ordinary language.
- Introduce notation only as needed.
- Put exact definitions before theorems that use them.
- State each theorem before proving it.
- Distinguish examples from general results typographically or verbally.
- Include proof roadmaps for long arguments.
- Give a final section titled or functionally equivalent to "Rigorous Answer to the Problem" when the user explicitly needs a definitive resolution.
- Do not place open directions before the exact answered conclusion; readers should be able to tell what was actually solved.
