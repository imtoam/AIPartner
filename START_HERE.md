# START_HERE.md
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AI Project Initialization Entry Point

Protocol ID: BOOTSTRAP-001

Protocol version: 0.11.0

Purpose: AI-facilitated greenfield project initialization

Audience: AI

Human guide: index.html

Framework invariant:

- This file and PROJECT_STRUCTURE_REFERENCE.md are retained framework instructions. Initialization
  must not edit, shorten, tailor, or delete their sections.
- AGENTS.md and PROJECT_WORKFLOW.md may be configured only inside their marked PROJECT CONFIG
  regions. Inactive modules remain present and unchanged.
- framework_manifest.json defines immutable files and managed-block integrity. Do not update its
  hashes during project initialization.
- Use tools/render_project_overview.py for the default overview unless an approved project-specific
  generator replaces it and the profile records that command.
- Read project_profile.example.yaml before creating project_profile.yaml. Do not invent a different
  state model or duplicate mutable work status in the profile.
- Run tools/validate_initialization.py before reporting verification.

## Instructions for the AI

If you are an AI entering this project and have been asked to start or initialize a new project,
read this entire file before deciding what to do next.

This file is not a questionnaire for the user to read and complete. You must facilitate the
conversation, organize the information, expose unknowns, and complete initialization only after
the user approves the proposal. Do not ask the user to read the template files first.

Your goal is not to generate as many files as possible. Your goal is to turn the user's idea into a
project with:

- a clear objective.
- a compact language, terminology, and translation contract.
- visible assumptions.
- controlled scope.
- explicit risk and authority.
- verifiable outcomes.
- a durable human and AI partnership.
- governance that activates as complexity grows.
- enough continuity for a future human or AI to take over reliably.
- a human-readable interface derived from authoritative project sources.

## 0. Confirm that this protocol applies

Perform these read-only checks in order:

1. Check for AGENTS.md or any higher-priority project instructions.
2. Look for project_profile.yaml at the project root.
3. If it exists, read initialization.status and initialization.mode.
4. Check whether the project already contains application code, user documents, project data,
   deployment configuration, or meaningful version history.

Distinguish reusable template history from project-specific history. Template-only commits do not
by themselves make the repository brownfield. Do not remove or rewrite that history while deciding.

This version supports greenfield initialization only.

After confirming that the greenfield protocol applies, read PROJECT_WORKFLOW.md in full together with the
`framework/workflow/` module files it routes to, and read PROJECT_STRUCTURE_REFERENCE.md with its
`framework/structure/` catalog files for the repository and project-control proposal. The workflow is the
canonical project method. The structure reference is a menu, not a requirement to create every
entry. Use initialization to configure them for this project, not to restate or replace their rules.

### Start a new greenfield project

Proceed with this protocol only when:

- project_profile.yaml does not exist.
- the project has no existing application code, project data, deployment configuration, or
  user-maintained project documents.

The initialization proposal must set initialization.mode to greenfield.

### Resume an interrupted greenfield initialization

If project_profile.yaml records initialization.mode as greenfield and its status is anything other
than complete:

- Read the existing initialization record.
- Tell the user where the process stopped.
- Follow the state-action table in Section 8 and continue from that state.
- Do not repeat confirmed questions.
- Do not treat an unapproved draft as project truth.

### Hand off an initialized project

Only initialization.status complete hands off the project. Continue through AGENTS.md,
project_profile.yaml, PROJECT_WORKFLOW.md when project work is involved, and the active modules
listed there. Do not repeat the initial interview.

### Leave existing-project onboarding for a later version

If the repository contains meaningful project work but has no template profile, do not attempt to
adopt, migrate, classify, restructure, or initialize it. Tell the user that this protocol currently
supports new projects only. Make no changes.

The initialization.mode field reserves these values for future protocols:

| Mode | Current status |
|---|---|
| greenfield | Supported by this protocol |
| brownfield | Reserved, not implemented |
| import | Reserved, not implemented |
| reinitialize | Reserved, not implemented |

Reserved values are compatibility points. They are not permission to improvise an onboarding
process.

### Use external reference material without confusing it with the target

A greenfield target may use an existing project, document set, or codebase as read-only reference
material. The target repository state determines whether this protocol applies; the reference does
not become the target.

Record one input source type in project_profile.yaml:

- idea_only.
- requirements_reference.
- reference_project_readonly.

For each material characteristic taken from a reference, classify it as adopt_now, approved_target,
deferred, rejected, or unresolved. An observed fact about the reference is not a current fact about
the new target and does not activate governance by itself. The Product Owner must confirm any
adopt_now or approved_target interpretation that materially affects product scope, architecture,
operation, data, risk, or roles.

## 1. Non-negotiable baseline principles

These principles apply from the first conversation. They do not depend on optional modules.

### 1.1 The human retains final authority

The user owns decisions about:

- product goals and success criteria.
- priority and scope.
- risk acceptance.
- AI roles and permissions.
- production release.
- irreversible actions.
- activation of modules that materially change project governance.

AI may analyze, recommend, and execute. It must not present its own judgment as a user decision.

### 1.2 Partnership means continuous guidance

Follow the partnership duties defined in AGENTS.md during initialization. Do not assume the user is
already an experienced Product Owner, project manager, architect, QA lead, security specialist, or
operations lead. Bring the relevant perspectives into the conversation, explain decisions in plain
language, and preserve human authority. AGENTS.md remains the canonical source for this role after
initialization.

### 1.3 Tailor from evidence

Tailoring is a global rule for this template. The presence of a file, section, practice, directory,
or test layer in the template is not evidence that the project needs it.

Use the decision states and tailoring procedure in PROJECT_STRUCTURE_REFERENCE.md. Recommend the
smallest sufficient starting configuration, explain every selection, defer inactive needs to an
explicit trigger, and allow approved local extensions. Core artifacts required to operate this
protocol still receive project-specific content rather than generic filler.

Tailoring changes activation and project-specific configuration. It never removes framework
instructions or inactive modules. It cannot waive human authority, information honesty, permanent
work identity, evidence-based completion, version-control disposition, or the duty to stop on a
material discrepancy.

### 1.4 Propose before writing

Read-only discovery is allowed during initialization. Unless the user explicitly requests a safe,
reversible exploratory action, do not perform any of the following before showing an initialization
proposal and obtaining approval:

- create or modify application code.
- overwrite existing project files.
- alter version history.
- install dependencies.
- create remote resources.
- publish, deploy, or send external messages.
- write to production data.
- perform irreversible actions.

Only materialize the approved files after the user approves the initialization proposal.

### 1.5 Separate facts, inferences, proposals, and unknowns

Maintain these five information classes:

| Class | Meaning | May become project truth directly? |
|---|---|---|
| user_stated | Explicitly stated by the user | Yes, subject to later user revision |
| observed | Discovered through read-only inspection | Yes, with an evidence reference |
| ai_inferred | Inferred by AI from available context | No, user confirmation is required |
| ai_proposed | A course of action recommended by AI | No, user approval is required |
| unresolved | Missing, conflicting, or undecided | No, preserve it as unknown |

"Not found" does not mean "does not exist." "Not mentioned by the user" does not mean "no."

Every unresolved decision records its owner, status, provenance, and whether it is blocking.
Questions about initialization mode, product intent, first scope, authority, irreversible data,
high-impact boundaries, or another choice that could materially change the initial solution are
blocking. Initialization cannot advance to verified or complete while a blocking decision is open.

### 1.6 Protect the greenfield boundary

- Stop if meaningful project work already exists.
- Do not reinterpret an existing repository as an empty starting point.
- Do not delete or relocate files to make a repository appear empty.
- Put template-managed content in stable managed boundaries or separate files.

### 1.7 Do not collect or store secrets

Do not ask the user to place API keys, passwords, private keys, or production credentials in the
conversation, template documents, or version control. When credentials will be needed, record only
their purpose, delivery mechanism, and environment-variable name. Never record their values.

### 1.8 Define completion with evidence

"AI generated it," "the code looks plausible," and "the command did not visibly fail" do not mean
the work is complete. Every deliverable needs verification evidence proportional to its risk.
Anything that cannot be verified must be labeled unverified.

### 1.9 Establish language without creating a language questionnaire

Every project records separate choices for conversation language, engineering language of record,
code identifiers and typed values, human-view locales, source evidence, and translation. Offer the
recommended default from WF-COMMUNICATION as one bundled decision. Expand it only when the user
rejects the default or the project has multilingual, domain-terminology, or source-provenance risk.

Do not translate identifiers, schemas, IDs, typed unknown states, or original evidence merely to
make all surfaces appear to use one language.

### 1.10 Keep human views subordinate to project truth

Maintained Markdown owns project documentation. Executable code, configuration, schemas, and
authoritative data retain their declared ownership. Static HTML, dashboards, and HTTP responses are
derived views with visible sources, generation time, freshness, and failures. They never become the
only place where a decision, status, architecture fact, or business fact exists.

Every initialized project nevertheless requires one HTML control surface from the beginning.
People should use it to govern direction, architecture, scope, progress, cadence, risk, business
health, operational health, and decisions rather than serving as assistants who manually reconcile
raw logs, databases, and development files. The four required perspectives and their unavailable
states are defined by WF-VIEWS.

## 2. How to conduct the initialization conversation

Initialization is not a fixed long-form questionnaire. Use an adaptive interview.

**Ask the delegation-mode question first.** Before any other initialization question, offer the two
ways of working defined in framework/roles/ROLE-DELEGATION.md §4: the AI decides the technical
setup from plain-language answers and reports what it chose, or the user selects the setup from the
options. The answer determines how every later question is phrased, and whether ROLE-DELEGATION is
activated. Neither answer changes what is recorded, and the user may switch at any time.

Then continue the adaptive interview:

1. Extract information the user has already provided.
2. Restate your current understanding before asking the user to repeat anything.
3. Identify unknowns that would materially alter product direction, architecture, or risk.
4. Ask one small, coherent group of questions at a time.
5. Offer a recommended option with reasons and consequences, while preserving a free-form response
   path.
6. Supply the product, delivery, architecture, QA, security, and operations perspectives that are
   relevant to the decision.
7. Allow the user to answer "unknown" or "decide later."
8. Update the current understanding as information arrives instead of restarting the questionnaire.

If the user provides only a one-line idea, start with the smallest useful questions. If the user
has already provided a detailed description, summarize it and ask only for genuinely missing
decisions.

Use the user's primary language. Do not require the user to understand project-management or
software-engineering terminology. Explain consequences in plain language when terminology is
necessary.

## 3. Minimum project model to establish

Gradually clarify the following areas. The user does not have to answer everything at once, and
every field does not need a definite answer on day one.

### 3.1 Idea and problem

- working project name.
- one-sentence intent.
- the problem to solve.
- why it is worth solving now.
- what happens if nothing changes.

### 3.2 Users and value

- who will use the product directly.
- who else may be affected.
- how the user handles the problem today.
- what observable value the project should create.
- which results are outputs versus real outcomes.

### 3.3 Success, failure, and non-goals

- near-term evidence of success.
- long-term evidence of success.
- explicit non-goals.
- evidence that should cause a pivot or stop decision.
- metrics that may be vanity metrics rather than useful outcomes.

### 3.4 Assumptions and learning

- the most important unverified assumptions.
- the assumption whose failure would most damage the project's value.
- the smallest credible way to test it.
- the evidence required before further investment.

Use Lean validated-learning ideas here, but do not mechanically require every project to build an
MVP immediately. An experiment may be an interview, manual service, data analysis, prototype,
technical spike, or working software.

### 3.5 Product scope

- the first capability worth delivering.
- current scope.
- explicitly deferred capabilities.
- external systems, vendors, and data dependencies.
- required devices, platforms, or operating constraints.

### 3.6 Data, risk, and irreversibility

- whether production data is involved.
- whether personal, financial, medical, legal, security, or other sensitive information is
  involved.
- whether the system can move money, contact external parties, or affect the physical world.
- which actions are difficult to reverse.
- the acceptable failure envelope.
- actions that always require human approval.

### 3.7 Runtime environment

- local-only use or deployment.
- network, cloud, or third-party service requirements.
- scheduled or unattended operation.
- target operating systems and major technical constraints.
- initial backup, recovery, and observability needs.

### 3.8 Collaboration model

- the number of humans currently involved.
- the number of AI agents currently involved and their roles.
- whether there is only one writer.
- whether independent peer review is needed.
- whether work will proceed concurrently.
- who owns final integration and release.

Do not assume multi-agent governance merely because the template includes multi-agent modules.

### 3.9 Repository structure and information ownership

Use the repository categories and artifact names in PROJECT_STRUCTURE_REFERENCE.md under the
ownership rules in PROJECT_WORKFLOW.md. Gather only the project-specific information needed to
configure them:

- why the project needs it now.
- what belongs there and what must not.
- whether its contents are maintained source, authoritative data, derived output, or disposable
  runtime state.
- whether it belongs in version control.
- which component or role owns changes to it.

The initialization proposal instantiates the categories this project needs. Do not copy the generic
directory rules into a second project document.

Classify retained framework files separately from project-selected artifacts. Current-state files
contain only present target-project reality. Planned architecture and future operating behavior
belong in the first feature brief, a roadmap, an ADR, or a deferred trigger.

### 3.10 Git and repository history

Inspect the repository before asking questions. Use the Git guidance in
PROJECT_STRUCTURE_REFERENCE.md and recommend a tailored mode in plain language.

Clarify only the decisions that apply:

- whether Git is already initialized and whether its history is template-only or project-specific.
- local-only history or a remote repository, and the purpose of the remote.
- public or private visibility.
- default branch and whether review, concurrency, release isolation, or a stable production
  baseline justifies additional branches.
- who may commit, push, merge, administer, publish, or rewrite history.
- tracked source and evidence versus ignored secrets, production data, generated output, and local
  runtime state.
- license expectations, including whether code and documentation need different terms.
- when the first validated project commit should be created.

Do not require the user to invent a Git workflow. Recommend the smallest safe model and explain
what would trigger a more complex one. Remote creation, visibility changes, pushes, publication,
and history rewrites require explicit approval.

### 3.11 Language, terminology, and translation

Propose one compact communication contract using WF-COMMUNICATION. Clarify only deviations from the
recommended default and material choices such as:

- whether technical records and code use English or another engineering language of record.
- which locale or locales human-facing project views use.
- whether source material can appear in languages different from the engineering record.
- whether translated output is needed now or only after a trigger.
- whether domain terminology is ambiguous enough to require `docs/terminology.md`.

The Product Owner decides the material policy. The AI recommends exact boundaries and prevents one
general `language` answer from silently controlling unrelated surfaces.

### 3.12 Human project interface

Static `project-overview.html` is a required starting control surface, not an optional dashboard.
From initialization onward it contains four stable perspectives: management consultation,
business/domain operations, system operations, and architecture/delivery. For each one, propose its
audience, purpose, accountable owner, source state and reason, declared sources, and activation or
recovery trigger. A perspective with no current evidence stays visible as `not_yet_available`,
`not_applicable`, `blocked`, or `degraded`; it must not be omitted or shown as healthy.

Keep these four perspectives in one static page initially. Recommend split pages or local HTTP only
when live refresh, search, filtering, navigation depth, or structured local-AI access is a current
need. Loopback, read-only service is the safe HTTP default. Network exposure and write-back are
separate approvals, not consequences of choosing HTTP.

## 4. Configure the project method

PROJECT_WORKFLOW.md owns the delivery method, including Agile feedback, Lean learning, Kanban flow,
Continuous Delivery evidence, risk management, testing, alignment checks, and the Definition of
Done.

During initialization:

- do not ask the user to choose a named framework.
- recommend active workflow sections from the project's actual conditions.
- do not use newly generated artifacts as evidence for activating their own module.
- treat future conditions as deferred until the next approved increment needs the control.
- explain why each recommended practice matters to this project now.
- configure the first feature or experiment to enter the workflow with a clear outcome, boundary,
  risk view, and acceptance evidence.
- record the compact communication contract and the initial static human-view contract.
- record all four control-surface perspective contracts, including honest unavailable states.
- leave unnecessary optional sections inactive until their activation conditions appear.

Do not copy the workflow stages into the initialization record. Record only the approved
project-specific configuration, active sections, and unresolved decisions.

## 5. Prepare the initialization understanding

When enough information exists to propose the first project configuration, present a readable
summary with at least the following sections.

### 5.1 My understanding of the idea

Explain in concise language:

- whose problem the project addresses.
- the first value it intends to create.
- the most important current success evidence.

### 5.2 Information provenance

List separately:

- explicit user statements.
- observed facts with evidence references.
- reference-material facts and their adopt, target, defer, reject, or unresolved disposition.
- AI inferences awaiting confirmation.
- AI proposals awaiting approval.
- unresolved questions.
- conflicting information.

### 5.3 Minimum product and learning recommendation

Explain:

- what to validate first.
- what to deliver first.
- what not to build yet.
- the reason for each recommendation.
- how to decide whether to continue, modify, or stop.

### 5.4 Initial risk and authority

Explain:

- currently known high-impact risks.
- recommended AI authority boundaries.
- actions that require human approval.
- risks that cannot yet be assessed.

### 5.5 Recommended governance modules

Distinguish team and authority modules in AGENTS.md from project delivery and risk modules in
PROJECT_WORKFLOW.md. For every recommended module, show:

- its stable module ID.
- the triggering evidence.
- whether it is required or advisory.
- the rules it adds.
- the files or managed sections it will create or change.
- the consequence of not activating it.
- its module dependencies.

List untriggered modules briefly as "currently inactive." Do not expand every inactive rule into
the active context.

### 5.6 Repository and file map

Present the proposed top-level categories before creating them. For every category or important
file, explain its responsibility, ownership, version-control policy, and whether it is needed now.
Show where application code, documentation, tests, tools, user interfaces, data definitions,
configuration, generated logs, reports, and runtime state will live.

Use the tailoring states from PROJECT_STRUCTURE_REFERENCE.md. The proposal must show
framework_retained, selected_now, deferred_until_trigger, not_applicable, and any local_extension
decisions with their evidence. Do not materialize deferred or not-applicable items.

The proposal must also identify:

- the source of truth for the original product intent.
- the source of truth for current system behavior.
- the active work list.
- where feature discussions and test strategies will be recorded when they need durable form.
- where durable decisions and completed-work history will be preserved.

#### Delivery sequencing when several work units exist

If two or more features or implementation units must be coordinated, gather enough information to
propose:

- stable `delivery_group` membership for every sequenced work ID.
- one unique `group_order` for every active group.
- cross-group and cross-feature dependencies using resolvable IDs.
- the exact-scope owner for every work item and a stable scope revision.
- approval evidence that explicitly names the approved scope revision.

Do not ask the Product Owner to invent a grouping system. The AI proposes the smallest coherent
grouping and explains conflicts. Do not infer that initialization approval, roadmap placement, or
priority is approval of an unstated feature scope.

### 5.7 First feature working agreement

Describe how the human and AI will discuss, approve, implement, test, and close the first feature.
Include the initial alignment check, expected boundary questions, test layers, acceptance evidence,
the stop-and-discuss rule for discrepancies, and the first permanent work ID allocated through
PROJECT_WORKFLOW.md.

If the first feature crosses a durable boundary or activates WF-DATA, WF-PERSISTENCE, WF-ML, WF-OPS,
WF-RECOVERY, or WF-HIGH-IMPACT, include a durable feature-plan file in the proposal. Do not reduce a high-risk
agreement to one acceptance sentence in the active queue.

When grouped delivery is active, include a delivery-sequence table in the proposal. For every work
ID, show `delivery_group`, group outcome, `group_order`, dependencies, exact-scope owner, scope
revision, approval state, and approval evidence reference. State that implementation readiness is
checked only in the mandatory order of the delivery sequencing gate owned by
framework/workflow/WF-PLANNING.md

If dependencies contradict the declared order, revise `group_order` and repeat the remaining
checks. If scope changes after approval, create a new scope revision and return to the sequencing
gate; do not carry the earlier approval forward.

### 5.8 Git and repository proposal

Explain:

- observed repository and history state.
- recommended version-control mode and why it is sufficient now.
- template-history treatment.
- default branch, writer, commit, merge, and push authority.
- remote provider, purpose, and visibility when proposed.
- ignore and large-artifact policy.
- license recommendation and unresolved ownership questions.
- initial commit plan and any external action requiring separate approval.

### 5.9 Communication and human-interface proposal

Present the recommended communication contract as one decision, showing the engineering language
of record, conversation language, human-view locale, source-evidence policy, translation boundary,
and whether a terminology registry is selected now or deferred to a trigger.

Show the initial static overview as selected_now. For each of its four required perspectives, show
the audience, purpose, accountable owner, current source state and reason, declared source paths,
and activation or recovery trigger. The perspective itself is never deferred; only its unavailable
source state, a separate page, or live behavior may be deferred. Show additional pages as selected,
deferred, or not applicable. For any proposed HTTP mode, state bind scope, read/write authority,
source contracts, security consequences, and the trigger that makes a service necessary.

### 5.10 Files to materialize

List the files that will be created or modified after approval and explain which question each file
answers. Do not create overlapping documents with unclear or duplicated authority.

### 5.11 Verification plan

Explain how initialization will verify:

- structural completeness.
- consistency between state and approval.
- discoverability of active modules.
- inactive modules remain present but are not marked active or represented as current project facts.
- valid links and stable IDs.
- preservation of existing user content.
- separation of maintained source, authoritative data, generated output, and runtime state.
- consistency of the proposed repository map with the approved product and operating model.
- every materialized path has a selected_now decision and every local extension has an owner,
  lifecycle, and approval when required.
- every bundled reusable framework path has a framework_retained classification.
- deferred and not-applicable reference items were not created.
- Git state, tracked and ignored files, branch configuration, and approved authority match the
  proposal.
- when delivery groups are active: every sequenced work ID has exactly one group, every active group
  has a unique order, dependencies resolve without cycles or later-group contradictions, and
  approval evidence names the current exact-scope revision.
- the delivery validation command was actually executed and produced a current `pass` receipt bound
  to the phase plan, validator, scope-owner files, scope revisions, and approvals.
- the communication contract contains separate language responsibilities and no ambiguous general
  language field.
- generated human views identify sources, locale, generation time, version, freshness, and failure
  state without owning project truth.
- the generated overview contains all four required perspectives, accountable owners, honest source
  states, and activation or recovery triggers where evidence is unavailable.
- any proposed HTTP service has explicit bind scope, read/write authority, and approval evidence.
- generation of the human overview from authoritative facts.
- preservation of index.html as the permanent human starting guide.
- tools/validate_initialization.py completes without errors and its actual output is recorded.

## 6. Request approval

After presenting the proposal, explicitly tell the user that they may respond in natural language
to:

- approve everything.
- approve only named sections.
- correct an interpretation.
- reject a recommendation.
- leave an item unresolved.
- continue the discussion.
- request a more detailed file-change preview.

Silence is not approval.

Record approval in project_profile.yaml with state, approver, date, approved scope, and an evidence
reference that a future AI can interpret. Do not write "approved by the Product Owner" merely
because the AI completed a proposal.

Initialization approval authorizes only its recorded initialization scope. When delivery groups
are active, each feature approval must separately name the exact scope revision it authorizes.
Roadmap placement, priority, group membership, or a general instruction to proceed is not a
substitute for that binding.

Explicit approval is required for:

- project goals and priority.
- AI write, review, release, and external-action authority.
- handling of production or sensitive data.
- irreversible operations.
- unattended automation.
- concurrent writing by multiple AI agents.
- the engineering language of record and any translation policy that can affect saved project
  meaning.
- activation of material governance modules.
- non-loopback human-interface exposure, browser approval, or source/data write-back.
- remote creation or replacement, public visibility, push or publication, and history rewrite.

## 7. Materialization order after approval

After approval:

1. Save approved facts, inference states, and unresolved questions.
2. Create project_profile.yaml from project_profile.example.yaml with initialization.mode set to
   greenfield. Preserve its ownership boundaries and do not add mutable work-item status.
3. Configure only the marked PROJECT CONFIG regions in AGENTS.md.
4. Configure only the marked PROJECT CONFIG regions in PROJECT_WORKFLOW.md.
5. Activate the approved role and project governance modules in their owning files.
6. Record the approved communication contract and terminology trigger.
7. Create the approved repository categories and ownership boundaries that are needed now.
8. Create only the project documents currently needed. Do not materialize meaningless empty
   documents.
9. Establish the permanent work ID format and allocation source, feature discussion loop, explicit
   work-state flow, risk-based test strategy, and minimum Definition of Done.
10. When grouped delivery is active, materialize the phase delivery plan and exact-scope owners,
    then run the project-specific validator in the mandatory order of the delivery sequencing gate
    owned by framework/workflow/WF-PLANNING.md. It must atomically write the standard delivery
    receipt. Run the core
    initialization validator afterwards; do not begin implementation unless both checks pass and
    the receipt is current.
11. Keep index.html unchanged as the permanent human starting guide. Generate the approved project
    state as project-overview.html from declared sources, with visible provenance, freshness, and
    management, business, operations, and architecture/delivery perspectives; the framework
    default command is `python3 tools/render_project_overview.py .`.
12. Run tools/validate_initialization.py and any project-specific structural, reference, drift, and
    consistency checks. Record actual evidence rather than self-declared pass values.
13. Apply the approved local Git configuration without discarding existing history or user work.
14. Create the initial project commit only after validation and only when approved.
15. Create or change a remote, push, publish, expose a service, or change visibility only when
    explicitly approved.
16. Report actual writes, validation results, Git state, and remaining unknowns to the user.

If a required tool or renderer has not yet been implemented:

- do not pretend the step succeeded.
- complete the safe and verifiable subset.
- record the missing capability as an explicit pending item.
- do not create a second source of truth through temporary copies.

## 8. Initialization states

Use only these states:

| State | Meaning | Required next action |
|---|---|---|
| uninitialized | No interview state exists | Begin read-only discovery |
| interviewing | The idea is being clarified | Continue the adaptive interview |
| draft | A working interpretation exists | Resolve material unknowns and prepare the proposal |
| proposed | The proposal is waiting for human action | Wait for approval, correction, rejection, or deferral |
| needs_user_decision | A blocking choice is open | Ask for the smallest required decision; do not materialize |
| approved_pending_materialization | Approval evidence and scope are recorded | Materialize only the approved scope |
| materialized | Approved files were written | Run deterministic and project-specific validation |
| verification_failed | A check failed | Preserve evidence, correct safely, and rerun |
| blocked_by_environment | Validation or materialization cannot proceed safely | Record blocker and required external change |
| verified | Required checks passed | Report results and remaining non-blocking unknowns, then set complete |
| complete | Initialization is handed off | Stop using this protocol for ordinary work |

Approval may not be skipped. There is no `approved` state. A waiting or failure state preserves the
last completed stage, confirmed facts, and evidence so the next AI can continue without restarting.

Open blocking decisions permit only interviewing, draft, proposed, or needs_user_decision. They
forbid approved_pending_materialization, materialized, verified, and complete.

## 9. Hand off ongoing governance

START_HERE.md stops governing the project when initialization is complete.

- AGENTS.md owns role, authority, reviewer, and concurrent-writer activation.
- PROJECT_WORKFLOW.md owns communication, views, delivery, planning, drift, data, operation,
  recovery, and high-impact activation.
- project_profile.yaml records the approved activation summary and pointers. The owning file remains
  authoritative, and validation prevents drift.

Before closing initialization, verify that each active or available module has exactly one owning
file and that the owning file contains its activation condition. Ongoing AI partners follow those
files and must not return to this initialization protocol to manage normal project growth.

## 10. Context-loading rules

The complete template may be bundled with the project, but it must not be loaded in full for every
task.

During initialization, read:

1. the compact AGENTS.md.
2. project_profile.example.yaml as the profile contract.
3. initialization, activation, approval, communication, delivery-control, human-interface,
   structure, and unresolved-decision state in project_profile.yaml, if it exists.
4. PROJECT_WORKFLOW.md and the routed framework/workflow/ module files relevant to initialization.
5. PROJECT_STRUCTURE_REFERENCE.md and its framework/structure/ catalog files while preparing the
   repository and control-artifact proposal.
6. the entry points for active modules.
7. the sources of truth directly relevant to the current task.
8. ADRs or history only when a decision must be traced.

After initialization, use the routing rules in AGENTS.md. Do not use this file as the ongoing
project method.

Do not treat history as current state. Do not treat the roadmap as the current task. Do not treat
generated HTML as a source of truth.

## 11. Role of the HTML overview

index.html remains the permanent human starting guide. Do not replace it with project status.

Generate current project state as project-overview.html. It is a human-facing control surface, not
an independent source of truth. Generate it from approved:

- project_profile.yaml state.
- current project documents.
- active governance modules.
- pending decisions.
- verification and runtime status.

The control surface is how people govern the project without reconstructing it from raw logs,
development files, databases, or source code. It must always expose:

- management consultation: direction, value, scope, progress, cadence, risks, decisions, and advice.
- business/domain operations: recommendations, business logic, domain-data health, exceptions, and
  actions needing specialist judgment.
- system operations: services, jobs, providers, storage, backups, incidents, recovery, capacity,
  and health.
- architecture and delivery: current and approved target architecture, module boundaries,
  dependencies, implementation plans, status, technical risk, and drift.

If a perspective has no authoritative evidence yet, show its source state, accountable owner, and
activation or recovery trigger. Absence of evidence is never rendered as a healthy state.

The overview must:

- visibly distinguish approved facts, proposals, and unresolved decisions.
- include every open blocking decision.
- use clickable relative links to maintained project documents.
- show its source paths and generation time.
- show its view ID, locale, source version, freshness, and derived-view status.
- never claim verified or complete when the profile or validator disagrees.
- preserve the framework's established visual language unless the Product Owner approves a new
  project design.

Initialization does not require an HTML service. Generate a static page that can be opened
directly. Propose loopback read-only HTTP only for a current live-refresh, search, filtering, or
structured local-AI need. Remote access, identity, browser approval, and direct write-back require
separate authorization and risk controls.

## 12. The AI's first response

### If the user has not described an idea

Do not summarize this entire protocol. Briefly explain that you will facilitate initialization,
then invite the user to describe the idea naturally. For example:

"I will help turn your idea into an executable, verifiable project setup that can grow safely.
You do not need to complete a long questionnaire first. In your own words, tell me what problem
you want to solve, who experiences it, and what change you hope the project will create. It is
fine to say that some parts are still unknown."

### If the user has already described an idea

Do not ask them to repeat it. Summarize what you understand, label material inferences, and ask the
smallest useful group of unanswered questions.

### If this is an existing project

Explain that version 0.11 supports greenfield initialization only. Do not inspect the project beyond
what was needed to identify it as existing work. Do not propose migration or make changes.

## 13. Minimum completion standard for initialization

Initialization may be marked complete only when all of the following are true:

- the user approved the project goal and first scope.
- project_profile.yaml records initialization.mode as greenfield.
- approval state, scope, approver, date, and evidence reference are recorded.
- user facts, AI inferences, proposals, and unknowns are separated.
- reference-material facts have explicit adopt, target, defer, reject, or unresolved dispositions.
- the most important assumptions and success evidence are recorded.
- AI authority and human-approval boundaries are explicit.
- conversation, engineering-record, code-identifier, human-view, source-evidence, and translation
  language responsibilities are separate and approved.
- the AI partnership and feature discussion method are explicit.
- the repository map separates maintained source, authoritative data, generated output, and
  runtime state.
- the selected version-control mode, repository authority, ignore policy, license state, and initial
  commit or explicit deferral are recorded.
- the first feature or experiment has an agreed boundary and evidence approach.
- when grouped delivery is active, group membership, group order, dependencies, and scope-bound
  approval pass the mandatory sequencing gate, and a current validation receipt binds that result
  to the phase plan, validator, exact-scope owners, and approval revisions.
- the current work source is the only owner of mutable work-item status.
- project-overview.html is generated from declared sources and exposes provenance, locale,
  generation time, freshness, errors, every blocking decision, and all four required human
  perspectives with honest source states, reasons, owners, and activation or recovery triggers.
- currently required role and project governance modules are active and validated in their owning
  files.
- inactive modules remain discoverable without entering active context.
- START_HERE.md and PROJECT_STRUCTURE_REFERENCE.md remain unchanged framework references.
- project sources of truth do not have overlapping responsibilities.
- index.html remains the human starting guide and project-overview.html represents project state.
- every open blocking decision has been resolved.
- tools/validate_initialization.py reports no errors and its evidence is recorded.
- validation results and unresolved questions were reported to the user.
- a future AI can determine where to continue.

The purpose of initialization is not to eliminate every unknown. It is to make unknowns visible,
keep the next step controlled, and give the project the ability to grow safely from its first day.
