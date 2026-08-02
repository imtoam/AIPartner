# WF-HIGH-IMPACT — High-impact changes
<!-- AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-HIGH-IMPACT` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Optional module: active only when its checkbox is checked in the spine; its activation condition is stated below.
- Sole normative owner of: high-impact boundaries, human approval for risk-increasing actions, and independent verification

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-HIGH-IMPACT: High-impact changes

Activation condition:

- system output can materially affect money, health, safety, legal rights, privacy, or security
- a change affects concurrency, critical data contracts, or another difficult-to-detect failure mode

Ignore the rest of this section until its checkbox is checked.

- Define the boundary between analysis and real-world action.
- Require explicit human approval for risk-increasing actions.
- Use independent calculation or review for critical logic and contracts.
- Record assumptions, uncertainty, and known limitations.
- Provide safe failure, rollback, and disable behavior.
- Do not allow learned or generated output to gain authority silently.
- Identify professional, legal, regulatory, or security review when applicable.
