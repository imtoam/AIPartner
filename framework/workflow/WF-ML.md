# WF-ML — Machine learning and model-derived output
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-ML` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: context of use, model-class and layer selection, model risk rating, learned-artifact freezing, re-validation triggers, effective challenge, and decay monitoring

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-ML: Machine learning and model-derived output

Activation condition:

- the project fits, trains, fine-tunes, or calibrates parameters from data
- the project uses a pretrained or third-party model as a component of what it produces

Ignore the rest of this section until its checkbox is checked.

**A calibrated threshold is a learned parameter.** Choosing a number by looking at outcomes is
training, whatever it is called in the code, and it carries every obligation below.

### 1. Context of use — declared before building

Record, before any model work begins: the question the model answers, the decision that consumes
its output, the population and period it is valid on, and what it must never be used for. A model
without a declared context of use cannot be evaluated, because there is no statement of what
"working" means.

### 2. Model risk is two-dimensional

| | Low decision consequence | High decision consequence |
|---|---|---|
| **Model output is one input among several** | Light evidence | Full evidence |
| **Model output drives the decision** | Full evidence | Full evidence, plus independent review before first use |

Evidence depth follows the higher dimension. A model with modest influence over a decision that
moves money, health, safety, rights, privacy, or security is not a low-risk model.

### 3. Model class — a selection, not a default

Each class states what is actually learned and by what mechanism, and therefore what evidence it
owes. Select classes explicitly and record the choice using the tailoring decision states in
PROJECT_STRUCTURE_REFERENCE.md; presence in this table is never evidence the project needs it.

| Class | What is learned | Mechanism | Evidence it owes |
|---|---|---|---|
| Retrieval and indexing | Nothing; the index encodes an existing corpus | Encode, store, search by similarity or term | Corpus provenance, reproducible rebuild, retrieval quality on a fixed question set |
| Calibrated rules | Thresholds and weights | Fitting numbers to observed outcomes | Same freezing and re-validation duties as any model; the fitting data is recorded |
| Supervised models | A mapping from features to a labelled target | Regression, trees, ensembles, networks | Held-out and out-of-period performance, feature provenance, leakage check |
| Sequential and time-series models | Temporal structure | Ordered fitting | Walk-forward evaluation with purge and embargo; a random split is invalid evidence |
| Unsupervised and representation models | Structure without labels | Clustering, reduction, anomaly scoring | Stability under resampling; a discovered group is not a real category until named and confirmed |
| Pretrained general models used as-is | Nothing in this project; behaviour comes from the provider | Prompting and context assembly | Pinned model version, prompts in version control, non-determinism and refusal handling |
| Adapted general models | Project-specific behaviour over provider parameters | Fine-tuning, adapters, instruction tuning | Pinned base version, training-corpus provenance and licence, before-and-after comparison, reproducibility |

### 4. Layers — selected one by one

A model-using project is built in layers. Each layer is selected, deferred with a trigger, or
declared not applicable, with evidence, exactly like any other tailoring decision.

| Layer | Question it owns | Recorded when selected |
|---|---|---|
| Data | What observations exist, where they came from, and what was knowable at each moment | Sources, provenance, point-in-time rule |
| Representation | How content becomes features or vectors | Embedding or feature version, and the re-computation policy when it changes |
| Retrieval | How relevant material is found | Retrieval method and its acceptance measure |
| Reasoning | What produces the answer, prediction, or score | The model class of section 3 |
| Governance | Freezing, evaluation, approval, monitoring, and the record | Everything in sections 5 to 8 |

**The governance layer is not optional.** A project may skip retrieval, skip representation, or use
a single model with no pipeline at all; it may not select any layer while leaving governance
unselected. Deferring governance means the project has no way to tell a working model from a
plausible one.

### 5. Separation and leakage

Training and evaluation material may not contain anything that was not knowable at the moment the
prediction would have been made. Evaluation data is not used for selection, and evaluation results
are recorded before deployment, not reconstructed afterwards.

### 6. Freezing and identity

Every deployed learned artifact has a version and a content hash. Every recorded prediction names
the artifact that produced it. An output that cannot name its artifact is not evidence, and the
artifact behind a past decision must remain retrievable for as long as that decision matters.

### 7. Re-validation and honest failure

Re-validation triggers are written down before deployment, and normally include: a change in input
distribution, a change in code or dependencies, elapsed time, and measured performance decay.
"It has not broken yet" is not evidence; only a measurement taken after the trigger is.

A model that fails its evaluation is recorded as failed. Retuning against the same evaluation set
until it passes consumes that set and produces a number that no longer means anything.

### 8. Effective challenge and monitoring

Review is proportional to risk and performed by someone who did not build the model, with a real
ability to reject it. Once deployed, performance is measured against outcomes as they arrive; a
model whose live behaviour is not measured is unvalidated regardless of how it tested.

### 9. Authority boundary

A learned output never becomes project truth on its own and never takes action on its own.

- Model output that would act on the world: framework/workflow/WF-HIGH-IMPACT.md.
- Where predictions, features, and artifacts are stored and for how long: framework/workflow/WF-PERSISTENCE.md.
- Crossing an authoritative or non-cleanable data boundary: framework/workflow/WF-DATA.md.
- Presenting model output to a human: framework/workflow/WF-VIEWS.md, which requires the view to
  show that the number is derived, and from which artifact.
