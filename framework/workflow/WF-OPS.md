# WF-OPS — Unattended operation
<!-- AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-OPS` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: scheduled/unattended operation rules, locks, health, and human takeover

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-OPS: Unattended operation

Activation condition:

- the current or next approved increment runs on a schedule or without a person present

Ignore the rest of this section until its checkbox is checked.

- Record the real runtime, schedule, and job owner.
- Consider whether files may be read while being edited.
- Use atomic replacement for shared runtime configuration when needed.
- Make repeated execution safe.
- Define locks, timeouts, retries, health checks, and human takeover conditions.
- Record failure evidence instead of silently treating failure as no data.
- Before runtime-sensitive edits in a production worktree, inspect related schedules and running
  processes and avoid leaving entry points in a readable intermediate state.
- A local HTTP project portal binds to loopback and stays read-only unless separately approved;
  non-loopback exposure and write-back require explicit security and authority controls.
