#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one comedy patch note for a bug in real life / human biology
to /output/entry.txt (the path the make.fun program/v1 harness grades).

Stdlib only. No network, no secrets, no reading outside this repository.
"""

import os

ENTRY = (
    "v3.0.2: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 at 3 a.m. instead of sleeping."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise SystemExit("entry must be 1-160 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write exactly one line, no trailing newline: the gate counts
    # /output/entry.txt as 1-160 UTF-8 characters.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
