#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 a.m.

Writes a single line of text to /output/entry.txt. Deterministic:
same output bytes on every run. No network, no external file reads.
"""

import os

PARTS = (
    "At 3 a.m. I'm a brick with opinions: ",
    "your eyes are half shut, ",
    "the gas costs more than the transfer, ",
    "and my screen is the only light still on in the house, judging you.",
)


def _join(parts) -> str:
    return "".join(parts)


TEXT = _join(PARTS)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
