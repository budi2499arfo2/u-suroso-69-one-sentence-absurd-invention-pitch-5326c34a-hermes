#!/usr/bin/env python3
"""One Sentence Absurd Invention Pitch — the sock that files a formal complaint.

The pitch is a single sentence, written as a complaint-desk log line for the
invention LAUNDRY-LEGAL MK1: a sock lost in the dryer files complaint #4471,
the claim is auto-filed one minute later, the laundry is fined $2, and the
missing pair is located in 4 minutes. The invention is the joke — a laundry
device that gives socks a legal department — and the humour comes from the
fields, not from a prose sentence. The log format also keeps the entry to a
single sentence: no decimal points in any figure (the fine is a whole $2),
so the only full stop is the final one.
"""

import os
import sys

TEXT = "LAUNDRY-LEGAL MK1: 1 sock lost in the dryer at 09:14 files complaint #4471, claim auto-filed at 09:15, laundry fined $2, missing pair located in 4 minutes, status: settled."


def main() -> int:
    text = TEXT
    # Gate: exactly one sentence, 1-220 characters, not whitespace-only.
    # The product name carries the invention (a device, not a complaint);
    # MK1 has no period, so the sentence gate still sees a single full stop.
    if not (1 <= len(text) <= 220):
        print(f"gate failed: entry is {len(text)} characters, must be 1-220", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is whitespace-only", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        # Exactly one full stop, at the end: the entry is one sentence.
        print("gate failed: entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Verify byte-for-byte: read back and compare with the TEXT constant.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(text)} characters, 1 sentence)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
