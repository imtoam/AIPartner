# WF-VIEWS — Human-readable project views
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-VIEWS` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Core module: always active in every project.
- Sole normative owner of: the four mandatory perspectives, derived-view markers, fail-closed generation, and view-split/HTTP triggers

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-VIEWS: Human-readable project views

Every initialized project provides a static `project-overview.html` as its mandatory human control
surface. `index.html` remains the permanent framework guide. Do not replace either role with the
other.

The human role is not to act as an assistant who reconstructs the project by reading raw logs,
development notes, databases, configuration, or source files. The interface must let people govern
direction, architecture, scope, progress, cadence, risk, health, and decisions while retaining
clickable access to the underlying evidence.

### Four mandatory perspectives

The control surface contains four stable perspectives from initialization onward:

| Perspective | Primary audience | Required content |
|---|---|---|
| Management | Product Owner, management, and project leadership | Direction, intended value, scope, progress, cadence, material risks, open decisions, and management advice |
| Business | Domain specialists and daily business operators | Business recommendations, domain logic, data health, decision status, exceptions, and actions needing specialist judgment |
| Operations | IT operators and reliability owners | Services, jobs, providers, storage, backups, incidents, recovery, capacity, and current health |
| Architecture and delivery | Developers, architects, and delivery owners | Current and approved target architecture, module boundaries, dependencies, phase and feature plans, implementation status, technical risk, and drift |

All four perspectives are present even when the project is new. A perspective without current data
must show `not_yet_available`, `not_applicable`, `blocked`, or `degraded` with its reason, source
owner, and activation or recovery trigger. It must not disappear, invent healthy status, or force
the user to inspect raw evidence to learn that the capability does not exist.

Management advice and business recommendations remain proposals unless their owning source records
an approval or decision. Business health is not inferred from system uptime, and operational health
is not inferred from business outcomes. Architecture views distinguish current observed structure
from approved target plans.

Every generated view displays or embeds:

- a stable page role and view ID.
- authoritative source paths.
- generation time and source version or commit when available.
- freshness, stale, incomplete, or generation-error state.
- visible unresolved decisions relevant to that view.
- a statement that the view is derived and not an independent source of truth.

Generation fails closed. Missing or conflicting sources produce visible error or discrepancy
evidence; an old HTML file must not silently stand in for missing current truth.

The four perspectives may begin as sections in one static page. Split pages activate when their
sources, audiences, or navigation depth justify independent surfaces:

| View | Normal sources | Trigger |
|---|---|---|
| Management | Product brief, roadmap, active work, risks, decisions, verification evidence | Management history or decision volume outgrows the overview section |
| Business | Typed domain read model, business contracts, recommendations, exception queues | Live business health or daily specialist workflow exists |
| Operations | Job manifest, health read model, runbooks, logs and status evidence | A service or unattended job requires live operational handling |
| Architecture and delivery | Current-state map, module owner docs, ADRs, phase and feature plans | Several modules or plans need interactive navigation |

When the control surface splits into a second generated page or live endpoint, create one view
registry, normally `docs/view_registry.md`, that owns view IDs, source lists, generator commands,
locale, freshness rules, and output paths. It does not own the facts being rendered.

Static HTML is the default. A local HTTP service activates only when live refresh, search, filtering,
or structured local-AI access is needed. It binds to loopback and remains read-only by default.
Network exposure, authentication, browser approval, source write-back, or business-data mutation are
separate capabilities requiring explicit authority, threat analysis, audit evidence, and applicable
WF-OPS or WF-HIGH-IMPACT controls. Local AI configuration is a consumer, never the sole store for
open decisions or project truth.
