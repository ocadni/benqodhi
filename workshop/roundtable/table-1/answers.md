# Table 1 — Genomics, molecular biology and life sciences

- **Date:** 11 September 2026
- **Gabriele Leoni:**
- **Rapporteur:**

## Participants

- **Mario Chizzini (MC)** — chair of the round table
- **Francesco Zamponi (FZ)**
- **Zev Kronenberg (ZK)**
- **Aurora Maurizio (AM)**
- **Gabriele Leoni (GL)** - note taker
- **Indaco Biazzo (IB)** - organizer

## Discussion summary

**Speed is not the argument for quantum computing in genomics.** AM, ZK and FZ
converged on the point that current clinical and research pipelines are already fast
enough. AM noted that even in urgent settings the lab queue and the genetic analyses
themselves are quick; most of the turnaround time is administrative rather than
computational. ZK confirmed that under three days is common, with ONT sequencing
during surgery already at proof-of-concept stage. FZ has never seen a pipeline
requiring months of computation. MC added that Grover's quadratic speed-up is not
enough to beat mature classical bioinformatics software in practice, so raw speed
should not be the selection criterion. The group's conclusion: what could justify
quantum is **problem dimension and model complexity**, not runtime.

**The interesting problems appear when you add structure on top of processed data.**
FZ pointed to epistatic states layered over alignments, and to interactions between
mutations of different size, which become extremely hard to process. ZK framed this
as haplotype complexity: the inference itself is hard, and inferring the biological
interaction between variants is harder still. FZ and ZK agreed that the concrete,
well-posed and difficult questions are of the form "are these two variants in cis?"
and "what is their biological interaction?"

**Research versus clinic.** AM argued that complicating the model is legitimate in
research but not in the clinic, and FZ agreed. FZ restated the workshop aim as
finding problems where quantum could plausibly be useful, while noting that for most
current tasks simple software is good enough. MC raised the practical constraint that
first-generation quantum devices will be noisy and imperfect, asking whether
approaches exist that tolerate this.

**Scale and data-space questions.** GL asked whether sample size could become a
reason to move to quantum, contrasting All of Us (around half a million individuals)
with the millions expected under EHDS. ZK described a related practical gap in All of
Us: coding versus non-coding regions are not annotated, ORF prediction is confounded
by sequencing errors that make proteins look truncated, and even with mass
spectrometry on top there is no true set. He and GL noted that the existing standards
were built by researchers, so they reflect research needs rather than clinical ones;
AM asked what standards EHDS would need across heterogeneous instruments and
technologies.

**Where quantum was seen as plausibly relevant.** AM suggested genome-wide
association studies, while judging genome assembly to have low health impact except
for viruses. GL extended this to haplotype phasing and genome sequencing in viruses,
for example SARS-CoV-2, where a single virus mutates at several positions and
generates a clonal population. FZ described his group's protein-family work as a
model case with known ground truth: infer the tree, infer the generative model for
mutations, then infer a new tree from that, now repeated on synthetic data, with the
open question of whether the tree can be reconstructed from limited information
alone. IB cautioned that the interpretation of quantum computing is still open and we
do not yet know what it will let us do.

**AI, ethics and clinical deployment.** MC asked about AI making clinical decisions.
AM's position, and the direction at San Raffaele, is that AI should assist the
clinician in the first phases rather than the reverse: clinicians are overloaded and
models often catch what a tired reader misses, such as a fracture. She was explicit
that the order matters and that clinicians should not be handed AI output first. MC
raised neuro-symbolic AI as a possible new paradigm and asked about bottlenecks; AM
identified training dataset size, with oncology and rare disease cohorts as small as
72 people. MC noted that drug-leaflet frequencies are inferred worst-case figures.
ZK summarized the risk trade-off with the Tesla analogy: when it fails it kills
people, but using it kills fewer than not using it. AM noted San Raffaele now teaches
AI to future doctors, and ZK and FZ observed that in practice the adoption so far is
generative models: LLMs, and code generation.

## Raw notes

AM: Utility: disussing AM and ZK with Guglielmo about reasonable time for analyses. Are there cases? Well in hospitals if you have only 24h for diagnosis (pediatric cases at births)- FZ similar situations in other labs and clinical cases. AM: most of the time actually goes in burocracy. The Lab que is straightforward and genetic analyses are quite fast. However then the response is delayed due to administrative stuff (here in Italy maybe). In ZK less than 3 day is common (also ONT actually during surgery: proof of concept right now). -> Compute doesn't require quantum. 

FZ: never saw pipelines that requires month of computational analyses. But when you add info to the data already processed (like epistatics state over alignements) -> then maybe that could be interesting to check with Quantum. 
MC: Grover has a quadratic advantage, but in practice this is not enought to give supremary over standard softwares. Personallly, speed should not be the reason to select quantum comp over standard bioinformatic approaches. Therefore, maybe is the dimension that could justify going to qc. 
AM: qc is in research, because complicating the model is right only in research not in clinic.
FZ: agree on AM. 
ZK: when you want to add genomes and you want to understand the relationship.
FZ: we work on proteins, and families, we infer the tree, we infer the generative models for mutations and then we infer a new tree based on that, but we know the groundtruth. Now we are doing the same on syntetic data. If I use now only the lead can we reconstruct the tree?
GL: do you beleave that sample size could became a reson to go in qc? in view of the EHDS
ALLOFUS vs HEDS, half a millions data vs millions, could this be a case for qc? 
ZK: in allofus, we don't know whic are coding vs non coding regions this is a practical issue that can be solved with AI. AM: are this healty individuals? ZK: yes. We try to predict orf, but because of sequencing errors, the protein can be seen broken. We use Mass spect to predict the protein on top of the orf sequencing, but we don't have the true set. 
GL: What about QC. 
GL and ZK: the standards are made by researchers therefore the standards are on the research side rather than the clinical standads.
AM: what about EHDS? what could be the standards? different instruments/tech/etc
FZ: goal of the workshop is to find issues that qc can or would be usefull.
FZ: simple softwares are good enought. 
MC: first generations of qc will be noise and not perfect. could you find different approaches with less?
ZK: readings the prompts.
FZ:Interactions between mutations of different size starts to be extremely difficult to process
ZK:this is aplotype complexity. You need to infer, and inference is hard. also the interaction is difficult to infer.
FZ and ZK: Are two variants in cis? This is difficult, what is their biological interaction? these questions are difficult to answer.
AM:Genome wide association studies. QC might be usefull there. Paper on genome assamblies, least impact for health, unless you have viruses. 
GL: haplotype phasing and genome sequencing in virus (e.g, COVID-19). a single virus can actually mutate in different points and create a clonal population. 
GL: What would be a good benchmarking dataset for this issue?
ZK: like in the past, atgc standard. You have two strings, in some positions there are mutations, that can be in one or in the other strings. you don't know. Standard bioinformatic approaches based on sequencing (most long reads) use linked information that overlaps multiple mutations location (loci). Or you can use many many samples and use frequency of the mutations in the population. It s a large combinatorial problem. 
ZK: Focusing only on Germline mutations
Deployed assemblies are used to create unknown assemblies to be used for phasing. 
MC: what about AI and ethics, do we will have issues in AI taking decisions in clinical. 
AM: I will prompt AI in clinic (imaging) for help clinitian not the other way around. The direction at san raffaele is that clinitian will be helped in the first phases by AI. Clinitian are buisy, and their results after hours of work loose. Often clinitina misses something that AI models detects (e.g., fracture not seen by doctor, while chatgpt spotted it easily).  
MC: would you use first AI and then clinitian? AM: No, clinitial are susciettibili. 
MC: Neurosimbolic AI, could introduce new paradigm in AI, do you think that there are bottlenecks?
AM: dataset sizes. For training.  -> Oncological sudies / rare diseases are limited. E.g, cohort size of 72 people.
MC: reading the information sheet from a drug, the frequencies are inferred and are worst case scenario.  
IB (Indaco Biazzo): we still don't know the interpretations of qc. We don't know actually what we will be able to do in the future with that. 
MC: Do you think that AI could have a negative impact in clinics?
ZK: It is the tesla experiment. When it do it wrong, it kills, people. When you use it however, it kills less that not using it. 
AM: in san raffaele we teach AI to the future doctors. 
ZK: only generative models LLM 
FZ: generative models for coding. 


ZK: predicting proteins from long reads. Building a true set based on sequencing. Info used: complete genome, long reads rna, sequences noise


## Candidate 1 — Haplotype phasing and variant-interaction inference (germline)

- **Problem:** Given the variants observed in an individual, decide which ones sit on
  the same physical chromosome copy (cis) and which are on opposite copies (trans),
  and then interpret their joint biological effect. It matters because clinical
  interpretation of two variants in the same gene depends entirely on their phase: two
  hits in cis leave one working copy, two hits in trans do not. The table restricted
  scope to germline mutations to keep the problem well posed. ZK and FZ identified
  this as the point where the questions become genuinely difficult, and where adding
  interaction structure, not raw speed, is what breaks current approaches.
- **Bottleneck:** A large combinatorial inference problem. Represented as two strings
  over the ATGC alphabet with mutations at known positions but unknown assignment
  between the strings, the assignment space grows exponentially in the number of
  heterozygous loci. Classical methods sidestep this using linked information from
  long reads that span several loci, or population mutation frequencies across many
  samples. Both degrade where reads are short, coverage is uneven or the population
  reference is thin. Interactions between mutations of different size, as FZ noted, are
  extremely hard to process, and epistatic interaction between phased variants is a
  second inference layer on top.
- **Moving ahead:** Missing is a benchmark instance set with genuine ground truth and
  a clear difficulty gradient. The practical route ZK described is to use deployed,
  validated assemblies to construct phasing instances whose answer is known, in the
  spirit of earlier community truth-set standards. Next step: define the instance
  format (loci, observed variants, available linkage evidence, population priors), fix
  a domain metric such as switch error rate, and publish a small graded set that a
  classical, hybrid or quantum solver can all be run against unchanged.

## Candidate 2 — Viral haplotype reconstruction in clonal populations

- **Problem:** Reconstructing the set of co-existing viral haplotypes and their
  abundances within a single infected host, where one virus mutates at several
  positions and produces a clonal population, as GL raised for SARS-CoV-2. It matters
  for tracking escape variants, drug resistance and transmission, and it is the one
  assembly-adjacent problem the table judged to carry real health impact. AM's view was
  that genome assembly has least impact for health, unless you have viruses.
- **Bottleneck:** Deconvolving an unknown number of haplotypes at unknown frequencies
  from mixed reads. Unlike the diploid germline case the ploidy is not fixed, so the
  solver must jointly infer how many haplotypes exist, their sequences and their
  proportions, while separating true low-frequency variants from sequencing error. This
  is a joint combinatorial and continuous estimation problem and the search space is
  far larger than in the two-string germline setting.
- **Moving ahead:** Missing is a public instance set where the true haplotype mixture
  is known. This is more tractable than in human genomics: mixtures can be constructed
  from known viral genomes at controlled ratios, giving exact ground truth. Next step:
  build a synthetic-plus-real benchmark with defined error models and coverage levels,
  and agree on metrics for both sequence accuracy and abundance accuracy.

## Candidate 3 — Phylogenetic tree reconstruction under generative mutation models

- **Problem:** Reconstructing evolutionary trees for protein families when the
  mutation process itself is modelled, including epistatic couplings, rather than
  assumed independent per site. FZ described his group's pipeline: infer the tree,
  infer the generative model for mutations, then infer a new tree from that model,
  with the advantage that the ground truth is known and the procedure is now being run
  on synthetic data. The open question he posed, whether the tree can be recovered from
  limited information alone, is directly a benchmark question.
- **Bottleneck:** Tree space grows super-exponentially in the number of taxa, and
  adding epistatic states over alignments couples the sites so the likelihood no longer
  factorizes. This is the case FZ flagged as becoming interesting for quantum: the cost
  comes from model dimension and coupling, not from data volume.
- **Moving ahead:** The synthetic-data setting already provides ground truth, which is
  the hardest ingredient to obtain and the reason this candidate is benchmark-ready.
  Missing is packaging: fixed generated datasets, a stated information-restriction
  regime, and a tree-distance metric. Next step: release the synthetic generator with
  fixed seeds plus reference trees, so any solver family can be scored on the same
  instances.

## Candidates considered and set aside

- **ORF and protein prediction from noisy sequencing.** ZK's All of Us example, where
  coding and non-coding regions are unannotated and sequencing errors make proteins
  appear truncated, with mass spectrometry used on top. Set aside as a benchmark
  candidate because there is no true set, which is precisely what a benchmark requires;
  the table saw it as an AI problem rather than a quantum one.
- **Genome-wide association studies at EHDS scale.** AM proposed GWAS as a plausible
  area and GL raised whether the jump from All of Us (about half a million) to EHDS
  (millions) changes the picture. Kept as a scale motivation for Candidate 1 rather
  than a standalone benchmark, since larger sample size alone does not create a
  quantum-relevant bottleneck.
- **Turnaround time in clinical genomics.** Explicitly rejected. The computation is
  not the bottleneck; administration is.

## Conclusions for the recap

- **Strongest conclusions:** Speed is the wrong argument for quantum in genomics.
  Current pipelines are fast enough, delays are administrative, and a quadratic
  speed-up does not beat mature classical software. What could justify quantum is
  problem dimension and model complexity, which appear when interaction structure is
  added on top of already-processed data. Model complication belongs to research, not
  the clinic. Existing genomic standards were written by researchers and do not cover
  clinical or EHDS-scale needs.
- **Main candidate problem:** Haplotype phasing with variant-interaction inference
  (Candidate 1), with viral haplotype reconstruction as the highest-impact variant.
- **Why it matters:** Phase determines clinical interpretation of variants, the
  question is precisely stated, and the combinatorial hardness is intrinsic rather
  than an artifact of implementation.
- **Most important missing piece:** Ground-truth instance sets. Every candidate the
  table liked is limited by the absence of a public truth set with a difficulty
  gradient, and every candidate it rejected was rejected for the same reason.
- **Next benchmark-building action:** Build phasing instances from deployed validated
  assemblies, publish them with a fixed input format and a switch-error-style metric,
  and keep them solver-agnostic so classical, AI, hybrid and quantum methods are
  scored identically.
- **Transversal next-step advice:** Start from ground truth and metrics, not from
  hardware. A benchmark is only useful if the answer is known and the score is
  domain-meaningful. Prefer synthetic and semi-synthetic instances where truth is
  constructible, since these are available now, and include noise-tolerant instance
  sizes so that noisy first-generation devices can be assessed honestly rather than
  excluded.

## Transversal reflection

<!-- Given the three pillars — infrastructure, community and governance — what
     advice, suggestions or lessons from experience would you give for the next
     steps after the workshop, so that BENQODHI can become a living benchmark
     repository and produce useful final outputs? -->

*Draft below assembled from points raised during the discussion. The three pillars
were not addressed directly, so the table should confirm or replace this.*

- **Infrastructure:** A GitHub repository with a simple website, an instance format,
  a metric definition and two or three graded instance sets is enough to start. The
  binding constraint is ground truth, so priority goes to instances whose answer is
  constructible (synthetic protein families, controlled viral mixtures, phasing
  instances derived from validated assemblies) rather than to compute resources.
- **Community:** ZK and GL noted that existing genomic standards were built by
  researchers and therefore encode research needs. If BENQODHI wants clinical
  relevance, clinical and EHDS-side contributors have to be in the loop from the
  start. AM's point about instrument and technology heterogeneity under EHDS argues
  for agreeing on data-description conventions early.
- **Governance:** Keep benchmarks solver-agnostic and admit noisy or approximate
  solvers rather than filtering them out, per MC's point that first-generation quantum
  devices will be imperfect. Small-cohort realities in oncology and rare disease
  (AM's example of 72 individuals) should be represented as a legitimate instance
  regime, not treated as insufficient data.
