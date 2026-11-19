"""Build the front page once, and check the result before it goes anywhere.

The check is the point: it re-opens the written PNG, re-measures it against the
gate, and verifies that every count the page claims adds up from the story list.
"""

from __future__ import annotations

import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from render import render  # noqa: E402
from stories import DATA  # noqa: E402


def png_size(path: str) -> tuple:
    with open(path, "rb") as fh:
        head = fh.read(24)
    if len(head) < 24:
        raise ValueError("%s is too short to be a PNG" % path)
    return struct.unpack(">II", head[16:24])


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    used, total, regions = render(DATA, target)

    size = os.path.getsize(target)
    width, height = png_size(target)
    problems = []
    if (width, height) != (1024, 1024):
        problems.append("image is %dx%d" % (width, height))
    if size > 1048576:
        problems.append("image is %d bytes" % size)
    if used > 1004:
        problems.append("content ran to y=%d, past the page" % used)
    counted = sum(n for _, n in regions)
    if counted != total:
        problems.append("region counts sum to %d, not %d" % (counted, total))

    print("wrote %s  %dx%d  %d bytes  bottom y=%d" % (target, width, height, size, used))
    print("stories %d  regions %s" % (total, ", ".join("%s=%d" % r for r in regions)))
    if problems:
        for p in problems:
            print("FAIL " + p, file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
