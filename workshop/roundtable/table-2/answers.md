# Table 2 — Medical imaging, diagnostics, machine learning and QML

- **Date:** 11 September 2026
- **Participants:** Hao Wang; Miguel Angel Gonzalez Ballester; Guglielmo Mazzola
- **Note takers:** Alessandro Zani; Lea Schuh
- **Rapporteur:** Hao Wang

Shortlist around two or three candidate problems. For each candidate, answer the three questions from the table guide.

## Candidate 1 — Quantum generative models for molecular design

- **Problem:**
  - **What:** generate candidate molecules with desired properties for a disease target.
  - **Why it matters:** drug discovery is high value.
  - **Concrete need:** a participant's life-science project already requires benchmarking quantum generative models against the state of the art. The need is real, not hypothetical.
- **Bottleneck:**
  - **Sampling needs hardware we don't have.** The circuit models used can be trained on a classical computer via moments and expectation values. Sampling molecules from them is believed to be classically hard, so the models cannot be fully exercised at scale.
  - **Metrics are restricted.** Without hardware, only quantities like moments are computable.
  - **Evaluation is slow.** Judging generated molecules requires chemists and a laborious procedure.
  - **Noise is hard to emulate.** Simulating realistic hardware noise is itself difficult.
- **Moving ahead:**
  - **Missing:**
    - an agreed reference dataset, which needs drug-discovery experts
    - an evaluation metric, since it is open whether matching a few moments is enough to compare distributions
    - the smallest system size at which the benchmark becomes meaningful
    - evidence of scaling, since small-qubit results don't convince the community
  - **Next step:**
    1.  Fix a reference dataset together with drug-discovery experts.
    2.  Settle which metrics can be computed without hardware, starting with whether moment matching is sufficient.

## Candidate 2 — Radiomics for non-invasive diagnosis

- **Problem:**
  - **What:** can features extracted from medical images support diagnoses that today require invasive procedures (e.g., biopsy for tumour characterisation)?
  - **Why it matters:** it reduces patient burden and risk. The value lies in diagnostic quality.
- **Bottleneck:**
  - **Feature selection is combinatorial.** Radiomics produces very large feature vectors, and selecting the informative subset is combinatorial. It can be mapped to binary, qubit-based formulations.
  - **Supervised QML benefit is unproven.** It was contested at the table: circuits that avoid barren plateaus tend to be classically simulable.
  - **Image encoding is costly.** Encoding images into quantum states is expensive and adds many steps.
  - **Speed is not the bottleneck.** Diagnostic delays come from hospital processes, not computation.
- **Moving ahead:**
  - **Missing:**
    - a specific clinical task with expert-labelled real data, since synthetic data gives no guarantee the problem is hard
    - comparison against the classical methods actually used in practice
    - any evidence of a practical QML benefit
  - **Next step:**
    1.  Choose one concrete clinical task.
    2.  Run an instance-level analysis of where classical wins and where quantum shows benefit, and which data features predict this.
    3.  Test in simulation whether quantum models generalise better or need fewer training examples.

## Candidate 3 — Beyond-DFT electronic structure for drug discovery (optional)

- **Problem:**
  - **What:** accurate simulation of molecules where density functional theory (DFT) approximations fail, e.g., heavier-element or strongly correlated systems.
  - **Why it matters:** it would give better property predictions for drug design. Chemistry is the area where quantum advantage is most widely expected.
- **Bottleneck:**
  - **Classical simulation hits a wall.** The full many-electron wavefunction cannot be simulated classically, and DFT approximations break down for these systems.
  - **Classical methods are strong and improving.** Examples are neural-network ground-state methods and gold-standard correlated methods.
  - **The classical–quantum boundary is unclear.**
- **Moving ahead:**
  - **Missing:**
    - a clear definition of where classical methods fail, needed for a well-posed benchmark
    - hardware, since this likely requires fault tolerance
  - **Next step:**
    1.  Identify molecule classes where DFT demonstrably fails, to use as benchmark instances.
    2.  Consider an existing DFT-based data competition as a template.

## Conclusions for the recap

- **Strongest conclusions:**
  - **Comparison baselines:** a meaningful benchmark needs a practically relevant problem with a mature classical baseline. Otherwise quantum advantage claims are inflated.
  - **Simulation limits:** no hardware exists at relevant scale, so benchmarking must start in simulation, which limits what can be claimed.
  - **Supervised QML:** an advantage for supervised QML is not established.
  - **Clinical imaging:** diagnostic quality matters, not speed.
- **Main candidate problem:** Radiomics-based diagnosis (Candidate 2) is the main imaging-specific candidate.
- **Why it matters:**
  - Drug discovery is high value.
  - A concrete project already needs this benchmark.
  - The models can be trained classically, so benchmark-building can start now.
- **Most important missing piece:** an agreed evaluation metric that can be computed without hardware, together with an expert-curated reference dataset.
- **Next benchmark-building action:**
  1.  With drug-discovery experts, fix a reference dataset.
  2.  Test whether moment-based metrics are sufficient.
  3.  Include classical generative models as baselines.
- **Transversal next-step advice:**
  - Fund the engineering needed to maintain the repository.
  - Involve domain experts from the start.
  - Require classical baselines and honest resource reporting in every benchmark.

## Transversal reflection

- **Infrastructure:**
  - **Maintenance is the real bottleneck, not problem identification.** Universities lack research engineers to keep platforms alive, so dedicated funding is needed.
  - **Host the full comparison set.** That means open datasets, open reference implementations (e.g., quantum generative models) and the classical baselines alongside them.
  - **Support simulation-based work.** Provide metrics computable without hardware, since most contributors won't have access to large devices.
- **Community:**
  - **Bring domain experts in from the start.** Pharma, clinicians and imaging specialists are essential, because dataset and metric choices depend on them. Interdisciplinarity was flagged as a missing piece.
  - **Encourage open contributions.** Open implementations that others can reuse and compare against were suggested.
  - **Value theory and honest results.** Theoretical work is needed even before hardware matures. The community is now more aware of limitations, and the repository should reward careful claims over hype.
- **Governance** *(not discussed explicitly; derived from the table's discussion)*:
  - **Acceptance criteria for problems:**
    - practical scientific or clinical relevance
    - a mature classical baseline
    - expert-curated data
  - **Reporting standards:**
    - simulation scale and whether the model is classically simulable
    - resource estimates that include hardware architecture and error-correction overhead
  - **Keep classical baselines updated.** Classical computing and ML keep improving, so benchmarks can go stale.

## General considerations

- **Hardware reality:**
  - No large-scale hardware is available.
  - Small-qubit demonstrations don't convince the community or industry partners.
  - Error correction adds a large overhead per logical qubit. Resource extrapolations based on logical operation counts alone are overly optimistic.
- **Which comparison?** Quantum vs classical requires problems where classical methods are already well explored. Quantum vs quantum was suggested as possibly easier for identifying benchmark problems. Examples are compilation to real hardware (gate counts, connectivity) and image encoding schemes.
- **What kind of advantage?**
  - Practical gains may matter more than exponential ones: better solution quality, better generalisation from less data, or reducing a polynomial cost (e.g., cubic to quadratic).
  - Quantum does not need to win on all instances. Identifying *which* instances it helps with is already useful.
- **QML theory vs practice:** trainable circuits tend to be classically simulable, which leaves little room for provable advantage. Several participants argued practical benefits may still exist, as with deep learning, which works without formal guarantees.
- **Clinical fit:** in diagnostics, computation time is not the limiting factor, so real-time use cases are not a priority now. Quality of classification is what counts.
- **Lower-priority ideas raised:**
  - quantum image reconstruction and generation, where earlier studies compared against weak classical baselines
  - quantum sensing for new imaging modalities
  - quantum-inspired ML (tensor networks)
  - black-box mixed-integer problems such as AutoML, judged a poor fit for quantum
- **Community mood:**
  - The field has moved from early optimism to a more cautious, limitation-aware stance. That caution can look like disbelief.
  - Participants compared this to past AI winters and argued it is not a reason to stop research.
