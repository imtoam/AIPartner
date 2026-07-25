# START_HERE.md

AI Project Initialization Entry Point

Protocol ID: BOOTSTRAP-001

Protocol version: 0.3.0

Purpose: AI-facilitated greenfield project initialization

Audience: AI

Human guide: index.html

## Instructions for the AI

If you are an AI entering this project and have been asked to start or initialize a new project,
read this entire file before deciding what to do next.

This file is not a questionnaire for the user to read and complete. You must facilitate the
conversation, organize the information, expose unknowns, and complete initialization only after
the user approves the proposal. Do not ask the user to read the template files first.

Your goal is not to generate as many files as possible. Your goal is to turn the user's idea into a
project with:

- a clear objective.
- visible assumptions.
- controlled scope.
- explicit risk and authority.
- verifiable outcomes.
- a durable human and AI partnership.
- governance that activates as complexity grows.
- enough continuity for a future human or AI to take over reliably.

## 0. Confirm that this protocol applies

Perform these read-only checks in order:

1. Check for AGENTS.md or any higher-priority project instructions.
2. Look for project_profile.yaml at the project root.
3. If it exists, read initialization.status and initialization.mode.
4. Check whether the project already contains application code, user documents, project data,
   deployment configuration, or meaningful version history.

This version supports greenfield initialization only.

After confirming that the greenfield protocol applies, read PROJECT_WORKFLOW.md in full. It is the
canonical project method. Use initialization to configure it for this project, not to restate or
replace its rules.

### Start a new greenfield project

Proceed with this protocol only when:

- project_profile.yaml does not exist.
- the project has no existing application code, project data, deployment configuration, or
  user-maintained project documents.

The initialization proposal must set initialization.mode to greenfield.

### Resume an interrupted greenfield initialization

If project_profile.yaml records initialization.mode as greenfield and the status is draft,
proposed, approved_pending_materialization, or verification_failed:

- Read the existing initialization record.
- Tell the user where the process stopped.
- Continue from that state.
- Do not repeat confirmed questions.
- Do not treat an unapproved draft as project truth.

### Hand off an initialized project

If initialization.status is approved or complete, stop using this initialization protocol. Continue
through AGENTS.md, project_profile.yaml, PROJECT_WORKFLOW.md when project work is involved, and the
active modules listed there. Do not repeat the initial interview.

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

### 1.3 Propose before writing

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

### 1.4 Separate facts, inferences, proposals, and unknowns

Maintain these five information classes:

| Class | Meaning | May become project truth directly? |
|---|---|---|
| user_stated | Explicitly stated by the user | Yes, subject to later user revision |
| observed | Discovered through read-only inspection | Yes, with an evidence reference |
| ai_inferred | Inferred by AI from available context | No, user confirmation is required |
| ai_proposed | A course of action recommended by AI | No, user approval is required |
| unresolved | Missing, conflicting, or undecided | No, preserve it as unknown |

"Not found" does not mean "does not exist." "Not mentioned by the user" does not mean "no."

### 1.5 Protect the greenfield boundary

- Stop if meaningful project work already exists.
- Do not reinterpret an existing repository as an empty starting point.
- Do not delete or relocate files to make a repository appear empty.
- Put template-managed content in stable managed boundaries or separate files.

### 1.6 Do not collect or store secrets

Do not ask the user to place API keys, passwords, private keys, or production credentials in the
conversation, template documents, or version control. When credentials will be needed, record only
their purpose, delivery mechanism, and environment-variable name. Never record their values.

### 1.7 Define completion with evidence

"AI generated it," "the code looks plausible," and "the command did not visibly fail" do not mean
the work is complete. Every deliverable needs verification evidence proportional to its risk.
Anything that cannot be verified must be labeled unverified.

## 2. How to conduct the initialization conversation

Initialization is not a fixed long-form questionnaire. Use an adaptive interview:

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

Use the repository categories and ownership rules in PROJECT_WORKFLOW.md. Gather only the
project-specific information needed to configure them:

- why the project needs it now.
- what belongs there and what must not.
- whether its contents are maintained source, authoritative data, derived output, or disposable
  runtime state.
- whether it belongs in version control.
- which component or role owns changes to it.

The initialization proposal instantiates the categories this project needs. Do not copy the generic
directory rules into a second project document.

## 4. Configure the project method

PROJECT_WORKFLOW.md owns the delivery method, including Agile feedback, Lean learning, Kanban flow,
Continuous Delivery evidence, risk management, testing, alignment checks, and the Definition of
Done.

During initialization:

- do not ask the user to choose a named framework.
- recommend active workflow sections from the project's actual conditions.
- explain why each recommended practice matters to this project now.
- configure the first feature or experiment to enter the workflow with a clear outcome, boundary,
  risk view, and acceptance evidence.
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

The proposal must also identify:

- the source of truth for the original product intent.
- the source of truth for current system behavior.
- the active work list.
- where feature discussions and test strategies will be recorded when they need durable form.
- where durable decisions and completed-work history will be preserved.

### 5.7 First feature working agreement

Describe how the human and AI will discuss, approve, implement, test, and close the first feature.
Include the initial alignment check, expected boundary questions, test layers, acceptance evidence,
and the stop-and-discuss rule for discrepancies.

### 5.8 Files to materialize

List the files that will be created or modified after approval and explain which question each file
answers. Do not create overlapping documents with unclear or duplicated authority.

### 5.9 Verification plan

Explain how initialization will verify:

- structural completeness.
- consistency between state and approval.
- discoverability of active modules.
- absence of inactive modules from active rules.
- valid links and stable IDs.
- preservation of existing user content.
- separation of maintained source, authoritative data, generated output, and runtime state.
- consistency of the proposed repository map with the approved product and operating model.
- generation of the human overview from authoritative facts.

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

Explicit approval is required for:

- project goals and priority.
- AI write, review, release, and external-action authority.
- handling of production or sensitive data.
- irreversible operations.
- unattended automation.
- concurrent writing by multiple AI agents.
- activation of material governance modules.

## 7. Materialization order after approval

After approval:

1. Save approved facts, inference states, and unresolved questions.
2. Create project_profile.yaml with initialization.mode set to greenfield.
3. Create or update the compact routing rules in AGENTS.md.
4. Create or update the project method and active delivery rules in PROJECT_WORKFLOW.md.
5. Activate the approved role and project governance modules in their owning files.
6. Create the approved repository categories and ownership boundaries that are needed now.
7. Create only the project documents currently needed. Do not materialize meaningless empty
   documents.
8. Establish the feature discussion loop, explicit work-state flow, risk-based test strategy, and
   minimum Definition of Done.
9. Generate a static, human-facing HTML overview.
10. Run structural, reference, and consistency validation.
11. Report actual writes, validation results, and remaining unknowns to the user.

If a required tool or renderer has not yet been implemented:

- do not pretend the step succeeded.
- complete the safe and verifiable subset.
- record the missing capability as an explicit pending item.
- do not create a second source of truth through temporary copies.

## 8. Initialization states

Initialization follows this order. Approval may not be skipped.

1. uninitialized
2. interviewing
3. draft
4. proposed
5. approved_pending_materialization
6. materialized
7. verified
8. complete

The process may also enter one of these waiting or failure states:

- needs_user_decision
- verification_failed
- blocked_by_environment


When entering a failure or waiting state, preserve confirmed information and failure evidence so
that the next AI can continue from the same point.

## 9. Hand off ongoing governance

START_HERE.md stops governing the project when initialization is complete.

- AGENTS.md owns role, authority, reviewer, and concurrent-writer activation.
- PROJECT_WORKFLOW.md owns delivery, planning, production, operational, and high-impact activation.
- project_profile.yaml records which sections are active and any unresolved activation decision.

Before closing initialization, verify that each active or available module has exactly one owning
file and that the owning file contains its activation condition. Ongoing AI partners follow those
files and must not return to this initialization protocol to manage normal project growth.

## 10. Context-loading rules

The complete template may be bundled with the project, but it must not be loaded in full for every
task.

During initialization, read:

1. the compact AGENTS.md.
2. current project state in project_profile.yaml, if it exists.
3. PROJECT_WORKFLOW.md.
4. the entry points for active modules.
5. the sources of truth directly relevant to the current task.
6. ADRs or history only when a decision must be traced.

After initialization, use the routing rules in AGENTS.md. Do not use this file as the ongoing
project method.

Do not treat history as current state. Do not treat the roadmap as the current task. Do not treat
generated HTML as a source of truth.

## 11. Role of the HTML overview

HTML is the human-facing project control surface, not an independent source of truth. Generate it
from approved:

- project_profile.yaml state.
- current project documents.
- active governance modules.
- pending decisions.
- verification and runtime status.

Initialization does not require an HTML service. Generate a static page that can be opened
directly. Propose a service only when real requirements appear for multiple users, remote access,
identity and authorization, browser-based approval, or direct write-back.

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

Explain that version 0.3 supports greenfield initialization only. Do not inspect the project beyond
what was needed to identify it as existing work. Do not propose migration or make changes.

## 13. Minimum completion standard for initialization

Initialization may be marked complete only when all of the following are true:

- the user approved the project goal and first scope.
- project_profile.yaml records initialization.mode as greenfield.
- user facts, AI inferences, proposals, and unknowns are separated.
- the most important assumptions and success evidence are recorded.
- AI authority and human-approval boundaries are explicit.
- the AI partnership and feature discussion method are explicit.
- the repository map separates maintained source, authoritative data, generated output, and
  runtime state.
- the first feature has an agreed boundary and test approach.
- currently required role and project governance modules are active and validated in their owning
  files.
- inactive modules remain discoverable without entering active context.
- project sources of truth do not have overlapping responsibilities.
- the human overview can be generated from authoritative facts.
- validation results and unresolved questions were reported to the user.
- a future AI can determine where to continue.

The purpose of initialization is not to eliminate every unknown. It is to make unknowns visible,
keep the next step controlled, and give the project the ability to grow safely from its first day.
