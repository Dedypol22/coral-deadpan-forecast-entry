"""One-line entry for make.fun: "Deadpan Forecasts for Cities That Do Not Exist".

Joke logic: the forecast is a perfectly straight broadcast line for a city
that does not exist, and the absurdity hides inside a measurement a real
meteorologist would never give. Fog "thick enough to lose a bus in" is a
concrete, visual image, and then visibility is reported not in metres but
in "one lamppost and a rumor" -- a deadpan downgrade from a unit of
distance to a unit of gossip, delivered as if it were a normal reading.
The sting lands in the last word: a rumor is not something you can see
through, and the forecaster reports it anyway, straight-faced. One
concrete picture, no clever twist to decode, no second sentence.
"""

import os

LINE = "Tonight in Wobbleford, fog thick enough to lose a bus in — visibility down to one lamppost and a rumor."
# Verified character count of LINE: 103 (within the 1-160 gate).
# Verified byte count of LINE (UTF-8): 105.


def output_dir():
    """Return the directory entry.txt must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the one-line entry and verify it round-trips exactly."""
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == LINE, "entry.txt does not match LINE"
    assert 1 <= len(written) <= 160, "entry.txt must be 1-160 characters"
    assert "\n" not in written, "entry.txt must contain no newline"
    assert written.strip(), "entry.txt must not be only whitespace"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
