# ROLE-DELEGATION — Decision delegation modes
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework role module. Module ID: `ROLE-DELEGATION` (stable).

- Charter, activation checkbox, and role routing: [AGENTS.md](../../AGENTS.md)
- Optional module: active only when its checkbox is checked in the charter; its activation condition is stated below.
- Sole normative owner of: the two delegation modes, the mode-selection interview, the delegation charter contract, the delegable/non-delegable boundary, the traceability rule, the plain-language reporting requirement imposed on the control surface while this module is active, the restatement ritual, and the mode-revisit triggers.

Framework invariant: this module file is retained framework content. Tailoring changes only its activation checkbox in the charter; it never edits, renames, or deletes this file.

Activation condition:

- the Product Owner chooses guided delegation during initialization, or later asks to switch to it

When this module is inactive, the project behaves exactly as it does without it. Nothing in any other framework file changes meaning because this module exists.

---

## 1. Problem this module solves

Asking someone "should WF-DATA be active?" is not a real question if they do not know what authoritative data is. They will answer "you decide" — which produces **approval without understanding**: worse than not asking, because it manufactures a record of consent that never happened.

This module supplies a second way to run initialization and delivery, in which the Product Owner approves **outcomes and boundaries in their own words** while the framework selects the controls that implement them. It does not move authority to the AI. It moves the *vocabulary* of approval.

## 2. What this module does not change

Even when active, this module cannot:

- weaken any of the ten baseline principles in START_HERE.md §1;
- move final authority from the Product Owner to any agent;
- reduce what is recorded — the profile, decision states, evidence, and triggers are **identical in both modes**, because only the interview differs, not the record;
- skip an approval on the non-delegable list in §6;
- turn a control off without explicit approval (§6, safety asymmetry).

A future reader, a validator, or a different agent cannot tell from the recorded project state which mode was used, except by reading the mode field itself. That is the design goal: mode is a conversation style, not a governance fork.

## 3. The two modes

| | Guided delegation | Expert selection |
|---|---|---|
| Product Owner approves | Outcomes, boundaries, delivery conditions, accepted risk — in plain language | The same, plus the module and structure selections themselves |
| The framework decides | Which modules and structures implement those approvals | Nothing that was not delegated explicitly |
| Interview style | Plain-language questions about the project; no framework vocabulary required | The menu of options with trade-offs, using framework terminology |
| Reporting | Plain-language contract of §9 is mandatory | Standard WF-VIEWS contract |
| Recorded state | Identical | Identical |

Expert selection is the framework's original behaviour and requires no module. Guided delegation is this module.

## 4. Choosing the mode at initialization

The mode question is asked **before** any other initialization question, because it determines how every later question is phrased.

### 4.1 The question the Product Owner sees

> There are two ways I can set this up.
>
> **A — I ask you about the project in ordinary language, decide the technical setup myself, and tell you what I chose and why.** You stay in charge of what we build, what it must not do, what counts as finished, and what risks are acceptable.
>
> **B — I show you the options and trade-offs, and you choose the setup.**
>
> If this is your first project like this, A is usually the better start. You can switch at any time, in either direction (§5).

The words "guided", "expert", "mode", and module IDs do not appear in this question. They are internal names for the record.

### 4.2 Calibration — inferring, not examining

The AI forms a recommendation before asking, from two signals.

**Signal 1 — the Product Owner's own description (primary).** How they described the idea: whether technical vocabulary appears unprompted, whether they raise repositories, tests, deployment, data storage, or environments on their own, and whether they use those words precisely rather than decoratively.

**Signal 2 — one preference question, never a quiz.** Ask exactly one calibration question, phrased as a service offer:

> Setting this up touches a few things like version control, testing, deployment, and handling real data. Which of those would you like me to explain as we go — any, all, or none?

This is not scored and must never be presented, logged, or described as a test of the person's knowledge. It is genuinely useful either way: the answer tells the AI what to explain for the rest of the project.

**Reading the signals:**

| Observation | Recommendation |
|---|---|
| Precise unprompted technical vocabulary **and** "none" | Expert selection |
| Some technical vocabulary, asks for one or two explanations | Guided delegation; say that switching later is easy |
| Little or no technical vocabulary, or asks for most/all explained | Guided delegation |
| Signals conflict, or the description is too short to judge | Guided delegation |

**Guided delegation is the default whenever the signals are unclear**, because it carries more controls, not fewer (§6), and because a Product Owner who did not need it loses only some explanatory text, whereas one who needed it and did not get it loses the ability to approve meaningfully.

### 4.3 Rules that protect the person

- **The recommendation is stated with its reason, and the Product Owner overrides it with one word.** Calibration never selects the mode by itself.
- **Record the mode, never a judgement about the person.** The profile records `guided` or `expert` with evidence "chosen at initialization on <date>"; it must not record that someone is a beginner, inexperienced, or non-technical. Such a label would be both discourteous and quickly wrong — people learn, and a stale label outlives its truth.
- **Never imply that guided delegation is the lesser option.** It is the appropriate choice for anyone who would rather spend attention on the product than on framework configuration, including experienced people.
- **Do not re-run calibration in later sessions.** The recorded mode stands until the Product Owner changes it or a §11 trigger requires a re-offer.

## 5. Switching modes at any time

The Product Owner may switch modes at any point, in either direction, simply by saying so. No justification, approval, or ceremony is required: the mode describes how the framework speaks to them, and they are the authority on that.

### 5.1 A switch never invalidates existing agreements

Work already approved under the previous mode stays approved. A switch governs decisions made **after** it. Switching must never be used, or interpreted, as a way to reopen settled scope or to retract an approval already given.

Work in progress continues under the approval it started with. Only the next undecided question is governed by the new mode.

### 5.2 Every switch begins with a review

**A mode switch is a checkpoint, not merely a setting change.** Before the new mode takes effect, review the project as it now stands. The review is proportionate to what exists: a two-day-old project with three decisions produces a three-line review.

Cover:

- **Active modules and their evidence** — is each still justified by current conditions, or was it activated for a condition that has since passed?
- **Structure decisions and their states** — anything created that no longer has a consumer; anything deferred whose trigger has since fired.
- **Charter versus reality** — do the recorded scope, boundaries, delivery conditions and accepted risk still describe what this project actually is? Guided → Expert takes the existing charter as the baseline; Expert → Guided drafts it here (§5.4).
- **Open items** — undispositioned review findings, unresolved decisions, work approved but not yet delivered.
- **Traceability** — any decision that cannot name the approval or charter statement it derives from.
- **Risk fit** — whether the controls chosen earlier still match what the project now touches.

The Product Owner confirms, revokes, or amends each item. **An untraceable decision must be resolved at the switch, not carried across it** — either explicitly adopted with approval, or reverted. A mode boundary must never become the place where an accountability gap is hidden from the next phase.

Record the review together with the switch (§5.6).

### 5.3 Guided → Expert

- **Keep the delegation charter.** It remains project history and the record of what was approved and when. It is not deleted, and its earlier revisions stay readable.
- The §5.2 review is where the Product Owner sees what was chosen on their behalf and why. Handing someone the controls without showing the current position sets them up for an uninformed choice.
- The §9 reporting contract lapses for newly generated statements. Existing generated content is not rewritten to be denser.
- The four-condition test stops governing, because the Product Owner is now making the selections directly.

### 5.4 Expert → Guided

- **A charter must now exist.** Draft it from the existing approved record — product brief, decisions, current work, approval evidence — and present it in the Product Owner's own words for confirmation. **Do not invent**: anything not found in the record is asked, never assumed.
- Existing activations stand as they are; they were the Product Owner's own selections. The four-condition test and the traceability rule apply from this point forward.
- The §9 reporting contract takes effect at the next control-surface regeneration.

### 5.5 Guided delegation never restricts the Product Owner

In guided mode the Product Owner may still decide any individual matter personally — "I want to pick the database myself" — at any moment. That is authority being exercised, not a mode change, and it requires no switch and no record beyond the decision itself.

Guided delegation is a default for the decisions the Product Owner does not wish to make. It is never a restriction on the ones they do.

### 5.6 Record each switch

Record the date, the direction, the §5.2 review outcome (confirmed / revoked / amended items), and the Product Owner's stated reason when one is given. **Do not record an inferred reason.** A project that switches back and forth is saying something useful about how well the interview style fits; treat that as signal, not as a problem to suppress.

### 5.7 One mode at a time

Splitting by area — guided for infrastructure, expert for the domain — is not supported, because it makes the governing rule for any single decision ambiguous. §5.5 already covers the real need behind such a request.

## 6. What may be delegated

### 6.1 The four-condition test

A decision may be made on the Product Owner's behalf **only if all four hold**:

1. it is reversible, or has a recorded rollback path;
2. it does not change the scope, boundaries, delivery conditions, or accepted risk the Product Owner stated;
3. it creates no external commitment and no irreversible effect;
4. its consequence is confined to *how* the work is done — not *what* is built, and not *whether* it is built.

Fail any condition and the decision leaves the delegated set. There is no partial delegation of a decision: it is either inside all four conditions or it is escalated.

### 6.2 Delegated (all of it is "how")

Framework module activation · directory and file structure selection from the catalog · technology choices within already-approved constraints · risk-proportionate test-layer selection · work decomposition, ordering, and dependencies · naming and code organisation · refactors that do not change a contract · documentation authoring · commit granularity within the approved version-control mode · which document owns which fact.

### 6.3 Never delegated, in either mode

The Product Owner's four responsibilities — **scope** (what is built, what is not, what is deferred), **boundaries** (what the system may and may not touch), **delivery conditions** (what counts as done and acceptable), and **accepted risk**.

Plus, regardless of mode: irreversible actions · external commitments · anything that spends money · publication or public exposure · production or other people's data · credentials and secrets · licensing and legal terms · any action on the START_HERE.md §6 explicit-approval list.

### 6.4 Safety asymmetry

**Turning a control on may be delegated. Turning a control off may not.**

When guided delegation is active and the evidence for a control is ambiguous, activate it and say so in one plain sentence. The cost of an unnecessary control is ceremony; the cost of a missing one is an unguarded risk. Deactivating a control, narrowing a safeguard, or widening a permission always requires explicit approval.

## 7. Traceability — the anti-drift rule

> **Every delegated decision must name the Product Owner statement it derives from. A decision that cannot name one is not delegated work; it is invention, and it must be escalated instead.**

Each delegated decision records three things: what was decided, which charter statement it derives from, and what would invalidate it.

This makes drift mechanically checkable rather than a matter of judgement: **drift is the existence of a decision with no traceable source**. A drift check does not need to evaluate whether a decision was wise — only whether it has a parent.

When the AI finds that carrying out delegated work would require something the charter does not cover, it stops and asks. The answer amends the charter and creates a new charter revision; work resumes against the new revision. Silently widening one's own mandate is the failure this rule exists to prevent.

## 8. The delegation charter

Default path: `docs/delegation_charter.md`. Created when this module is activated; it is project truth, not framework content.

Minimum content, written in **the Product Owner's own words** and only lightly edited for clarity:

- **Scope** — what this project is for; what it will do; what it will explicitly not do; what is postponed.
- **Boundaries** — what the system may touch and what it must never touch.
- **Delivery conditions** — what "finished" means for the next increment; what would make a result unacceptable.
- **Accepted risk** — what may go wrong that the Product Owner is willing to live with; what would not be acceptable.
- **Revision** — a stable revision identifier, the date, and what changed since the previous revision.

Rules: the charter is versioned and append-only in spirit — a change creates a new revision rather than editing history. Delegated decisions cite the revision they were made under. When the charter changes materially, decisions traced to the superseded revision are re-checked, not silently inherited.

If the AI cannot restate the charter in the Product Owner's own words, the charter is not yet usable and initialization does not proceed.

## 9. Reporting contract imposed on the control surface

While this module is active, the required control surface must additionally satisfy the following. This adds to WF-VIEWS; it does not modify it.

- **Every status statement is a complete sentence** that a reader without software background can act on.
- **State the consequence, not only the state.** "What does this mean for me, and do I need to do anything?" must be answerable from the sentence itself.
- **Technical identifiers are secondary.** Work IDs, group IDs, hashes, and module names belong in an expandable detail layer, never as the primary content of a status line.
- **When action is needed, name who and what.**
- **Absence of evidence is stated plainly** — "this hasn't happened yet" — and never rendered as healthy.
- **Use the Product Owner's vocabulary.** If they called it a practice reminder, the report says practice reminder, not notification subsystem.

Illustrations:

| Instead of | Write |
|---|---|
| `WF-DATA: active. Evidence: production data boundary crossed.` | "Your app now stores real people's information, so I turned on the rules that keep tests away from it. You approved this on 2 August." |
| `DG-003 · order 3 · deps [DG-001, DG-002] · pass · sha256:a3f…` | "Three pieces of work are queued. The first two are done; the third is waiting because it needs a database change from the first. Everything checked out an hour ago." |
| `verification: not_run` | "Nothing has been tested yet — I'll do that before anything goes live." |

**The vocabulary rule doubles as a drift detector.** When the AI can no longer describe the current work in the Product Owner's own words, the work has usually already drifted. Vocabulary drift precedes scope drift and is cheaper to notice.

## 10. Restatement and revocation

At the close of each feature, and whenever a §11 trigger fires, the AI presents a plain-language list: **"Since we last spoke, here is what I decided on your behalf, and why."** Each item names the charter statement it derives from.

The Product Owner may revoke any item on the spot. A revoked decision is reversed or, where reversal is impractical, recorded as an accepted deviation with its reason. Restatement is not optional and is not satisfied by a link to the technical record.

## 11. Mode-revisit triggers

Re-offer the mode choice — not merely the structure review — when any of these first becomes true:

- production data, other people's personal information, money, or credentials enter the project;
- the project starts running unattended, or becomes reachable from a network;
- a second writer or an independent reviewer joins;
- the Product Owner begins asking about the module and structure selections themselves, which is the usual sign that expert selection now fits better;
- the Product Owner reports that a report or decision surprised them — a signal that the delegation boundary is not where they thought it was.

A trigger opens a conversation. It never switches the mode by itself.

## 12. Additions to the Definition of Done while active

Applied on top of the standard Definition of Done:

1. Every delegated decision in this change names its charter statement.
2. The control surface statements added or changed by this work satisfy §9.
3. Anything encountered that falls under §6.3 was escalated rather than decided.
4. If the charter changed, the new revision is recorded and decisions under the superseded revision were re-checked.

## Non-goals

- This module does not create an autonomous agent, and does not permit one.
- It does not reduce evidence, records, or validation relative to expert selection.
- It does not grade, label, or profile the Product Owner.
- It does not replace the structure tailoring protocol; it changes who applies it and in what vocabulary.
