<!--
FILLABLE TEMPLATE — Table 2 scratch notes.
HOW TO USE: type after each `:` or on the empty `-` lines. Tick boxes with [x].
Leave blanks empty if not discussed — Kiro will flag gaps.
Fields marked (*) are required by answers.md.
-->

# Table 2 — SCRATCH NOTES

**Date:** 11 September 2026
**Note taker:** Lea Schuh
**Rapporteur:**

Most benchmarking problems are "artificial" and not only classical vs. quantum but also quantum vs. quantum
atom and small molecules Sch. Eq is solvable through DFT. Quantum chemistry could benefit from quantum computing.

let us focus on quantum vs. quantum benchmarking problems,
---

# CANDIDATE 1

**Name (*): benchmarks medical imaging quantum generative and classification models

**Domain:**
- [ ] imaging: reconstruction
- [ ] imaging: segmentation
- [ ] imaging: classification
- [ ] imaging: generation
- [ ] QML
- [ ] explainable ML / feature selection / rule extraction
- [ ] diagnostic inference / uncertainty quantification
- [ ] other:

**Benchmark shape (*)** — what exactly is optimized?
- Objective: 
- Decision variables: vectors of 3D numbers for each image
- Constraints: encoding each image to be loaded is very hard for a quantum computer. Error correction for each qbit would require 1000s of classical bits of memory (general to all applications).
- Separate tracks (if any): image loading for large amount of images is a challenge

**Why it matters (*)**
- medical imaging is a continuusly evolving fields since the physical mechanisms behind can also be improved, so are the diagnostics and detection. needles in the haystack problems that could benefit from quantum computing.

**Available material**
- Datasets / instances: radiomics (vector for each image) --> feature selection process.
- Baselines: benchmark for just tolerance or 
- Metrics: 
- Prior work / tools named:

**What is computationally hard (*)**
-

**Fair-comparison risks**
- quantum ml and computing is to be benchmarked to classical omologues, but they are also evolving. Need to have benchmark problems for which the classical approach already saturated.

**Missing pieces (*)** — what must be built or frozen?
- both creating and maintenance of the benchmark is an issue. But maintenance is a long-term issue

**Readiness label:**
- [ ] ready / near-ready
- [ ] promising
- [ ] formulation needed
- [ ] asset / infrastructure
- [ ] control / caution


**Expert judgment needed** — open question for the table:
- 

**Next practical step (*)**
- Action: what is the best detail of the distribution that generates the best QBo? Which detail is the hardest to be spotted from classical techniques? experiment of same radiomics analysed by means of classical and quantum machine. Runtime is not the problem, but quality of discovery. 
- Owner:

**Verdict:**
- [ ] concrete enough for a fair benchmark
- [ ] still too abstract
- Because:


---

# CANDIDATE 2

**Name (*): drug discovery: potential good molecules for medicines: Quantum generatve models (QSVM)

**Domain:**
- [ ] imaging: reconstruction
- [ ] imaging: segmentation
- [ ] imaging: classification
- [ ] imaging: generation
- [ ] QML
- [ ] explainable ML / feature selection / rule extraction
- [ ] diagnostic inference / uncertainty quantification
- [ ] other:

**Benchmark shape (*)**
- Objective: dataset (molecular structure design), metrics, algorithms
- Decision variables:
- Constraints:
- Separate tracks (if any):

**Why it matters (*)**
- 

**Available material**
- Datasets / instances:
- Baselines:
- Metrics: reactivity of the drug ADME, toxicity, 
- Prior work / tools named:

**What is computationally hard (*)**
- exponentially hard problem. np hard. 

**Fair-comparison risks**
- Classical simulation with DFT methodology have a limit

**Missing pieces (*)**
- what kinf of molecules to test? what kind of metrics should be use for benchmarking? HArdware but it is general.

**Readiness label:**
- [ ] ready / near-ready
- [ ] promising
- [ ] formulation needed
- [ ] asset / infrastructure
- [ ] control / caution

**Expert judgment needed**
-

**Next practical step (*)**
- Action:
- Owner:

**Verdict:**
- [ ] concrete enough for a fair benchmark
- [ ] still too abstract
- Because:

---

# CANDIDATE 3 (optional)

**Name:**

**Domain:**
- [ ] imaging: reconstruction
- [ ] imaging: segmentation
- [ ] imaging: classification
- [ ] imaging: generation
- [ ] QML
- [ ] explainable ML / feature selection / rule extraction
- [ ] diagnostic inference / uncertainty quantification
- [ ] other:

**Benchmark shape**
- Objective:
- Decision variables:
- Constraints:
- Separate tracks (if any):

**Why it matters**
-

**Available material**
- Datasets / instances:
- Baselines:
- Metrics:
- Prior work / tools named:

**What is computationally hard**
-

**Fair-comparison risks**
-

**Missing pieces**
- hardware.

**Readiness label:**
- [ ] ready / near-ready
- [ ] promising
- [ ] formulation needed
- [ ] asset / infrastructure
- [ ] control / caution

**Expert judgment needed**
-

**Next practical step**
- Action:
- Owner:

**Verdict:**
- [ ] concrete enough for a fair benchmark
- [ ] still too abstract
- Because:

---

# REJECTED / DEFERRED

| Candidate | Why rejected / deferred | Could it be reframed? |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

---

# RECAP CONCLUSIONS (for the rapporteur)

**Strongest conclusions:**
-
-

**Main candidate problem:**

**Why it matters:**

**Most important missing piece:** for supervised learning tasks should we wait to have an advantage in the simplest systems (spin glass)

**Next benchmark-building action:**

**Transversal next-step advice (one line):**

---

# TRANSVERSAL REFLECTION

real-time issue is not for now and not for benchmarks


## Infrastructure
- Minimum to start:
- Longer-term goal:
- Lessons from experience:

## Community
- Attracting contributors:
- Sustaining participation:
- Lessons from experience:

## Governance
- Ownership / who reviews and accepts a benchmark:
- Quality control, licensing, ethics:
- Avoiding overclaiming:
- Lessons from experience:

potential tension between needing proofs and proceeding in algorithms evolution.

---

# PARKING LOT
<!-- anything unsorted or to clarify with the table -->
-
-
-

---

<!--
LEGEND — readiness labels
ready / near-ready ..... objective, data, baselines, metrics mostly exist; needs packaging
promising .............. plausibly benchmarkable, but formulation/instances/baselines unclear
formulation needed ..... must first define the benchmarkable subproblem
asset / infrastructure . not for ranking solvers; useful for data quality, governance, repo design
control / caution ...... useful negative control or boundary case; do not oversell as flagship

MAPPING to answers.md
  Benchmark shape + Why it matters ................................. Problem
  What is computationally hard + Fair-comparison risks ............. Bottleneck
  Available material + Missing pieces + Readiness + Next step ...... Moving ahead
-->
