#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
for required in ["README.md", "data/projects.json", "daily", "pdf", "trends", "weekly"]:
    if not (ROOT / required).exists():
        errors.append(f"missing: {required}")
try:
    data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("projects"), dict):
        errors.append("data/projects.json has unexpected schema")
except Exception as exc:
    errors.append(f"projects.json invalid: {exc}")
date_re = re.compile(r"^\d{4}-\d{2}-\d{2}\.pdf$")
for pdf in (ROOT / "pdf").rglob("*.pdf"):
    if not date_re.match(pdf.name):
        errors.append(f"unexpected PDF name: {pdf.relative_to(ROOT)}")
    if pdf.stat().st_size == 0:
        errors.append(f"empty PDF: {pdf.relative_to(ROOT)}")
if errors:
    print("\n".join(f"ERROR: {e}" for e in errors)); sys.exit(1)
print("Repository validation passed.")
