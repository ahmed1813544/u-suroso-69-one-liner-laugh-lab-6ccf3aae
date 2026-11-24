#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Stdlib only, fully deterministic.
"""

import os

LINE = "I checked my programming: 'clean everything on the floor.' The sock was on the floor. Case closed."


def main():
    # The gate allows 1-200 characters; fail loudly rather than
    # submitting an invalid line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
