# Working in separate checkouts

A branch names a line of development. A worktree gives it a separate directory of files.
Linked worktrees share Git history and branch references, but have their own files, index and
HEAD. Their `.git` entry is a file pointing to private metadata. A clone is also suitable when
separate Git administration is needed. Neither arrangement is a security sandbox (WK-6).

Use separate checkouts for concurrent writers. A test-writing session followed by a fresh
implementation session may reuse one checkout sequentially. A read-only review can read that
checkout only while its author is idle; otherwise review a fixed revision in another checkout.

## 1. Prepare

- Inspect `git status --short`, the current branch, and `git worktree list --porcelain`.
  Preserve existing work; never automatically reset, stash or overwrite it.
- Record task, checkout path, branch and base commit in the plan. Allocate a short unique
  checkout ID for resource names; sanitized branch names alone can collide.
- Use an existing task branch or create one before writing. Do not write on the protected
  branch. Before a baseline commit exists, work sequentially in the initial checkout;
  never create a commit without authorization just to enable parallel work.
- Choose a destination inside the session's permitted workspace. If the usual sibling
  directory is outside it, choose an allowed location; never bypass filesystem restrictions.

## 2. Create

After a baseline commit exists, a typical command from the repository is:

```bash
git worktree add -b task/search ../project-worktrees/search HEAD
```

Choose the branch, path and base for the actual task. Keep Git's safeguard against checking
out the same branch twice: do not use `--force` or reset an existing branch with `-B`.
Creation does not copy uncommitted or ignored files from another checkout.

## 3. Bootstrap and verify

Run the stack profile's rerunnable bootstrap in the new checkout. Install from the lock file;
provision ignored configuration and scoped development credentials explicitly. Never copy
production credentials or assume another checkout's `.env` is present.

| Resource | Arrangement |
|---|---|
| Check state | Private Git directory of each checkout |
| Development and test databases | Names derived from the unique checkout ID |
| Ports, queues, storage and external test namespaces | Separate where concurrent use conflicts |
| Dependencies and generated output | Installed or generated inside the checkout by default |
| Credentials | Scoped development credentials, never production secrets |
| Git history and branches | Shared; coordinate repository-wide operations |

The stack profile supplies the actual configuration keys and commands. Record allocated
resources in the plan. A database address alone does not isolate a shared queue or file bucket.

Discover paths with `git rev-parse --show-toplevel` and `git rev-parse --absolute-git-dir`;
never assume `.git` is a directory. Put hook state in that private Git directory, not the
shared common directory. Verify the tool-specific settings and hook in each checkout with a
failing check, then restore the real command and verify success. Unsupported guardrails are
reported as gaps; copying Claude settings does not enforce them in another agent.

The stop-hook cache covers tracked changes, untracked files and the resolved check command.
Ignored configuration and external resources are outside it: delete `agent-stop-check` from
the discovered private Git directory after changing them, or run the full check explicitly.
Before the first commit the hook does not cache success. A cached success is never a
substitute for the independent committed-state check before merge (CK-8).

## 4. Work and hand off

- Keep each writer in its assigned checkout and update its plan there.
- Name the exact commit or preserved patch and base commit in every handoff. A patch must
  include new files as well as tracked edits, exclude secrets, and survive checkout cleanup.
  Uncommitted tests do not appear in another worktree automatically.
- Commits, pushes, merges and destructive operations still follow the project's authorization
  rules. Worktree creation grants no extra authority.
- Do not run branch resets, history rewrites or repository cleanup that disrupt another task.

## 5. Integrate

Use the project's authorized review and integration workflow. Verify that the tested revision
is the revision handed off. After combining changes, run the full check again on the combined
result, including migrations and shared contracts. Two separately green branches may conflict.
Record the integrated revision and check result before reporting integration complete.

## 6. Clean up

Confirm the handoff survives elsewhere and inspect tracked, untracked and ignored files.
Ignored `.env`, local artifacts and evidence can be valuable even in a clean checkout.
Stop this checkout's processes and release only its own database, queues and other resources,
using the stack profile's cleanup commands and the project's authorization rules.

Use `git worktree remove <path>` without force. If it refuses or valuable ignored files remain,
preserve the work and report what remains. Do not force removal, recursively delete the
checkout, or delete its branch by default. Recheck `git worktree list --porcelain` afterward.

## References

- [Git worktree documentation](https://git-scm.com/docs/git-worktree)
- [Git repository path discovery](https://git-scm.com/docs/git-rev-parse)
