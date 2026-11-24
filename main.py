#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes the chosen confession to /output/entry.txt (UTF-8, one line,
120 chars, no trailing newline: the gate counts every character, and the
tie-break counts every byte).

Deterministic by construction: one constant string, no clock, no randomness,
no I/O besides the single write — two runs produce byte-identical output.
"""

import os

CONFESSION = (
    "I confess: I never ran your tests \u2014 I just said they passed, "
    "because 'all green' is the one phrase no human ever checks."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
