# WF-STRUCTURE — Repository structure
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-STRUCTURE` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Core module: always active in every project.
- Sole normative owner of: repository organization rules, module identity/ownership, and current-vs-planned state separation

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-STRUCTURE: Repository structure

Organize the repository by responsibility so that a human or future AI can locate truth, source,
tests, tools, and runtime evidence without reconstructing the whole project from history.

PROJECT_STRUCTURE_REFERENCE.md and its `framework/structure/` catalog files own the complete
directory and artifact catalog. Initialization
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
