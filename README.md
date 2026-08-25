# mathematical-research

A Codex/Agent Skill for rigorous mathematical investigation: definition repair, quantifier audits, counterexample-first research, theorem/lemma discovery, proof writing, computational exploration, optional formal verification, and explicit evidence-status tracking.

## Install in a repository

Copy this directory to:

```text
.agents/skills/mathematical-research/
```

with `SKILL.md` directly inside it.

## Main files

- `SKILL.md` — core workflow and trigger description
- `references/` — deeper protocols loaded only when relevant
- `scripts/init_workspace.py` — optional `.math-research/` research workspace scaffold
- `scripts/check_claim_ledger.py` — validates claim statuses/dependencies
- `assets/claim-ledger.json` — starter ledger template
- `agents/openai.yaml` — optional Codex UI/invocation metadata
- `tests/activation-cases.md` — trigger and behavioral test prompts

## Optional long-running workspace

```bash
python3 .agents/skills/mathematical-research/scripts/init_workspace.py --root .
python3 .agents/skills/mathematical-research/scripts/check_claim_ledger.py
```

The skill does **not** require Lean. If Lean/LeanProbe/Rocq/Isabelle/SMT tooling is available, it treats those as verification backends while retaining responsibility for statement correctness and proof/evidence status.
