#!/usr/bin/env python3
"""Publish workshop presentations into the rendered Quarto site."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


PUBLIC_EXTENSIONS = {
    ".css",
    ".gif",
    ".html",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".map",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".svg",
    ".ttf",
    ".webp",
    ".woff",
    ".woff2",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def is_generated_support_file(path: Path) -> bool:
    return any(part.endswith("_files") for part in path.parts)


def should_copy(path: Path) -> bool:
    return is_generated_support_file(path) or path.suffix.lower() in PUBLIC_EXTENSIONS


def render_quarto_decks(presentations_dir: Path) -> None:
    quarto = shutil.which("quarto")
    qmd_files = sorted(presentations_dir.rglob("*.qmd"))

    if qmd_files and not quarto:
        raise RuntimeError("quarto not found on PATH; cannot render presentation .qmd files")

    for qmd in qmd_files:
        print(f"Rendering presentation deck: {qmd.relative_to(repo_root())}")
        subprocess.run([quarto, "render", str(qmd)], check=True)


def publish_assets(source_dir: Path, output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)

    for source in sorted(source_dir.rglob("*")):
        if not source.is_file() or not should_copy(source):
            continue

        relative = source.relative_to(source_dir)
        destination = output_dir / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def main() -> int:
    root = repo_root()
    presentations_dir = root / "workshop" / "presentations"
    site_dir = root / "website" / "_site"
    output_dir = site_dir / "presentations"

    if not presentations_dir.exists():
        print("No workshop presentations directory found; nothing to publish.")
        return 0

    if not site_dir.exists():
        print(f"ERROR: rendered site directory does not exist: {site_dir}", file=sys.stderr)
        return 1

    render_quarto_decks(presentations_dir)
    publish_assets(presentations_dir, output_dir)
    print(f"Published presentations to {output_dir.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
