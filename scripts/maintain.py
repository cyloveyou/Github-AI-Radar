#!/usr/bin/env python3
"""Run deterministic maintenance tasks for GitHub AI Radar."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
steps = [
    [sys.executable, "scripts/update_archive_index.py"],
    [sys.executable, "scripts/update_readme_stats.py"],
    [sys.executable, "scripts/validate_repo.py"],
]
for cmd in steps:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)
print("Maintenance completed.")
