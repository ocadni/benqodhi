# Table 4 — Benchmarking methods and the repository

> **This file is a worked EXAMPLE.** It shows the level of detail expected from a
> note taker. The content below is illustrative, not an agreed workshop position.
> Replace it with the table's real conclusions.

- **Date:** 11 September 2026
- **Note takers:** A. Example, B. Example
- **Rapporteur:** C. Example

## Answers to the table's questions

### Q1 — Fair comparison across methods

*When the same problem is tackled by classical, AI-based, hybrid and quantum
methods, what has to be agreed so the comparison is honest, and what should be
measured?*

The table agreed that a comparison is only honest if the **target is fixed in
advance**: a common problem definition, the same instances, and a stated
solution-quality target (for example, "reach within 1% of the best known value").
Against that fixed target, submissions should report:

- **solution quality** achieved (objective value, and gap to best known);
- **time to reach the target** (wall-clock), plus the hardware used;
- **resources** consumed — cores/GPUs/QPU shots, and, where available, energy;
- **number of runs and success rate**, since heuristic and quantum methods are
  stochastic — report a distribution, not a single best run;
- **full configuration** (solver version, parameters, seed) for reproducibility.

Strongest point raised: the most common way comparisons mislead is a **weak
classical baseline**. A quantum or AI result only means something against a
genuinely strong, well-tuned classical solver, so baselines must be named and
reproducible.

### Q2 — Good benchmark instances

*How should problem instances be chosen so the benchmark is meaningful and not
trivially settled by one type of method?*

- Instances should span a **difficulty range**, with sizes that actually stress
  each platform — small enough to run on current quantum hardware, large enough to
  be hard for classical solvers.
- Include a mix of **generated** instances (with controllable hardness) and
  **real-world / domain** instances from Tables 1–3, so the benchmark keeps health
  meaning.
- Each instance set needs a **best-known solution or bound** and a **checker** so
  results can be validated automatically.
- Avoid instances that a good classical heuristic settles instantly — they make the
  benchmark look easy and hide real differences.

### Q3 — "Online" in practice, and versioning

*What does "online" mean in practice for BENQODHI, how should instances and results
be versioned, and what is the smallest first release the group can commit to with a
date?*

- "Online" means a **public repository** with, per problem: a clear description,
  the instance files, at least one classical baseline, the metrics, a license, and a
  named owner — following the style of an existing open benchmarking library as a
  template.
- **Versioning:** instances and result tables get version tags; a result always
  records which instance version and which solver version it used, so past
  comparisons stay valid when instances are added or corrected.
- **Smallest first release:** one problem class with one curated instance set, one
  classical baseline and one checker, published with a fixed date and an owner —
  something concrete people can point to, then grow.

## Conclusions for the recap

- **Strongest conclusions:** a fair comparison needs a fixed target + honest
  reporting (quality, time, resources, runs) and, above all, a strong classical
  baseline; "online" should start small and versioned, not comprehensive.
- **Main infrastructure need:** a public, versioned repository with per-problem
  baselines and automatic checkers.
- **Why it matters:** without agreed reporting and strong baselines, "quantum
  advantage" claims cannot be trusted or reproduced.
- **Most important missing piece:** owners for the first release and an agreed
  minimum reporting format.
- **Next benchmark-building action:** commit to one problem class as a first
  release, with a named owner and a target date.

## Transversal governance answer

The table's outputs stay credible if every accepted benchmark has a **named owner**
and passes a light **review** (baseline is strong, instances are valid, reporting is
complete) before it is listed. The table's community should act as the first
reviewers and maintain the minimum reporting standard, revisiting it as classical
and quantum methods evolve.
