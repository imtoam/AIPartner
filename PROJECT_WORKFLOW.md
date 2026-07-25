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
permanent work identity, honest separation of fact and inference, evidence-based completion, or the
duty to stop on a material discrepancy.

## Sections in use

Checked sections apply. Unchecked sections are ignored except for their activation condition.

<!-- BEGIN PROJECT CONFIG: WORKFLOW MODULE ACTIVATION -->
- [x] WF-CORE: Core feature delivery
- [x] WF-STRUCTURE: Repository structure
- [x] WF-VCS: Version control
- [x] WF-DOCS: Documentation and work tracking
- [x] WF-DOD: Definition of Done
- [ ] WF-PLANNING: Multi-level planning
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
- identify new evidence, invalidated assumptions, and follow-up work.
- ask whether the result changes the next priority when the learning is material.

This is the project's practical use of Agile feedback, Lean learning, Kanban flow, Continuous
Delivery evidence, and risk management.

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

One line of work has one detailed owner. Other documents may point to it but must not copy its
status in full.

Do not treat history as current state. Do not treat a roadmap as the current work list. Generated
HTML is a human view and not a source of truth.

project_profile.yaml owns initialization state, approval evidence, module activation summary,
structure decisions, unresolved decisions, and pointers. It does not own current work status,
current system behavior, roadmap status, or completed-work history.

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

## WF-DOD: Definition of Done

A change is complete only when every applicable item below is satisfied.

1. Alignment

   The delivered behavior matches the approved feature outcome, the original product intent, the
   agreed boundaries, and the stated non-goals. Any discrepancy has been resolved with the Product
   Owner.

2. Structure

   Changed files pass the project's syntax, type, schema, or structural checks.

3. Function

   A test or direct check demonstrates that the intended behavior works. A syntax check alone is
   not enough.

4. Test strategy

   The agreed risk-based test layers and acceptance evidence have been completed. Negative,
   boundary, failure, and recovery cases are covered where applicable. Untested areas are explicit.

5. Regression

   Relevant regression checks pass. Add a regression case when the change fixes a defect that
   could return.

6. Current state

   Update the current-state document when the change adds or alters a module, interface, data
   contract, schema, schedule, failure mode, or operating behavior.

7. Tracking

   Remove completed work from the active list. Record the outcome in history. Update the roadmap or
   feature plan when an activated planning section requires it.

8. Documentation checks

   Run the project's documentation and reference checks.

9. Version control

   Commit only intended source, configuration, tests, and maintained documentation. Keep runtime
   output, caches, logs, and unrelated user changes out of the commit.

10. Risk

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

Use three levels only when each level has a distinct purpose:

| Level | Purpose |
|---|---|
| Roadmap | Major outcomes, releases, and future priority |
| Current work list | Work in the current phase or release |
| Feature plan | Detailed breakdown of one large feature |

Rules:

- The Product Owner approves movement between phases or major priorities.
- The current work list contains current unfinished work only.
- Future work belongs in the roadmap, not the current queue.
- A large feature keeps its detailed status in one feature plan.
- Other files point to the feature plan instead of copying its details.
- Completed work moves to history.

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

Structure tailoring decisions:

Deferred structure triggers:

Local structure extensions and reasons:

Planning and tracking artifact paths:

Syntax and structural check commands:

Functional test commands:

Regression commands:

Documentation check commands:

Current-state document:

Current work list:

Roadmap:

Decision records:

History:

Production data locations:

Scheduled jobs:

Generated or runtime-only paths:

Known environment constraints:
<!-- END PROJECT CONFIG: PROJECT FACTS -->
