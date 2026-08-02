# PROJECT_STRUCTURE_REFERENCE.md

Repository and project-control artifact reference

Purpose: provide a complete menu of proven directory boundaries and planning or tracking artifacts
derived from the Invest project experience.

This file is a reference, not the current state of a project and not a command to create every
entry. PROJECT_WORKFLOW.md owns the rules for using the structure. The project's current-state
document and Project facts record what actually exists.

Framework invariant:

- Retain this complete reference unchanged inside the project.
- Tailoring selects from this reference; it never deletes sections, renumbers them, or turns this
  file into a project-specific structure description.
- Stable section names and catalog entries remain discoverable for later activation.
- Project-specific choices belong in project_profile.yaml, PROJECT_WORKFLOW.md Project facts, and
  the current-state document.

Tailoring is the top rule for this reference. Presence in the catalog is never evidence that an
item belongs in a project.

Read this file during greenfield initialization, repository restructuring, or creation of a new
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

## 3. Root files

| Path | Responsibility | When needed |
|---|---|---|
| AGENTS.md | Roles, authority, permissions, review, and concurrent-writer rules | Always |
| START_HERE.md | One-time greenfield initialization protocol | Template and uninitialized project |
| PROJECT_WORKFLOW.md | Canonical delivery and governance method | Always |
| PROJECT_STRUCTURE_REFERENCE.md | Directory and control-artifact reference | Template; retained for future growth |
| project_profile.yaml | Approved initialization state, active modules, unresolved decisions, and actual paths | After initialization begins |
| project_profile.example.yaml | Exact machine-readable profile contract | Retained framework reference |
| index.html | Permanent human starting guide | Always; never overwrite during initialization |
| project-overview.html | Mandatory four-perspective human control surface generated from project truth | After initialization materializes approved facts |
| README.md | Short repository orientation and entry links | Normally |
| LICENSE | Reuse and distribution terms | Public or shared repository |
| framework_manifest.json | Integrity contract for retained rules and managed configuration boundaries | Always |
| .gitignore | Exclusion policy for secrets, generated output, runtime state, and local tools | Version-controlled repository |
| tools/validate_initialization.py | Deterministic framework and initialization validator | Retained framework tool |
| tools/delivery_receipt.py | Shared evaluator for current, failed, invalid, and stale delivery receipts | Retained framework tool |
| tools/render_project_overview.py | Atomic default renderer from declared project sources to the derived overview | Retained framework tool |

`project-overview.html` is the only generated project page in the minimal starting set. It contains
management, business, system-operations, and architecture/delivery perspectives from day one.
Additional pages normally live under `project_views/` and activate through one view registry when
a perspective's sources, audience, live behavior, or navigation depth justify a separate surface.

## 4. Git and version-control reference

Git is the recommended version-control system for software projects. The AI inspects the existing
repository and recommends a tailored Git configuration. It does not ask the user to design a branch
strategy without guidance.

### 4.1 Repository discovery

Before proposing Git changes, inspect and report:

- whether the directory is already a Git repository.
- whether history contains only the reusable template or actual project work.
- the current branch, working-tree state, remotes, and upstream tracking.
- untracked or modified files that may belong to the user.
- existing ignore rules, hooks, submodules, worktrees, large-file support, and repository policies.
- whether the repository is local only, private remote, or public remote.
- whether any existing history or remote relationship must be preserved.

Do not delete or replace the .git directory, rewrite history, change a remote, or discard local work
to make the repository match the reference.

### 4.2 Version-control modes

| Mode | Use when | Default controls |
| local_git | One person or AI needs recoverable local history | One default branch, small commits, no remote |
| remote_single_writer | One writer needs backup, publishing, or cross-device access | One remote, explicit push authority, simple branch policy |
| protected_collaboration | Review or several contributors affect a shared baseline | Protected default branch, short feature branches, pull requests |
| integration_branch | A long-running release or phase must develop apart from a stable baseline | Stable baseline, named integration branch, frequent baseline merges |
| deferred | The current output does not yet justify version control | Record the trigger and risk; do not pretend history exists |

For a normal software project, recommend local_git unless repository inspection shows an existing
safe configuration or the user needs a remote. Lack of a remote does not prevent local version
control.

### 4.3 Template history

Prefer a repository created from a Git hosting template or a copy of the template files placed into
a new empty repository. This gives the new project its own history.

If the repository was cloned with the reusable template's history:

- identify template-only history separately from project work.
- explain whether preserving that history is useful.
- do not remove .git or rewrite commits without explicit approval.
- record the template source and version used.
- if a clean project history is required, propose a safe copy into a separately initialized
  repository rather than silently destroying the existing history.

Template-only commits do not by themselves make the directory a brownfield project. Meaningful
project code, project data, project documents, deployment configuration, or project-specific
commits do.

### 4.4 Branch models

| Situation | Recommended model |
|---|---|
| One writer, no protected production baseline | Commit small verified changes to the default branch |
| Short reviewed change | Short-lived feature branch and pull request |
| Multiple concurrent writers | One branch or worktree per writer with one integration owner |
| Stable production baseline and long-running next phase | Stable default branch plus one integration branch |

Do not create branches for ceremony. Activate branch or worktree rules when review, concurrency,
release isolation, or production stability creates the need.

Every non-default model records both its activation condition and its retirement condition. Branch
topology is not a work-status source. When topology is retired, preserve historical receipts and
remove old branch commands, merge sources, and worktree paths from current governance documents.

Invest-derived integration lessons:

- keep the production baseline stable and integrate small fixes independently.
- create long-running feature branches from the current integration branch, not an outdated base.
- merge baseline changes into the integration branch promptly instead of accumulating a large final
  conflict.
- do not rebase or otherwise rewrite shared baseline and integration history.
- inspect repository status before and after merges, commits, and worktree integration.
- never carry runtime output or unrelated user changes across branches accidentally.
- when the default branch is also a production worktree, inspect schedules and running processes
  before runtime-sensitive edits and keep entry points out of readable intermediate states.

### 4.5 Commit contract

Each commit should:

- represent one coherent verified change.
- carry the applicable permanent work ID.
- explain what changed and why.
- include only intended maintained source, configuration, tests, and documentation.
- leave secrets, production data, logs, reports, caches, backups, and unrelated user changes out.
- follow the applicable Definition of Done before the work is reported complete.

The commit message or linked history entry records the important verification evidence. Do not use
one large commit to hide several unrelated outcomes.

### 4.6 Ignore policy

Tailor .gitignore to the selected runtime and tools. Consider:

- operating-system and editor metadata.
- local environment files and all secret-bearing files.
- virtual environments, dependency caches, build output, and compiled artifacts.
- logs, generated reports, disposable caches, locks, and temporary state.
- live database files, production snapshots, backups, and recovery archives.
- local tool state that cannot be shared safely.

Do not ignore maintained schema, migrations, safe fixtures, source configuration, tests, or required
evidence merely because they share a parent directory with generated files.

### 4.7 Remote, visibility, and license

Creating a remote repository, changing visibility, pushing commits, or publishing a site is an
external action and requires explicit user approval.

The proposal states:

- local-only or remote mode.
- hosting provider and remote purpose when applicable.
- public or private visibility.
- who may push, merge, administer, or change protection.
- whether pull requests and required review are active.
- license choice and whether code and documentation need different licenses.
- large binary or generated artifact handling.

Record commit, push, merge, administration, visibility, and history-rewrite authority in AGENTS.md
under Team facts. Record repository mode, provider, template source, ignore policy, license, and
initial checkpoint in PROJECT_WORKFLOW.md under Project facts.

Git history is not a substitute for database backup, artifact retention, or disaster recovery.

### 4.8 Initial repository checkpoint

Create the first project commit only after the approved initialization files have been materialized
and validated. Record:

- the template source and version.
- the approved structure and active governance sections.
- the first permanent work ID.
- validation evidence and unresolved limitations.

Do not push the initial commit unless remote creation or use and push authority were explicitly
approved.

## 5. Maintained source directories

Choose a compact profile or a layered profile. Do not create both without an explicit mapping.

### 5.1 Compact application profile

Use this profile when one application can remain understandable without top-level architecture
layers.

| Path | Responsibility |
|---|---|
| app/ or src/ | Maintained application code |
| app/domain/ | Business rules and typed domain concepts when separation becomes useful |
| app/services/ | Application use cases and orchestration |
| app/adapters/ | Database, provider, network, and platform integrations |
| app/entrypoints/ | CLI, API, worker, scheduler, and composition roots |

Only create the internal subdirectories that the project needs.

### 5.2 Layered application profile

Use this profile when several pipelines, providers, data stores, or delivery surfaces require hard
dependency boundaries.

| Path | Responsibility | Dependency rule |
|---|---|---|
| domain/ | Provider-independent rules, contracts, value objects, and states | Depends on no infrastructure SDK |
| application/ | Use cases, orchestration, and transaction boundaries | Depends on domain and ports |
| ports/ | Interfaces for storage, providers, clocks, models, brokers, and delivery | Defines boundaries, not implementations |
| infrastructure/ | Database, queue, provider, scheduler, model, and external-system adapters | Implements ports |
| entrypoints/ | CLI, API, worker, scheduled job, and composition roots | Wires application and infrastructure |

The normal dependency direction is entrypoints to application to domain and ports, with
infrastructure implementing ports. Application and domain do not import entrypoints.

### 5.3 Shared maintained categories

| Path | Responsibility | Version-control policy |
|---|---|---|
| config/ | Non-secret configuration, registries, policy files, and schemas | Include maintained configuration |
| dashboard/ or web/ | Maintained generators and optional human-facing control, status, or observation service | Include maintained source; generated HTML remains derived |
| db/schema/ | Canonical database schema definitions | Include |
| db/migrations/ | Ordered, reversible where practical, schema and data migrations | Include |
| db/fixtures/ | Small synthetic or development-only fixtures | Include when safe |
| tools/ | Human-invoked validation, inspection, maintenance, migration, and recovery utilities | Include |
| setup/ | Installation, deployment, service, scheduler, and environment setup | Include |
| assets/ | Maintained static images, styles, templates, or other packaged assets | Include |

Live database files do not become source merely because they are stored under db/. Their authority,
backup, recovery, sensitivity, and version-control policy must be explicit.

A local project service is not selected merely because `dashboard/` or `web/` exists. Static HTML
remains the default. When HTTP is justified, bind to loopback and expose read-only projections unless
the Product Owner separately approves network exposure or a write control plane with security,
identity, audit, and recovery evidence.

## 6. Test structure

Create test categories according to actual risk and system boundaries.

| Path | Responsibility |
|---|---|
| tests/unit/ | Isolated rules, calculations, validation, and edge cases |
| tests/integration/ | Components working with storage, providers, processes, or runtime wiring |
| tests/contract/ | Interfaces, schemas, events, compatibility, and dependency-direction contracts |
| tests/end_to_end/ | Critical user or operator journeys across the running system |
| tests/replay/ | Historical decisions, events, or workflows reproduced deterministically |
| tests/migration/ | Schema, data, configuration, or compatibility migrations |
| tests/fixtures/ | Synthetic, immutable, and clearly non-production test inputs |

Do not create a test directory merely to claim a test layer exists. Create it when a real test owns
that responsibility.

## 7. Generated and runtime directories

These paths normally exist outside maintained source history. Their retention and backup rules may
differ because some contain evidence or authoritative operational state.

| Path | Responsibility | Normal treatment |
|---|---|---|
| logs/ | Append-only or rotating execution and diagnostic logs | Exclude; define retention |
| reports/ | Generated analysis, test, audit, or user reports | Exclude unless curated as a release artifact |
| state/status/ | Current health, readiness, and job-status projections | Exclude; usually reconstructible |
| state/cache/ | Disposable provider, query, or computation cache | Exclude; reconstructible |
| state/snapshots/ | Point-in-time operational or recovery snapshots | Exclude; govern retention and integrity |
| state/receipts/ | Backup, restore, migration, retention, release, or approval evidence | Preserve according to audit policy |
| state/tracking/ | Runtime checkpoints, cursors, claims, and progress state | Exclude; define recovery semantics |
| state/locks/ | Process and occurrence locks | Exclude; disposable with safe stale-lock handling |
| archive/ | Immutable large objects or retired runtime material | Govern authority, retention, and checksums |
| backups/ | Verified recovery copies | Keep outside the working repository when practical |

Do not assume every state file is disposable. Classify each as authoritative, reconstructible,
evidence, or cache before defining deletion and backup rules.

## 8. Documentation directory

The docs/ directory contains maintained AI-readable project truth and history. Human-facing HTML
may be generated from these sources, but generated HTML is not an independent source of truth.

| Path | Question answered | Lifecycle |
|---|---|---|
| docs/product_brief.md | Why does the project exist, for whom, and what proves value? | Maintained baseline; update only through product decision |
| docs/module_structure.md | What is true about the system now? | Current-state source; update with lasting system changes |
| docs/modules/ | Which detailed contracts and operating boundaries belong to one stable module? | Create only when a module outgrows the compact current-state map |
| docs/phase_roadmap.md | Which major outcomes, releases, or phases are planned? | Activate only for multi-level planning |
| docs/phase_plans/ | What order, dependency, and early-start boundary governs one phase? | Activate only when roadmap and current queue cannot own this detail cleanly |
| docs/current_work.md | What unfinished work is active now? | Active queue only; remove completed items |
| docs/feature_plans/ | What durable scope, boundary, risk, and verification agreement governs one feature? | One file for a large, multi-session, boundary-crossing, or high-risk feature |
| docs/adr/ | Why was a durable architecture or data decision made? | Immutable decision history with explicit supersession |
| docs/history/ | What work was completed and what was learned? | Append by period or controlled engineering log |
| docs/review_scope.md | What standing criteria does independent review apply? | Change only with Product Owner approval |
| docs/review.md | What did the latest independent review find? | Replace each review; history preserves accepted work |
| docs/runbooks/ | How are deployment, operation, incident response, backup, and recovery performed? | Maintain with operating behavior |
| docs/archives/ | Which superseded maintained documents must be retained for reference? | Never use as current truth |
| docs/risk_register.md | Which enduring material risks need owners and treatment? | Optional when risks outlive one feature plan |
| docs/terminology.md | Which terms, definitions, code forms, and translations are canonical? | Create when ambiguity, domain language, or multiple locales trigger it |
| docs/view_registry.md | Which sources, generators, locales, and freshness rules own split or live human views? | Create when the control surface expands beyond one static page |

If a machine-readable dashboard already depends on docs/plan.txt, that path may replace
docs/current_work.md. Record the choice in Project facts and keep one active queue only.

## 9. Planning and tracking artifact contracts

### 9.1 Product brief

Default path: docs/product_brief.md

Minimum content:

- original idea and problem.
- intended users and affected parties.
- intended outcomes and observable success evidence.
- non-goals and acceptable failure envelope.
- key assumptions and stop or pivot evidence.
- product authority and approval boundaries.

This is the alignment source checked before and after each feature.

### 9.2 Current-state document

Default path: docs/module_structure.md

Minimum content:

- entrypoints and operating surfaces.
- module responsibilities and dependency direction.
- interfaces, data contracts, schemas, and authoritative data ownership.
- runtime schedules, failure modes, degradation, recovery, and observability.
- current environment constraints and known limitations.
- last verified version or commit when the repository supports it.

Describe only what is true now. Plans belong elsewhere. When code and this document disagree, report
the discrepancy and correct the document through the normal workflow.

### 9.3 Product roadmap

Default path: docs/phase_roadmap.md

Activation condition: several outcomes, releases, or long-running features compete for priority.

Minimum content:

- phase or release ID and intended outcome.
- feature or epic IDs assigned to that phase.
- priority and current high-level state.
- entry and exit evidence.
- pointer to the one detailed feature plan when one exists.

The roadmap does not contain task-level implementation detail. Only the Product Owner changes major
priority or moves work between phases.

### 9.4 Phase delivery plan

Default path pattern: `docs/phase_plans/PHASE-ID.md`

Create only when a phase or long-running release needs an internal order or dependency graph that
does not belong in the roadmap or active queue.

Minimum content:

- phase or release ID and intended outcome.
- delivery-group registry with stable `DG-NNN` IDs, one unique positive `group_order` per active
  group, and the intended outcome of each group.
- membership table assigning every sequenced work ID to exactly one `delivery_group`.
- resolvable cross-group and cross-feature dependencies, including dependency type and reason.
- for every work ID, pointers to its exact-scope owner, scope revision, and approval evidence.
- entry, early-start, and exit conditions.
- data-clock-critical items, latest activation points, maturity delays, and isolated shadow options.
- pointers to detailed feature plans without copying their milestone status.

The phase plan owns `delivery_group`, `group_order`, and within-phase cross-item dependencies. It
does not own exact scope or approval prose; it points to their owner and records the approved scope
revision needed by the sequencing gate. The roadmap owns phase priority; the current work list owns
active status; feature plans own detailed milestones.

Before implementation, read the phase plan in the mandatory sequence
`delivery_group -> group_order -> dependencies -> approval/exact scope`. Missing group membership,
duplicate order, unresolved or cyclic dependencies, a dependency on a later group, or approval that
does not name the current scope revision blocks the affected work.

#### Delivery validation receipt

Default current receipt path: `state/status/delivery_sequence_validation.json`

The project-specific delivery validator writes this receipt atomically after evaluating the active
phase plan. It is derived status, not a source of planning truth. Minimum JSON contract:

- `schema_version`: `1`.
- `result`: `pass` or `fail`.
- `validated_on`: non-empty UTC timestamp.
- `coordination_source` and `coordination_source_sha256`.
- `validator_path` and `validator_sha256`.
- `validation_command`.
- `check_order` and `checked_steps` in the mandatory order.
- `items`: at least one record containing `work_id`, `delivery_group`, `group_order`,
  `dependencies`, `scope_owner`, `scope_owner_sha256`, `scope_revision`, `approval_state`,
  `approval_evidence_ref`, and `approved_scope_revision`.
- `errors`: an array, empty only when `result` is `pass`.

The core validator verifies the receipt rather than trusting its filename: all paths and commands
must match `project_profile.yaml`; all bound files must exist and match their recorded SHA-256; work
IDs must be unique; group IDs and order values must be valid and consistent; approval state must be
`approved`; and `approved_scope_revision` must equal the current `scope_revision`. Any mismatch is
`stale` or `failed` and blocks implementation. Completed-work history preserves the receipt or its
digest when the active receipt is replaced.

### 9.5 Current work list

Default path: docs/current_work.md

Invest-compatible alternative: docs/plan.txt when a live parser requires that filename.

Minimum content for every item:

- permanent work ID.
- priority.
- status.
- concise outcome or next action.
- owner.
- blocker, entry condition, and evidence path when blocked.
- pointer to a detailed feature plan instead of copied detail.
- `delivery_group` pointer when grouped delivery is active.
- when no feature plan is justified: exact scope, non-goals, stable scope revision, approval state,
  approval evidence, and the approved scope revision.

Keep unfinished work only. Before removing a completed item, update current state when necessary and
record the outcome in history under the same permanent work ID.

### 9.6 Feature plan

Default path pattern: docs/feature_plans/WORK-ID_short_name.md

Use for a feature that is too large for the current work list, crosses a durable boundary, spans
sessions or milestones, or is governed by WF-DATA, WF-OPS, WF-RECOVERY, or WF-HIGH-IMPACT.

Minimum content:

- permanent parent work ID and child work IDs.
- connection to product intent and roadmap outcome.
- exact scope, non-goals, boundaries, contracts, assumptions, and risks.
- stable scope revision plus approval state, approver, date, evidence reference, and approved scope
  revision. A scope change creates a new revision and requires approval to be re-evaluated.
- `delivery_group` pointer and phase-plan pointer when grouped delivery is active.
- ordered milestones with phase ownership where relevant.
- test strategy, acceptance evidence, rollback, and observability.
- evidence-generation funnel, maturity delay, and gate reachability when thresholds depend on data.
- done and pending status maintained only in this file.
- history and commit references for completed milestones.

The current work list remains the only source of the feature's current queue status. The feature
plan owns exact scope, approval binding, milestone detail, and evidence state. The phase plan owns
delivery grouping, group order, and cross-item dependencies. The roadmap and current work list point
to these owners; they do not reproduce their checklists.

### 9.7 Architecture Decision Record

Default path pattern: docs/adr/ADR-NNN_short_name.md

Minimum content:

- status and date.
- context and decision pressure.
- options considered.
- decision and rationale.
- consequences, limitations, and rollback or supersession path.
- related permanent work IDs.

Do not reopen an accepted decision without new evidence. Supersede it with a new ADR rather than
rewriting history.

### 9.8 Engineering history

Default path pattern: docs/history/YYYY-MM_engineering_log.md

Minimum content:

- completion date.
- permanent work ID.
- delivered outcome and reason.
- important implementation or migration facts.
- verification evidence.
- commit or version reference.
- remaining limitations or follow-up IDs.

History records completed work. It does not remain in the active queue.

### 9.9 Review scope

Default path: docs/review_scope.md

Minimum content:

- standing review boundaries.
- architecture, correctness, security, data, testing, and documentation criteria.
- commands the reviewer may run.
- files or data the reviewer must not modify.
- output path and severity definitions.

### 9.10 Latest review report

Default path: docs/review.md

Minimum content:

- review date, reviewed version, and scope.
- severity, file and line, reason, suggested correction, and uncertainty for every finding.
- separation of confirmed defects from methodology recommendations.

This file represents the latest complete review and may be replaced. Once accepted, a finding links
to a permanent work ID outside this temporary report.

### 9.11 Terminology registry

Default path: `docs/terminology.md`

Minimum content for each governed term:

- stable term ID and canonical engineering term.
- exact definition and code, schema, or typed-value form.
- approved human-view translations.
- deprecated, ambiguous, or forbidden aliases.
- version or supersession relationship when meaning changes.

Translation is presentation. It does not replace source evidence or alter identifiers, IDs, enum
values, unknown semantics, or stored lineage.

### 9.12 Human-view registry

Default path: `docs/view_registry.md`

Create when the control surface expands beyond `project-overview.html` into a second generated page
or live endpoint. Record view ID, output path, page role, perspective, authoritative sources,
runtime-evidence inputs, generator command, locale, source version, freshness rule, failure
behavior, bind scope, and write-back authority. The registry owns view configuration, not rendered
facts.

### 9.13 Runbooks

Default path pattern: docs/runbooks/operation_name.md

Create a runbook for operations that must be repeatable under pressure, including deployment,
incident response, backup, restore, migration, key rotation, or scheduler cutover. Include
prerequisites, authority, commands, evidence, failure handling, rollback, and completion criteria.

## 10. Artifact relationship rules

- Product brief owns purpose and success.
- Roadmap owns future major priority.
- A phase delivery plan owns order and dependencies inside one phase when that layer is active.
- That phase plan also owns delivery-group membership and group order; exact scope and its approval
  remain together in the feature plan or small current-work item.
- Current work owns the active queue.
- One feature plan owns the detailed status of one large feature.
- Current state owns what the system is now.
- ADRs own durable decision rationale.
- Review report owns only the latest review findings.
- History and version control own completed-work evidence.
- Runbooks own repeatable operations.
- Terminology registry owns canonical project vocabulary when activated.
- View registry owns generation contracts; Markdown, executable sources, and authoritative data own
  the facts being rendered.
- Every feature and bug fix keeps the same permanent work ID across all applicable artifacts.

When two files answer the same question, choose one owner and replace the other detail with a
pointer.

## 11. Minimal greenfield starting set

The reusable framework files may all be present, but they are framework_retained rather than
evidence that every project artifact or governance module is active.

Do not create the full project tree on day one. A typical approved project-controlled starting set
contains:

- local Git and a tailored .gitignore unless version control is explicitly deferred with a reason.
- project_profile.yaml.
- docs/product_brief.md.
- docs/current_work.md with the first permanent work ID.
- project-overview.html generated from approved facts and unresolved decisions, with management,
  business, operations, and architecture/delivery perspectives.
- a compact communication contract in project_profile.yaml, using the recommended language default
  unless the Product Owner approves a different boundary.

Create docs/module_structure.md only when maintained code, executable configuration, schema, or
operating behavior exists. It must describe present reality, never planned architecture.

Create the first application source path and the first required test layer when the first work item
is ready to materialize code. Do not create empty directories for appearance.

The four perspectives are required even before all their source systems exist. An unavailable
perspective contains a real source state and reason, accountable owner, and activation or recovery
trigger; it is not an empty placeholder and does not claim healthy status.

Create config/, dashboard/, db/, logs/, reports/, state/, setup/, roadmap, phase plans, feature
plans, module owner docs, terminology, view registry, additional HTML views, ADRs, review files, and
runbooks only when they have an immediate consumer and meaningful current content.
A planned future responsibility normally receives a deferred trigger. A high-risk first feature is
an exception only for its durable feature brief and required safety controls.

Initialization must show the proposed starting set and explain why every selected item is needed.
Placeholders that merely say "nothing exists yet" do not satisfy the inclusion rule.
