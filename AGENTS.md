# AGENTS.md

Project working agreement

This file defines roles, change control, documentation responsibilities, and the Definition of
Done. Project-specific facts belong in the final section.

## Sections in use

Checked sections apply. Unchecked sections are ignored except for their activation condition.

- [x] Core roles and working rules
- [x] Documentation and work tracking
- [x] Definition of Done
- [ ] Independent peer review
- [x] Multi-level planning
- [ ] Multiple writers and worktrees
- [ ] Production data and scheduled operation
- [ ] High-impact changes

During initialization, the AI recommends which optional sections are needed. The Product Owner
approves the selection.

After initialization, if an activation condition becomes true, the AI explains why the section is
needed and asks the Product Owner before checking it. The normal project history records the
change. No separate activation system is required.

## Core roles and working rules

### Roles

Product Owner: the user

Implementer: the primary AI working in this project

Reviewer: not assigned unless Independent peer review is checked

The Product Owner decides:

- product purpose and success criteria
- priority and scope
- acceptance of material risk
- AI roles and permissions
- production release
- irreversible actions

The Implementer is the only writer until Multiple writers and worktrees is checked.

### Working rules

- Follow the user's instruction within its stated scope.
- Ask when a missing decision would materially change the result.
- Do not expand scope merely because another improvement is available.
- Preserve user work and unrelated changes.
- Read relevant project facts before changing files.
- Make reasonable, reversible assumptions when they do not change the agreed objective.
- State important assumptions and unresolved questions.
- Do not claim completion while required work remains.

A clear user request authorizes ordinary, safe implementation work. Do not request approval for
every technical detail.

Stop and ask for a decision when work requires a new external commitment, a destructive action, a
material scope change, acceptance of a new risk, or a change in authority.

### Information discipline

Keep these categories separate:

| Category | Meaning |
|---|---|
| User statement | The user explicitly said it |
| Observed fact | Read-only evidence supports it |
| AI inference | AI inferred it and needs confirmation |
| AI proposal | AI recommends it and needs approval |
| Unresolved | It is unknown, conflicting, or deferred |

An inference is not a project fact until the user confirms it.

## Documentation and work tracking

### Document map

Initialization fills the actual paths. Create only documents that have a clear responsibility.

| Question | Owner |
|---|---|
| Why does the project exist? | Product brief |
| What is true now? | Current-state document and executable system |
| What work is active? | Current work list |
| What is planned later? | Roadmap, when Multi-level planning is checked |
| Why was a decision made? | Decision record |
| What already happened? | History and version control |
| What did the latest review find? | Review report, when Independent peer review is checked |

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

1. Structure

   Changed files pass the project's syntax, type, schema, or structural checks.

2. Function

   A test or direct check demonstrates that the intended behavior works. A syntax check alone is
   not enough.

3. Regression

   Relevant regression checks pass. Add a regression case when the change fixes a defect that
   could return.

4. Current state

   Update the current-state document when the change adds or alters a module, interface, data
   contract, schema, schedule, failure mode, or operating behavior.

5. Tracking

   Remove completed work from the active list. Record the outcome in history. Update the roadmap or
   feature plan when an activated planning section requires it.

6. Documentation checks

   Run the project's documentation and reference checks.

7. Version control

   Commit only intended source, configuration, tests, and maintained documentation. Keep runtime
   output, caches, logs, and unrelated user changes out of the commit.

8. Risk

   Apply any additional evidence required by Production data and scheduled operation or High-impact
   changes when those sections are checked.

The project-specific commands used for these checks belong in Environment facts.

## Independent peer review

Activation condition:

- a second AI or human is asked to perform independent review

Ignore the rest of this section until its checkbox is checked.

### Role separation

The Reviewer examines code and documents independently. The Implementer verifies findings, makes
changes, tests, updates documents, and commits.

Unless the Product Owner approves a different arrangement:

- the Reviewer does not edit application files
- the Reviewer does not run commands that write production data
- the Reviewer does not modify version control
- the Reviewer writes only the agreed review report

### Review report

Default path: docs/review.md

The report represents the latest complete review and replaces the previous contents. History and
version control preserve accepted findings and past reports.

The report begins with:

- review date
- reviewed commit or version
- review scope

Each finding includes:

- severity
- file and line reference
- why it is a problem
- suggested correction
- uncertainty when the conclusion is not fully established

Separate confirmed defects from methodology suggestions.

When the user asks the Implementer to read or address the review, the Implementer must reread the
current review file. Do not rely on memory from an earlier version.

The Implementer verifies every finding before changing code. An accepted finding receives a stable
work reference outside the temporary review report.

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

## Multiple writers and worktrees

Activation condition:

- more than one human or AI writer works at the same time

Ignore the rest of this section until its checkbox is checked.

- Define one integration owner.
- Give each writer a branch, worktree, or explicit file boundary.
- Do not allow simultaneous edits to shared control files.
- Inspect repository status before and after integration.
- Keep branches short-lived when practical.
- Use merge for shared integration branches unless the Product Owner approves another policy.
- Resolve cross-feature conflicts at one integration point before redistributing the result.
- Do not overwrite or carry unrelated changes from another worktree.

Project-specific branch names and worktree paths belong in Environment facts.

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

## Environment facts

Initialization fills this section. Keep it factual and current.

Project name:

Primary runtime:

Supported operating systems:

Syntax and structural check commands:

Functional test commands:

Regression commands:

Documentation check commands:

Current-state document:

Current work list:

Roadmap:

Decision records:

History:

Review report:

Production data locations:

Scheduled jobs:

Default branch:

Integration branch:

Worktree locations:

Generated or runtime-only paths:

Known environment constraints:
