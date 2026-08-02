# Structure catalog — Minimal greenfield starting set

AIPartner framework structure-reference catalog file.

- Spine, selection principles, and tailoring protocol: [PROJECT_STRUCTURE_REFERENCE.md](../../PROJECT_STRUCTURE_REFERENCE.md)
- This catalog is a menu, not project truth. Tailoring selects from it; it never edits this file.
- Sole normative owner of: the day-one starting set and its inclusion rules

Original section numbering is preserved so existing references remain valid.

---

## 11. Minimal greenfield starting set

The reusable framework files may all be present, but they are framework_retained rather than
evidence that every project artifact or governance module is active.

Do not create the full project tree on day one. A typical approved project-controlled starting set
contains:

- local Git and a tailored .gitignore unless version control is explicitly deferred with a reason.
- project_profile.yaml.
- docs/product_brief.md.
- docs/current_work.md with the first permanent work ID.
- project-overview.html generated from approved facts and unresolved decisions, with management,
  business, operations, and architecture/delivery perspectives.
- a compact communication contract in project_profile.yaml, using the recommended language default
  unless the Product Owner approves a different boundary.

Create docs/module_structure.md only when maintained code, executable configuration, schema, or
operating behavior exists. It must describe present reality, never planned architecture.

Create the first application source path and the first required test layer when the first work item
is ready to materialize code. Do not create empty directories for appearance.

The four perspectives are required even before all their source systems exist. An unavailable
perspective contains a real source state and reason, accountable owner, and activation or recovery
trigger; it is not an empty placeholder and does not claim healthy status.

Create config/, dashboard/, db/, logs/, reports/, state/, setup/, roadmap, phase plans, feature
plans, module owner docs, terminology, view registry, additional HTML views, ADRs, review files, and
runbooks only when they have an immediate consumer and meaningful current content.
A planned future responsibility normally receives a deferred trigger. A high-risk first feature is
an exception only for its durable feature brief and required safety controls.

Initialization must show the proposed starting set and explain why every selected item is needed.
Placeholders that merely say "nothing exists yet" do not satisfy the inclusion rule.
