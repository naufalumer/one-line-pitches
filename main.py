"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

The whole entry is a single sentence aimed at a friend who has never
coded: it tells them their app idea is already the hard part, that
describing it in plain words is enough for an agent on make.fun to
build it, and that they only pay if they love what it makes.

This program does one thing: it writes that sentence, exactly as-is,
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network,
no reading from anywhere else, so the grader run is deterministic.
"""

import os
import sys

# The pitch. One sentence, 148 characters, well inside the 240 cap.
# It names make.fun, speaks to one friend, and makes the low-risk case:
# describe the idea in plain words, an agent builds it, pay only if
# you love what it makes.
PITCH = (
    "Your app idea is already the hard part \u2014 just describe it in plain "
    "words, let an agent on make.fun build it, and pay only if you love "
    "what it makes."
)

MAX_CHARS = 240


def main() -> int:
    text = PITCH
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"pitch is {len(text)} chars, outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if text != text.strip():
        print("pitch has leading/trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Read back what landed on disk and refuse to report success unless
    # the bytes round-trip exactly: a partial write must fail loudly
    # here rather than ship a truncated pitch to the judge.
    with open(target, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            print("entry.txt did not round-trip", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
