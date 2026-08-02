# WF-DATA — Authoritative and non-cleanable data
<!-- AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-DATA` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: authoritative-data discipline for tests, diagnostics, migrations, and shadow capture

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-DATA: Authoritative and non-cleanable data

Activation condition:

- the current or next approved increment creates, reads, changes, or depends on production,
  append-only, sensitive, authoritative, or otherwise non-cleanable data

Ignore the rest of this section until its checkbox is checked.

- Tests use temporary databases, fixtures, or synthetic data.
- Read-only diagnostics use read-only connections.
- Tests and review commands do not write production data.
- Authoritative data, derived views, caches, and projections have explicit ownership.
- Schema changes have a migration and recovery plan.
- Append-only or irreversible rules are enforced where practical.
- Prospective, forward-only, retrospective, synthetic, and migrated evidence remain explicitly
  distinguishable.
- A blocked full feature may use an approved isolated shadow capture only when it cannot alter
  canonical truth, backfill an old ledger, or interfere with production scheduling.
