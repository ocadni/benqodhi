# Table 4 — Benchmarking methods and the repository

> **This file is a worked EXAMPLE.** It shows the level of detail expected from a
> note taker. The content below is illustrative, not an agreed workshop position.
> Replace it with the table's real conclusions.

- **Date:** 11 September 2026
- **Note takers:** A. Example, B. Example
- **Rapporteur:** C. Example

## Answers to the table's questions

### Q1 — Comparing approaches

How should standard classical, AI-based, hybrid and quantum approaches be compared
on the same problems?

Example answer: a comparison is only honest if the **target is fixed in advance**:
a common problem definition, the same instances and a stated solution-quality
target, for example "reach within 1% of the best known value". Quantum, hybrid and
AI results should always be compared against genuinely strong, well-tuned classical
baselines, not weak or default implementations.

### Q2 — What to measure

Which measures matter most: solution quality, running time, efficiency, energy
consumption, resources used, reproducibility?

Example answer:

- **solution quality** achieved, including objective value and gap to best known;
- **time to reach the target**, using wall-clock time and reporting the hardware;
- **resources used**, including cores, GPUs, QPU shots and, where available, energy;
- **number of runs and success rate**, since heuristic and quantum methods are often
  stochastic;
- **reproducibility information**, including solver version, parameters and seed.

### Q3 — Methods to include

From your point of view, which best current methods and new approaches should be
included?

Example answer: each benchmark should include at least one strong classical solver
or heuristic, one transparent reference implementation and, when relevant, AI-based,
hybrid or quantum approaches. New methods should be accepted only when their setup,
parameters and hardware assumptions are reported clearly enough to reproduce or
audit the result.

### Q4 — Online and credible

What is the simplest route to put benchmark material online, and who should
maintain or review it?

Example answer: start with a **public repository** with, per problem, a clear
description, instance files or data links, at least one baseline, the metrics, a
license and a named owner. The smallest first release could be one problem class
with one curated instance set, one classical baseline and one checker, published
with a fixed date and an owner.

## Conclusions for the recap

- **Strongest conclusions:** a fair comparison needs fixed targets, honest reporting
  and strong classical baselines; "online" should start small and versioned, not
  comprehensive.
- **Main infrastructure need:** a public, versioned repository with per-problem
  baselines and automatic checkers.
- **Why it matters:** without agreed reporting and strong baselines, claims of
  progress cannot be trusted or reproduced.
- **Most important missing piece:** owners for the first release and an agreed
  minimum reporting format.
- **Next action:** commit to one problem class as a first release, with a named owner
  and a target date.
- **Transversal next-step advice:** start with a minimal useful repository and grow
  it through clear review, credit and maintenance roles.

## Transversal reflection

Given the three pillars — infrastructure, community and governance — what advice,
suggestions or lessons from experience would you give for the next steps after the
workshop, so that BENQODHI can become a living benchmark repository and produce
useful final outputs?
