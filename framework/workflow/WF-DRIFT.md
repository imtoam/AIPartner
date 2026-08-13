# WF-DRIFT — Architecture and governance drift control
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-DRIFT` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: drift-check categories and drift-report semantics

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

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
- delivery-group membership completeness, unique group order, dependency/order consistency, and
  approval-to-scope-revision binding.
- code dependency direction and public interface boundaries.
- code, schema, job manifest, current-state, and human-view consistency.
- stale paths, commands, modules, branch markers, and retired operating instructions in live docs.
- generated-view freshness and source completeness.
- agreed-scope coverage: implemented behaviour covers the full set of items in the approved feature
  brief, and any unimplemented item is explicitly marked rather than silently dropped.
- work-ID tree integrity: every ID resolves to exactly one parent and one detailed owner; no ID is
  defined in two lineages, orphaned, or duplicated.
- parallel-implementation lifecycle: every capability implemented by more than one coexisting module
  or algorithm has a recorded reason, one authoritative producer at a time with challengers
  explicitly marked, a pre-agreed comparison metric, a distinct version identity per implementation,
  and a dated retirement trigger with an owner; no parallel state outlives its trigger.
- waiver integrity: every active waiver names a rule, an approver, and an unexpired expiry or review
  trigger; expired waivers are surfaced, not silently honoured.
- deprecated or ambiguous terminology.

The project records the commands in Project facts and adds regression cases for drift that has
already occurred. A drift report is evidence or a work input, not a second current-state source.
