# Structure catalog — Documentation and planning artifact contracts
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework structure-reference catalog file.

- Spine, selection principles, and tailoring protocol: [PROJECT_STRUCTURE_REFERENCE.md](../../PROJECT_STRUCTURE_REFERENCE.md)
- This catalog is a menu, not project truth. Tailoring selects from it; it never edits this file.
- Sole normative owner of: the docs/ catalog, every planning/tracking artifact contract including the delivery validation receipt, and artifact relationship rules

Original section numbering is preserved so existing references remain valid.

---

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

Before implementation, read the phase plan in the mandatory sequence defined by the delivery
sequencing gate in [framework/workflow/WF-PLANNING.md](../workflow/WF-PLANNING.md). Missing group membership,
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
sessions or milestones, or is governed by WF-DATA, WF-PERSISTENCE, WF-ML, WF-OPS, WF-RECOVERY, or
WF-HIGH-IMPACT.

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

### 9.14 Feature source and discussion material

Default path pattern: docs/feature_sources/WORK-ID_short_name.md

Optional. Preserve the raw discussion, scope conversation, and background reasoning behind a feature
when the formal brief cannot capture all of it. This material is supporting input, not a scope owner.

- Carry a stable reference linked to the permanent work ID and child IDs it supports, so a feature ID
  can be traced back to the conversation it came from and cross-checked.
- Keep it searchable and durable; it is a memo and provenance aid, not a live status source.
- It never owns scope, non-goals, approval, or current state. The feature plan or current-work item
  remains the sole authoritative owner of exact scope; where the two differ, the brief governs.
- A conclusion that must constrain implementation is promoted into the feature brief (WF-CORE step 3
  in PROJECT_WORKFLOW.md); leaving it only in source material does not make it binding.

### 9.15 Rule waiver register

Default path: docs/waivers.md

Records approved exceptions to a framework or project rule that remains in scope. A waiver cancels or
replaces one rule for a bounded case; it does not retire the rule (that is tailoring) or edit it for
everyone (that is a framework change).

Each waiver records:

- the waived rule, cited by its owning module ID and rule name, and the work IDs or module it covers.
- whether the rule is cancelled or replaced, and the alternative constraint when replaced.
- the rationale and the residual risk accepted.
- the approver — the Product Owner — and the grant date.
- an expiry date or a review trigger; a waiver without one is invalid.
- status: active, expired, or withdrawn.

A waiver may not weaken human authority, information honesty, or a required safety boundary — the same
floor tailoring may not cross. The project's drift checks surface every active and expired waiver so
no exception is silent.

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
- Feature source material owns nothing normative; it is work input linked to a work ID, and the
  feature plan still owns exact scope.
- The waiver register owns recorded rule exceptions only; each waived rule keeps its own owner.

When two files answer the same question, choose one owner and replace the other detail with a
pointer.
