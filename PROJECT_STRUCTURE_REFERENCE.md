# PROJECT_STRUCTURE_REFERENCE.md

Repository and project-control artifact reference

Purpose: provide a complete menu of proven directory boundaries and planning or tracking artifacts
derived from the Invest project experience.

This file is a reference, not the current state of a project and not a command to create every
entry. PROJECT_WORKFLOW.md owns the rules for using the structure. The project's current-state
document and Project facts record what actually exists.

Framework invariant:

- Retain this spine and every catalog file under `framework/structure/` unchanged inside the
  project.
- Tailoring selects from this reference; it never deletes sections, renumbers them, or turns this
  file into a project-specific structure description.
- Stable section names and catalog entries remain discoverable for later activation.
- Project-specific choices belong in project_profile.yaml, PROJECT_WORKFLOW.md Project facts, and
  the current-state document.

Tailoring is the top rule for this reference. Presence in the catalog is never evidence that an
item belongs in a project.

Read this spine and the relevant catalog files during greenfield initialization, repository restructuring, or creation of a new
project-control artifact. For ordinary feature work, load only the actual paths relevant to the
task.

## 1. Selection principles

- Create a directory or document only when it has one clear responsibility.
- Prefer stable responsibility-based names over names tied to one temporary feature.
- Separate maintained source, authoritative data, derived output, and disposable runtime state.
- Give each important module, interface, data set, and document one owner.
- Do not copy the same detailed status into several planning files. Use pointers.
- Keep maintained Markdown authoritative over generated human views; every view declares its
  sources, locale, generation time, version, and freshness.
- Keep engineering language, source evidence, presentation locale, and translation responsibilities
  separate.
- Keep generated and runtime-only content out of version control unless an explicit evidence policy
  requires it.
- Record the selected paths and exceptions in PROJECT_WORKFLOW.md under Project facts.
- Keep current target-project facts separate from approved future design and from facts observed in
  external reference material.

## 2. Tailoring protocol

The human is not expected to select the structure alone. The AI evaluates the project conditions,
recommends a tailored structure, explains the consequences, and asks the Product Owner to approve
material choices.

### 2.1 Decision states

Assign every considered directory or control artifact one state:

| State | Meaning | Action |
|---|---|---|
| selected_now | A current responsibility, consumer, or risk requires it | Include it in the proposal and materialize after approval |
| deferred_until_trigger | It is not needed now, but a known event would require it | Do not create it; record the trigger |
| not_applicable | It does not fit the current product or operating model | Do not create it or load its rules |
| local_extension | The project has a real responsibility not represented by the reference | Define and approve the smallest new boundary |
| framework_retained | It is part of the reusable control framework | Retain it unchanged; do not treat it as project-specific evidence |

Silence is not a decision state. Do not create every reference entry merely because no one rejected
it.

### 2.2 Include an item when

Select a directory or artifact when at least one of these is true and an existing owner cannot
handle the responsibility clearly:

- it owns a distinct source of truth, contract, or maintained responsibility.
- it separates maintained source from production data, generated evidence, or disposable state.
- a user, runtime component, test, operator, or external system has a real need for it.
- verification, recovery, security, compliance, or audit requires a stable boundary.
- a tool or deployment contract requires a stable path.
- the activation condition already exists, not merely because it might exist one day.

The AI must identify the evidence for every selected item. A general statement such as "best
practice" is not sufficient evidence.

Evidence must predate the selection or come from an approved next-increment boundary. A directory,
roadmap, review file, or runbook created by activating a module cannot serve as evidence that the
module was needed.

### 2.3 Defer or exclude an item when

Do not select an item when:

- it has no current content, consumer, owner, or activation evidence.
- another existing directory or document already answers the same question.
- it represents one temporary feature rather than a stable responsibility.
- it would create a second source of truth or require duplicated status updates.
- it contains only disposable generated output that needs no stable project boundary yet.
- the cost of navigation, synchronization, or context exceeds the control it provides.

Use deferred_until_trigger when the need is credible but not active. Use not_applicable when the
category does not fit the known project model.

### 2.4 Tailoring sequence

During initialization or restructuring, the AI performs these steps:

1. Start with the Minimal greenfield starting set, not the full tree.
2. Inspect the product, runtime, data, testing, collaboration, deployment, and risk model.
3. Evaluate each relevant reference item against the inclusion and exclusion rules.
4. Reuse an existing responsibility before proposing a new one.
5. Present a tailoring table with path, state, evidence, owner, information class,
   version-control policy, and activation trigger.
6. Identify material choices that require Product Owner approval.
7. Materialize selected_now items only after approval.
8. Record retained framework files, selected paths, deferred triggers, local extensions, and
   deviations in project_profile.yaml and summarize actual paths in Project facts.
9. Update the current-state document when the implemented structure becomes true.
10. Revisit deferred items only when their trigger appears.

Recommended proposal format:

| Candidate path or artifact | State | Evidence or reason | Owner | Information class | Version control | Trigger or approval |
|---|---|---|---|---|---|---|

Information class is one of maintained source, authoritative data, derived evidence, runtime state,
or disposable cache.

### 2.5 Adding a missing local need

When the project needs a category or artifact absent from this reference:

1. Describe the missing responsibility and its consumer in one sentence.
2. Confirm that no existing selected item can own it without ambiguity.
3. Choose the smallest stable path based on responsibility, not a temporary implementation name.
4. Define what belongs there and what must not.
5. Classify its information, authority, sensitivity, retention, backup, and version-control policy.
6. Define its owner, interfaces, verification, and activation condition.
7. Check migration, compatibility, generated-output, and recovery consequences.
8. Request Product Owner approval when it creates a new source of truth, top-level boundary,
   governance artifact, external commitment, or material risk.
9. Add the approved path to Project facts and the current-state document. Add tests, ignore rules,
   runbooks, or recovery controls when applicable.
10. Record the decision and permanent work ID that introduced it.

A local need belongs in the project's actual structure first. Do not edit this reusable reference
merely to describe one project's exception.

Consider adding a local extension to the reusable reference only after evidence shows that it is
useful across projects. A reference update must define a general responsibility, inclusion and
exclusion criteria, lifecycle, ownership, and compatibility with existing categories.

### 2.6 Revisit triggers

Re-evaluate the tailored structure when any of these occurs:

- a new deployable component, user interface, data store, provider, or external integration appears.
- production, sensitive, append-only, or non-cleanable data is introduced.
- scheduled or unattended operation begins.
- a second writer or independent reviewer joins.
- several phases or long-running features begin competing for priority.
- backup, restore, migration, audit, or incident response becomes necessary.
- an existing directory accumulates unrelated responsibilities or unclear ownership.
- a tool requires a stable path or machine-readable document contract.
- a second human view, presentation locale, or local HTTP consumer appears.
- terminology ambiguity or translation begins affecting code, schemas, decisions, or business meaning.

The trigger starts a proposal. It does not authorize silent restructuring.


## Structure catalog routing

The complete catalog lives in one file per topic under `framework/structure/`. This spine owns the
selection principles and the tailoring protocol; each catalog file is the sole normative owner of
its entries. Original section numbers are preserved inside the catalog files, so references such as
"section 9.4" remain valid.

| Catalog | File | Sections | Load when |
|---|---|---|---|
| Root files | [framework/structure/root-files.md](framework/structure/root-files.md) | 3 | Deciding which root-level files a project keeps |
| Git and version control | [framework/structure/git-reference.md](framework/structure/git-reference.md) | 4 | Proposing or changing repository configuration |
| Source, test, and runtime directories | [framework/structure/directory-catalog.md](framework/structure/directory-catalog.md) | 5–7 | Selecting application, test, or runtime boundaries |
| Documentation and planning artifacts | [framework/structure/documentation-catalog.md](framework/structure/documentation-catalog.md) | 8–10 | Creating or restructuring docs, plans, or tracking artifacts |
| Minimal greenfield starting set | [framework/structure/minimal-start.md](framework/structure/minimal-start.md) | 11 | Initializing a new project |
