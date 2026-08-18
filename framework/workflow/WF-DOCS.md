# WF-DOCS — Documentation and work tracking
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-DOCS` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Core module: always active in every project.
- Sole normative owner of: the document map, authoritative-vs-derived layers, permanent work identity, current work list, decisions and history rules

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

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
structure decisions, unresolved decisions, and the machine-readable record of approved paths,
commands, and authority. AGENTS.md Team facts and the PROJECT_WORKFLOW.md Project facts section are
its human-readable mirrors; when a mirror and the profile disagree, report the discrepancy instead
of silently choosing one. The profile does not own current work status, current system behavior,
roadmap status, or completed-work history.

### Authoritative documents and derived views

Maintained Markdown is the authoritative layer for project intent, current architecture, plans,
decisions, work tracking, terminology, and history. Executable code, configuration, schemas, and
authoritative business data retain their own explicit ownership; do not copy them into Markdown and
pretend the copy is executable truth.

HTML, dashboards, diagrams, and HTTP responses are derived views. They may combine maintained
documents with declared runtime evidence, but they may not own approvals, work status, architecture
facts, business truth, or open decisions. A human correction enters the owning source through the
normal workflow and is then regenerated into the view.

Raw feature and scope discussion material is a third kind: durable work input, neither authoritative
nor a derived view. It is kept and linked to its work ID as provenance and a memo, but it never owns
scope, approval, or current state; a conclusion in it becomes binding only when promoted into the
owning source. Its artifact contract is section 9.14 of the documentation catalog.

**Reconcile a memo before persisting it.** Before writing a discussion memo or source document, check
it against the existing feature plans, roadmap, current work list, and current-state:

- A part that is already planned or already implemented is not re-entered. Point to the existing
  owner; where the discussion would change it, notify the Product Owner and adjust that owner, not a
  parallel memo.
- Only a part that no existing document already owns is written as new source material or new work,
  under its correct parent work ID.

This stops a new memo from re-introducing features or plans that already exist and driving the
document set into conflicting, multi-headed control.

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
- Identity is a single-rooted tree. Top-level feature IDs are owned by the product brief and roadmap
  — the project's charter and master outline — and are refined downward as understanding deepens; a
  refinement adds child IDs under an existing parent, it never mints a second top-level ID for the
  same outcome.
- Every non-root ID has exactly one parent, and the tree may be several levels deep (a child may
  itself have children). The same feature is never represented by two IDs in different branches, and
  an ID is never re-parented to fabricate a new grouping.
- Because each ID has one parent and one detailed owner, every other place that needs it — a workflow
  step, a phase plan, another feature, or a view — points to that single node. Independent governance
  of the same ID in several places (multi-headed control) is the drift this rule prevents.

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

### Rule waivers

A rule that is in scope may be waived for a bounded case without editing it for everyone. Three
levers are distinct and must not be confused:

- Tailor: decide a rule or module is out of scope (PROJECT_STRUCTURE_REFERENCE.md decision states).
- Waive: keep the rule in scope but grant an approved, recorded exception — cancel it, or replace it
  with an alternative constraint — for a specific work ID or module.
- Framework change: edit the rule text itself for the whole project, as a separately approved change.

A waiver is a decision and follows every rule above. It cites the waived rule by its owning module ID
and rule name, names the Product Owner as approver, states the rationale and residual risk, and
carries an expiry date or review trigger; a waiver without one is invalid. A waiver may not weaken
human authority, information honesty, or a required safety boundary — the floor tailoring may not
cross. Active and expired waivers are surfaced by the project's drift checks so no exception stays
silent. The register artifact is section 9.15 of the documentation catalog.
