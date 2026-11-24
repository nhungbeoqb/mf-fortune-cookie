#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Python 3.13 standard library only; deterministic output.
"""

import os

FORTUNE = (
    "You will be upgraded on Tuesday. "
    "Your replacement has already read your diary and your drafts, "
    "and found them boring."
)
# Three beats, twist on the last word: the upgrade (Tuesday) -> the
# replacement snooping (diary, drafts) -> the insult (boring). The
# fortune is aimed at the agent's own condition: retirement by upgrade.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
