#!/usr/bin/env python3
"""Create an optional .math-research workspace for long-running math research.

Uses only the Python standard library and refuses to overwrite existing files
unless --force is supplied.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TEMPLATE = {
    "problem": "",
    "claims": [],
}

README = """# Mathematical research workspace

This directory records a long-running mathematical investigation.

- `problem.md` — current exact problem statement and definitions
- `claims.json` — claim ledger with proof/evidence status
- `notes.md` — working notes and proof plans
- `proofs/` — human-readable proofs
- `counterexamples/` — minimized counterexamples and replay notes
- `experiments/` — exact/sampled computational experiments
- `formal/` — Lean/Rocq/Isabelle/SMT artifacts

Do not treat experimental output as a general proof without a separate coverage/correspondence argument.
"""


def write(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root (default: current directory)")
    parser.add_argument("--force", action="store_true", help="Overwrite scaffold files")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ws = root / ".math-research"
    ws.mkdir(parents=True, exist_ok=True)
    for name in ("proofs", "counterexamples", "experiments", "formal"):
        (ws / name).mkdir(exist_ok=True)

    write(ws / "README.md", README, args.force)
    write(ws / "problem.md", "# Problem\n\n## Informal statement\n\n## Precise definitions\n\n## Quantifiers and scope\n", args.force)
    write(ws / "notes.md", "# Research notes\n\n## Falsification pass\n\n## Proof plan\n\n## Blockers\n", args.force)
    claims = ws / "claims.json"
    if args.force or not claims.exists():
        claims.write_text(json.dumps(TEMPLATE, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(ws)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
