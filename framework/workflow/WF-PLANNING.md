# WF-PLANNING — Multi-level planning
<!-- AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-PLANNING` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: the planning tiers, delivery-group ownership, the mandatory sequencing gate order, and forward-data/gate-reachability checks

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-PLANNING: Multi-level planning

Activation condition:

- the target project currently has at least two phases, releases, or long-running work lines whose
  priority or dependency must be managed separately

Ignore the rest of this section until its checkbox is checked.

A roadmap imagined during initialization is not activation evidence. If only one bounded work item
is ready, keep this module inactive and record a trigger for the point at which competing work
appears.

Use up to four levels, and only when each active level has a distinct purpose:

| Level | Purpose |
|---|---|
| Roadmap | Major outcomes, releases, and future priority |
| Phase delivery plan | Ordered dependencies and early-start boundaries inside one release or long work line |
| Current work list | Work in the current phase or release |
| Feature plan | Detailed breakdown of one large feature |

Rules:

- The Product Owner approves movement between phases or major priorities.
- The current work list contains current unfinished work only.
- Future work belongs in the roadmap, not the current queue.
- A phase delivery plan owns within-phase order and dependencies; the roadmap does not copy them.
- A large feature keeps its detailed status in one feature plan.
- Other files point to the feature plan instead of copying its details.
- Completed work moves to history.

### Delivery-group ownership and sequencing gate

Activate delivery groups when two or more approved or proposed work units must be coordinated as a
delivery sequence. Do not create groups merely to decorate a single bounded item.

Information ownership is fixed:

| Control | Sole detailed owner | Other files may contain |
|---|---|---|
| `delivery_group` membership | Active phase delivery plan | A pointer to the group ID |
| `group_order` | Active phase delivery plan | A rendered summary or pointer |
| Cross-group and cross-feature dependencies | Active phase delivery plan | Internal feature-plan dependencies that do not redefine delivery order |
| Exact feature scope and non-goals | Feature plan; current-work item only when no feature plan is justified | Scope revision and pointer |
| Approval of exact scope | The same feature plan or current-work item that owns exact scope | Approval state, evidence pointer, and approved scope revision |

The phase plan uses stable `DG-NNN` group IDs. Every sequenced work item belongs to exactly one
delivery group. Every active group has one unique positive `group_order`; order values define the
delivery sequence and may have gaps so later insertion does not require renumbering stable groups.
Dependencies use stable group or work IDs, name their reason and type, and must be resolvable and
acyclic. A dependency on a later group means the declared order is invalid; correct `group_order`
before implementation rather than treating the dependency as an informal exception.

Exact scope has a stable revision, such as `WORK-012-scope-v3`. Approval evidence must name that
same revision. Changing scope, non-goals, delivery-group membership, or a material dependency
invalidates readiness; re-evaluate the sequence and obtain new approval when the approved scope
changed. Approval of an earlier scope revision must never authorize a later one implicitly.

An active gate has a project-specific validator and one current machine-readable receipt. The
validator runs the four checks, then atomically writes the receipt described in
[framework/structure/documentation-catalog.md](../structure/documentation-catalog.md) section 9.4. The receipt binds its `pass` result to SHA-256 digests of the phase
plan, validator, and every exact-scope owner. Any bound file change makes the receipt stale. Merely
declaring a command, keeping an old receipt, or setting delivery control to active is not evidence
that the gate passed.

Before beginning any grouped implementation, check in this exact order
(`delivery_group -> group_order -> dependencies -> approval/exact scope`):

1. `delivery_group`: every intended work item has exactly one group; membership and the group
   outcome are coherent.
2. `group_order`: every active group has one unique order and the proposed execution sequence is
   explicit.
3. `dependencies`: all dependency IDs resolve, the graph is acyclic, and no dependency contradicts
   the declared group order. If it does, return to step 2 and correct the order.
4. `approval/exact scope`: the next work item has an exact scope, non-goals, scope revision, approval
   state, and approval evidence bound to that same revision.

This is a gate, not a reporting format. Failure at any step prevents implementation of the affected
item. Completing step 4 does not excuse a failure in steps 1-3, and an approval does not determine
delivery order by itself.

Implementation may begin only when the delivery validator exits successfully and the core project
validator confirms a current `pass` receipt. A missing, malformed, failed, or stale receipt is
blocking. The HTML control surface displays configuration state separately from validation state
and must never render `active` as if it meant `pass`.

### Forward-data timing and gate reachability

When proposing implementation order, dependencies, or early work, check each item for a data clock:

- whether valid evidence can be faithfully reconstructed later.
- whether collection is prospective or only forward from an activation epoch.
- how long labels, roots, outcomes, or other evidence require to mature.
- whether delay permanently loses point-in-time availability, provider latency, market context,
  cost, or concurrent-condition evidence.

Mark work `data-clock critical` when code may be implemented later but its valid observation window
cannot be recovered. Record the latest safe activation point, the smallest isolated shadow or
bounded capture that can begin earlier, and how it avoids canonical write-back and production
interference. Mark retrospective reconstruction separately; it must not masquerade as prospective
or point-in-time calibration evidence.

Before adopting an evidence threshold or exit gate, estimate its reachability from the actual or
expected generation funnel: exclusion reasons, eligible rate, independence, maturity delay, and
time to threshold. A methodologically attractive gate that can never receive enough valid evidence
is an unresolved product or methodology decision, not a completed plan.
