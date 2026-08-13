# BENQODHI Workshop — Plan

**Workshop:** 10–11 September 2026 · JRC Ispra, Buildings 27B and 36
**Organisers:** Indaco Biazzo · Antonio Puertas Gallardo · Tobias Wiesenthal
**Coordination and logistics:** Ilse Verspreet
**Status:** working draft, v0.2 · revised 12 August 2026

This document tracks organisation of the workshop and the supporting GitHub repo/website.
It stays in `_internal/` so it is not published by the Quarto site.

---

## 1. Timeline

| When | Action |
|---|---|
| Now → Mon 17 Aug | Set up public GitHub repo, enable Discussions, Quarto site skeleton; seed Discussions with 1–2 example problems; draft speaker email |
| Tue 18 Aug | Send the speaker email (title/abstract ask + round-table problem prompt + link to Discussions) |
| Mon 24 Aug | Reminder nudge — most invitees back from summer break around this time |
| **Fri 28 Aug** | **Deadline: titles + abstracts back** (suggested; confirm with organisers) |
| 28 Aug → 4 Sep | Publish agenda with real titles as they arrive; curate Discussions input into candidate problems per Day 2 table |
| Fri 4 Sep | Freeze agenda and Day 2 table/participant allocation |
| 7–9 Sep | Practical-info email to participants (venue, hybrid link); test hybrid setup |
| 10–11 Sep | Workshop |

Open point: exact deadline date should be confirmed by the organisers — 28 Aug is a suggestion, chosen to land after most people are back from holiday and still leave ~10 days to finalise the agenda.

---

## 2. Day 2 structure (context, from the internal prep notes)

**Morning — parallel working tables, 09:00–10:30** (Building 36). Four working tables, not yet confirmed as final:

1. Large-scale bioinformatics/genomics optimisation and NP-hard problems
2. AI / QML
3. Radiotherapy and other hard health problems, medical imaging
4. Benchmark framework — instances, baselines, repository, reporting

Fallback if four tables prove infeasible: merge tables 1 and 2 into one bioinformatics/biological-networks table.

**Common output template**, one per scientific table (this is the template to reuse everywhere — shared doc, website problem pages, Day 2 output forms):

> use case → formal problem → data/instance provenance and scale → source of computational difficulty → candidate baselines → intended measures of success → what's ready vs. missing → named next action

Table 4 turns the other three tables' outputs into a shared framework note.

Indicative contributors per table (not final allocations): Table 1 — Kronenberg, Maurizio, Ponce-de-Leon; Table 2 — Zamponi, Mazzola, Wang; Table 3 — Mancini Terracciano, Reforgiato Recupero, Gonzalez Ballester; Table 4 — Ricci-Tersenghi, Palmisano, Spada, Dunjko (if confirmed). Daniel J. Egger will not be present on Day 2.

Facilitator/rapporteur pool (to be assigned): Zani, Bertolini, Chizzini, Leoni, Petrillo, Travagnin, Schuh, Curion, Ceresa, Consoli, Del Bono, Palmisano, Scala.

**Afternoon** (Building 36): quantum-lab visit 13:00–14:20, then the policy session 14:30–16:00, with a moderated round table 15:10–15:50 (DG CNECT, DG SANTE, DG DEFIS, DG RTD perspectives plus one scientific voice). Open items there: infrastructure/access speaker (EuroHPC JU / CINECA, tbc), research & innovation contact (awaiting reply from Carolina, DG assumed RTD), round-table moderator (Tobias or Indaco), and short interventions from Tolias (SANTE) and Domps (DEFIS).

All speaker titles on both days are currently "to be confirmed" — this is what the speaker email needs to resolve.

---

## 3. Speaker email

One combined email, sent once the repo/site/Discussions are live (so the links work).

**Ask 1 — talk details.** Title, 3–5 line abstract, and confirmation of slot length (30+10 min Q&A for Day 1 morning slots, 17+3 min for Day 1 afternoon slots).

**Ask 2 — Day 2 round table.** Ask speakers to start thinking of a candidate problem or open question for the Day 2 working tables / policy round table — just a seed idea, not a full write-up yet.

**Ask 3 — shared input.** Link to the GitHub Discussions where they can leave suggestions on structure, propose a problem, or comment on others' ideas in advance. For anyone who'd rather not use GitHub: offer to post on their behalf if they just reply by email.

**Deadline:** Friday 28 August for titles and abstracts (see §1).

I can draft the actual email text once you confirm the deadline and repo/Discussions link.

---

## 4. Shared pre-workshop input document

**GitHub Discussions** in the repo, since the repo is being set up anyway and it keeps contributions attributed, threaded, and easy to fold into problem pages later.

- Seed it with 1–2 example problems *before* sending the email — an empty forum gets no first post.
- Repo needs to be public for Discussions to work without adding friction (private repos require sign-in that many external invitees won't have set up).
- Offer the email-reply escape hatch (see §3, Ask 3) for anyone who won't use GitHub.

---

## 5. GitHub repo / website

Public repo, Quarto site published to GitHub Pages.

Minimum content for the site:

- **Workshop info pages** — agenda, speakers (titles/abstracts as they arrive), practical info (venue, hybrid link) — sourced from the existing agenda/leaflet docs, kept up to date as speaker details come in.
- **Problems section** — one page per candidate problem, using the common output template from §2 (use case / formal problem / instances / source of difficulty / baselines / metrics / ready-vs-missing / next action).
- **Contribute page** — how to propose a problem, with a link to Discussions.

`_internal/` (this file and similar planning material) stays out of the rendered site by virtue of the underscore prefix, which Quarto excludes by convention.

**On `draft/main.tex`:** it's raw material, not ready to publish as-is. Before any of it goes on the public site it needs conversion to markdown and a careful review — some of its claims about current state-of-the-art methods and benchmarks look like they need fact-checking rather than being taken at face value. Treat it as a starting point for the problem write-ups, not as source of truth.

---

## 6. Open items — not yet decided, don't pre-decide these

- Four-table vs. merged-table structure for Day 2 (§2)
- Facilitator/rapporteur assignment per table
- Policy session: infrastructure speaker, RTD contact, round-table moderator, Tolias/Domps slots
- Speaker titles/abstracts for both days
- Anything about benchmark-suite naming, code/data licensing, or long-term repo governance — deliberately out of scope until there's real content and real contributors to decide with; don't lock this in now.
