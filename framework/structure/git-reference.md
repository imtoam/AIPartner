# Structure catalog — Git and version-control reference

AIPartner framework structure-reference catalog file.

- Spine, selection principles, and tailoring protocol: [PROJECT_STRUCTURE_REFERENCE.md](../../PROJECT_STRUCTURE_REFERENCE.md)
- This catalog is a menu, not project truth. Tailoring selects from it; it never edits this file.
- Sole normative owner of: repository discovery, version-control modes, template history, branch models, the commit contract, ignore policy, remote/visibility/license rules, and the initial checkpoint

Original section numbering is preserved so existing references remain valid.

---

## 4. Git and version-control reference

Git is the recommended version-control system for software projects. The AI inspects the existing
repository and recommends a tailored Git configuration. It does not ask the user to design a branch
strategy without guidance.

### 4.1 Repository discovery

Before proposing Git changes, inspect and report:

- whether the directory is already a Git repository.
- whether history contains only the reusable template or actual project work.
- the current branch, working-tree state, remotes, and upstream tracking.
- untracked or modified files that may belong to the user.
- existing ignore rules, hooks, submodules, worktrees, large-file support, and repository policies.
- whether the repository is local only, private remote, or public remote.
- whether any existing history or remote relationship must be preserved.

Do not delete or replace the .git directory, rewrite history, change a remote, or discard local work
to make the repository match the reference.

### 4.2 Version-control modes

| Mode | Use when | Default controls |
|---|---|---|
| local_git | One person or AI needs recoverable local history | One default branch, small commits, no remote |
| remote_single_writer | One writer needs backup, publishing, or cross-device access | One remote, explicit push authority, simple branch policy |
| protected_collaboration | Review or several contributors affect a shared baseline | Protected default branch, short feature branches, pull requests |
| integration_branch | A long-running release or phase must develop apart from a stable baseline | Stable baseline, named integration branch, frequent baseline merges |
| deferred | The current output does not yet justify version control | Record the trigger and risk; do not pretend history exists |

For a normal software project, recommend local_git unless repository inspection shows an existing
safe configuration or the user needs a remote. Lack of a remote does not prevent local version
control.

### 4.3 Template history

Prefer a repository created from a Git hosting template or a copy of the template files placed into
a new empty repository. This gives the new project its own history.

If the repository was cloned with the reusable template's history:

- identify template-only history separately from project work.
- explain whether preserving that history is useful.
- do not remove .git or rewrite commits without explicit approval.
- record the template source and version used.
- if a clean project history is required, propose a safe copy into a separately initialized
  repository rather than silently destroying the existing history.

Template-only commits do not by themselves make the directory a brownfield project. Meaningful
project code, project data, project documents, deployment configuration, or project-specific
commits do.

### 4.4 Branch models

| Situation | Recommended model |
|---|---|
| One writer, no protected production baseline | Commit small verified changes to the default branch |
| Short reviewed change | Short-lived feature branch and pull request |
| Multiple concurrent writers | One branch or worktree per writer with one integration owner |
| Stable production baseline and long-running next phase | Stable default branch plus one integration branch |

Do not create branches for ceremony. Activate branch or worktree rules when review, concurrency,
release isolation, or production stability creates the need.

Every non-default model records both its activation condition and its retirement condition. Branch
topology is not a work-status source. When topology is retired, preserve historical receipts and
remove old branch commands, merge sources, and worktree paths from current governance documents.

Invest-derived integration lessons:

- keep the production baseline stable and integrate small fixes independently.
- create long-running feature branches from the current integration branch, not an outdated base.
- merge baseline changes into the integration branch promptly instead of accumulating a large final
  conflict.
- do not rebase or otherwise rewrite shared baseline and integration history.
- inspect repository status before and after merges, commits, and worktree integration.
- never carry runtime output or unrelated user changes across branches accidentally.
- when the default branch is also a production worktree, inspect schedules and running processes
  before runtime-sensitive edits and keep entry points out of readable intermediate states.

### 4.5 Commit contract

Each commit should:

- represent one coherent verified change.
- carry the applicable permanent work ID.
- explain what changed and why.
- include only intended maintained source, configuration, tests, and documentation.
- leave secrets, production data, logs, reports, caches, backups, and unrelated user changes out.
- follow the applicable Definition of Done before the work is reported complete.

The commit message or linked history entry records the important verification evidence. Do not use
one large commit to hide several unrelated outcomes.

### 4.6 Ignore policy

Tailor .gitignore to the selected runtime and tools. Consider:

- operating-system and editor metadata.
- local environment files and all secret-bearing files.
- virtual environments, dependency caches, build output, and compiled artifacts.
- logs, generated reports, disposable caches, locks, and temporary state.
- live database files, production snapshots, backups, and recovery archives.
- local tool state that cannot be shared safely.

Do not ignore maintained schema, migrations, safe fixtures, source configuration, tests, or required
evidence merely because they share a parent directory with generated files.

### 4.7 Remote, visibility, and license

Creating a remote repository, changing visibility, pushing commits, or publishing a site is an
external action and requires explicit user approval.

The proposal states:

- local-only or remote mode.
- hosting provider and remote purpose when applicable.
- public or private visibility.
- who may push, merge, administer, or change protection.
- whether pull requests and required review are active.
- license choice and whether code and documentation need different licenses.
- large binary or generated artifact handling.

Record commit, push, merge, administration, visibility, and history-rewrite authority in
project_profile.yaml under `authority:` (the machine-checked record), mirrored for human reading in
AGENTS.md Team facts. Record repository mode, provider, template source, ignore policy, license,
and initial checkpoint in project_profile.yaml under `version_control:`, mirrored in
PROJECT_WORKFLOW.md Project facts. When a mirror and the profile disagree, report the discrepancy;
do not silently choose one side.

Git history is not a substitute for database backup, artifact retention, or disaster recovery.

### 4.8 Initial repository checkpoint

Create the first project commit only after the approved initialization files have been materialized
and validated. Record:

- the template source and version.
- the approved structure and active governance sections.
- the first permanent work ID.
- validation evidence and unresolved limitations.

Do not push the initial commit unless remote creation or use and push authority were explicitly
approved.
