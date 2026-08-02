# WF-VCS — Version control
<!-- AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

AIPartner framework workflow module. Module ID: `WF-VCS` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Core module: always active in every project.
- Sole normative owner of: version-control rules, the Git complexity ladder, and branch activation/retirement discipline

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-VCS: Version control

Use the Git tailoring guidance in
[framework/structure/git-reference.md](../structure/git-reference.md) to select and record the
repository mode. Local Git is the normal software-project default; remote hosting and branch complexity require
their own evidence and approval.

- Inspect repository state before changing files or Git configuration.
- Preserve existing history, user work, remotes, and unrelated changes.
- Never remove .git, rewrite shared history, force-push, or discard work without explicit authority.
- Keep commits small, coherent, verified, and traceable to permanent work IDs.
- Inspect status and intended diffs before and after commits, merges, and integration.
- Keep secrets, production data, runtime output, caches, reports, and backups out of commits unless
  an explicit evidence policy says otherwise.
- Activate branches, pull requests, worktrees, protection, and integration rules only when review,
  concurrency, release isolation, or baseline stability requires them.
- Treat remote creation, visibility changes, pushes, publication, and administrative changes as
  external actions requiring user approval.

The initial project commit follows successful initialization validation. Git history does not
replace data backup, artifact retention, or recovery testing.

### Complexity ladder

Use the least complex Git mode supported by current evidence:

| Condition | Normal mode |
|---|---|
| One writer and no protected production baseline | Small verified commits on the default branch |
| Independent review or a protected remote baseline | Short-lived branch and pull request |
| Concurrent writers | One branch or worktree per writer and one integration owner |
| Stable production baseline plus long-running next release | Default baseline plus one integration branch |

A branch isolates code; it is not the source of work-item status, phase ownership, or completed-work
truth. Do not encode mutable phase, priority, status, or assignee in permanent work IDs.

Record an activation condition and a retirement condition for every non-default branch model. When
the condition disappears, preserve necessary historical receipts, retire the topology deliberately,
and remove obsolete branch commands and merge sources from live governance documents. Historical
documents may retain them as history.

When the default branch is also a production worktree, inspect related schedules and running
processes before editing runtime-sensitive files. Verify schema and runtime changes with temporary
data, synthetic fixtures, regression checks, and deployment preflight before a scheduler or service
can observe the new version. Do not stage, overwrite, or clean runtime state merely to prepare a
code commit.

If Git is deliberately deferred, Project facts and project_profile.yaml must record the reason,
risk, approval evidence, and activation trigger. The rest of this section remains in force.
