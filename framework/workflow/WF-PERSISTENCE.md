# WF-PERSISTENCE — Where project state lives
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-PERSISTENCE` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: the decision to persist at all, storage mechanism selection, schema ownership and evolution, write semantics, and retention periods

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-PERSISTENCE: Where project state lives

Activation condition:

- the project keeps any state that must survive a restart, beyond source files and generated views
- an existing store changes its shape, its owner, or how long it keeps what it holds

Ignore the rest of this section until its checkbox is checked.

### Boundary with neighbouring modules

This module decides **whether state is kept, where, in what shape, and for how long**. It does not
restate what its neighbours own:

| Question | Owner |
|---|---|
| May a test, diagnostic, or migration touch this data? Is a shadow capture allowed? | framework/workflow/WF-DATA.md |
| Is the backup verified and the recovery path tested? | framework/workflow/WF-RECOVERY.md |
| Which directories may exist for stores, schemas, migrations, and runtime state? | framework/structure/directory-catalog.md |

### Rules

- Before adding or keeping a store, apply the necessity-before-structure discipline in WF-CORE to
  the store itself: justify why it exists as a separate store and whether a near-equivalent store
  should absorb it, rather than adding stores by default.
- Record the persistence decision even when the answer is none. "This project keeps no state" is a
  decision with evidence, not an omission.
- State the access pattern before naming a mechanism: what is written, how often, who reads it,
  which query shapes matter, and how large it may plausibly grow. A mechanism chosen for
  familiarity rather than for the pattern is recorded as such, honestly.
- Every store has one owning module and one schema definition kept in version control. A live store
  file is never the schema; a schema reconstructed by reading production is a finding, not a source.
- Classify every store at creation as authoritative or derived. A derived store records the command
  that rebuilds it from authoritative sources and must be safe to delete. Handling rules for
  authoritative and non-cleanable stores are owned by WF-DATA.
- Schema changes move through ordered migrations, and the schema version is readable from the store
  itself rather than inferred from code.
- Write semantics are explicit for each store: whether a record is overwritten in place or appended
  as a new observation, and whether the state at a past moment remains answerable. Choosing
  overwrite silently destroys history that no later decision can recover.
- Retention is an approved period with a named owner, not a consequence of running out of disk.
  State what deletion requires and who may approve it.
- Documents, exports, and binary artifacts are persistence too. Record where they live, what names
  them, and whether the repository or the store is authoritative when the two disagree.
- Presence in the directory catalog is never evidence that the project needs a store.
- Schemas, fixtures, and migrations carry no credentials — only the variable names and the purpose
  of the values they expect.
