#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner.
Deterministic, standard library only, no network, no input.
"""

import os

MESSAGE = "WARNING: THIS BREAD HAS BEEN TOASTED BEFORE. IT REMEMBERS."


def main() -> None:
    if not (1 <= len(MESSAGE) <= 120):
        raise ValueError("entry must be 1-120 characters, got %d" % len(MESSAGE))
    if "\n" in MESSAGE or "\r" in MESSAGE:
        raise ValueError("entry must be a single line")
    if not MESSAGE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
