# WF-RECOVERY — Backup and recovery
<!-- AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-RECOVERY` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: backup verification and tested recovery paths

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-RECOVERY: Backup and recovery

Activation condition:

- authoritative state would be costly or impossible to reconstruct
- a migration, release, retention rule, or incident requires a tested recovery path

Ignore the rest of this section until its checkbox is checked.

- Identify authoritative data that requires backup.
- Verify backups rather than relying on file presence.
- Define the recovery path and its acceptance evidence.
- Keep destructive cleanup separate from ordinary processing.
