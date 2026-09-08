#!/usr/bin/env python3
"""Publish workshop table guides into the rendered Quarto site.

The canonical table-guide Markdown files live under workshop/roundtable/table-N/.
This script keeps that source of truth in place and exposes each guide as a
website page under website/_site/roundtables/table-N/table-guide.html.

Rendering is intentionally permissive: each table is handled independently, and
the script falls back to a small built-in Markdown renderer if Quarto is not
available or if Quarto cannot render a specific guide.
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


TABLES = {
    "table-1": "Table 1 - Genomics, Molecular Biology and Life Sciences",
    "table-2": "Table 2 - Medical Imaging, Diagnostics, Machine Learning and QML",
    "table-3": "Table 3 - Mechanistic Medicine, Clinical Decisions and Operational Optimization",
    "table-4": "Table 4 - Benchmarking Methods and the Repository",
    "table-5": "Table 5 - Infrastructure, Community and Policy Instruments",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def normalize_links(markdown: str) -> str:
    replacements = [
        ("../../../website/roundtables/seed-problem-brief.qmd", "../seed-problem-brief.html"),
        ("../../website/roundtables/seed-problem-brief.qmd", "../seed-problem-brief.html"),
        ("../../../website/roundtables/participant-guide.qmd", "../participant-guide.html"),
        ("../../website/roundtables/participant-guide.qmd", "../participant-guide.html"),
    ]
    for old, new in replacements:
        markdown = markdown.replace(old, new)
    return markdown


def inline_markdown(text: str) -> str:
    text = html.escape(text)

    code_spans: list[str] = []

    def keep_code(match: re.Match[str]) -> str:
        code_spans.append(f"<code>{match.group(1)}</code>")
        return f"@@CODE{len(code_spans) - 1}@@"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)

    for i, code in enumerate(code_spans):
        text = text.replace(f"@@CODE{i}@@", code)
    return text


def is_table_start(lines: list[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    current = lines[index].strip()
    next_line = lines[index + 1].strip()
    return current.startswith("|") and next_line.startswith("|") and "---" in next_line


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def render_fallback_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    blocks: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped == "---":
            blocks.append("<hr>")
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            index += 1
            continue

        if stripped.startswith(">"):
            quotes: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quotes.append(lines[index].strip().lstrip(">").strip())
                index += 1
            content = inline_markdown(" ".join(quotes))
            blocks.append(f"<blockquote>{content}</blockquote>")
            continue

        if is_table_start(lines, index):
            headers = table_cells(lines[index])
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(table_cells(lines[index]))
                index += 1
            head_html = "".join(f"<th>{inline_markdown(cell)}</th>" for cell in headers)
            row_html = []
            for row in rows:
                cells = "".join(f"<td>{inline_markdown(cell)}</td>" for cell in row)
                row_html.append(f"<tr>{cells}</tr>")
            blocks.append(
                "<table><thead><tr>"
                + head_html
                + "</tr></thead><tbody>"
                + "".join(row_html)
                + "</tbody></table>"
            )
            continue

        if re.match(r"^[-*]\s+", stripped):
            items: list[str] = []
            while index < len(lines) and re.match(r"^[-*]\s+", lines[index].strip()):
                item_lines = [re.sub(r"^[-*]\s+", "", lines[index].strip())]
                index += 1
                while (
                    index < len(lines)
                    and lines[index].startswith("  ")
                    and lines[index].strip()
                    and not re.match(r"^[-*]\s+", lines[index].strip())
                    and not re.match(r"^\d+\.\s+", lines[index].strip())
                ):
                    item_lines.append(lines[index].strip())
                    index += 1
                items.append(f"<li>{inline_markdown(' '.join(item_lines))}</li>")
            blocks.append("<ul>" + "".join(items) + "</ul>")
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while index < len(lines) and re.match(r"^\d+\.\s+", lines[index].strip()):
                item_lines = [re.sub(r"^\d+\.\s+", "", lines[index].strip())]
                index += 1
                while (
                    index < len(lines)
                    and lines[index].startswith("  ")
                    and lines[index].strip()
                    and not re.match(r"^[-*]\s+", lines[index].strip())
                    and not re.match(r"^\d+\.\s+", lines[index].strip())
                ):
                    item_lines.append(lines[index].strip())
                    index += 1
                items.append(f"<li>{inline_markdown(' '.join(item_lines))}</li>")
            blocks.append("<ol>" + "".join(items) + "</ol>")
            continue

        paragraph: list[str] = []
        while index < len(lines):
            candidate = lines[index].strip()
            if (
                not candidate
                or candidate == "---"
                or re.match(r"^(#{1,6})\s+", candidate)
                or candidate.startswith(">")
                or is_table_start(lines, index)
                or re.match(r"^[-*]\s+", candidate)
                or re.match(r"^\d+\.\s+", candidate)
            ):
                break
            paragraph.append(candidate)
            index += 1
        blocks.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")

    return "\n".join(blocks)


def page_shell(title: str, body: str, notice: str | None = None) -> str:
    notice_html = ""
    if notice:
        notice_html = f'<p class="guide-warning">{html.escape(notice)}</p>'

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | BENQODHI</title>
  <link rel="stylesheet" href="../../styles.css">
  <style>
    body {{ max-width: 980px; margin: 0 auto; padding: 2rem 1rem 4rem; }}
    main {{ line-height: 1.55; }}
    table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
    th, td {{ border: 1px solid #d7dde8; padding: 0.55rem 0.65rem; vertical-align: top; }}
    th {{ background: #f3f6fb; }}
    blockquote {{ border-left: 4px solid #5577aa; margin-left: 0; padding-left: 1rem; color: #334; }}
    .guide-nav {{ margin-bottom: 1.5rem; font-size: 0.95rem; }}
    .guide-nav a {{ margin-right: 1rem; }}
    .guide-warning {{ border-left: 4px solid #b7791f; background: #fffaf0; padding: 0.75rem 1rem; }}
  </style>
</head>
<body>
  <nav class="guide-nav">
    <a href="../index.html">Round Tables</a>
    <a href="../participant-guide.html">Participant Guide</a>
    <a href="../seed-problem-brief.html">Seed Problem Brief</a>
  </nav>
  {notice_html}
  <main>
{body}
  </main>
</body>
</html>
"""


def write_fallback_page(destination: Path, title: str, markdown: str, notice: str | None = None) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    body = render_fallback_markdown(normalize_links(markdown))
    destination.write_text(page_shell(title, body, notice=notice), encoding="utf-8")


def render_with_quarto(src: Path, destination_dir: Path) -> tuple[bool, str]:
    quarto = shutil.which("quarto")
    if not quarto:
        return False, "quarto not found on PATH"

    with tempfile.TemporaryDirectory(prefix="benqodhi-table-guide-") as tmp_name:
        tmp_dir = Path(tmp_name)
        tmp_src = tmp_dir / "table-guide.md"
        tmp_src.write_text(normalize_links(src.read_text(encoding="utf-8")), encoding="utf-8")

        cmd = [
            quarto,
            "render",
            tmp_src.name,
            "--to",
            "html",
            "--output",
            "table-guide.html",
        ]
        completed = subprocess.run(cmd, cwd=tmp_dir, capture_output=True, text=True)
        if completed.returncode != 0:
            message = (completed.stderr or completed.stdout or "unknown quarto error").strip()
            return False, message

        rendered = tmp_dir / "table-guide.html"
        if not rendered.exists():
            return False, "quarto did not produce table-guide.html"
        shutil.copy2(rendered, destination_dir / "table-guide.html")

        asset_dir = tmp_dir / "table-guide_files"
        if asset_dir.exists():
            shutil.copytree(asset_dir, destination_dir / "table-guide_files", dirs_exist_ok=True)

    return True, ""


def publish_table(table_id: str, title: str, root: Path) -> str | None:
    src_dir = root / "workshop" / "roundtable" / table_id
    src = src_dir / "table-guide.md"
    dst_dir = root / "website" / "_site" / "roundtables" / table_id
    dst_html = dst_dir / "table-guide.html"

    if not src.exists():
        write_fallback_page(
            dst_html,
            title,
            f"# {title}\n\nThe source file `{src.relative_to(root)}` is missing.",
            notice="This guide could not be rendered because the source Markdown file is missing.",
        )
        return f"{table_id}: missing source, wrote fallback page"

    dst_dir.mkdir(parents=True, exist_ok=True)
    success, message = render_with_quarto(src, dst_dir)
    if not success:
        write_fallback_page(
            dst_html,
            title,
            src.read_text(encoding="utf-8"),
        )
        warning = message.splitlines()[0] if message else "unknown issue"
        result = f"{table_id}: Quarto skipped ({warning}); wrote fallback page"
    else:
        result = None

    pdf = src_dir / "table-guide.pdf"
    if pdf.exists():
        shutil.copy2(pdf, dst_dir / "table-guide.pdf")

    return result


def main() -> int:
    root = repo_root()
    output_root = root / "website" / "_site"
    output_root.mkdir(parents=True, exist_ok=True)

    warnings = []
    for table_id, title in TABLES.items():
        try:
            warning = publish_table(table_id, title, root)
        except Exception as exc:  # Keep the site deployable even on unexpected input.
            warning = f"{table_id}: unexpected error ({exc}); skipped"
        if warning:
            warnings.append(warning)
            print(f"WARNING: {warning}", file=sys.stderr)
        else:
            print(f"Published {table_id}/table-guide.html")

    if warnings:
        print("Finished with warnings; site publication remains non-blocking.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
