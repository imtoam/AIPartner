# PROJECT_WORKFLOW.md

Project delivery and governance method

This file is the canonical project method throughout the project lifecycle. It defines how work
moves from an idea to verified delivery. Roles, authority, permissions, and collaboration
boundaries belong in AGENTS.md. One-time initialization belongs in START_HERE.md. Project-specific
paths and commands belong in the final section of this file.

Framework invariant:

- Keep every workflow module in this file.
- Tailoring changes module activation inside the marked configuration region. It never deletes,
  renames, reorders, or rewrites an inactive module.
- Initialization may edit only the two regions marked BEGIN PROJECT CONFIG and END PROJECT CONFIG.
- Stable workflow module IDs remain unchanged.
- WF-VCS is a core module. A project may defer Git, but it may not remove version-control
  discovery, authority, or deferral rules.
- WF-COMMUNICATION and WF-VIEWS are core modules. Every project records a compact language
  contract and keeps human-facing projections subordinate to authoritative sources.

Do not duplicate this methodology in AGENTS.md or START_HERE.md. Those files may route to it,
configure it, or record approvals without redefining its rules.

Read this file before shaping, planning, implementing, testing, reviewing, releasing, or operating
a project change. A factual answer or a small mechanical edit may not require the complete file.

Read PROJECT_STRUCTURE_REFERENCE.md only when initializing or restructuring the repository,
selecting a new directory category, or creating a new planning or tracking artifact. It is a menu of
defaults, not project truth.

## Global tailoring rule

Use the smallest process and artifact set that can control the project's current value, complexity,
and risk.

- Apply core principles to every applicable change, but tailor their depth and evidence to impact.
- Activate optional sections only when their stated conditions exist.
- Do not create a planning layer, document, directory, test layer, role, or ceremony merely because
  the template contains it.
- Use the tailoring protocol in PROJECT_STRUCTURE_REFERENCE.md for selections, deferrals,
  exclusions, and local extensions.
- Re-evaluate the selection when product, architecture, collaboration, operation, or risk changes.
- Base activation on user-stated or observed target-project conditions. An artifact created by
  activating a module is never evidence that the module was needed.
- A planned future condition normally creates a deferred trigger. It activates a module now only
  when the next approved increment would cross that boundary and needs the control before work
  begins.

Tailoring may avoid unnecessary ceremony. It may not remove framework sections, human authority,
permanent work identity, honest separation of fact and inference, the language-of-record contract,
source-versus-view separation, evidence-based completion, or the duty to stop on a material
discrepancy.

## Sections in use

Checked sections apply. Unchecked sections are ignored except for their activation condition.

<!-- BEGIN PROJECT CONFIG: WORKFLOW MODULE ACTIVATION -->
- [x] WF-CORE: Core feature delivery
- [x] WF-COMMUNICATION: Language, terminology, and translation
- [x] WF-STRUCTURE: Repository structure
- [x] WF-VCS: Version control
- [x] WF-DOCS: Documentation and work tracking
- [x] WF-VIEWS: Human-readable project views
- [x] WF-DOD: Definition of Done
- [ ] WF-PLANNING: Multi-level planning
- [ ] WF-DRIFT: Architecture and governance drift control
- [ ] WF-DATA: Authoritative and non-cleanable data
- [ ] WF-OPS: Unattended operation
- [ ] WF-RECOVERY: Backup and recovery
- [ ] WF-HIGH-IMPACT: High-impact changes
<!-- END PROJECT CONFIG: WORKFLOW MODULE ACTIVATION -->

During initialization, the AI recommends which optional sections are needed. The Product Owner
approves the selection.

After initialization, if an activation condition becomes true, the AI explains why the section is
needed and asks the Product Owner before checking it. Record the change in project history. Do not
activate project governance silently.

## WF-CORE: Core feature delivery

Use this loop for every non-trivial feature, defect, or operational change. A mechanical edit may
use a shorter version, but it still needs a stated intent and proportionate verification.

### 1. Reconnect to purpose

Before proposing implementation, read the current product intent, relevant current-state facts,
active work, and applicable decisions. State:

- which user or project problem this change addresses.
- what observable outcome should improve.
- how it supports the original idea and current priority.
- what is explicitly outside this change.

If the connection is weak, contradictory, or based on a new product direction, stop and discuss it
with the Product Owner.

### 2. Shape the feature together

The AI leads a concise discussion covering the applicable questions:

- Who experiences the problem and what do they need to do?
- What behavior or outcome would count as success?
- What is included, excluded, and deliberately deferred?
- Which module, interface, data, permission, external system, or operating process is crossed?
- What existing behavior and compatibility must remain?
- Which assumptions are unverified?
- Which language, terminology, source-text, or translation boundary could change the meaning?
- What can fail, how harmful is failure, and how will the system fail safely?
- What must be observable, recoverable, reversible, or approved by a human?

Do not respond to a vague request by asking the Product Owner to design the feature. Summarize the
request, identify missing product, delivery, architecture, QA, security, risk, or operations
perspectives, recommend a bounded solution, and explain the tradeoffs. Ask only for decisions that
would materially change value, scope, risk, cost, or authority.

### 3. Agree on test strategy before implementation

Define acceptance evidence from the user's perspective, then select test layers according to risk.
Consider:

- unit tests for isolated rules and edge cases.
- integration tests for components, storage, providers, and runtime wiring.
- contract tests for interfaces, schemas, events, and compatibility.
- end-to-end tests for critical user journeys.
- replay or migration tests when history or stored data must remain valid.
- security, privacy, performance, concurrency, and recovery tests when the risk requires them.
- terminology, source-preservation, translation, and generated-view checks when those contracts are
  affected.

Cover applicable positive, negative, boundary, failure, retry, idempotency, permission, and data
isolation cases. State what will not be tested and why. Use temporary or synthetic data when real
data is unsafe or cannot be cleaned.

The test strategy is part of feature design. Do not wait until the code is finished to decide what
evidence would prove it works.

Record a durable feature brief before implementation when the work is non-trivial and any of these
is true:

- it crosses an architecture, data, permission, external-system, or operational boundary.
- WF-DATA, WF-OPS, WF-RECOVERY, or WF-HIGH-IMPACT applies.
- more than one session, contributor, or delivery milestone is likely.
- the agreed boundary, non-goals, failure behavior, or test strategy would otherwise be lost.

A small low-risk change may keep the agreement in the active-work item. A high-risk change may not
skip durable agreement merely because it is the first feature.

### 4. Pass the readiness and alignment gate

Implementation may begin when:

- the intended outcome, scope, and non-goals are clear enough for the next increment.
- affected boundaries and material risks are understood.
- unresolved decisions that could change the solution are owned or resolved.
- acceptance evidence and test approach are agreed.
- affected canonical terms, source-language rules, and human-view consequences are explicit.
- the work fits the current priority and does not contradict the product brief, current state,
  roadmap, or accepted decisions.

The Product Owner approves material product, priority, authority, and risk choices. The AI owns
ordinary technical execution within those choices.

### 5. Implement in small controlled increments

- Keep active work visible and limit parallel work.
- Preserve module and data ownership boundaries.
- Verify the riskiest assumption early.
- Keep changes small enough to review and recover.
- Report evidence and limitations, not activity alone.

If implementation reveals a material discrepancy, stop at a safe point and use the discrepancy
protocol below.

### 6. Verify and check back

Before declaring completion, compare:

- implemented behavior against the agreed feature outcome and acceptance evidence.
- the feature against the original project idea and current product intent.
- changed boundaries against the documented architecture and data ownership.
- actual risk and operating behavior against the approved assumptions.
- delivered scope against the agreed non-goals and deferred work.
- maintained sources against generated HTML or service views, including freshness and unresolved
  discrepancies.

Passing tests does not excuse a product or architecture mismatch. Product alignment does not excuse
missing verification.

### 7. Discrepancy protocol

When a material mismatch is found, report:

1. Expected: the approved intent, boundary, plan, or evidence.
2. Observed: what the code, data, environment, or result actually shows.
3. Impact: effect on users, scope, risk, schedule, compatibility, or recovery.
4. Options: realistic responses and their tradeoffs.
5. Recommendation: the AI's preferred next step and reason.
6. Decision needed: what the Product Owner must approve or clarify.

Do not continue through a material discrepancy merely to finish the planned task. Record the
resolution in the appropriate decision, plan, or current-state document.

### 8. Close the learning loop

After verification:

- update current system truth before closing the work item.
- record durable decisions and completed-work history.
- regenerate affected human views from their declared sources and preserve visible stale or error
  evidence when regeneration cannot succeed.
- identify new evidence, invalidated assumptions, and follow-up work.
- ask whether the result changes the next priority when the learning is material.

This is the project's practical use of Agile feedback, Lean learning, Kanban flow, Continuous
Delivery evidence, and risk management.

## WF-COMMUNICATION: Language, terminology, and translation

Every project records a compact communication contract during initialization. Ask for one bundled
decision with a recommended default rather than presenting a language questionnaire.

Recommended default:

- the Product Owner and AI converse in the Product Owner's preferred language.
- maintained code identifiers, schemas, typed values, technical documentation, configuration names,
  and version-control records use one engineering language of record, normally English.
- human-facing views may use one or more approved presentation locales.
- externally sourced evidence preserves its original text, source language when known, time, URL,
  hash, and lineage.
- translation is a derived presentation artifact. It does not replace source evidence, add claims,
  change typed values, or turn unknown, stale, or insufficient data into a conclusion.

Record conversation languages, the engineering language of record, the language of code identifiers
and typed values, human-view locales, source-evidence treatment, and the translation policy as
separate facts. Do not use one field called merely `language` for all of these responsibilities.

Create a terminology registry only when domain language, multiple locales, external contracts, or
observed ambiguity justify it. The normal path is `docs/terminology.md`. Each governed term records
a stable term ID, canonical engineering term, definition, code or schema form, approved
translations, and deprecated or ambiguous aliases. A semantic change receives a new version or
term ID; do not silently redefine a term already present in code, data, decisions, or history.

Conversation and human-view translation may be flexible in style, but engineering terms and typed
semantics remain exact. Historical material without a versioned language or terminology marker is
unknown under that contract; do not infer, translate, backfill, re-embed, re-index, or rewrite it as
if missing provenance were known.

## WF-STRUCTURE: Repository structure

Organize the repository by responsibility so that a human or future AI can locate truth, source,
tests, tools, and runtime evidence without reconstructing the whole project from history.

PROJECT_STRUCTURE_REFERENCE.md owns the complete directory and artifact catalog. Initialization
selects from that reference and records the actual names and ownership in Project facts. Use only
categories the project needs.

Rules:

- Do not create every category by default or keep empty directories for appearance.
- Do not mix production data, generated output, or cache with maintained source.
- Identify authoritative data, derived projections, and disposable output explicitly.
- Keep entry points small and preserve a clear dependency direction between modules.
- Give each important data set, interface, and module one owner.
- Put secrets outside version control and record only how they are supplied.
- Update this map when a new responsibility or runtime category appears.

### Module identity and ownership

Once maintained code exists, give each stable module or pipeline a responsibility-based module ID.
The current-state document records, at a depth proportionate to the project:

- module ID, responsibility, and owner.
- entry points and public interfaces.
- data, schema, and configuration it owns.
- allowed and forbidden dependency directions.
- test owner and operating surface.
- a pointer to a detailed module document when one is justified.

Keep a compact project in one current-state map. Create `docs/modules/MODULE-ID.md` only when a
module has enough contracts, risks, or operating detail to need its own owner document. The
current-state map then keeps a summary and pointer instead of copying the detail.

Every non-trivial feature names the modules it changes and whether it introduces a new dependency,
data owner, runtime boundary, or public contract. A small request that unexpectedly crosses several
unrelated modules is drift evidence and must be explained before implementation continues.

### Current and planned state

- Current-state documents and Project facts contain observed present reality only.
- Approved future architecture, paths, schedules, and commands belong in a feature brief, roadmap,
  ADR, or deferred trigger.
- Never turn a proposed default branch, runtime command, production store, or schedule into a
  current fact before it exists.
- "Not found" and "not yet established" remain explicit unknowns or deferred items.

## WF-VCS: Version control

Use the Git tailoring guidance in PROJECT_STRUCTURE_REFERENCE.md to select and record the repository
mode. Local Git is the normal software-project default; remote hosting and branch complexity require
their own evidence and approval.

- Inspect repository state before changing files or Git configuration.
- Preserve existing history, user work, remotes, and unrelated changes.
- Never remove .git, rewrite shared history, force-push, or discard work without explicit authority.
- Keep commits small, coherent, verified, and traceable to permanent work IDs.
- Inspect status and intended diffs before and after commits, merges, and integration.
- Keep secrets, production data, runtime output, caches, reports, and backups out of commits unless
  an explicit evidence policy says otherwise.
- Activate branches, pull requests, worktrees, protection, and integration rules only when review,
  concurrency, release isolation, or baseline stability requires them.
- Treat remote creation, visibility changes, pushes, publication, and administrative changes as
  external actions requiring user approval.

The initial project commit follows successful initialization validation. Git history does not
replace data backup, artifact retention, or recovery testing.

### Complexity ladder

Use the least complex Git mode supported by current evidence:

| Condition | Normal mode |
|---|---|
| One writer and no protected production baseline | Small verified commits on the default branch |
| Independent review or a protected remote baseline | Short-lived branch and pull request |
| Concurrent writers | One branch or worktree per writer and one integration owner |
| Stable production baseline plus long-running next release | Default baseline plus one integration branch |

A branch isolates code; it is not the source of work-item status, phase ownership, or completed-work
truth. Do not encode mutable phase, priority, status, or assignee in permanent work IDs.

Record an activation condition and a retirement condition for every non-default branch model. When
the condition disappears, preserve necessary historical receipts, retire the topology deliberately,
and remove obsolete branch commands and merge sources from live governance documents. Historical
documents may retain them as history.

When the default branch is also a production worktree, inspect related schedules and running
processes before editing runtime-sensitive files. Verify schema and runtime changes with temporary
data, synthetic fixtures, regression checks, and deployment preflight before a scheduler or service
can observe the new version. Do not stage, overwrite, or clean runtime state merely to prepare a
code commit.

If Git is deliberately deferred, Project facts and project_profile.yaml must record the reason,
risk, approval evidence, and activation trigger. The rest of this section remains in force.

## WF-DOCS: Documentation and work tracking

### Document map

Initialization fills the actual paths. Create only documents that have a clear responsibility.

| Question | Owner |
|---|---|
| Why does the project exist? | Product brief |
| What is true now? | Current-state document and executable system |
| What work is active? | Current work list |
| What was agreed for a non-trivial feature? | Feature brief or feature plan |
| What is planned later? | Roadmap, when WF-PLANNING is active |
| Why was a decision made? | Decision record |
| What already happened? | History and version control |
| What did the latest review find? | Review report, when peer review is active in AGENTS.md |
| Which engineering terms have exact meanings? | Terminology registry, when ambiguity triggers it |
| What must each human role see to govern the project? | Required HTML control surface and its declared sources |
| Which maintained sources generate each split or live view? | View registry, when the control surface expands beyond one static page |

One line of work has one detailed owner. Other documents may point to it but must not copy its
status in full.

Do not treat history as current state. Do not treat a roadmap as the current work list. Generated
HTML is a human view and not a source of truth.

project_profile.yaml owns initialization state, approval evidence, module activation summary,
structure decisions, unresolved decisions, and pointers. It does not own current work status,
current system behavior, roadmap status, or completed-work history.

### Authoritative documents and derived views

Maintained Markdown is the authoritative layer for project intent, current architecture, plans,
decisions, work tracking, terminology, and history. Executable code, configuration, schemas, and
authoritative business data retain their own explicit ownership; do not copy them into Markdown and
pretend the copy is executable truth.

HTML, dashboards, diagrams, and HTTP responses are derived views. They may combine maintained
documents with declared runtime evidence, but they may not own approvals, work status, architecture
facts, business truth, or open decisions. A human correction enters the owning source through the
normal workflow and is then regenerated into the view.

### Permanent work identity

Every feature and every bug fix receives a permanent unique work ID before implementation begins.

- Allocate the ID from one project-owned registry or sequence.
- Never reuse, rename, or delete an ID from historical records.
- Do not encode mutable priority, status, phase, release, or assignee in the ID.
- Use the same ID in the feature discussion, active work list, implementation plan, test evidence,
  commits, accepted review findings, decisions, and completed-work history wherever those artifacts
  apply.
- A review-local finding ID is temporary. When the finding is accepted as work, assign or link it to
  a permanent work ID immediately.
- Removing completed work from the active list does not retire its ID. History and version control
  retain it permanently.
- If one item is split into independently deliverable work, create permanent child IDs and preserve
  the parent relationship. Do not silently reuse the original ID for several unrelated outcomes.

The identifier proves continuity of the work, not its current location or status.

### Current work list

- Keep unfinished work only.
- Give each item a priority and a clear status.
- This list is the only source of truth for current work-item status. Other artifacts point to the
  item and must not copy its mutable status.
- Record why blocked work is blocked and what would unblock it.
- Remove completed work after its result is recorded in history.
- Before removing an item, confirm that the current-state document reflects any lasting system
  change.

### Decisions and history

- Record decisions that affect architecture, data contracts, authority, or long-term behavior.
- Record the reason, not only the outcome.
- Give accepted defects or follow-up work stable references.
- Use history and version control for completed work.
- Do not use a temporary review report as a permanent backlog.

## WF-VIEWS: Human-readable project views

Every initialized project provides a static `project-overview.html` as its mandatory human control
surface. `index.html` remains the permanent framework guide. Do not replace either role with the
other.

The human role is not to act as an assistant who reconstructs the project by reading raw logs,
development notes, databases, configuration, or source files. The interface must let people govern
direction, architecture, scope, progress, cadence, risk, health, and decisions while retaining
clickable access to the underlying evidence.

### Four mandatory perspectives

The control surface contains four stable perspectives from initialization onward:

| Perspective | Primary audience | Required content |
|---|---|---|
| Management | Product Owner, management, and project leadership | Direction, intended value, scope, progress, cadence, material risks, open decisions, and management advice |
| Business | Domain specialists and daily business operators | Business recommendations, domain logic, data health, decision status, exceptions, and actions needing specialist judgment |
| Operations | IT operators and reliability owners | Services, jobs, providers, storage, backups, incidents, recovery, capacity, and current health |
| Architecture and delivery | Developers, architects, and delivery owners | Current and approved target architecture, module boundaries, dependencies, phase and feature plans, implementation status, technical risk, and drift |

All four perspectives are present even when the project is new. A perspective without current data
must show `not_yet_available`, `not_applicable`, `blocked`, or `degraded` with its reason, source
owner, and activation or recovery trigger. It must not disappear, invent healthy status, or force
the user to inspect raw evidence to learn that the capability does not exist.

Management advice and business recommendations remain proposals unless their owning source records
an approval or decision. Business health is not inferred from system uptime, and operational health
is not inferred from business outcomes. Architecture views distinguish current observed structure
from approved target plans.

Every generated view displays or embeds:

- a stable page role and view ID.
- authoritative source paths.
- generation time and source version or commit when available.
- freshness, stale, incomplete, or generation-error state.
- visible unresolved decisions relevant to that view.
- a statement that the view is derived and not an independent source of truth.

Generation fails closed. Missing or conflicting sources produce visible error or discrepancy
evidence; an old HTML file must not silently stand in for missing current truth.

The four perspectives may begin as sections in one static page. Split pages activate when their
sources, audiences, or navigation depth justify independent surfaces:

| View | Normal sources | Trigger |
|---|---|---|
| Management | Product brief, roadmap, active work, risks, decisions, verification evidence | Management history or decision volume outgrows the overview section |
| Business | Typed domain read model, business contracts, recommendations, exception queues | Live business health or daily specialist workflow exists |
| Operations | Job manifest, health read model, runbooks, logs and status evidence | A service or unattended job requires live operational handling |
| Architecture and delivery | Current-state map, module owner docs, ADRs, phase and feature plans | Several modules or plans need interactive navigation |

When the control surface splits into a second generated page or live endpoint, create one view
registry, normally `docs/view_registry.md`, that owns view IDs, source lists, generator commands,
locale, freshness rules, and output paths. It does not own the facts being rendered.

Static HTML is the default. A local HTTP service activates only when live refresh, search, filtering,
or structured local-AI access is needed. It binds to loopback and remains read-only by default.
Network exposure, authentication, browser approval, source write-back, or business-data mutation are
separate capabilities requiring explicit authority, threat analysis, audit evidence, and applicable
WF-OPS or WF-HIGH-IMPACT controls. Local AI configuration is a consumer, never the sole store for
open decisions or project truth.

## WF-DOD: Definition of Done

A change is complete only when every applicable item below is satisfied.

1. Alignment

   The delivered behavior matches the approved feature outcome, the original product intent, the
   agreed boundaries, and the stated non-goals. Any discrepancy has been resolved with the Product
   Owner.

2. Structure

   Changed files pass the project's syntax, type, schema, or structural checks.

3. Communication

   Changed identifiers, documents, terms, source evidence, derived content, and translations obey
   the approved language and terminology contract. Original evidence and typed unknown semantics
   remain intact.

4. Function

   A test or direct check demonstrates that the intended behavior works. A syntax check alone is
   not enough.

5. Test strategy

   The agreed risk-based test layers and acceptance evidence have been completed. Negative,
   boundary, failure, and recovery cases are covered where applicable. Untested areas are explicit.

6. Regression

   Relevant regression checks pass. Add a regression case when the change fixes a defect that
   could return.

7. Current state

   Update the current-state document when the change adds or alters a module, interface, data
   contract, schema, schedule, failure mode, or operating behavior.

8. Tracking

   Remove completed work from the active list. Record the outcome in history. Update the roadmap or
   feature plan when an activated planning section requires it.

9. Human views

   Regenerate affected HTML or service projections from declared sources. Verify page role, source
   links, version, freshness, locale, unresolved decisions, and visible failure behavior. Confirm
   the control surface still exposes management, business, operations, and architecture-and-delivery
   perspectives with honest source states, reasons, accountable owners, and activation or recovery
   triggers where applicable.

10. Documentation checks

   Run the project's documentation and reference checks.

11. Version control

   Commit only intended source, configuration, tests, and maintained documentation. Keep runtime
   output, caches, logs, and unrelated user changes out of the commit.

12. Risk

   Apply any additional evidence required by WF-DATA, WF-OPS, WF-RECOVERY, or WF-HIGH-IMPACT when
   those modules are active.

The project-specific commands used for these checks belong in Project facts.

## WF-PLANNING: Multi-level planning

Activation condition:

- the target project currently has at least two phases, releases, or long-running work lines whose
  priority or dependency must be managed separately

Ignore the rest of this section until its checkbox is checked.

A roadmap imagined during initialization is not activation evidence. If only one bounded work item
is ready, keep this module inactive and record a trigger for the point at which competing work
appears.

Use up to four levels, and only when each active level has a distinct purpose:

| Level | Purpose |
|---|---|
| Roadmap | Major outcomes, releases, and future priority |
| Phase delivery plan | Ordered dependencies and early-start boundaries inside one release or long work line |
| Current work list | Work in the current phase or release |
| Feature plan | Detailed breakdown of one large feature |

Rules:

- The Product Owner approves movement between phases or major priorities.
- The current work list contains current unfinished work only.
- Future work belongs in the roadmap, not the current queue.
- A phase delivery plan owns within-phase order and dependencies; the roadmap does not copy them.
- A large feature keeps its detailed status in one feature plan.
- Other files point to the feature plan instead of copying its details.
- Completed work moves to history.

### Forward-data timing and gate reachability

When proposing implementation order, dependencies, or early work, check each item for a data clock:

- whether valid evidence can be faithfully reconstructed later.
- whether collection is prospective or only forward from an activation epoch.
- how long labels, roots, outcomes, or other evidence require to mature.
- whether delay permanently loses point-in-time availability, provider latency, market context,
  cost, or concurrent-condition evidence.

Mark work `data-clock critical` when code may be implemented later but its valid observation window
cannot be recovered. Record the latest safe activation point, the smallest isolated shadow or
bounded capture that can begin earlier, and how it avoids canonical write-back and production
interference. Mark retrospective reconstruction separately; it must not masquerade as prospective
or point-in-time calibration evidence.

Before adopting an evidence threshold or exit gate, estimate its reachability from the actual or
expected generation funnel: exclusion reasons, eligible rate, independence, maturity delay, and
time to threshold. A methodologically attractive gate that can never receive enough valid evidence
is an unresolved product or methodology decision, not a completed plan.

## WF-DRIFT: Architecture and governance drift control

Activation condition:

- the project has several stable modules, pipelines, or generated views whose ownership or
  dependency direction must remain consistent
- a material architecture or documentation drift has been observed
- a branch strategy, module, interface, or source of truth has been retired or replaced

Ignore the rest of this section until its checkbox is checked.

Define proportionate, repeatable checks for:

- stable work, module, term, view, and decision IDs.
- pointers and single ownership of mutable status or detailed plans.
- phase dependency existence, ordering, and cycles.
- code dependency direction and public interface boundaries.
- code, schema, job manifest, current-state, and human-view consistency.
- stale paths, commands, modules, branch markers, and retired operating instructions in live docs.
- generated-view freshness and source completeness.
- deprecated or ambiguous terminology.

The project records the commands in Project facts and adds regression cases for drift that has
already occurred. A drift report is evidence or a work input, not a second current-state source.

## WF-DATA: Authoritative and non-cleanable data

Activation condition:

- the current or next approved increment creates, reads, changes, or depends on production,
  append-only, sensitive, authoritative, or otherwise non-cleanable data

Ignore the rest of this section until its checkbox is checked.

- Tests use temporary databases, fixtures, or synthetic data.
- Read-only diagnostics use read-only connections.
- Tests and review commands do not write production data.
- Authoritative data, derived views, caches, and projections have explicit ownership.
- Schema changes have a migration and recovery plan.
- Append-only or irreversible rules are enforced where practical.
- Prospective, forward-only, retrospective, synthetic, and migrated evidence remain explicitly
  distinguishable.
- A blocked full feature may use an approved isolated shadow capture only when it cannot alter
  canonical truth, backfill an old ledger, or interfere with production scheduling.

## WF-OPS: Unattended operation

Activation condition:

- the current or next approved increment runs on a schedule or without a person present

Ignore the rest of this section until its checkbox is checked.

- Record the real runtime, schedule, and job owner.
- Consider whether files may be read while being edited.
- Use atomic replacement for shared runtime configuration when needed.
- Make repeated execution safe.
- Define locks, timeouts, retries, health checks, and human takeover conditions.
- Record failure evidence instead of silently treating failure as no data.
- Before runtime-sensitive edits in a production worktree, inspect related schedules and running
  processes and avoid leaving entry points in a readable intermediate state.
- A local HTTP project portal binds to loopback and stays read-only unless separately approved;
  non-loopback exposure and write-back require explicit security and authority controls.

## WF-RECOVERY: Backup and recovery

Activation condition:

- authoritative state would be costly or impossible to reconstruct
- a migration, release, retention rule, or incident requires a tested recovery path

Ignore the rest of this section until its checkbox is checked.

- Identify authoritative data that requires backup.
- Verify backups rather than relying on file presence.
- Define the recovery path and its acceptance evidence.
- Keep destructive cleanup separate from ordinary processing.

## WF-HIGH-IMPACT: High-impact changes

Activation condition:

- system output can materially affect money, health, safety, legal rights, privacy, or security
- a change affects concurrency, critical data contracts, or another difficult-to-detect failure mode

Ignore the rest of this section until its checkbox is checked.

- Define the boundary between analysis and real-world action.
- Require explicit human approval for risk-increasing actions.
- Use independent calculation or review for critical logic and contracts.
- Record assumptions, uncertainty, and known limitations.
- Provide safe failure, rollback, and disable behavior.
- Do not allow learned or generated output to gain authority silently.
- Identify professional, legal, regulatory, or security review when applicable.

## Project facts

Initialization fills this section. Keep it factual and current.

Proposals, planned paths, and commands that do not yet work belong in project_profile.yaml as
unresolved or deferred decisions, not in this facts block.

<!-- BEGIN PROJECT CONFIG: PROJECT FACTS -->
Project name:

Version-control system and mode:

Repository discovery state:

Version-control deferral reason and trigger:

Template source and version:

Remote purpose, provider, and visibility:

Ignore policy:

License policy:

Initial project commit:

Permanent work ID format:

Work ID registry or allocation source:

Primary runtime:

Conversation language:

Engineering language of record:

Code identifier and typed-value language:

Human-view locales:

Source-evidence language policy:

Translation and derived-content policy:

Terminology registry and activation trigger:

Supported operating systems:

Application source:

Documentation:

Tests:

Tools:

Dashboard or web interface:

Database definitions:

Configuration:

Setup and deployment:

Selected structure profile:

Module ID and ownership source:

Structure tailoring decisions:

Deferred structure triggers:

Local structure extensions and reasons:

Planning and tracking artifact paths:

Human-interface mode and bind scope:

Human-view registry and generator commands:

Required control-surface perspective sources, states, and owners:

Human-view write-back authority:

Syntax and structural check commands:

Functional test commands:

Regression commands:

Documentation check commands:

Drift and dependency check commands:

Current-state document:

Current work list:

Roadmap:

Decision records:

History:

Production data locations:

Scheduled jobs:

Generated or runtime-only paths:

Known environment constraints:

Git complexity level, activation condition, and retirement condition:
<!-- END PROJECT CONFIG: PROJECT FACTS -->
