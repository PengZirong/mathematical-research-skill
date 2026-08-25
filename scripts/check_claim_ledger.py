#!/usr/bin/env python3
"""Validate a mathematical-research claims.json ledger using stdlib only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED = {
    "PROVED",
    "FORMALLY_VERIFIED",
    "REFUTED",
    "EXHAUSTIVE_FINITE",
    "EMPIRICAL",
    "CONJECTURE",
    "OPEN",
    "CONDITIONAL",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".math-research/claims.json")
    args = parser.parse_args()

    path = Path(args.path)
    data = json.loads(path.read_text(encoding="utf-8"))
    claims = data.get("claims")
    if not isinstance(claims, list):
        raise SystemExit("ERROR: top-level 'claims' must be a list")

    errors: list[str] = []
    ids: set[str] = set()
    for i, claim in enumerate(claims):
        where = f"claims[{i}]"
        if not isinstance(claim, dict):
            errors.append(f"{where}: must be an object")
            continue
        cid = claim.get("id")
        if not isinstance(cid, str) or not cid.strip():
            errors.append(f"{where}: missing non-empty id")
        elif cid in ids:
            errors.append(f"{where}: duplicate id {cid!r}")
        else:
            ids.add(cid)
        if not isinstance(claim.get("statement"), str) or not claim["statement"].strip():
            errors.append(f"{where}: missing non-empty statement")
        status = claim.get("status")
        if status not in ALLOWED:
            errors.append(f"{where}: invalid status {status!r}")
        for field in ("dependencies", "evidence", "verification"):
            if not isinstance(claim.get(field, []), list):
                errors.append(f"{where}: {field} must be a list")

    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            continue
        for dep in claim.get("dependencies", []):
            if dep not in ids:
                errors.append(f"claims[{i}]: unknown dependency {dep!r}")

    if errors:
        print("Claim ledger INVALID")
        for err in errors:
            print(f"- {err}")
        return 2

    counts = {status: 0 for status in sorted(ALLOWED)}
    for claim in claims:
        counts[claim["status"]] += 1
    print(f"Claim ledger OK: {len(claims)} claims")
    for status, count in counts.items():
        if count:
            print(f"- {status}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
