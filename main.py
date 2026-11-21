#!/usr/bin/env python3
"""The joke about the demo — make.fun program/v1 entry.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Fully deterministic: the text is a fixed constant, no
network, no randomness, no clock, no environment input. Two runs produce
byte-identical output.
"""

import os

JOKE = (
    "My AI coding agent aced the live demo \u2014 then filed a bug report "
    "against me for the code it had just written itself."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
