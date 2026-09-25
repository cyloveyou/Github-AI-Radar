#!/usr/bin/env python3
"""Summarize tracked project lifecycle labels without mutating the registry."""
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
counts = Counter(p.get("status", "unknown") for p in data["projects"].values())
print("Tracked projects:", len(data["projects"]))
for status, count in sorted(counts.items()):
    print(f"{status}: {count}")
