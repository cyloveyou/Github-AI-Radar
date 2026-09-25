#!/usr/bin/env python3
"""Update README counters between stable markers."""
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))

stats = {
    "projects": len(data["projects"]),
    "daily": len(list((ROOT / "daily").glob("*/*/*.md"))),
    "trends": len([p for p in (ROOT / "trends").glob("*.md") if p.name != "README.md"]),
    "weekly": len([p for p in (ROOT / "weekly").glob("*.md") if p.name != "README.md"]),
    "pdf": len(list((ROOT / "pdf").glob("*/*/*.pdf"))),
}

badge = (
    f"![Tracked](https://img.shields.io/badge/tracked_projects-{stats['projects']}-blue)\n"
    f"![Reports](https://img.shields.io/badge/daily_reports-{stats['daily']}-blueviolet)"
)
text = re.sub(
    r"<!-- RADAR_BADGES_START -->.*?<!-- RADAR_BADGES_END -->",
    "<!-- RADAR_BADGES_START -->\n" + badge + "\n<!-- RADAR_BADGES_END -->",
    text,
    flags=re.S,
)

table = f"""<!-- RADAR_STATS_START -->
| Metric | Current |
|---|---:|
| Tracked projects | **{stats['projects']}** |
| Triggered daily reports | **{stats['daily']}** |
| Trend notes | **{stats['trends']}** |
| Weekly reviews | **{stats['weekly']}** |
| Historical PDF reports | **{stats['pdf']}** |
| First observation | **2026-09-17** |
<!-- RADAR_STATS_END -->"""
text = re.sub(
    r"<!-- RADAR_STATS_START -->.*?<!-- RADAR_STATS_END -->",
    table,
    text,
    flags=re.S,
)
readme.write_text(text, encoding="utf-8")
print("README stats:", stats)
