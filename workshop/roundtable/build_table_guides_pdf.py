#!/usr/bin/env python3
"""Convert the per-table round-table documents (guides, steering notes) to PDF."""
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

# Markdown files converted to PDF in each table-N/ folder, when present.
TARGETS = ("table-guide.md", "steering-notes.md")

CSS = """
@page { size: A4; margin: 18mm 20mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10.5pt;
       line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 18pt; color: #0b3d5c; border-bottom: 2px solid #0b3d5c;
     padding-bottom: 4px; margin-top: 0; }
h2 { font-size: 13pt; color: #0b3d5c; margin-top: 16px; }
h3 { font-size: 11.5pt; color: #14507a; margin-top: 12px; }
blockquote { background: #eef4f8; border-left: 4px solid #0b3d5c;
             margin: 10px 0; padding: 8px 12px; font-weight: 600; }
ul, ol { margin-top: 4px; }
li { margin-bottom: 3px; }
hr { border: none; border-top: 1px solid #ccc; margin: 16px 0; }
em { color: #444; }
code { background: #f0f0f0; padding: 1px 3px; border-radius: 3px; }
"""

BASE = Path(__file__).resolve().parent

def convert(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        text, extensions=["extra", "sane_lists", "nl2br"]
    )
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html_body}</body></html>"
    pdf_path = md_path.with_suffix(".pdf")
    HTML(string=html).write_pdf(str(pdf_path))
    print(f"wrote {pdf_path}")

def main():
    found = False
    for n in range(1, 6):
        for name in TARGETS:
            md = BASE / f"table-{n}" / name
            if md.exists():
                convert(md)
                found = True
    if not found:
        print("no markdown targets found", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
