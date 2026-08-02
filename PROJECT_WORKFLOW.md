# PROJECT_WORKFLOW.md
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

Project delivery and governance method

This file is the canonical project method throughout the project lifecycle. It defines how work
moves from an idea to verified delivery. Roles, authority, permissions, and collaboration
boundaries belong in AGENTS.md. One-time initialization belongs in START_HERE.md. Project-specific
paths and commands belong in the final section of this file.

Framework invariant:

- Keep every workflow module in the framework: WF-CORE and WF-DOD in this spine, every other
  module in its own retained file under `framework/workflow/`.
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

Read this spine, plus the routed module files whose topics the change touches, before shaping,
planning, implementing, testing, reviewing, releasing, or operating a project change. A factual
answer or a small mechanical edit may not require the complete method.

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
- [ ] WF-PERSISTENCE: Where project state lives
- [ ] WF-ML: Machine learning and model-derived output
- [ ] WF-OPS: Unattended operation
- [ ] WF-RECOVERY: Backup and recovery
- [ ] WF-HIGH-IMPACT: High-impact changes
<!-- END PROJECT CONFIG: WORKFLOW MODULE ACTIVATION -->

During initialization, the AI recommends which optional sections are needed. The Product Owner
approves the selection.

After initialization, if an activation condition becomes true, the AI explains why the section is
needed and asks the Product Owner before checking it. Record the change in project history. Do not
activate project governance silently.

## Workflow module routing

WF-CORE and WF-DOD apply to every change and remain in this spine. Every other module lives in one
file under `framework/workflow/`; its checkbox above controls activation, and the module file is the
sole normative owner of its rules. Load a module file only when the task touches its topic.

| Module | File | Load when |
|---|---|---|
| WF-COMMUNICATION | [framework/workflow/WF-COMMUNICATION.md](framework/workflow/WF-COMMUNICATION.md) | Language, terminology, source evidence, or translation is affected |
| WF-STRUCTURE | [framework/workflow/WF-STRUCTURE.md](framework/workflow/WF-STRUCTURE.md) | Repository layout, module ownership, or current-state mapping changes |
| WF-VCS | [framework/workflow/WF-VCS.md](framework/workflow/WF-VCS.md) | Commits, branches, remotes, history, or repository policy is involved |
| WF-DOCS | [framework/workflow/WF-DOCS.md](framework/workflow/WF-DOCS.md) | Documents, work tracking, work IDs, decisions, or history are touched |
| WF-VIEWS | [framework/workflow/WF-VIEWS.md](framework/workflow/WF-VIEWS.md) | A human view, control surface, or generated page is created or changed |
| WF-PLANNING | [framework/workflow/WF-PLANNING.md](framework/workflow/WF-PLANNING.md) | Phases, delivery groups, sequencing, or evidence gates are involved |
| WF-DRIFT | [framework/workflow/WF-DRIFT.md](framework/workflow/WF-DRIFT.md) | Consistency checks or drift control are involved |
| WF-DATA | [framework/workflow/WF-DATA.md](framework/workflow/WF-DATA.md) | Authoritative, production, or non-cleanable data is crossed |
| WF-PERSISTENCE | [framework/workflow/WF-PERSISTENCE.md](framework/workflow/WF-PERSISTENCE.md) | State must survive a restart, or a store's shape, ownership, or retention changes |
| WF-ML | [framework/workflow/WF-ML.md](framework/workflow/WF-ML.md) | Parameters are learned from data, or a pretrained model becomes part of the output |
| WF-OPS | [framework/workflow/WF-OPS.md](framework/workflow/WF-OPS.md) | Scheduled or unattended operation is involved |
| WF-RECOVERY | [framework/workflow/WF-RECOVERY.md](framework/workflow/WF-RECOVERY.md) | Backup, restore, or recovery paths are involved |
| WF-HIGH-IMPACT | [framework/workflow/WF-HIGH-IMPACT.md](framework/workflow/WF-HIGH-IMPACT.md) | Output can materially affect money, health, safety, rights, privacy, or security |

## Concept ownership registry

Each cross-cutting concept has exactly one normative owner. Other framework files may summarize it
in one sentence and link here; they must not restate its details. A conflicting restatement is a
framework defect.

| Concept | Sole normative owner |
|---|---|
| Core delivery loop and discrepancy protocol | This spine (WF-CORE) |
| Definition of Done | This spine (WF-DOD) |
| Delivery sequencing gate, its mandatory order, and gate reachability | framework/workflow/WF-PLANNING.md |
| Machine constant of the gate order | tools/delivery_receipt.py (`DELIVERY_CHECK_ORDER`) |
| Delivery validation receipt JSON contract | framework/structure/documentation-catalog.md (section 9.4) |
| Four mandatory perspectives and derived-view rules | framework/workflow/WF-VIEWS.md |
| Language, terminology, and translation contract | framework/workflow/WF-COMMUNICATION.md |
| Permanent work identity | framework/workflow/WF-DOCS.md |
| Git complexity ladder and commit contract | framework/workflow/WF-VCS.md and framework/structure/git-reference.md |
| Tailoring decision states and protocol | PROJECT_STRUCTURE_REFERENCE.md |
| Persistence decision, schema ownership, write semantics, and retention | framework/workflow/WF-PERSISTENCE.md |
| Context of use, model class and layer selection, model risk, artifact freezing, and re-validation | framework/workflow/WF-ML.md |
| Directory and artifact catalogs | framework/structure/ catalog files |
| Roles, authority, and information discipline | AGENTS.md |
| One-time initialization protocol and its state machine | START_HERE.md |
| Machine-readable record of approved paths, commands, authority, and activation | project_profile.yaml (contract: project_profile.example.yaml) |

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
- when delivery groups are active, the delivery sequencing gate owned by
  framework/workflow/WF-PLANNING.md has passed in its mandatory order.

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
   feature plan when an activated planning section requires it. When delivery groups are active,
   preserve the group assignment, group order, dependency, scope-revision, and approval receipt
   that governed the delivered work.

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

Active delivery-group and group-order source:

Exact-scope and approval owner paths:

Delivery-sequence validation command:

Delivery-sequence validator and current receipt paths:

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
