#!/usr/bin/env python3
"""Generate pdf/README.md from archived PDFs and Markdown reports."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pdf_root = ROOT / "pdf"
daily_root = ROOT / "daily"

dates = set()
for p in pdf_root.glob("*/*/*.pdf"):
    dates.add(p.stem)
for p in daily_root.glob("*/*/*.md"):
    dates.add(p.stem)

lines = [
    "# PDF Archive", "",
    "这里保存 GitHub AI Radar 的**发布版 PDF 日报**。PDF 统一按年份和月份归档，仓库阅读入口以 Markdown 为主。", "",
    "## Reports", "",
    "| Date | PDF | Markdown |", "|---|---|---|"
]
for date in sorted(dates, reverse=True):
    y, m, _ = date.split("-")
    pdf = ROOT / "pdf" / y / m / f"{date}.pdf"
    md = ROOT / "daily" / y / m / f"{date}.md"
    pdf_link = f"[PDF](./{y}/{m}/{date}.pdf)" if pdf.exists() else "—"
    md_link = f"[Report](../daily/{y}/{m}/{date}.md)" if md.exists() else "—"
    lines.append(f"| {date} | {pdf_link} | {md_link} |")
lines += ["", "> 没有实质变化的日期不会创建日报，因此日期不连续是正常的。", "",
          "## Naming convention", "", "`pdf/YYYY/MM/YYYY-MM-DD.pdf`", "",
          "PDF 用于固定版式归档、下载、打印和邮件发送。", ""]
(pdf_root / "README.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Indexed {len(dates)} report dates.")
