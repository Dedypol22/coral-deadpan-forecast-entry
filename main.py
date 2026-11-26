"""Deadpan forecast for a city that does not exist.

The joke is delivered dead straight, like a TV weather anchor reading the
night forecast without blinking: the absurdity is smuggled inside the units
of measurement themselves, which no real meteorologist would ever use. The fog in
Wobbleford is so thick it could swallow a bus whole, and then visibility is
reported not in metres but as "one lamppost and a rumor" -- a slide from a
distance measure to a piece of gossip, read out as if it were a perfectly
normal reading. The sting lands on the very last word.
"""

import os
import sys

# Verified winning line: 103 characters / 105 bytes (em dash is 3 bytes UTF-8).
LINE = "Tonight in Wobbleford, fog thick enough to lose a bus in \u2014 visibility down to one lamppost and a rumor."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt content mismatch"
    assert 1 <= len(written) <= 160, "entry.txt length out of range"
    assert "\n" not in written, "entry.txt must not contain a newline"
    assert written.strip() != "", "entry.txt must not be whitespace-only"
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
