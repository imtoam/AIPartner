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
