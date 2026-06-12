#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


path = Path("/home/tobias/Projects/almost-idempotent-positive-maps/refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt")
data = path.read_bytes()
text = data.decode("utf-8", errors="replace")
lines = text.split("\n")

for lineno in [2246, 2276, 2277, 2337]:
    line = lines[lineno - 1]
    print(f"{lineno}:{line}")
    print("  repr:", repr(line))

for needle in [b"d \x03 d", "conditions (1.1)".encode()]:
    idx = data.find(needle)
    print("needle", needle, "offset", idx)
    if idx >= 0:
        print(data[idx : idx + 80])
