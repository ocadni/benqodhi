# Round-table outputs (Day 2 morning)

Working documents produced by the note takers during the Day 2 morning round
tables (11 September 2026). These are the raw material for a possible BENQODHI
paper, report, roadmap or policy note, and for the Day 2 closing sessions.

## How this folder is used

- Each table has its **own subfolder** (`table-1/` … `table-5/`).
- Each table has **one or two note takers** working on a laptop with an AI-assisted
  editor (for example Kiro or VS Code).
- Each subfolder starts with an `answers.md` file that already contains the table's
  questions from the
  [round tables page](../../website/roundtables/index.qmd) — the job is to
  fill in the answers and the conclusions live during the session.
- A table may add **as many notes files as it finds useful** — for example a
  second notes file or a per-candidate file. This lets more than one person work in
  the same table folder at the same time without editing the same file.
- At the end of the session, **push the completed files to this repository**.

## Structure

| Folder | Table |
|---|---|
| [`table-1/`](table-1/) | Genomics, molecular biology and life sciences |
| [`table-2/`](table-2/) | Medical imaging, diagnostics, machine learning and QML |
| [`table-3/`](table-3/) | Mechanistic medicine, clinical decisions and operational optimization |
| [`table-4/`](table-4/) | Benchmarking methods and the repository — **worked example** |
| [`table-5/`](table-5/) | Infrastructure, community and policy instruments |

- [`answer-template.md`](answer-template.md) — blank template if you need to start a
  fresh document.
- `table-N/table-guide.md` — the table's own questions and short guide, extracted from the
  [round tables page](../../website/roundtables/index.qmd) so each table has
  only what it needs on the table.
- Regenerate the PDFs with `python3 build_table_guides_pdf.py` (needs `markdown` and
  `weasyprint`) if you need local copies.
- During the GitHub Pages build, printable PDFs are restored from cache or regenerated
  for changed/missing `table-guide.md` sources, then copied into the published site.
- [`table-4/answers.md`](table-4/answers.md) is filled in as an **example** to show
  the level of detail expected. The other tables are placeholders ready to
  complete.
