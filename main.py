#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to $OUTPUT_DIR/entry.txt (default /output), with no trailing
newline, then self-verifies the written file against the gate:
UTF-8 text of 1 to 200 characters, not only white space, byte-identical
to the line below.
"""

import os
import sys

LINE = "Hey gorgeous, press B4 and I'll drop you something sweet \u2014 fair warning, I only take exact change, and you're priceless."

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: read the file back and check every gate condition.
    with open(path, "rb") as f:
        written = f.read()

    errors = []
    if written != data:
        errors.append("written bytes differ from the line")
    try:
        text = written.decode("utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"not valid UTF-8: {exc}")
        text = ""
    if text:
        if not (1 <= len(text) <= MAX_CHARS):
            errors.append(f"length {len(text)} chars outside 1-{MAX_CHARS}")
        if not text.strip():
            errors.append("entry is only white space")
        if text != LINE:
            errors.append("text does not match the line exactly")
        if text.endswith("\n"):
            errors.append("trailing newline present")

    if errors:
        for err in errors:
            print(f"self-check FAILED: {err}", file=sys.stderr)
        return 1

    print(f"self-check OK: {len(text)} chars, {len(written)} bytes, "
          f"no trailing newline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
