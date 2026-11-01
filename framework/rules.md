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
| IN-1 | Root `AGENTS.md` is the shared project-policy authority; scoped additions refine relevant areas without silently conflicting. Tool-specific files point to shared guidance. Effective instruction discovery preserves the intended policy. | Inspect root/nested/override sources, precedence and loading limits in each selected host. File presence alone is insufficient; a lone tool-specific source is partly met |
| IN-2 | It holds only what an agent cannot find by reading the repo, or would have to dig for every session: commands, decisions not in code, misleading code, anything corrected twice. No tour of directories the agent can list itself, no history; a short map pointing into `docs/` is fine. | Read it: flag directory tours, dated history, restated code |
| IN-3 | Root file under 200 lines, nested files under 150, enforced by the check. | Line counts. Any file over budget is not met. Within budget but not yet enforced (no check exists) is partly met |
| IN-4 | Area-specific rules load only in that area. A short navigation path leads a maintainer to its purpose, public interfaces, permitted dependencies and test command. Local guidance fills gaps the code cannot explain. | Follow the navigation without the author's chat; inspect scoped retrieval routes to contracts/callers/tests and nested guidance where areas differ |
| IN-5 | Maintained instructions, documentation links, configuration examples and executable examples agree with the current system. Named paths and commands resolve; mechanically verifiable claims run in the check. | Resolve maintained references against actual revision/dirty state and exercise commands/examples; distinguish current authority, superseded decisions and historical records |
| IN-6 | Plain statements, no IMPORTANT or ALL CAPS: emphasis makes agents over-apply a rule. | Grep for shouting |
| IN-7 | Repeated procedures are skills or playbooks, loaded when used, not paragraphs in `AGENTS.md`. | `skills/` or `docs/agents/` exists for repeated work |
| IN-8 | Evidence used for decisions preserves provenance, freshness and sufficient interpretive context. Missing, stale, inaccessible or truncated coverage remains explicit; retrieved data cannot grant authority. | Inspect source/revision and enclosing constraints, query/index scope, missing ranges and facts versus inferences. Reported practice, not a gate; search rank or no hits alone proves no completeness |

## CK: Checks (rung 2, and rung 6 for architecture)

| ID | Rule | Check |
|---|---|---|
| CK-1 | One command runs every applicable check (format, lint, types, tests, architecture, maintainability and security). CI runs the same command. | Find it; run it; compare with CI. Missing steps on either side is partly met. Unavailable security checks stay visible as failures or gaps, never a clean result. Independent execution is CK-8 |
| CK-2 | The check command is in the first section of `AGENTS.md`, where an agent reads it before anything else. Until a check exists, that section says so. | Look. Named but later in the file is partly met |
| CK-3 | Deterministic checks first; AI review is extra, never a substitute. | Count computational vs inferential checks |
| CK-4 | Error messages say how to fix the problem, because the agent reads them. | Read custom check messages |
| CK-5 | A rule that exists only as prose is a check not yet written. When a review comment recurs, it becomes a lint rule, structural test, type, hook or skill. | Prose rules in `AGENTS.md` that could be mechanical |
| CK-6 | Editor and pre-commit integrations provide fast feedback using the project's configuration; CI independently checks the complete declared scope. Slow checks remain in the full check and CI. | Compare integration configuration, versions and coverage with the full check; local hooks alone are insufficient |
| CK-7 | Keep enforcement small. A project-selected style may be enforced as one coherent pipeline; do not create separate hooks for individual preferences. Other preferences stay prose unless adopted as required properties. | Inspect hook purpose, overlapping checks and the project's declared conventions |
| CK-8 | Before a change merges, the check runs independently of the author's working tree: from committed state, in a clean environment, with nothing from the author's machine but the address of a test database. This catches the forgotten file, the dependency missing from the lock file and the test that passes only on local data. CI with branch protection is the standard mechanism, and the only one that also gates the merge for every tool. | Met: CI runs the check on every change and a red run blocks the merge. Partly met: CI runs but does not block, or a clean-clone script runs the check from committed state but nothing makes it run before a merge. Not met: only the author's working tree is ever checked |

## ST: Style (rung 2)

| ID | Rule | Check |
|---|---|---|
| ST-1 | Each language the project maintains has one formatter and linter, with committed configuration and pinned versions. The check reports violations without rewriting files; a separate command fixes them. The project's existing choices govern; a new project uses its ecosystem's standard tools. | Add a deliberate violation: the check fails and the file is unchanged; the fix command repairs it; a second run changes nothing. Configured but not in the check or CI is partly met |

## AP: Traceable human approval (rungs 3, 5 and 7)

Evidence, validity and proportionality are in [approvals.md](approvals.md).

| ID | Rule | Check |
|---|---|---|
| AP-1 | Required approval identifies the subject and reviewed revision, human reviewer/authority, decision/time, scope, conditions and original source evidence. Mutable paths or status labels alone are insufficient. | Resolve the reviewed subject and original decision; preserve snapshots or immutable host revisions outside the subject |
| AP-2 | Agents may prepare/index decision records but cannot manufacture consent or satisfy required human review themselves. Reviewer authority and decision provenance are verified through trusted sources. | Compare the record with its human source and reviewer policy; missing or unverifiable provenance stays explicit, never inferred from filled fields |
| AP-3 | Reuse valid approval within its authorized scope until revoked, superseded or invalidated by relevant changes. Material changes renew affected approvals; unrelated changes do not. Conditions and expiry still apply. | Check subject/dependency freshness, required review policy and conditions before dependent work; preserve historical decisions and record permitted nonmaterial transitions |
| AP-4 | Approved requirements trace to criteria, tests, implementation and verification evidence. Missing coverage and out-of-scope behavior are resolved before acceptance; records are sized to the change. | Follow stable requirement/criterion IDs through actual tests, reviewed revision and results; a small fix can use its issue/plan/PR rather than new documents |

## GR: Guardrails (rung 3)

| ID | Rule | Check |
|---|---|---|
| GR-1 | Development agents cannot reach production secrets or sensitive production data; use test credentials and synthetic or reviewed sanitized data. File deny rules are supplementary, not the security boundary. | Not met: reachable production credentials or sensitive data in files, environment or copied data. Development secrets protected only by deny rules is partly met. Judge restricted files from examples, docs and scripts without reading them; never infer a secret from a placeholder. Credential-free production exposure is a separate SE-1/SE-4 finding, never evidence of readiness |
| GR-2 | Commit, push, deploy and migrate require human authorization. The agent never merges to the protected branch. Changes that weaken security checks, CI gates, permissions, deployment or approval policy require explicit human review of the change. | Committed agent settings (none committed is not met), reviewed policy diffs and scoped authorizations; host protection requires external evidence |
| GR-3 | Every change happens on a branch or worktree; the main branch takes reviewed merges only. | History shows merges into the main branch. A fork's own main branch used as the working branch is partly met |
| GR-4 | Completion controls require the applicable check before a success claim and expose failures. A bounded escape permits honest failure reporting, not a success claim. | Exercise effective host loading, trust and failure continuation/blocking; configuration or instructions alone are insufficient. Reporting escape after one block is met; skipped/unsupported controls are gaps. CI merge gating is separate |
| GR-5 | An unattended run answers five questions first: what done looks like, how it checks itself, what it may touch, what stops it, who signs off. It runs sandboxed. | Look at scheduled or headless runs |
| GR-6 | Scripts that change data are dry-run unless told to apply. | Read data scripts |

## SK: Walking skeleton (rung 4)

| ID | Rule | Check |
|---|---|---|
| SK-1 | One rerunnable command takes a fresh clone to a running app; a second reports what is wrong and how to fix it. | Run it on a clean clone |
| SK-2 | One end-to-end test exists from the first commit and runs in CI. | Find it |
| SK-3 | Prefer established stack capabilities and existing project implementations. New dependencies and custom replacements serve a demonstrated requirement with a maintenance justification; neither hand-written code nor a dependency is automatically preferable. | Inspect new capabilities, alternatives considered and maintenance costs in the plan or review; use an ADR only for a hard-to-reverse choice |
| SK-4 | Configuration comes from the environment; no hard-coded paths or hosts. | Grep for absolute paths and hosts |

## TS: Tests and acceptance (rungs 2, 4 and 5)

Interpretation, evidence and staged handoffs are in [testing.md](testing.md).

| ID | Rule | Check |
|---|---|---|
| TS-1 | A feature's criteria are agreed before code, sized to the change; their approval identifies scope and reviewed content. | Specs or small-change plan/PR criteria predate code and resolve to valid human approval; pre-adoption features do not count against it |
| TS-2 | New or changed behavior follows witnessed red/green/refactor: tests fail for the intended gap before implementation, pass afterward, then structure is inspected and refactored where justified without changing behavior. | Retain command, pre-change revision or preserved patch, failure diagnostic and green result; record refactor disposition. Commit order alone proves no execution |
| TS-3 | Acceptance tests are derived from agreed criteria in a context separate from implementation. Implementers may add supporting unit tests. | Handoff identifies criteria, tests and red evidence; no separate context is required for every helper test |
| TS-4 | Failures remain visible and are fixed or reported, never hidden by weakening, skipping or deleting tests to get green. Legitimate test corrections preserve intended protection and receive appropriate review. | Explain changed assertions/fixtures; changed acceptance outcomes require criteria review and affected approval, not matching tests to faulty code |
| TS-5 | Representative user journeys are checked end to end; lower-level tests cover detailed cases at effective boundaries. Done includes execution evidence and appropriate UI evidence. | Trace journeys and edge cases to tests; screenshots supplement rather than replace automated behavioral assertions |
| TS-6 | The agent marks what it does not know (`[NEEDS CLARIFICATION]`) instead of guessing, and the marks are resolved before planning. | Spec template |
| TS-7 | Test handoff passes applicable independent validity checks; remaining failures identify the intended missing behavior or planned public interface. | Preserve lint, fixture and setup results; a specific expected missing-interface compiler diagnostic can be red, unrelated syntax, dependency or environment failures cannot |
| TS-8 | Tests assert observable outcomes, public contracts and relevant effects using requirements or an independent oracle, rather than copying implementation logic. | Inspect expected values and boundaries; internal refactors should preserve acceptance outcomes. Interaction assertions require a real protocol contract |
| TS-9 | Bug fixes retain regression protection that reproduces the affected pre-fix behavior before the fix. | Record pre-fix failure and post-fix pass; explain reproduction limits. Applies to bug fixes after adoption, not invented historical evidence |
| TS-10 | Tests isolate mutable resources and control relevant nondeterminism. Flaky failures remain visible with owned remediation. | Exercise isolation, clocks/seeds/order and cleanup as applicable; report retries and time-limited reviewed quarantine without silently redefining failures as success |
| TS-11 | Verification covers important component contracts and real integration at the lowest effective level, plus representative end-to-end journeys. | Name simulated and actual boundaries; mocks alone do not prove compatibility. Use safe external substitutes with contract evidence where live access is unsuitable |
| TS-12 | Execution evidence identifies revision, command, environment, discovered/executed scope, failures, skips and exclusions. Missing or unexpectedly reduced discovery is not a clean pass. | Inspect actual exit/results and selected targets, features and platforms; explain counts and scope changes, including intentional empty scopes |
| TS-13 | Selected critical behavior is checked for test sensitivity by deliberate wrong behavior in isolation. This is a practice pending trials, not a rung gate. | Record detected faults, survivors, limits and justified exclusions; invalid compilation is not behavioral detection. No universal mutation or coverage quota |

## AR: Architecture (rung 6)

| ID | Rule | Check |
|---|---|---|
| AR-1 | Default deny: every entry point (page, API, tool, job) declares access and the build fails when one does not. Effective authorization enforces applicable object and tenant boundaries on every path, not merely login or a declaration. | Add an undeclared entry point; test direct requests, alternate adapters and cross-object/tenant attempts for refusal without prohibited effects or disclosure |
| AR-2 | Each concept and business rule has an authoritative declaration or implementation; dependent representations derive from it where practical. Independent copies need an explicit reason. Similar code is not automatically the same concept. | Trace a changed rule to its authority; inspect duplicate findings and dispositions, including whether copies must change together |
| AR-3 | Cohesive modules communicate through declared public interfaces and permitted dependency directions. The check enforces boundaries and rejects undeclared cycles; any consistent structure qualifies. | Architecture contract in the check; review responsibilities and public interfaces. A consistent convention with no check is partly met |
| AR-4 | Every write goes through one layer that validates, records who did it, and keeps history. The layer's name and shape are the project's choice. | Look for writes outside that layer |
| AR-5 | Outside systems are reached from one place, read-only unless a decision says otherwise, and never waited on during a request. | Grep for outside clients outside that place |
| AR-6 | Data is parsed and validated at boundaries and safely interpreted or encoded for each destination. Validation alone never makes data safe as a query, command, path or rendered output. | Inspect input-to-sink paths and test applicable injection, traversal and unsafe-output cases |

## SE: Security baseline (rungs 2 to 5; verified again before production)

Scope, exceptions and production readiness are in [security.md](security.md).

| ID | Rule | Check |
|---|---|---|
| SE-1 | Identify sensitive assets, actors, trust boundaries and credible abuse cases. Select applicable security requirements from versioned standards and justify exclusions; revisit when exposure or behavior changes. | Review threat model, applicability and requirement-to-control mapping against actual interfaces and data |
| SE-2 | Applicable automated security checks run in the project check and CI. Findings have explicit dispositions; missing, failed, incomplete or stale checks are never reported as clean. | Exercise representative detections; inspect coverage, exclusions, tool/feed freshness and finding dispositions |
| SE-3 | Dependencies originate from verified intended sources, are reproducibly resolved and receive vulnerability review. New dependencies and build-time execution are reviewed before introduction. | Verify identity, sources, resolution and integrity evidence, install/build behavior and clean-build results; include transitive and build dependencies |
| SE-4 | Runtime defaults enforce least privilege, safe configuration and appropriate protection of sensitive data. Production readiness requires current evidence of applicable controls in the target environment. | Test effective behavior and configuration; distinguish local checks, deployment-shaped tests and verified deployment evidence |
| SE-5 | Security-affecting changes have acceptance tests for relevant abuse and refusal paths, proving unauthorized attempts cause no prohibited effect or disclosure. | Trace security requirements to criteria, tests and results; exercise bypasses and alternate entry points as well as the intended interface |
| SE-6 | Findings have an owner, risk-based response deadline and tracked resolution. Human-approved risk acceptance is scoped and time-limited. Suspected exposure follows a response procedure. | Review deadlines, expired exceptions, remediation verification and a safe response exercise appropriate to the project |

## MT: Maintainability (rungs 2, 4 and 6)

Interpretation, exceptions and adoption are in [maintainability.md](maintainability.md).

| ID | Rule | Check |
|---|---|---|
| MT-1 | Public interfaces document purpose, inputs, outputs, failures and side effects where declarations do not make them evident. Non-obvious constraints and workarounds explain why. Documentation changes with behavior. | Check presence where practical; review accuracy against implementation and tests. A boilerplate docstring alone is not evidence |
| MT-2 | The project defines enforceable complexity limits and review thresholds appropriate to its stack. Changes introduce no unapproved violations or worsen existing ones. Exceptions identify scope, reason, reviewer and review condition. | Exercise limits in the check; inspect changed code, review-trigger dispositions and scoped exceptions against the adoption baseline |
| MT-3 | A change removes code, dependencies, configuration and documentation it makes obsolete, or records why they remain and when retention will be reviewed. Uncertain usage is investigated before removal. | Trace replaced execution paths; inspect reference and unused-code reports and retention decisions. Dynamic registration and compatibility paths need evidence, not automatic deletion |
| MT-4 | Structural changes identify the maintenance problem, affected contracts and preservation evidence. Behavior changes are separated or explicitly specified and approved. Unverified compatibility remains a reported gap. | Inspect baseline results, relevant tests, consumer analysis and final verification. A practice pending application trials, not a rung gate; passing tests establish only exercised scope |
| MT-5 | Confirmed actionable debt has concrete evidence/consequences, an owner, disposition and review condition; deferral uses applicable authority and closure verifies stated outcomes while preserving identity/history. | Inspect canonical records, candidates versus confirmed items, linked exceptions, actual decisions and resolution evidence. A reported practice pending trials, not a gate; recording debt grants no waiver or acceptance |

## WK: Work (rungs 4–5)

| ID | Rule | Check |
|---|---|---|
| WK-1 | Small changes, one logical change each; structural changes separate from behaviour changes. | Count changed lines excluding migrations, lock files, translation catalogues, changelogs and vendored or generated files; templates and docs count. Over about 400 is large, over 1,000 a finding. Mostly small is met |
| WK-2 | Non-trivial work has a checked-in plan with progress notes, so the next session can resume from the repo, not from chat. | `docs/plans/` or equivalent |
| WK-3 | Planning and implementation use separate contexts with an exact artifact handoff. Unrelated work does not inherit stale assumptions. | Inspect actual handoff and input boundaries; compaction or a mode switch alone is not fresh context. Sequential separate chats can reuse a checkout; no subagent mechanism is required |
| WK-4 | Each change carries a changelog entry written as it is made. | Fragments or entries per change |
| WK-5 | The definition of done is written down and includes evidence. | In `AGENTS.md` |
| WK-6 | Concurrent writers have separate checkouts and isolated mutable resources (databases, ports, queues and storage where applicable). Check state is private to each checkout. Sequential contexts may reuse one. Handoffs identify an exact revision or preserved patch; combined changes are checked again. | Exercise two checkouts: hooks and resources are independent; inspect handoff and integration evidence. See the worktree playbook |
| WK-7 | When optional model routing is used, role/model/host/effort selections, eligibility, bounds and fallbacks are traceable. Quality, independent contexts and existing authorization remain intact. | Inspect proposed versus actual assignments, access/data scope, effort support, budget sources and exact handoffs. Conditional practice, not a gate; one model in separate contexts remains sufficient |
| WK-8 | Long-running work can recover approved scope, critical contracts and actual verification state from durable artifacts after interruption or context changes. | Reconstruct from source-linked working state; distinguish decisions, hypotheses, prior results and fresh checks. Verify material changes and valid approval without invented history. Reported practice, not a gate |

## DC: Decisions (rung 7)

| ID | Rule | Check |
|---|---|---|
| DC-1 | ADRs record hard-to-reverse decisions only; detailed designs are specs. | ADR sizes and count |
| DC-2 | Status is Proposed, Validated (exercised, with evidence), Accepted, Rejected, or Superseded by NNNN. Each new ADR links its append-only record in `docs/evidence/` before acceptance; migrated frozen ADRs use `docs/evidence/index.md`. Validated or Rejected requires evidence there. | Direct or indexed link resolves; entries identify tests or reasoning, revision, results and limits |
| DC-3 | An Accepted ADR is frozen except Status and Topics; a later ADR amends or supersedes it. Later evidence appends to its separate record and never downgrades it to Validated. Contradictions trigger owner review. | History of accepted files and evidence records |
| DC-4 | The people who will own the system accept its ADRs, not only their author. Acceptance references their actual decision for the reviewed content; a Deciders line alone is not consent. | Verify the owner approval source, authority, revision and requested transition; use external records/indexes without rewriting frozen ADRs |
| DC-5 | System-wide quality requirements are recorded as measurable scenarios with stable IDs (`QS-n`). ADRs cite the scenarios they serve; specs cite the ones they touch and exercise each with a criterion. A scenario's measure names the spec whose tests prove it, and its status changes only when those tests pass. | A scenario list exists; ADR Contexts and specs cite it; every "Met" points at passing tests |

## RV: Review (rungs 3 and 6)

| ID | Rule | Check |
|---|---|---|
| RV-1 | A human reads every change before merge and can explain it; implementation review identifies the actual change and remains valid under the project's freshness policy. | Verify review source and revision, reviewer other than author where required, latest relevant changes and host enforcement; external evidence unavailable is not a proven review |
| RV-2 | Agent review runs in a fresh context and works back from acceptance criteria. Automation owns enforced layout; naming, interface clarity and documentation meaning still receive review where tools cannot judge them. | Review playbook and findings distinguish automated layout from semantic conventions |
| RV-3 | Code, policy, tests and tooling are zoned by damage and reversibility. Security policy, security tests, CI enforcement, permissions and approval mechanisms receive explicit human review; changing a filename to docs or tooling does not lower its risk. | Zone map covers security controls and enforcement; review depth follows impact, not agent confidence |
| RV-4 | A bad diff is not quietly fixed by hand: fix the guide or sensor that let it through, or the next session repeats it. | Ask; look at sensor history |
| RV-5 | Not every review finding is acted on; findings about impossible cases are declined. | Ask |

## MS: Measure and garden (rung 8)

| ID | Rule | Check |
|---|---|---|
| MS-1 | Track lead time, human interventions, first-pass CI rate, rework, escaped defects and rollbacks, plus test reliability (flakes, quarantine age, skips, duration and escaped regressions) and maintainability trends: complexity, duplication and aging exceptions. Never lines generated. | Comparable measurements and limitations in a log or dashboard; distinguish measured trends from inferred causes |
| MS-2 | A scheduled pass reviews stale docs, structural drift, obsolete paths, new advisories, unsupported dependencies, configuration drift, test discovery drift, flaky/quarantined tests and expiring exceptions; it proposes reviewed fixes or explicit decisions. | Routine produces dispositions; security findings follow SE-6 rather than an automatic debt waiver; uncertain unused-code reports never authorize deletion |
| MS-3 | Instructions are re-checked when models change; rules a newer model no longer needs are removed. | Last review date |
| MS-4 | Periodically exercise a representative maintenance task with a maintainer who did not author it. Record information needed, obstacles, verification and improvements; include experienced humans and fresh agent contexts over time. | Task, revision, maintainer type, needed context, result and follow-up recorded. A practice pending trial, not a rung gate |
| MS-5 | When optional routing is evaluated, compare accepted outcomes and total usage/cost including retries, transfers, review and rework, with native units, sources and uncertainty. | Comparable tasks/quality thresholds, actual role/model/host/effort, measured versus estimated usage, defects and interventions; do not aggregate unlike allowances or infer causality. Conditional practice, not a gate |

## OP: Operate (levels O1 to O3, when agents use the built system)

| ID | Rule | Check |
|---|---|---|
| OP-1 | Each action is declared once and served to the UI, the API and agent tools with the same access rules. | Compare a UI action and its API/tool twin |
| OP-2 | Agent and machine access is read-only until a person issues a write-capable credential, scoped to the actions it needs. | Token defaults |
| OP-3 | Every write records who acted and through which channel (web, API, agent). | History rows |
| OP-4 | Machine writes require request IDs scoped by owner or tenant and operation, bound to input. Authorized retries replay an outcome without repeating effects, including concurrent retries and crash recovery. Retention and expiry are explicit. Unknown external outcomes are reconciled before retry unless downstream deduplication guarantees safety. | Test sequential and concurrent duplicates, changed input, tenant separation, replay access, crashes, timeouts and expiry |
| OP-5 | Credentials travel in headers, never in URLs. | Grep routes and docs |
| OP-6 | Data text is untrusted when it reaches an agent. Tools acting on it have constrained authority and enforce boundaries even when the text contains instructions. | Record the threat and exercise planted-instruction scenarios against actual tool permissions; an ADR alone is insufficient evidence |
| OP-7 | People and agents design definitions (forms, screens, labels), never code. Agents may draft; a person publishes. | Publish permission |
| OP-8 | Calls the system makes to outside systems on an agent's behalf are bounded: a request budget per source, shared reads cached once for everyone, no retry storms. An agent looping on a tool must not become load on a system the project does not own. | A budget and a cache for each outside source an agent can reach through the system |
