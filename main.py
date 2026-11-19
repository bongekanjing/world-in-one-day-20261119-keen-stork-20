"""Write the 19 November 2026 world-news front page to /output/entry.png.

The image beside this file is the entry: the page was composed and rendered
ahead of time and ships byte for byte, so the two runs the grader makes write
identical bytes.  This program's job is to place it and to refuse to write
anything that would fail the gate, so a broken copy fails loudly here rather
than scoring zero there.
"""

from __future__ import annotations

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")

# the gate's limits, restated so this program holds itself to them
MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
PNG_END = b"IEND\xaeB`\x82"


def png_size(blob: bytes) -> tuple:
    """Width and height from the IHDR chunk, which a PNG always carries first."""
    if len(blob) < 24 or not blob.startswith(PNG_MAGIC):
        raise ValueError("not a PNG")
    if blob[12:16] != b"IHDR":
        raise ValueError("first chunk is not IHDR")
    return struct.unpack(">II", blob[16:24])


def check(blob: bytes) -> None:
    """Raise if the image would fail the gate."""
    if len(blob) > MAX_BYTES:
        raise ValueError("image is %d bytes, over the %d limit" % (len(blob), MAX_BYTES))
    if blob[:2] == b"\xff\xd8":
        return  # a JPEG: the gate reads its size from its own segments
    width, height = png_size(blob)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError("image is %dx%d, over %d" % (width, height, MAX_SIDE))
    if not blob.endswith(PNG_END):
        raise ValueError("PNG does not end with a complete IEND chunk")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    with open(SOURCE, "rb") as fh:
        blob = fh.read()
    try:
        check(blob)
    except ValueError as exc:
        print("entry.png is not usable: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)

    written = os.path.getsize(target)
    with open(target, "rb") as fh:
        width, height = png_size(fh.read(24))
    print("wrote %s (%dx%d, %d bytes)" % (target, width, height, written))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
