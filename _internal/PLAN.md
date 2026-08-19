# BENQODHI Workshop — Plan

**Workshop:** 10-11 September 2026 · JRC Ispra, Buildings 27B and 36  
**Organisers:** Indaco Biazzo · Antonio Puertas Gallardo · Tobias Wiesenthal  
**Coordination and logistics:** Ilse Verspreet  
**Status:** working draft, v0.3 · revised 17 August 2026

This document tracks organisation of the workshop and the supporting GitHub
repo/website. It stays in `_internal/`, so it is not published by the Quarto site.

---

## 1. Current status

### Done

- Public GitHub repo exists: <https://github.com/ocadni/benqodhi>
- Quarto website is set up and renders locally with `./run.sh render`.
- GitHub Pages publishing through GitHub Actions is working.
- `gh-pages` branch has been initialized.
- Homepage has been simplified and visually improved.
- Homepage subtitle now uses the BENQODHI acronym expansion:
  **BENchmarking Quantum Optimization: from Datasets to Health Innovation**.
- Speakers page has been removed from the public website.
- Contribution page now uses a simple "share an idea" flow.
- GitHub Issues are used for pre-workshop ideas, with label `workshop-idea`.
- Two seed issues are open:
  - Haplotype phasing as a candidate benchmark:
    <https://github.com/ocadni/benqodhi/issues/1>
  - Proposal for Day 2 expert tables:
    <https://github.com/ocadni/benqodhi/issues/2>

### Current public site structure

- Home
- Workshop
- Program
- Problems
- Contribute

No separate Speakers page is currently planned. Speaker titles and abstracts can be
added directly to the Program page when available.

---

## 2. Immediate next step

The next important action is to write and send the speaker/participant email.

The email should ask for:

1. **Talk title and abstract**
   - title;
   - 3-5 line abstract;
   - confirmation of talk slot.

2. **One optional pre-workshop idea**
   - a candidate benchmark problem;
   - a suggestion for the Day 2 expert tables;
   - a panel/discussion question;
   - a useful dataset, metric, baseline or reference.

3. **Use the contribution page**
   - link to the website contribution page;
   - link to existing submitted ideas;
   - email fallback for people who do not want to use GitHub.

Suggested deadline for titles and abstracts: **Friday 28 August 2026**.

Open point: confirm whether this is the deadline to use before sending the email.

---

## 3. Updated timeline

| When | Action |
|---|---|
| Done | Set up public repo, Quarto site, local run script, GitHub Pages deployment |
| Done | Create simple contribution page and seed GitHub Issues |
| Next | Draft speaker/participant email |
| Tue 18 Aug | Send email asking for title, abstract and optional contribution idea |
| Mon 24 Aug | Reminder nudge |
| **Fri 28 Aug** | **Suggested deadline: titles and abstracts back** |
| 28 Aug-4 Sep | Add confirmed titles/abstracts to Program page; review submitted ideas |
| Fri 4 Sep | Freeze agenda and Day 2 table format/participant allocation |
| 7-9 Sep | Practical-info email to participants; test hybrid setup |
| 10-11 Sep | Workshop |

---

## 4. Day 2 structure

Current proposal: small expert tables during the Day 2 morning session.

- Around **3-4 experts per table**.
- Start with **three provisional tables**.
- Leave room for **at least one additional table** if participants suggest a useful
  theme.

### Proposed tables

1. **Bioinformatics and biological data problems**
   - genomics, biological networks, sequence comparison, phasing, alignment,
     metabolic networks.

2. **Health optimization problems**
   - radiotherapy planning, medical imaging workflows, resource allocation,
     scheduling, logistics or other clinical optimization problems.

3. **Benchmark organisation, measures and governance**
   - datasets and instances, baselines, metrics, resource accounting, repository
     structure, and fair comparison of classical, AI-based, hybrid and quantum
     methods.

Possible fourth table:

- machine learning / QML, if participants can frame these cases clearly as
  optimization benchmarks;
- quantum/hybrid methods and infrastructure;
- another theme proposed through the contribution page.

### Roles

Each table could have:

- a **facilitator**, to keep discussion focused and inclusive;
- a **rapporteur**, to capture main points and prepare a short plenary recap.

### Shared table template

Problem-oriented tables could fill a short template:

> candidate problem/theme -> biological or health use case -> optimization
> formulation -> data or instances -> baselines -> metrics -> what is missing ->
> next step

The benchmark/governance table could fill:

> minimum benchmark metadata -> metrics and reporting rules -> resource accounting ->
> repository structure -> open decisions after the workshop

---

## 5. Pre-workshop ideas

Ideas live as GitHub Issues:

- Submit form:
  <https://github.com/ocadni/benqodhi/issues/new?template=workshop-contribution.yml>
- Read submitted ideas:
  <https://github.com/ocadni/benqodhi/issues?q=is%3Aissue%20label%3Aworkshop-idea>

Keep this lightweight. The workshop is small, so the goal is not a large discussion
forum. The goal is simply to collect useful seed ideas before the meeting.

If someone does not want to use GitHub, they can reply by email and the organisers can
collect or post the idea on their behalf.

---

## 6. Website and repo notes

- Public website source lives in `website/`.
- Generated site lives in `website/_site/` and is ignored.
- Local rendering:
  - `./run.sh render`
  - `./run.sh preview`
- Contribution issue template:
  `.github/ISSUE_TEMPLATE/workshop-contribution.yml`
- Internal planning material lives in `_internal/` and is not published.

`_internal/draft/main.tex` is raw material for candidate problems. It should not be
published as-is. Use it as a starting point, then review and fact-check before turning
content into public problem pages or GitHub issues.

---

## 7. Open items

- Confirm the title/abstract deadline before sending email.
- Draft and send the speaker/participant email.
- Decide whether Day 2 uses 3 tables or adds a 4th table.
- Assign facilitators and rapporteurs.
- Confirm whether machine learning/QML belongs in its own table.
- Confirm whether health resource allocation belongs in the health optimization table.
- Policy session: infrastructure/access speaker, RTD contact, round-table moderator,
  and short interventions still need confirmation.
- Add confirmed titles and abstracts to the Program page.
- Curate submitted GitHub Issues into Day 2 table preparation notes.
- Later: convert selected candidate problems into public problem pages.
