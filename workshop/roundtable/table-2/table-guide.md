# Table 2 — Medical Imaging, Diagnostics, Machine Learning and QML

**BENQODHI Day 2 morning round tables · 11 September 2026**

*Printable guide for the table.*

---

## Aim of the round tables

Collect focused expert input for a possible BENQODHI output (paper, report,
roadmap or policy note). The central question is how important challenges in
health and the life sciences can become **credible, reusable benchmarks** for
classical, AI-based, hybrid and quantum algorithms.

The preferred focus is **optimization** problems, but the discussion is not
restricted to them: inference, sampling, simulation, reconstruction and learning
problems also count when they have a clear health or life-science motivation and a
plausible route to benchmarkability.

We are **not** building the benchmark repository during the workshop. The goal is
to identify which problems would make a future benchmark repository useful.

## The discussion path

> **health or life-science challenge → computational bottleneck → candidate
> benchmark → available evidence and missing pieces → fair comparison of
> algorithms → next benchmark-building action**

## How the table will work

This table uses an experimental setup: the main value remains the in-person expert
discussion, enriched by lightweight AI-assisted note taking. The aim is to preserve
the value of live discussion while using new AI tools to help capture, organize and
enrich the results.

A suggested way to organize the work is to have one note taker at the blackboard,
writing the main points of the discussion so everyone can see, correct and refine
the emerging answers together. Another note taker can keep `answers.md` open on a
laptop, using Kiro, VS Code or another AI-assisted editor if useful. The laptop
note taker can use the blackboard, the live discussion and, when useful, help from
LLMs or internet searches to improve, expand and clarify the written answers. The
group is small, so the table can self-organize and share these roles naturally
among note takers and participants. The text should be reviewed continuously by the
table, corrected when needed and finalized by the participants before the end of
the session.

At the end, the final `answers.md` is committed and pushed to the repository, so it
becomes visible online. The table also chooses one rapporteur, who presents the
results in the plenary after the coffee break, using the finalized answer document
as the basis for the presentation. The document can also be projected in the room
during the presentation.

## This table's role

Identify candidate imaging, diagnostic, ML and QML problems that could become
benchmarkable. First collect possible candidates from the table's own expertise.
If useful, then consult the problem prompts at the end of this guide and the
[problem brief](../../../website/roundtables/seed-problem-brief.qmd). Select the
strongest candidates and answer the questions for each.

## Questions to answer

### For each selected candidate problem (aim for 2–3 candidates)

1. **Problem** — What health or life-science problem should be benchmarked, and why
   does it matter?
2. **Bottleneck** — What is hard computationally?
3. **Moving ahead** — What is missing, and what is the next practical step?

### Transversal reflection — answer once for the table

Discuss freely and focus on the aspects where your table has the most useful
experience, concerns or advice.

Given the three pillars — **infrastructure**, **community** and **governance** —
what advice, suggestions or lessons from experience would you give for the next
steps after the workshop, so that BENQODHI can become a living benchmark
repository and produce useful final outputs? For example, what would be enough to
start — such as a GitHub repository with a simple website, templates and a few
benchmark candidates — and what should be the longer-term goal?

## Expected output

- a short list of selected candidate problems;
- for each candidate, short answers to the three questions above;
- one short transversal reflection on next steps for the project.

---

*Note takers: draft answers live into `answers.md` in this folder. Rapporteur:
report the main conclusion, main candidate problem, why it matters, the most
important missing piece, the next action, and the transversal next-step advice.*

## Problem prompts for discussion

*Use these only after starting from the table's own expertise and judgment.*

- medical image reconstruction, segmentation, classification or generation;
- quantum machine-learning approaches for imaging, diagnosis or biomedical data
  analysis;
- explainable machine learning in health, including feature selection, rule
  extraction and interpretable model compression;
- Boltzmann-machine, QBoost-style, diffusion-model or related model families
  attached to a concrete biomedical target;
- diagnostic inference and uncertainty quantification.

**Focus:** identify which ML, QML, imaging or diagnostic problems are concrete
enough to become fair and useful benchmarks, and which remain too abstract.
