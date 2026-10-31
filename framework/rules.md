# Rules

Every rule has an ID, the rule, and how `assess` checks it. The published work it was
checked against is in `validation.md`.

A rule states the **property**, never the tool. "The build fails when an entry point declares no
access rule" holds in any stack; how a stack makes it fail lives in its profile (`profiles/`).

Words: **must** is required at the rung the rule belongs to; **should** is the default, and a
project that departs from it says why in an ADR.

## IN: Instructions (rung 1)

| ID | Rule | Check |
|---|---|---|
| IN-1 | One instructions file is the source for every agent: `AGENTS.md`. Tool-specific files (`CLAUDE.md`, Cursor rules) only point to it. | `AGENTS.md` exists and other agent files point to it. A single tool-specific file that is the only source (a lone `CLAUDE.md`) is partly met: one tool reads it, others do not |
| IN-2 | It holds only what an agent cannot find by reading the repo, or would have to dig for every session: commands, decisions not in code, misleading code, anything corrected twice. No tour of directories the agent can list itself, no history; a short map pointing into `docs/` is fine. | Read it: flag directory tours, dated history, restated code |
| IN-3 | Root file under 200 lines, nested files under 150, enforced by the check. | Line counts. Any file over budget is not met. Within budget but not yet enforced (no check exists) is partly met |
| IN-4 | Rules for one area live in that area (nested `AGENTS.md` or path-scoped rules) so they load only there. | Nested files where areas differ |
| IN-5 | Every claim is true now. File paths and commands it names must exist, and the check verifies that. | Run the named commands; resolve the named paths |
| IN-6 | Plain statements, no IMPORTANT or ALL CAPS: emphasis makes agents over-apply a rule. | Grep for shouting |
| IN-7 | Repeated procedures are skills or playbooks, loaded when used, not paragraphs in `AGENTS.md`. | `skills/` or `docs/agents/` exists for repeated work |

## CK: Checks (rung 2, and rung 6 for architecture)

| ID | Rule | Check |
|---|---|---|
| CK-1 | One command runs every check (format, lint, types, tests, architecture). CI runs the same command. | Find it; run it; compare with CI. CI listing the same steps separately is fine; CI running steps the command lacks (or the reverse) is partly met. Whether it runs independently is CK-8 |
| CK-2 | The check command is in the first section of `AGENTS.md`, where an agent reads it before anything else. Until a check exists, that section says so. | Look. Named but later in the file is partly met |
| CK-3 | Deterministic checks first; AI review is extra, never a substitute. | Count computational vs inferential checks |
| CK-4 | Error messages say how to fix the problem, because the agent reads them. | Read custom check messages |
| CK-5 | A rule that exists only as prose is a check not yet written. When a review comment recurs, it becomes a lint rule, structural test, type, hook or skill. | Prose rules in `AGENTS.md` that could be mechanical |
| CK-6 | Fast checks run on every edit or commit; slow ones in CI. | Hooks and pre-commit present |
| CK-7 | Keep enforcement small. Preferences stay prose; only must-always and must-never rules are enforced. | Count hooks and deny rules; flag preferences enforced as rules |
| CK-8 | Before a change merges, the check runs independently of the author's working tree: from committed state, in a clean environment, with nothing from the author's machine but the address of a test database. This catches the forgotten file, the dependency missing from the lock file and the test that passes only on local data. CI with branch protection is the standard mechanism, and the only one that also gates the merge for every tool. | Met: CI runs the check on every change and a red run blocks the merge. Partly met: CI runs but does not block, or a clean-clone script runs the check from committed state but nothing makes it run before a merge. Not met: only the author's working tree is ever checked |

## GR: Guardrails (rung 3)

| ID | Rule | Check |
|---|---|---|
| GR-1 | No production secret is within the agent's reach. Production credentials live outside the repository and the agent's environment; sessions use none, or test or scoped development credentials. Deny rules on secret files are a useful extra, not the control: a shell can always find another way to print a file. | Not met: credentials that reach production systems (read or write) sit in files or environment the agent can read, or a script copies production data with secrets into the working tree. Partly met: no production secrets, but development secrets are protected only by deny rules. If secret files may not be read, judge from `.env.example` (including its comments on which sources need no secret), docs and scripts, say so, and never infer a secret from a placeholder alone. Production reachable with no credential at all (a database open to the network) is outside the repository's control: it does not fail GR-1, and the report notes it as an outside risk, with any rule that limits ad-hoc queries against it |
| GR-2 | Commit, push, deploy and migrate ask a human. The agent never merges to the protected branch. | Committed agent settings (none committed is not met); branch protection is not verifiable from the repo |
| GR-3 | Every change happens on a branch or worktree; the main branch takes reviewed merges only. | History shows merges into the main branch. A fork's own main branch used as the working branch is partly met |
| GR-4 | The agent cannot report a task finished while the check is red (a stop hook or equivalent). | Hook present and blocking. Releasing after one block so the agent reports the failure, rather than looping, is met |
| GR-5 | An unattended run answers five questions first: what done looks like, how it checks itself, what it may touch, what stops it, who signs off. It runs sandboxed. | Look at scheduled or headless runs |
| GR-6 | Scripts that change data are dry-run unless told to apply. | Read data scripts |

## SK: Walking skeleton (rung 4)

| ID | Rule | Check |
|---|---|---|
| SK-1 | One rerunnable command takes a fresh clone to a running app; a second reports what is wrong and how to fix it. | Run it on a clean clone |
| SK-2 | One end-to-end test exists from the first commit and runs in CI. | Find it |
| SK-3 | The stack is boring, typed and well known; small helpers are written rather than imported from opaque libraries. | Read the dependency list |
| SK-4 | Configuration comes from the environment; no hard-coded paths or hosts. | Grep for absolute paths and hosts |

## TS: Tests and acceptance (rung 5)

| ID | Rule | Check |
|---|---|---|
| TS-1 | A feature's acceptance criteria are written before its code, sized to the change (see `spec`). | Specs exist for every feature since the workflow was adopted and predate its code. Features from before adoption do not count against it |
| TS-2 | Tests are written first and seen to fail (red/green). | Separate test commits before implementation commits, or a workflow that requires it. Tests always arriving in the same commit as the code is not met |
| TS-3 | The session that writes acceptance tests is not the session that makes them pass. | Workflow or playbook says so |
| TS-4 | A failing test is fixed or reported, never skipped, weakened or deleted to get green. | `AGENTS.md` says so; grep for new skips |
| TS-5 | User-facing behaviour is checked end to end, and "done" comes with evidence: the command and its output, or a screenshot. | PR template or definition of done |
| TS-6 | The agent marks what it does not know (`[NEEDS CLARIFICATION]`) instead of guessing, and the marks are resolved before planning. | Spec template |
| TS-7 | Acceptance tests pass the project's own lint and type checks before they are handed to implementation, so the only failures are the intended ones. | Run the check on the tests-only change: everything passes except the new acceptance tests |

## AR: Architecture (rung 6)

| ID | Rule | Check |
|---|---|---|
| AR-1 | Default deny: every entry point (page, API, tool, job) declares who may use it, and the build fails when one does not. | Add an undeclared entry point; does the check fail? |
| AR-2 | Each concept is declared once, and everything else (navigation, routing, permissions, docs) is derived from that declaration. | Pick a concept; count where it is spelled out |
| AR-3 | Modules talk only through public read and write interfaces; the boundary is checked. Any consistent structure qualifies; what matters is that a check enforces it. | Architecture contract in the check. A consistent convention with no check is partly met |
| AR-4 | Every write goes through one layer that validates, records who did it, and keeps history. The layer's name and shape are the project's choice. | Look for writes outside that layer |
| AR-5 | Outside systems are reached from one place, read-only unless a decision says otherwise, and never waited on during a request. | Grep for outside clients outside that place |
| AR-6 | Data is parsed and validated at the boundary, not trusted inside. | Read entry points |

## WK: Work (rungs 4–5)

| ID | Rule | Check |
|---|---|---|
| WK-1 | Small changes, one logical change each; structural changes separate from behaviour changes. | Count changed lines excluding migrations, lock files, translation catalogues, changelogs and vendored or generated files; templates and docs count. Over about 400 is large, over 1,000 a finding. Mostly small is met |
| WK-2 | Non-trivial work has a checked-in plan with progress notes, so the next session can resume from the repo, not from chat. | `docs/plans/` or equivalent |
| WK-3 | Plan in one session, implement in a fresh one. Clear context between unrelated tasks. | Playbooks say so |
| WK-4 | Each change carries a changelog entry written as it is made. | Fragments or entries per change |
| WK-5 | The definition of done is written down and includes evidence. | In `AGENTS.md` |
| WK-6 | Agent sessions working in parallel each have their own worktree or clone and their own test database. Two writers never share a checkout: one session's intended red tests block the other's stop hook, and shared test databases make runs fail at random. | How parallel sessions are started; whether test database names differ per worktree |

## DC: Decisions (rung 7)

| ID | Rule | Check |
|---|---|---|
| DC-1 | ADRs record hard-to-reverse decisions only; detailed designs are specs. | ADR sizes and count |
| DC-2 | Status is Proposed, Validated (exercised, with evidence), Accepted, Rejected, or Superseded by NNNN. Each Validated or Rejected ADR has an evidence line. | Status and evidence present |
| DC-3 | An Accepted ADR is frozen; a later ADR amends or supersedes it. | History of accepted files |
| DC-4 | The people who will own the system accept its ADRs, not only their author. | Deciders line |
| DC-5 | System-wide quality requirements are recorded as measurable scenarios with stable IDs (`QS-n`). ADRs cite the scenarios they serve; specs cite the ones they touch and exercise each with a criterion. A scenario's measure names the spec whose tests prove it, and its status changes only when those tests pass. | A scenario list exists; ADR Contexts and specs cite it; every "Met" points at passing tests |

## RV: Review (rungs 3 and 6)

| ID | Rule | Check |
|---|---|---|
| RV-1 | A human reads every change before it merges and can explain it. | Merges through pull requests with a reviewer other than the author, where the host shows it; otherwise not verifiable |
| RV-2 | Agent review runs in a fresh context, works back from the acceptance criteria, and skips style (the formatter owns style). | Review playbook |
| RV-3 | The code is zoned green, yellow or red by how much damage a change could do. Autonomy and review depth follow the zone, not the model's confidence. | A zone map exists |
| RV-4 | A bad diff is not quietly fixed by hand: fix the guide or sensor that let it through, or the next session repeats it. | Ask; look at sensor history |
| RV-5 | Not every review finding is acted on; findings about impossible cases are declined. | Ask |

## MS: Measure and garden (rung 8)

| ID | Rule | Check |
|---|---|---|
| MS-1 | Track lead time, human interventions, first-pass CI rate, rework, escaped defects and rollbacks. Never lines generated. | A log or dashboard exists |
| MS-2 | A scheduled pass finds stale docs and drift and opens small fixes. | Schedule or routine exists |
| MS-3 | Instructions are re-checked when models change; rules a newer model no longer needs are removed. | Last review date |

## OP: Operate (levels O1 to O3, when agents use the built system)

| ID | Rule | Check |
|---|---|---|
| OP-1 | Each action is declared once and served to the UI, the API and agent tools with the same access rules. | Compare a UI action and its API/tool twin |
| OP-2 | Agent and machine access is read-only until a person issues a write-capable credential, scoped to the actions it needs. | Token defaults |
| OP-3 | Every write records who acted and through which channel (web, API, agent). | History rows |
| OP-4 | Writes accept a request ID, and a repeat changes nothing. | Send one twice |
| OP-5 | Credentials travel in headers, never in URLs. | Grep routes and docs |
| OP-6 | Text that came from data (notes, comments, outside systems) is untrusted when it reaches an agent; tools that act on it are scoped accordingly. | Threat noted in an ADR |
| OP-7 | People and agents design definitions (forms, screens, labels), never code. Agents may draft; a person publishes. | Publish permission |
| OP-8 | Calls the system makes to outside systems on an agent's behalf are bounded: a request budget per source, shared reads cached once for everyone, no retry storms. An agent looping on a tool must not become load on a system the project does not own. | A budget and a cache for each outside source an agent can reach through the system |
