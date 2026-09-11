# Table 3 — Mechanistic medicine, clinical decisions and operational optimization

- **Date:** 11 September 2026
- **Note takers:** Sergio Consoli
- **Rapporteur:** Diego Reforgiato

Shortlist of candidate problems discussed at the table. For
each candidate we answer the three questions from the table guide (problem,
bottleneck, moving ahead).

## Candidate 1 — Molecular docking as a conflict/compatibility graph (main candidate) - Main contact: Gabriele Spada

- **Problem:** Predict how a ligand binds a receptor, cast as a graph problem
  (maximum-weight clique / maximum independent set over a ligand–receptor
  compatibility graph or QUBO problem). It matters for drug discovery, and
  it is the most physically "quantum-native" of the candidates: some formulations
  map naturally onto neutral-atom hardware. Molecules are represented through
  simplified abstractions — pharmacophore points, and contact/effective potentials rather than full atomic
  dynamics.
- **Bottleneck:** The problem is NP-hard. Combinatorial matching explodes as soon
  as the number of pharmacophore points grows, so larger ligands quickly exceed
  what current hardware can hold. The literature focuses on small ligands and
  simplified instances precisely because of the limited qubit counts and the size
  of the QUBO/MIS encoding.
- **Moving ahead:** Build a public repository of easy, well-characterized instances
  with simplified ligand-point data and classical reference solutions, so that
  classical, quantum-annealing and gate-based solvers can be compared on the same
  footing. Because quantum algorithms return statistical answers, success rate
  (e.g. how many times the correct solution appears out of ~2000 shots) is a good
  metric, rather than raw time-to-solution. Open expert question: how should
  graph-objective quality be connected to physical docking validity?

## Candidate 2 — Context-specific metabolic network extraction / reconstruction - Main contact: Miguel Ponce de Leon

- **Problem:** **Problem:** Constraint-based (stoichiometric) modelling of the human metabolic network. Cells express only a subset of the genome-encoded network, so gene and protein expression data must be integrated with stoichiometric mass-balance constraints, thermodynamic information and gene–protein–reaction rules to extract an active, consistent, context-specific model. This is relevant to cancer metabolism, tissue-specific models and drug-target discovery. The same machinery can also be used to infer the metabolic network of a newly discovered organism from candidate reactions derived from genome annotations, enabling predictions of metabolic capabilities, minimal media, growth rates and essential genes.
- **Bottleneck:** The gap-filling / reaction-selection step becomes a mixed-integer linear program with tens of thousands of variables and up to ~50,000 constraints, pushing CPLEX and Gurobi to their limits as the combinatorial search space and number of alternative optima increase (MILP is NP-hard). Separately, sampling the high-dimensional allowed flux space is non-trivial: the feasible polytope can be extremely elongated and non-uniform, so Monte Carlo and simplex-style moves can mix very slowly because random steps easily leave the polytope. Efficient exploration requires selecting directions compatible with the constraints, while the geometry and large diameter of the polytope make uniform sampling computationally challenging.
- **Moving ahead:** Freeze a model version and preprocessing, then define the exact MILP / reaction-selection objective for the benchmark (expert judgment needed here). Anchors exist: Recon3D, Human-GEM/Human1, BiGG, MEMOTE, GTEx/TCGA and COBRA-style tooling. A stochastic sampler that works efficiently in high-dimensional, non-uniform, bottlenecked spaces — capturing the fluctuation of the data rather than a single unique solution — would already be a major improvement. A QUBO formulation provides a natural interface to quantum annealing and gate-based variational algorithms, but straightforward encodings can require thousands of binary variables and introduce substantial penalty terms. This makes direct solution of genome-scale instances unrealistic on current hardware, while leaving open the question of whether reduced or structured, biologically realistic instances exhibit useful quantum scaling.

## Candidate 3 — Radiotherapy beam-angle / beamlet / aperture selection - Main contact: Carlo Mancini Terracciano

- **Problem:** Optimize radiotherapy treatment planning: deliver a dose as uniform
  as possible to the tumour target while sparing healthy tissues and organs.
  Clinically, typically ~95% of the tumour should receive the prescribed dose while
  limiting maximum exposure to healthy systems. It is clinically meaningful (e.g.
  prostate re-treatment after ~5 years is plausible) and already linked to hybrid
  optimization work.
- **Bottleneck:** Hundreds of thousands of decision variables — beam orientations,
  energies, intensities, machine shifts, location and timing. The objective is
  noisy, non-convex and riddled with local minima; the discrete slice
  (beam-angle / beamlet / aperture) is NP-hard. Simulating the ~100 qubits a
  faithful quantum formulation would need is currently infeasible.
- **Moving ahead:** Package a public discrete instance with frozen dose-influence
  matrices and a fixed inner protocol (matRad, CORT, TROTS, OpenKBP as anchors),
  using public segmentation structures to keep real-world complexity while avoiding
  sensitive patient data. A first challenge is producing a quantum-digestible
  formulation of the voxel-based dose problem. Rather than a single scalar cost,
  computing the Pareto surface lets the doctor make empirical, patient-specific
  decisions (e.g. by age). Expert judgment needed: which discrete slice keeps enough
  clinical meaning while staying fair for algorithm comparison?

## Candidate 4 — Home health care routing and scheduling - Main contact: Diego Reforgiato Recupero,

- **Problem:** Assign and route caregivers to patients (home health care) under
  skills, time windows, synchronization, precedence and continuity constraints —
  a real health-logistics problem with direct operational value. Related to
  hospital routing where the objective can also be to minimize the probability of
  spreading infection (two people should not be in the same place).
- **Bottleneck:** Discrete variables plus continuity/synchronization constraints
  create a labyrinth-like feasible space where the vast majority of points are
  disallowed; the more constraints included, the higher the complexity. Classical
  stochastic exploration is slow and risky because a wrong move violates a
  constraint without progressing. Lagrangian relaxation breaks down with thousands
  of variables and constraints, so interior-point or stochastic methods are needed.
  For very large instances the true optimum is unreachable, so robust "good enough"
  solutions (stable under 10–20% changes in parameters/population, maximizing margin
  to the feasibility boundary) matter more than strict optimality.
- **Moving ahead:** A benchmark is missing — classical OR instances exist
  (Mankowska–Meisel–Bierwirth instances, University of Halle data), but a
  quantum/hybrid track needs a formulation. Start from the smallest realistic
  subproblem that still keeps the essential health-care constraints. A QUBO
  formulation is possible in principle (for quantum annealers or ML solvers), as are
  iterative hybrid classical–quantum algorithms; a related smart-grid optimization
  was mapped using Grover (quadratic speedup), though annealing may do better.

## Candidate 5 — Constrained routing / random walks in complex, bottlenecked spaces - Main contact: Federico Ricci-Tersenghi

- **Problem:** A more foundational, statistical-mechanics framing of routing under
  strong constraints (hospital infection control, supply distribution during crisis
  events). The open question: how does a stochastic process behave when the feasible
  space is high-dimensional (say a thousand dimensions) but only a few directions are
  actually allowed — an ideal random walker trapped in a bottlenecked labyrinth?
- **Bottleneck:** With strong constraints the cost function is dominated by the
  constraints, and classical random walks either get stuck or waste time crossing
  infeasible regions. Exploring such low-effective-dimension spaces embedded in a
  huge ambient space is where a quantum advantage might plausibly appear.
- **Moving ahead:** This is the least benchmark-ready candidate — a benchmark is
  missing and it is far from obtainable. A promising idea: reformulate the
  constraint-space random walk so quantum interference explores through disallowed
  regions and integrates only paths that stay in allowed regions (Monte-Carlo-like),
  with parallel workers examining multiple directions at once. Largely unexplored.

## Conclusions for the recap

- **Strongest conclusions:** All five candidates are, at heart, optimization
  problems in high-dimensional spaces, and it was good to brainstorm them — but a
  clear quantum advantage is still an open question. A recurring worry: since one
  can pick any small instance of any optimization problem, what is the added value
  of framing it as a biological problem rather than just a mixed-integer program?
- **Main candidate problem:** Molecular docking.
- **Why it matters:** It already has a quantum formulation, some simple benchmarks
  exist, and it is the most physically quantum-native of the candidates.
- **Most important missing piece:** The hardware — number of qubits, noise levels,
  and accessibility of hardware (e.g. via EuroHPC). Current hardware is noisy, which
  pushes the focus toward QUBO-style formulations.
- **Next benchmark-building action:** Write a white paper, and stand up a public
  repository with code, a toy example and classical reference solutions so quantum
  and non-quantum solvers can be compared (using success rate as a key metric).
- **Transversal next-step advice:** To compare quantum computers fairly against
  commercial solvers, benchmark on standard mixed-integer optimization problems with
  proper scaling analysis first, then connect results back to the health/life-science
  applications afterwards.

## Transversal reflection

Given infrastructure, community and governance, the table's advice is pragmatic.
On **infrastructure**, the main blocker is hardware: current quantum machines are
small, limited in qubits and noisy, so near-term work should target QUBO-friendly
formulations and lean on simulators/emulators. EuroHPC already offers accessible
quantum resources (photonic ~8 qubits, neutral-atom ~140 qubits, superconducting
~20 qubits, and quantum annealers, hosted in Bologna, France and Barcelona);
compute hours can be requested through calls, provided applicants show seriousness
and prior emulation/simulation results — a far cheaper route than purchasing
hardware (roughly 5–50 million).

On **community and governance**, enough to start would be a GitHub repository with
a simple website, answer/instance templates, and a few benchmark candidates —
each shipped with a toy example, classical reference solutions, complexity metrics
and clear success-rate metrics so results stay comparable and trustworthy. The
longer-term goal is a living, curated repository seeded with standard optimization
benchmarks (for fair scaling comparisons) that then link back to concrete health
applications such as docking, metabolic-model extraction and radiotherapy planning.
A candid note for governance: quantum computing here remains futuristic, with no
demonstrated advantage yet, so benchmarks should be honest about noise limitations
and avoid overclaiming supremacy.
