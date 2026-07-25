# PROJECT_WORKFLOW.md

Project delivery and governance method

This file is the canonical project method throughout the project lifecycle. It defines how work
moves from an idea to verified delivery. Roles, authority, permissions, and collaboration
boundaries belong in AGENTS.md. One-time initialization belongs in START_HERE.md. Project-specific
paths and commands belong in the final section of this file.

Do not duplicate this methodology in AGENTS.md or START_HERE.md. Those files may route to it,
configure it, or record approvals without redefining its rules.

Read this file before shaping, planning, implementing, testing, reviewing, releasing, or operating
a project change. A factual answer or a small mechanical edit may not require the complete file.

## Sections in use

Checked sections apply. Unchecked sections are ignored except for their activation condition.

- [x] Core feature delivery
- [x] Repository structure
- [x] Documentation and work tracking
- [x] Definition of Done
- [ ] Multi-level planning
- [ ] Production data and scheduled operation
- [ ] High-impact changes

During initialization, the AI recommends which optional sections are needed. The Product Owner
approves the selection.

After initialization, if an activation condition becomes true, the AI explains why the section is
needed and asks the Product Owner before checking it. Record the change in project history. Do not
activate project governance silently.

## Core feature delivery

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

## Repository structure

Organize the repository by responsibility so that a human or future AI can locate truth, source,
tests, tools, and runtime evidence without reconstructing the whole project from history.

Initialization records the actual names and ownership. Use only categories the project needs.

| Typical path | Responsibility | Normal version-control policy |
|---|---|---|
| app/ or src/ | Maintained application code and internal modules | Include |
| docs/ | Product intent, current state, plans, decisions, runbooks, and history | Include |
| tests/ | Unit, integration, contract, end-to-end, replay, and test fixtures | Include |
| tools/ | Human-invoked validation, inspection, maintenance, and migration utilities | Include |
| dashboard/ or web/ | Human-facing control or observation interface | Include maintained source |
| db/ | Schema, migrations, and safe development fixtures | Include definitions, govern data separately |
| config/ | Non-secret configuration and canonical registries | Include maintained configuration |
| setup/ | Installation, deployment, scheduling, and environment setup | Include |
| logs/ and reports/ | Generated evidence for operation or analysis | Usually exclude |
| state/ and cache/ | Runtime state, checkpoints, projections, and disposable cache | Usually exclude |

Rules:

- Do not create every category by default or keep empty directories for appearance.
- Do not mix production data, generated output, or cache with maintained source.
- Identify authoritative data, derived projections, and disposable output explicitly.
- Keep entry points small and preserve a clear dependency direction between modules.
- Give each important data set, interface, and module one owner.
- Put secrets outside version control and record only how they are supplied.
- Update this map when a new responsibility or runtime category appears.

## Documentation and work tracking

### Document map

Initialization fills the actual paths. Create only documents that have a clear responsibility.

| Question | Owner |
|---|---|
| Why does the project exist? | Product brief |
| What is true now? | Current-state document and executable system |
| What work is active? | Current work list |
| What was agreed for a non-trivial feature? | Feature brief or feature plan |
| What is planned later? | Roadmap, when Multi-level planning is checked |
| Why was a decision made? | Decision record |
| What already happened? | History and version control |
| What did the latest review find? | Review report, when peer review is active in AGENTS.md |

One line of work has one detailed owner. Other documents may point to it but must not copy its
status in full.

Do not treat history as current state. Do not treat a roadmap as the current work list. Generated
HTML is a human view and not a source of truth.

### Current work list

- Keep unfinished work only.
- Give each item a priority and a clear status.
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

## Definition of Done

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

   Apply any additional evidence required by Production data and scheduled operation or High-impact
   changes when those sections are checked.

The project-specific commands used for these checks belong in Project facts.

## Multi-level planning

Activation condition:

- the project has several phases, releases, or long-running features competing for priority

Ignore the rest of this section until its checkbox is checked.

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

## Production data and scheduled operation

Activation condition:

- the project uses production, append-only, sensitive, or otherwise non-cleanable data
- a job runs on a schedule or without a person present

Ignore the rest of this section until its checkbox is checked.

### Data safety

- Tests use temporary databases, fixtures, or synthetic data.
- Read-only diagnostics use read-only connections.
- Tests and review commands do not write production data.
- Authoritative data, derived views, caches, and projections have explicit ownership.
- Schema changes have a migration and recovery plan.
- Append-only or irreversible rules are enforced where practical.

### Scheduled work

- Record the real runtime, schedule, and job owner.
- Consider whether files may be read while being edited.
- Use atomic replacement for shared runtime configuration when needed.
- Make repeated execution safe.
- Define locks, timeouts, retries, health checks, and human takeover conditions.
- Record failure evidence instead of silently treating failure as no data.

### Backup and recovery

- Identify authoritative data that requires backup.
- Verify backups rather than relying on file presence.
- Define the recovery path and its acceptance evidence.
- Keep destructive cleanup separate from ordinary processing.

## High-impact changes

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

Project name:

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
