# Structure catalog — Root files
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework structure-reference catalog file.

- Spine, selection principles, and tailoring protocol: [PROJECT_STRUCTURE_REFERENCE.md](../../PROJECT_STRUCTURE_REFERENCE.md)
- This catalog is a menu, not project truth. Tailoring selects from it; it never edits this file.
- Sole normative owner of: the root-file catalog and their responsibilities

Original section numbering is preserved so existing references remain valid.

---

## 3. Root files

| Path | Responsibility | When needed |
|---|---|---|
| AGENTS.md | Roles, authority, permissions, review, and concurrent-writer rules | Always |
| START_HERE.md | One-time greenfield initialization protocol | Template and uninitialized project |
| PROJECT_WORKFLOW.md | Canonical delivery and governance method | Always |
| PROJECT_STRUCTURE_REFERENCE.md | Directory and control-artifact reference | Template; retained for future growth |
| project_profile.yaml | Approved initialization state, active modules, unresolved decisions, and actual paths | After initialization begins |
| project_profile.example.yaml | Exact machine-readable profile contract | Retained framework reference |
| index.html | Permanent human starting guide | Always; never overwrite during initialization |
| project-overview.html | Mandatory four-perspective human control surface generated from project truth | After initialization materializes approved facts |
| README.md | Short repository orientation and entry links | Normally |
| LICENSE | Reuse and distribution terms | Public or shared repository |
| framework_manifest.json | Integrity contract for retained rules and managed configuration boundaries | Always |
| .gitignore | Exclusion policy for secrets, generated output, runtime state, and local tools | Version-controlled repository |
| tools/validate_initialization.py | Deterministic framework and initialization validator | Retained framework tool |
| tools/delivery_receipt.py | Shared evaluator for current, failed, invalid, and stale delivery receipts | Retained framework tool |
| tools/render_project_overview.py | Atomic default renderer from declared project sources to the derived overview | Retained framework tool |
| tools/render_framework_scope.py | Atomic renderer of the framework scope map from the module activation blocks and module files | Retained framework tool |

`project-overview.html` is the only generated project page in the minimal starting set. It contains
management, business, system-operations, and architecture/delivery perspectives from day one.
Additional pages normally live under `project_views/` and activate through one view registry when
a perspective's sources, audience, live behavior, or navigation depth justify a separate surface.
