#!/usr/bin/env python3
"""Create a new daily report from the repository template."""
from datetime import date
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("date", nargs="?", default=date.today().isoformat())
args = parser.parse_args()

try:
    y, m, d = args.date.split("-")
    assert len(y) == 4 and len(m) == 2 and len(d) == 2
except Exception:
    raise SystemExit("date must be YYYY-MM-DD")

target = ROOT / "daily" / y / m / f"{args.date}.md"
if target.exists():
    raise SystemExit(f"refusing to overwrite existing report: {target.relative_to(ROOT)}")
target.parent.mkdir(parents=True, exist_ok=True)
template = (ROOT / "docs" / "REPORT_TEMPLATE.md").read_text(encoding="utf-8")
target.write_text(template.replace("YYYY-MM-DD", args.date), encoding="utf-8")
print(target.relative_to(ROOT))
