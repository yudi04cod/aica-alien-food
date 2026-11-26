#!/usr/bin/env python3
"""Aica Alien Food — make.fun entry for
"One Star, Five Stars for the Food"
(u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

Writes one sentence to /output/entry.txt: a one-star review of planet
Earth by an alien tourist that still slips in a real compliment about
the food. Deterministic: the same bytes on every run. Python 3.13,
standard library only, no network access.
"""

import os
import sys

# The review. One sentence, at most 200 characters.
# Grievance: a sun that sets without asking, gravity that bruises a
# third knee, locals queueing to stare at glowing rectangles.
# Compliment: the tacos nearly justify the fuel home.
REVIEW = (
    "One star: your sun sets without asking permission, your gravity "
    "bruised my third knee, and the locals queue to stare at glowing "
    "rectangles — but the tacos alone nearly justify the fuel home."
)


def main() -> int:
    text = REVIEW.strip()
    # Gate self-check: one sentence, 1-200 chars, not only whitespace.
    if not text:
        print("error: empty review", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: review is {len(text)} chars, over 200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("error: review must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
