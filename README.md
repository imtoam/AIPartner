# AIPartner
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

**A governance framework for building software with AI agents — where the rules are machine-checked
instead of merely written down.**

AGENTS.md tells an agent how to behave. It does not tell you whether the agent actually did. This
framework supplies the structure behind that file: one owner per rule, an approval boundary the
agent cannot cross on its own, and a validator that fails when the documents and the project
disagree. Your agent cannot report `pass`. The validator decides, and its receipt is bound to
content hashes, so an edited source invalidates the receipt automatically.

Protocol version: 0.11.0 · Licence: CC BY-SA 4.0 · Guide: <https://imtoam.github.io/AIPartner/>

## Try it

1. Copy this framework into an empty repository intended for a new project.
2. Open that repository with an AI tool that can read files and, after your approval, write them.
3. Send one instruction:

```text
Read START_HERE.md in full and follow its greenfield initialization protocol.
Guide me through the initialization in my preferred language.
Do not create project files until I approve the initialization proposal.
My idea is:
```

Then describe your idea, however unfinished. The AI interviews you, proposes a starting structure,
and waits. Silence is not approval. After you approve, it creates only what was agreed, runs the
validator, and reports what it could not verify.

## What makes it different

**Governance an agent cannot quietly skip.** A hash manifest covers every framework file, a
standard-library validator checks the project contract, and derived HTML pages are regenerated and
compared byte for byte against their Markdown sources. Drift is an error, not a discovery made
months later.

**A menu, not a mandate.** Every rule belongs to one module. A baseline set applies to every
project; the rest stay dormant until a stated condition becomes true — production data appears, work
runs unattended, parameters are learned from data, a second writer joins. Nothing activates
silently, and an artifact created by activating a module is never treated as evidence that the
module was needed. See the
[framework scope map](https://imtoam.github.io/AIPartner/introduction/framework-scope.html), which
is generated from the modules themselves.

**Human authority is structural, not advisory.** Purpose, scope, risk acceptance, release, and every
irreversible action stay with the Product Owner. The AI must keep user statement, observed fact, its
own inference, and its own proposal in separate classes; an inference never becomes a project fact
without confirmation.

**Evidence beats assertion.** Completion requires recorded verification output, not a claim of
success. When several work units compete, the delivery sequencing gate owned by
[framework/workflow/WF-PLANNING.md](framework/workflow/WF-PLANNING.md) must pass — in its mandatory
order, with a current validated receipt — before implementation begins.

## Current limits

- Greenfield projects only. Adoption into an existing repository is not supported yet.
- The AI performs the protocol; there is no separate service to install.
- Passwords, API keys, and credentials must never enter project documents.
- Generated HTML is a human view, never an independent source of project truth.
- This is an early working framework, published for testing and criticism.

## Entry points

| Who | Opens | Purpose |
|---|---|---|
| Human | [index.html](index.html) | What to expect, what stays under your authority, how to begin. Remains the human entrance after initialization. |
| AI, before initialization | [START_HERE.md](START_HERE.md) | The one-time greenfield initialization protocol. |
| AI, after initialization | [AGENTS.md](AGENTS.md), `project_profile.yaml`, [PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) | Roles, authority, and the delivery method, plus the module files they route to. Do not repeat the initial interview. |

## Layout

[PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) and
[PROJECT_STRUCTURE_REFERENCE.md](PROJECT_STRUCTURE_REFERENCE.md) are spines. Topic modules live one
per file under `framework/workflow/` and `framework/roles/`; structure catalogs live under
`framework/structure/`. Each concept has exactly one normative owner, listed in the spine's concept
ownership registry — a conflicting restatement anywhere else is a defect.

Maintained Markdown is the authoritative document layer. Human-facing HTML and any local HTTP portal
are derived views owned by
[framework/workflow/WF-VIEWS.md](framework/workflow/WF-VIEWS.md). Generated project status belongs
in `project-overview.html`; initialization must not overwrite `index.html`.

```sh
python3 tools/validate_initialization.py .    # framework integrity and project contract
python3 tools/render_project_overview.py .    # the four-perspective control surface
python3 tools/render_framework_scope.py .     # the scope map, from the modules themselves
```

## Background

[Why AI Still Needs a Human to Build Software](https://imtoam.github.io/AIPartner/introduction/ai-native-project.html)
— the experience this framework came from. Also in
[français](https://imtoam.github.io/AIPartner/introduction/ai-native-project-fr.html),
[繁體中文](https://imtoam.github.io/AIPartner/introduction/ai-native-project-cn.html), and a
[version for students and non-specialists](https://imtoam.github.io/AIPartner/introduction/ai-native-project-youth.html).

Criticism is more useful than stars. If you find a way past the approval boundary, or make the
validator pass on an inconsistent project, please open an issue.
