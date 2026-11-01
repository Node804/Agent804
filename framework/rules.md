# Rules

Every rule has an ID, the rule, and how `assess` checks it. The published work it was
checked against is in `validation.md`.

A rule states the **property**, never the tool. "The build fails when an entry point declares no
access rule" holds in any stack; how a stack makes it fail lives in its profile (`profiles/`).

Most rules are **core** and belong to a rung. Rules in a [module](modules.md) apply only when
that module's trigger does; each family below says which.

Words: **must** is required at the rung or module the rule belongs to; **should** is the default, and a
project that departs from it says why in an ADR.

## IN: Instructions (rung 1)

IN-8 is in the Context module.

| ID | Rule | Check |
|---|---|---|
| IN-1 | Root `AGENTS.md` is the shared project-policy authority; scoped additions refine relevant areas without silently conflicting. Tool-specific files point to shared guidance. Effective instruction discovery preserves the intended policy. | Inspect root/nested/override sources, precedence and loading limits in each selected host. File presence alone is insufficient; a lone tool-specific source is partly met |
| IN-2 | It holds only what an agent cannot find by reading the repo, or would have to dig for every session: commands, decisions not in code, misleading code, anything corrected twice. No tour of directories the agent can list itself, no history; a short map pointing into `docs/` is fine. | Read it: flag directory tours, dated history, restated code |
| IN-3 | Root file under 200 lines, nested files under 150, enforced by the check. | Line counts of the root instruction file (a tool-specific file when there is no `AGENTS.md`) and nested ones. Any file over budget is not met. Within budget but not yet enforced (no check exists) is partly met |
| IN-4 | Area-specific rules load only in that area. A short navigation path leads a maintainer to its purpose, public interfaces, permitted dependencies and test command. Local guidance fills gaps the code cannot explain. | Follow the navigation without the author's chat; inspect scoped retrieval routes to contracts/callers/tests and nested guidance where areas differ |
| IN-5 | Maintained instructions, documentation links, configuration examples and executable examples agree with the current system. Named paths and commands resolve; mechanically verifiable claims run in the check. | Resolve maintained references against actual revision/dirty state and exercise commands/examples; distinguish current authority, superseded decisions and historical records |
| IN-6 | Plain statements, no IMPORTANT or ALL CAPS: emphasis makes agents over-apply a rule. | Grep for shouting |
| IN-7 | Repeated procedures are skills or playbooks, loaded when used, not paragraphs in `AGENTS.md`. | `skills/` or `docs/agents/` exists for repeated work |
| IN-8 | Evidence used for decisions preserves provenance, freshness and sufficient interpretive context. Missing, stale, inaccessible or truncated coverage remains explicit; retrieved data cannot grant authority. | Inspect source/revision and enclosing constraints, query/index scope, missing ranges and facts versus inferences. Reported practice, not a gate; search rank or no hits alone proves no completeness |

## CK: Checks (rungs 1, 2, 4 and 6)

| ID | Rule | Check |
|---|---|---|
| CK-1 | One command runs every applicable check (format, lint, types, tests, architecture, maintainability and security). CI runs the same command. | Find it; run it; compare with CI. Not met when there is no single command; partly met when CI runs something different. Whether a particular kind of check is in the command is graded under its own rule (ST-1, MT-2, SE-2, TS-12), never again here, even when that check runs somewhere else such as a pre-commit hook. Unavailable security checks stay visible as failures or gaps, never a clean result. Independent execution is CK-8 |
| CK-2 | The check command is in the first section of `AGENTS.md`, where an agent reads it before anything else. Until a check exists, that section says so. | Look, in the root instruction file (a tool-specific file when there is no `AGENTS.md`). Named but later in the file is partly met |
| CK-3 | Deterministic checks first; AI review is extra, never a substitute. | Count computational vs inferential checks |
| CK-4 | Error messages say how to fix the problem, because the agent reads them. | Read custom check messages |
| CK-5 | A rule that exists only as prose is a check not yet written. When a review comment recurs, it becomes a lint rule, structural test, type, hook or skill. | Prose rules in `AGENTS.md` that could be mechanical |
| CK-6 | Editor and pre-commit integrations provide fast feedback using the project's configuration; CI independently checks the complete declared scope. Slow checks remain in the full check and CI. | Compare integration configuration, versions and coverage with the full check; local hooks alone are insufficient |
| CK-7 | Keep enforcement small. A project-selected style may be enforced as one coherent pipeline; do not create separate hooks for individual preferences. Other preferences stay prose unless adopted as required properties. | Inspect hook purpose, overlapping checks and the project's declared conventions |
| CK-8 | Before a change merges, the check runs independently of the author's working tree: from committed state, in a clean environment, with nothing from the author's machine but the address of a test database. This catches the forgotten file, the dependency missing from the lock file and the test that passes only on local data. CI with branch protection is the standard mechanism, and the only one that also gates the merge for every tool. | Met: CI runs the check on every change and a red run blocks the merge. Partly met: CI runs but does not block, or a clean-clone script runs the check from committed state but nothing makes it run before a merge. Not met: only the author's working tree is ever checked |

## ST: Style (rung 2)

| ID | Rule | Check |
|---|---|---|
| ST-1 | Each language the project maintains has one formatter and linter, with committed configuration and pinned versions. The check reports violations without rewriting files; a separate command fixes them. The language's standard style is the default (for example PEP 8 for Python, PSR-12 for PHP); a project that keeps a different one records why, in its profile or an ADR. | Add a deliberate violation: the check fails and the file is unchanged; the fix command repairs it; a second run changes nothing. Configured but not in the check or CI is partly met; a non-standard style with no recorded reason is partly met |

## GR: Guardrails (rung 3)

| ID | Rule | Check |
|---|---|---|
| GR-1 | Development agents cannot reach production secrets or sensitive production data; development uses test credentials and synthetic or reviewed sanitized data. One exception, when production is the only source to develop against: a development credential that a person decided in writing, that the source itself limits to reading non-sensitive data, that is rate-limited, and that is separate from production's own, so revoking it does not break production. File deny rules are supplementary, not the security boundary. | Grade credentials and data separately; the rung takes the worse. Credentials: a reachable production credential outside the exception is not met; a development secret, or an exception credential shared with production or kept only behind deny rules, is partly met. Data: sensitive production data in files, environment or copied data is not met; non-sensitive production data, reached without a credential or under the exception, is not a GR-1 finding but belongs in the threat model (SE-1). Judge restricted files from examples, docs and scripts without reading them. An example's empty slot says a setting exists, not that it is set or unset: when the grade depends on it, mark the half not verifiable and ask the owner |
| GR-2 | Commit, push, deploy and migrate require human authorization. The agent never merges to the protected branch. Changes that weaken security checks, CI gates, permissions, deployment or approval policy require explicit human review of the change. | Committed agent settings (none committed is not met), reviewed policy diffs and scoped authorizations; host protection requires external evidence |
| GR-3 | Every change happens on a branch or worktree; the main branch takes reviewed merges only. | History shows merges into the main branch. A fork's own main branch used as the working branch is partly met |
| GR-4 | Completion controls require the applicable check before a success claim and expose failures. A bounded escape permits honest failure reporting, not a success claim. | Exercise effective host loading, trust and failure continuation/blocking; configuration or instructions alone are insufficient. Reporting escape after one block is met; skipped/unsupported controls are gaps. CI merge gating is separate |
| GR-5 | An unattended run answers five questions first: what done looks like, how it checks itself, what it may touch, what stops it, who signs off. It runs sandboxed. | Look at scheduled or headless runs |
| GR-6 | Scripts that change data are dry-run unless told to apply. | Read data scripts |
| GR-7 | Agents cannot supply consent. Approval comes from the person directing the work, for the specific action or content, in their own words. An approved plan, a tool permission prompt, a passing check or a record an agent filled in is not approval. Agreement covers what the person saw: when the agent's work changes it materially, the agent asks again. An agent never marks a decision Accepted or a review done itself. | Instructions say so; history shows no agent-set Accepted status, agent-written approval, commit that followed only a plan approval, or agreed criteria changed without the person seeing them again. Instructions alone with no contrary history is met. A co-author trailer says who wrote a commit, not who decided |

## SK: Walking skeleton (rung 4)

| ID | Rule | Check |
|---|---|---|
| SK-1 | One rerunnable command takes a fresh clone to a running app. | Run it on a clean clone. A read-only assessment that cannot clone grades the command and its tests, and says it was not run |
| SK-2 | One end-to-end test exists from the first commit and runs in CI. | Find it |
| SK-3 | Prefer established stack capabilities and existing project implementations. New dependencies and custom replacements serve a demonstrated requirement with a maintenance justification; neither hand-written code nor a dependency is automatically preferable. | Inspect new capabilities, alternatives considered and maintenance costs in the plan or review; use an ADR only for a hard-to-reverse choice |
| SK-4 | Configuration comes from the environment; no hard-coded paths or hosts. | Grep for absolute paths and hosts |

## TS: Tests and acceptance (rungs 2, 4 and 5)

Interpretation, evidence and staged handoffs are in [testing.md](testing.md).

| ID | Rule | Check |
|---|---|---|
| TS-1 | A feature's criteria are agreed before code by the person directing the work, sized to the change. | Specs or small-change plan/PR criteria predate code and show the person's agreement; pre-adoption features do not count against it |
| TS-2 | New or changed behavior: tests fail for the intended reason before the code, pass afterwards, then structure is improved where it helps without changing behavior. | The red and green output (command and result) is in the plan or PR, with the refactor done or "none needed". Commit order alone proves nothing ran |
| TS-3 | Acceptance tests are derived from agreed criteria in a context separate from implementation. Implementers may add supporting unit tests. | Handoff identifies criteria, tests and red evidence; no separate context is required for every helper test |
| TS-4 | Failures remain visible and are fixed or reported, never hidden by weakening, skipping or deleting tests to get green. A changed test keeps the protection it gave; a changed expected outcome goes back to the person who agreed the criteria (GR-7). | History and diffs: new skips, deleted or loosened assertions each have a stated reason and, for acceptance tests, the person's agreement. Instructions alone with no contrary history is met |
| TS-5 | Representative user journeys are checked end to end; lower-level tests cover detailed cases at effective boundaries. Done includes execution evidence and appropriate UI evidence. | Trace journeys and edge cases to tests; screenshots supplement rather than replace automated behavioral assertions |
| TS-6 | The agent marks what it does not know (`[NEEDS CLARIFICATION]`) instead of guessing, and the marks are resolved before planning. | Spec template |
| TS-7 | Test handoff passes applicable independent validity checks; remaining failures identify the intended missing behavior or planned public interface. | Preserve lint, fixture and setup results; a specific expected missing-interface compiler diagnostic can be red, unrelated syntax, dependency or environment failures cannot |
| TS-8 | Tests assert observable outcomes, public contracts and relevant effects using requirements or an independent oracle, rather than copying implementation logic. | Inspect expected values and boundaries; internal refactors should preserve acceptance outcomes. Interaction assertions require a real protocol contract |
| TS-9 | Bug fixes retain regression protection that reproduces the affected pre-fix behavior before the fix. | Record pre-fix failure and post-fix pass; explain reproduction limits. Applies to bug fixes after adoption, not invented historical evidence |
| TS-10 | Tests isolate the data they change and control time, randomness and order where it matters. A flaky test is reported, never retried silently into a pass. | Two runs give the same result; retries and quarantined tests are visible in the output |
| TS-11 | Verification covers important component contracts and real integration at the lowest effective level, plus representative end-to-end journeys. | Name simulated and actual boundaries; mocks alone do not prove compatibility. Use safe external substitutes with contract evidence where live access is unsuitable |
| TS-12 | The check prints how many tests it found and ran, lists skips and exclusions, and fails when it finds none where tests are expected. | Run it: the counts appear. Partly met when an empty run passes |
| TS-13 | Selected critical behavior is checked for test sensitivity by deliberate wrong behavior in isolation. This is a practice pending trials, not a rung gate. | Record detected faults, survivors, limits and justified exclusions; invalid compilation is not behavioral detection. No universal mutation or coverage quota |

## AR: Architecture (rung 6)

| ID | Rule | Check |
|---|---|---|
| AR-1 | Default deny: every entry point (page, API, tool, job) declares access and the build fails when one does not. Effective authorization enforces applicable object and tenant boundaries on every path, not merely login or a declaration. | Add an undeclared entry point; test direct requests, alternate adapters and cross-object/tenant attempts for refusal without prohibited effects or disclosure |
| AR-2 | Each concept and business rule has an authoritative declaration or implementation; dependent representations derive from it where practical. Independent copies need an explicit reason. Similar code is not automatically the same concept. | Trace a changed rule to its authority; inspect duplicate findings and dispositions, including whether copies must change together |
| AR-3 | Cohesive modules communicate through declared public interfaces and permitted dependency directions. The check enforces boundaries and rejects undeclared cycles; any consistent structure qualifies. | Architecture contract in the check; review responsibilities and public interfaces. A consistent convention with no check is partly met |
| AR-4 | Every write is validated in one place before it is stored. The layer's name and shape are the project's choice. | Look for writes that skip it |
| AR-6 | Data is parsed and validated at boundaries and safely interpreted or encoded for each destination. Validation alone never makes data safe as a query, command, path or rendered output. | Inspect input-to-sink paths and test applicable injection, traversal and unsafe-output cases |

## SE: Security (SE-2 at rung 2, SE-3 at rung 3; the rest in the Security module)

Scope and exceptions are in [security.md](security.md).

| ID | Rule | Check |
|---|---|---|
| SE-1 | The threat model is written where agents read it: assets, actors including agents, trust boundaries, credible abuse cases, and requirements selected from a versioned standard with exclusions explained. It has an owner and is revisited when exposure changes. | `docs/security.md` (or equivalent) exists, is linked from the instructions and matches the real interfaces and data; selected requirement IDs carry their version |
| SE-2 | Security scanners (secrets, static analysis, dependencies) run in the check and CI. A scanner that errored, was skipped or used stale advisory data is reported as a gap, never as clean. | A planted fixture makes each scanner fail; inspect how errors, skips and feed age are reported |
| SE-3 | New dependencies are verified before installation: publisher, package identity, install and build behaviour. Versions are locked with integrity data and the project builds cleanly without production credentials. | Lock file with hashes; a review step for new packages, including transitive and build-time ones; a clean build |
| SE-4 | The application uses its framework's security mechanisms and safe defaults, enforces access server-side on every path, and fails safe when production configuration is missing. Production controls are verified in the real environment by an authorized person or deployment check. | Test refusals on alternate paths; inspect defaults and production settings; local checks are not deployed evidence |
| SE-5 | Security-affecting changes have refusal criteria and tests written first, showing an unauthorized attempt fails with no write, disclosure or outside effect. | Trace the criteria to tests and results; for agent tools, a planted-instruction test against the tool's real permissions |
| SE-6 | Findings have an owner, a deadline and a recorded outcome. Only a person accepts a risk, with a scope and an expiry; a suppression is not an acceptance. Leaked secrets are rotated, not just deleted. | Findings list and risk decisions with expiry |

## MT: Maintainability (rungs 2, 4 and 6)

MT-4 and MT-5 are in the Maintenance module.

Interpretation, exceptions and adoption are in [maintainability.md](maintainability.md).

| ID | Rule | Check |
|---|---|---|
| MT-1 | Public interfaces document purpose, inputs, outputs, failures and side effects where declarations do not make them evident. Non-obvious logic, constraints and workarounds carry a comment that says why. Documentation changes with behavior. | Check presence where practical; review accuracy against implementation and tests. A boilerplate docstring alone is not evidence |
| MT-2 | The project defines enforceable limits appropriate to its stack: function complexity, file or module size (so a unit can be read whole within an agent's context), and duplicated code. Changes introduce no unapproved violations or worsen existing ones. Exceptions identify scope, reason, reviewer and review condition. | A deliberate violation of each limit fails the check; inspect changed code and scoped exceptions against the adoption baseline. Some limits enforced is partly met |
| MT-3 | A change removes code, dependencies, configuration and documentation it makes obsolete, or records why they remain and when retention will be reviewed. Uncertain usage is investigated before removal. | Trace replaced execution paths; inspect reference and unused-code reports and retention decisions. Dynamic registration and compatibility paths need evidence, not automatic deletion |
| MT-4 | Structural changes identify the maintenance problem, affected contracts and preservation evidence. Behavior changes are separated or explicitly specified and approved. Unverified compatibility remains a reported gap. | Inspect baseline results, relevant tests, consumer analysis and final verification. A practice pending application trials, not a rung gate; passing tests establish only exercised scope |
| MT-5 | Confirmed debt has a real consequence, an owner, a person's decision and a date or event to look again. A debt record never waives a failing check, security finding or defect, and closing it shows the stated outcome. | Inspect the record; scanner output and style preferences are candidates, not debt. Trial module: reported without a mark |

## WK: Work (practices; WK-6 in the Parallel work module)

WK-6 is in the Parallel work module, WK-7 in Routing and WK-8 in Context.

| ID | Rule | Check |
|---|---|---|
| WK-1 | Small changes, one logical change each; structural changes separate from behaviour changes. | Count changed lines per merged change (a pull request, or a commit where there are none), excluding migrations, lock files, translation catalogues, changelogs and vendored or generated files; templates and docs count. Over about 400 is large, over 1,000 a finding. Mostly small is met |
| WK-2 | Non-trivial work has a checked-in plan with progress notes, so the next session can resume from the repo, not from chat. | `docs/plans/` or equivalent |
| WK-3 | Planning and implementation use separate contexts with an exact artifact handoff. Unrelated work does not inherit stale assumptions. | Inspect actual handoff and input boundaries; compaction or a mode switch alone is not fresh context. Sequential separate chats can reuse a checkout; no subagent mechanism is required |
| WK-4 | Each change carries a changelog entry written as it is made. | Fragments or entries per change |
| WK-5 | The definition of done is written down and includes evidence. | In `AGENTS.md` |
| WK-6 | Concurrent writers have separate checkouts and isolated mutable resources (databases, ports, queues and storage where applicable). Check state is private to each checkout. Sequential contexts may reuse one. Handoffs identify an exact revision or preserved patch; combined changes are checked again. | Exercise two checkouts: hooks and resources are independent; inspect handoff and integration evidence. See the worktree playbook |
| WK-7 | When models are routed, roles are assigned by capability tier, not model name; review uses a different model from the author where one is available; a reserve covers review and the final check; and the actual model per role is recorded. Running out never silently skips a step or falls back to paid usage. | Inspect the routing record and plan/PR notes for actual assignments. Trial module: reported without a mark; one model in separate contexts is always sufficient |
| WK-8 | Long-running work can recover approved scope, critical contracts and actual verification state from durable artifacts after interruption or context changes. | Reconstruct from source-linked working state; distinguish decisions, hypotheses, prior results and fresh checks. Verify material changes and valid approval without invented history. Reported practice, not a gate |

## DC: Decisions (rung 7)

| ID | Rule | Check |
|---|---|---|
| DC-1 | ADRs record hard-to-reverse decisions only; detailed designs are specs. | ADR sizes and count |
| DC-2 | Each ADR's status shows where the decision stands: at least Proposed, Accepted and Superseded by NNNN (Validated and Rejected if the project uses them). Each ADR has an append-only evidence record before acceptance: a separate file it links, or a final Evidence section of the ADR that only grows. | The record exists for each ADR; entries identify tests or reasoning, revision and results; history shows entries are added, never rewritten. Either form meets the rule |
| DC-3 | An Accepted ADR's decision text is frozen; only its Status, Topics and evidence record change. A later ADR amends or supersedes it. Later evidence never downgrades it to Validated. Contradictions trigger owner review. | History of accepted ADRs: the decision text unchanged since acceptance |

## RV: Review (RV-1 at rung 4)

| ID | Rule | Check |
|---|---|---|
| RV-1 | A human reads every change before merge and can explain it; implementation review identifies the actual change and remains valid under the project's freshness policy. | Verify review source and revision, reviewer other than author where required, latest relevant changes and host enforcement; external evidence unavailable is not a proven review |
| RV-2 | Agent review runs in a fresh context and works back from acceptance criteria. Automation owns enforced layout; naming, interface clarity and documentation meaning still receive review where tools cannot judge them. | Review playbook and findings distinguish automated layout from semantic conventions |
| RV-3 | Code, policy, tests and tooling are zoned by damage and reversibility. Security policy, security tests, CI enforcement, permissions and approval mechanisms receive explicit human review; changing a filename to docs or tooling does not lower its risk. | Zone map covers security controls and enforcement; review depth follows impact, not agent confidence |
| RV-4 | A bad diff is not quietly fixed by hand: fix the guide or sensor that let it through, or the next session repeats it. | Ask; look at sensor history |
| RV-5 | Not every review finding is acted on; findings about impossible cases are declined. | Ask |

## MS: Measure and garden (rung 8)

MS-5 is in the Routing module.

| ID | Rule | Check |
|---|---|---|
| MS-1 | Track whether agent work holds: first-pass check rate, human corrections, rework, escaped defects and reverts, test reliability (flakes, quarantine age, skips, duration) and maintainability trends. Never count lines generated. | A periodic report from git, CI and a corrections log; missing data stays missing |
| MS-2 | A scheduled pass reviews stale docs, structural drift, obsolete paths, new advisories, unsupported dependencies, configuration drift, test discovery drift, flaky/quarantined tests and expiring exceptions; it proposes reviewed fixes or explicit decisions. | Routine produces dispositions; security findings follow SE-6 rather than an automatic debt waiver; uncertain unused-code reports never authorize deletion |
| MS-3 | Instructions are re-checked when models change; rules a newer model no longer needs are removed. | Last review date |
| MS-5 | Routes are compared on accepted outcomes and defects first, then total cost including retries, rework and review, in each provider's own units. | Comparable tasks and stated sample size; no converted totals across providers, no claimed cause from a small sample |

## OP: Operate (Operate module, levels O1 to O3)

Scope and the MCP design choices are in [operate.md](operate.md).

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
| OP-9 | Each model-facing action has a stable name, when to use it and when not to, a validated input schema, a bounded result that omits secrets, and a declared effect of read, write, or destructive. The set is the actions a task needs. A declared read does not write, send, delete, or spend. The server enforces the effect. | Compare the exposed list with internal functions. A wrapper per function, an unbounded or secret-bearing result, or a read that changes state is not met |
| OP-10 | An embedded model feature keeps its instructions, allowed actions, accepted inputs, and output effects in the repository, and is specified, tested, and reviewed like other behavior. Model output is data: it cannot grant access, publish, approve, or bypass a check. Planted instructions in user or retrieved content have no forbidden effect. | Trace the prompt, allowlist, and effects to repo artifacts, tests, and a person's review. Output that writes or publishes without the same checks as a direct call is not met. No such feature is not applicable |
| OP-11 | A credential accepted by an agent or MCP endpoint was issued for that endpoint. The server does not accept or forward a token issued for another audience. An OAuth proxy obtains consent for the specific client before forwarding to third-party authorization; another client's consent does not cover it. A session identifier is not authentication. A local server process does not receive production credentials and does not run with more privilege than its actions need. | Foreign-token passthrough, OAuth-proxy consent skipped for a later client, or a session used as login is not met. A local process holding a production credential or broader privilege is not met. No such path, with credentials limited to the action, is met |
