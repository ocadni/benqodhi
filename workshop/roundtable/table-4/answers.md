# Table 4 — Benchmarking methods and the repository

- **Date:** 11 September 2026
- **Participants:** Vito Palmisano, Mario Ceresa, Rene Chatwell
- **Note takers:** Luca Maria Del Bono, Federico Celauro
- **Rapporteur:** _to be confirmed_

## Answers to the table's questions

### Q1 — Comparing approaches

How should standard classical, AI-based, hybrid and quantum approaches be compared
on the same problems?

A comparison is only meaningful if it aggregates the **three dimensions that
jointly determine the result**: the structure of the problem, the algorithm and
the hardware it runs on. Reporting one of them without the others produces numbers
that cannot be interpreted, and certainly cannot be reproduced.

- **The hardware and the infrastructure are part of the result.** This is not only
  a matter of the processor: on HPC systems the interconnect alone can change the
  outcome of a benchmark. The execution environment must therefore be reported at
  the same level of detail as the algorithm.
- **AI-based methods must separate training from inference.** Training time is a
  real cost and must be counted, but it is amortized over many instances, so it
  has to be recorded separately from inference time rather than folded into a
  single figure.
- **The origin of the data matters, and must be declared.** Randomly generated
  instances and real-world instances are not interchangeable, and a problem whose
  data is natively quantum should be run on quantum hardware rather than compared
  through a classical re-encoding.
- **There is no free lunch, so there is no single ranking.** Different hardware
  excels at different tasks — especially in the quantum case — so approaches must
  be compared across a *diverse set of problem classes*. A comparison restricted to
  one class gives the false impression that one platform works for everything.
  Classes to cover include QUBO problems, constraint satisfaction problems,
  continuous problems and natively quantum problems.

To keep comparisons honest, **the solutions to part of the instances must not be
published**. A held-out set of instances with private solutions is what allows a
proposed algorithm to be verified independently, and it prevents an ML method from
simply being trained on the full set of published solutions.

### Q2 — What to measure

Which measures matter most: solution quality, running time, efficiency, energy
consumption, resources used, reproducibility?

The three quantities the table converged on are **time, cost and accuracy**. Cost
is the difficult one: it depends on the architecture and cannot be established a
priori, so it has to be reported rather than assumed, in both a static and a
dynamic form, and the figures need to be refreshed regularly as prices change.

Rather than a fixed metric, the table's proposal is a **checklist that a "good"
benchmark entry must fill in** — effectively a benchmark of the benchmark. The
checklist is organized in tables covering:

- **Structure of the problem** — theoretical complexity (for example NP-hardness),
  the nature of the solution space (such as its smoothness), whether the problem is
  continuous or discrete, the range of problem sizes, and the origin of the data
  (random versus real-world).
- **The algorithm in the abstract sense** — theoretical complexity and expected
  performance.
- **The algorithm in the practical sense**, which is where the hardware enters —
  throughput, accuracy and, for quantum hardware, noise level, energy and
  efficiency, and cost both static and dynamic, with prices kept up to date
  (possibly with automated help, for example via LLMs).
- **Reproducibility information** — solver and library versions, parameters, seeds,
  and the execution environment including the interconnect where relevant.

For AI-based entries the checklist must carry training and inference figures in
separate fields, and for stochastic methods the number of runs and the success
rate, since a single best run is not a measurement.

### Q3 — Online and credible

What is the simplest route to put benchmark material online, and who should
maintain or review it?

The simplest route is a **public repository organized around the checklist**: per
problem, a clear description, the instance files or links to the data, the
structure-of-the-problem table, at least one baseline, the metrics, a license and a
named owner. The checklist is what makes the entries comparable, and what makes it
obvious when an entry is incomplete.

Two design choices matter from the first release:

- **A private held-out set.** The repository publishes the instances but withholds
  the solutions for a subset of them, so that submitted algorithms can be verified
  and cannot be trained on the answers.
- **Maintained cost figures.** Cost and price information ages quickly and must be
  owned by someone and revised on a regular cycle, otherwise the entries silently
  become misleading.

The smallest credible first release is one problem class with one curated instance
set, one classical baseline, one checker and a held-out subset, published with a
fixed date and a named owner.

## Conclusions for the recap

- **Strongest conclusions:** a benchmark result only means something if problem,
  algorithm and hardware are reported together; there is no free lunch, so the
  repository must cover diverse problem classes rather than produce a single
  ranking; and part of the solutions must stay private.
- **Main infrastructure need:** a public repository built around a shared checklist,
  with per-problem tables, baselines, and a held-out set of instances whose
  solutions are not published.
- **Why it matters:** without a common checklist, results across classical, AI,
  hybrid and quantum approaches are not comparable, and a benchmark covering only
  one problem class would suggest that one platform is best at everything.
- **Most important missing piece:** an agreed checklist, and an owner for the cost
  and price information, which needs regular updating.
- **Next action:** draft the checklist as concrete tables and apply it to one
  problem class as a first release, with a named owner and a target date.
- **Transversal next-step advice:** start from the checklist and one problem class,
  and grow the repository through clear ownership, review and maintenance roles.

## Summary of the discussion

A good benchmark should be able to aggregate the different elements that come into
play: the structure of the problem, the algorithm and the hardware. For this
reason, people should be able to use a **checklist** of the things that must be
included in a "good" benchmark.

The first point is the **diversity of problems**. Since different hardware excels
at different tasks — especially in the quantum case — the benchmark needs enough
coverage not to give the false impression that there is a one-for-all hardware that
works for everything: there is no free lunch. Classes of problems to cover include
QUBO problems, constraint satisfaction problems, continuous problems and natively
quantum problems.

The database should then include information, in the form of tables, on:

- **Structure of the problem:** complexity (for example NP-hardness), the solution
  space (for example its smoothness), continuous versus discrete, problem sizes,
  and the origin of the data (random versus real-world).
- **Information about the algorithm**, both in the abstract and in the practical
  sense:
  - *abstract side:* theoretical complexity and performance;
  - *practical side*, especially on the hardware: throughput, accuracy and noise
    level for quantum hardware, energy and efficiency, and cost both static and
    dynamic — reported at the time and kept updated, since prices are subject to
    regular revision, possibly with automated help such as LLMs.

On comparing approaches specifically: HPC infrastructure matters, and even the
interconnect has an effect on the benchmark. For AI-based algorithms, training time
must be taken into account, recording training and inference separately. The origin
of the data also matters — if it is quantum, the work should be done on quantum
computers.

The quantities one wants out of a benchmark are **time, cost and accuracy**. Cost
is related to the architecture, but it is not established a priori.

Finally, the benchmark should **not publish the solutions to all the instances**: a
group of instances should have its solutions kept private, so that proposed
algorithms can be verified and so that ML methods cannot be trained on the whole
set of solutions.
