# Agent804

**Build the harness before the app.** A framework and skill set for working with coding
agents, from Node 804.

**Why.** Asking an agent to "build me an app, make no mistakes"
fails for the same reasons every time: the agent has no memory of your standards, no way to
check its own work, nothing stopping it from doing irreversible things, and it grades its own
homework. Better prompts do not fix that. A repository that holds the rules, and checks that
enforce them, does.

Agent804 comes from my own experience building several agentic line-of-business apps with
coding agents: what broke when I prompted without structure, what I changed, and what held
once the rules lived in the repository and the checks enforced them. I then
checked it against published practice from Anthropic, OpenAI, Simon Willison, Harper Reed, Addy
Osmani, Kent Beck, Birgitta Böckeler and GitHub Spec Kit, and used their work to reinforce
it: see [framework/validation.md](framework/validation.md).

## Core and modules

**The core is what every project built with agents needs**: eight rungs, from an instructions
file to measurement ([rungs.md](framework/rungs.md)). Along the way it covers:

| Goal | What the core requires |
|---|---|
| [Witnessed TDD](framework/testing.md) | Tests written from agreed criteria in a separate context, shown failing first and then passing; bug fixes keep a test that failed before the fix; isolated, reliable tests and real integration boundaries |
| [Maintainable code](framework/maintainability.md) | Documented public interfaces, enforced complexity limits, one authority for each business rule, and obsolete code removed. Existing projects can adopt a reviewed baseline without a rewrite |
| [One style per language](framework/rules.md#st-style-rung-2) | A pinned formatter and linter for each language, run by the check without rewriting files. The project's existing choices win |
| [Security basics](framework/security.md) | Security scanners in the check, reviewed dependencies, no production secrets within an agent's reach, and a person reading every change before merge |

**Modules cover problems a project has only in some situations.** Each has a trigger; when
it is true the module is scored and a gap is a real finding, and when it is false the module
costs nothing ([modules.md](framework/modules.md)).

| Module | Applies when |
|---|---|
| **Operate** | Agents, scripts or AI assistants call the system. One contract for people and agents; read-only until a person grants write; every write attributed; repeats harmless; untrusted text and outside load bounded. Most guidance stops at agents *building* software; once an assistant can call your system, this matters as much |
| **Security** | The system holds sensitive data, handles money or safety, writes to other systems of record, or is reachable beyond the team. Threat model, safe defaults, abuse tests, owned findings, and production readiness reported separately |
| **Approvals** | Someone other than the author must sign off. Who approved which revision, from what source, traced to tests and results |
| **Parallel work** | Several agents or people write at once. A checkout, database and port each, and a check of the combined result |
| **Maintenance** (trial) | Adopting the harness onto existing code. Verified refactoring and a debt record that never waives a failing check |
| **Context** (trial) | Work spans many sessions. Evidence with a known source and age; state recoverable from the repository, not from chat |
| **Routing** (trial) | Several models or a spend budget. Traceable assignments and cost compared against accepted outcomes |

Trial modules have not run on a real project yet; `assess` reports them without a score.

Other guides: [agent hosts](framework/agents/README.md) (Claude Code, Codex, Grok Build,
ChatGPT and custom hosts, kept separate from language profiles), and
[independent roles](framework/model-routing.md#independent-roles) (separate
contexts write the tests, the code and the review; different models are optional).

The process scales to the change: a small fix needs a focused test, not a spec, and
high-impact changes get deeper review.

## Choose a starting workflow

| Situation | Start here |
|---|---|
| Empty or near-empty project | [`start`](skills/start/SKILL.md): select stack/host, establish the harness and exercise its controls |
| Existing repository | [`assess`](skills/assess/SKILL.md): read-only foundation/coverage report and next three steps |
| Feature or bug fix | [`spec`](skills/spec/SKILL.md), then separate acceptance/implementation contexts and [`review`](skills/review/SKILL.md) |
| Standalone restructuring | [`refactor`](skills/refactor/SKILL.md), using preservation evidence rather than artificial red tests |
| Choosing models, effort or allowance allocation | Optional [`route`](skills/route/SKILL.md), producing recommendations and handoffs |
| Incomplete evidence or context recovery | Optional [`context`](skills/context/SKILL.md), preparing the next decision from actual sources |
| Recurring maintenance/debt follow-up | [`garden`](skills/garden/SKILL.md) and [`measure`](skills/measure/SKILL.md); authorized repayment uses the existing work/refactor workflow |

## What is in it

| Path | What |
|---|---|
| [framework/rungs.md](framework/rungs.md) | The eight core rungs, what each prevents, how a project is scored and how much it needs |
| [framework/modules.md](framework/modules.md) | The modules, their triggers and rules, the Operate levels and production readiness |
| [framework/rules.md](framework/rules.md) | The rules, each with an ID, its source and how to check it |
| [framework/profiles/](framework/profiles/) | Support matrix, Django reference baseline and draft stack profiles with explicit parent/extension guidance |
| [framework/agents/](framework/agents/) | Host capabilities and setup: Claude Code, Codex, Grok Build CLI, ChatGPT/custom harnesses; exercised evidence and explicit gaps |
| [framework/model-routing.md](framework/model-routing.md) | Optional role/model/effort selection, budget pools, escalation, independent adversarial roles and quality-adjusted usage evidence |
| [framework/context-management.md](framework/context-management.md) | Scoped retrieval, provenance/freshness, incomplete output, durable working state and recovery; research-backed limits and proposed trials |
| [framework/worktrees.md](framework/worktrees.md) | Separate checkouts for concurrent writers: resource isolation, handoff, integration and cleanup |
| [framework/maintainability.md](framework/maintainability.md) | Understandable contracts, complexity controls, retirement, baselines and maintenance exercises |
| [framework/technical-debt.md](framework/technical-debt.md) | Confirmed debt, ownership, deferral, consequence-based priority and verified closure; lightweight record template and existing-skill workflow |
| [framework/security.md](framework/security.md) | Security requirements, threats, verification, dependency trust, runtime protection, response and production readiness |
| [framework/approvals.md](framework/approvals.md) | Scoped human decisions, original evidence, freshness, requirement trace and mechanical-check limits |
| [framework/testing.md](framework/testing.md) | Witnessed red/green/refactor, independent assertions, regression protection, isolation, integration and complete execution evidence |
| [templates/](templates/) | Agent instructions; specs/plans/PRs; ADR/evidence and approval records/validator; maintainability/security/debt records; host/routing records; `.editorconfig` and `.gitattributes` starters; Claude/Codex/Grok starters |
| [skills/](skills/) | The skills below, as plain playbooks any agent can follow |

**Two readers.** `framework/` is written for people: why each rule exists, its trade-offs and
evidence. Skills and templates are written for agents and say only what to do, because an
agent pays for every line it loads. Skills send agents into `framework/` only for the tables
and playbooks they execute (rules, rungs, modules, profiles, hosts, worktrees); the check
enforces that and keeps each skill and the `AGENTS.md` template within a size budget.

The kit ships one language profile, Django, because it is the only stack it has been run
on. For any other stack, `start` writes a Draft profile for the project from the template,
against the real code. A profile joins the kit once it has been used on a real project; see
[profiles](framework/profiles/README.md). **Host profiles** in `framework/agents/` cover agent
integration separately.

| Skill | Does |
|---|---|
| [`start`](skills/start/SKILL.md) | New project: interview, then a running skeleton with one check command, guardrails, CI, decisions and risk zones, before any feature; if agents will use it, the first action goes through one contract |
| [`assess`](skills/assess/SKILL.md) | Existing project: foundation and coverage, which modules apply and how they score, with evidence, and the next three steps. Read-only |
| [`spec`](skills/spec/SKILL.md) | Acceptance criteria sized to the change; tests from a separate session, written first |
| [`refactor`](skills/refactor/SKILL.md) | Scoped restructuring with baseline tests, consumer/contract analysis and preservation evidence; routine feature refactoring needs no separate invocation |
| [`route`](skills/route/SKILL.md) | Optional model/host/effort and budget recommendations; prepares independent-role handoffs without launching agents or spending allowance |
| [`context`](skills/context/SKILL.md) | Optional focused retrieval and context recovery for large tasks, incomplete evidence and handoffs; uses existing plan/PR notes |
| [`sensor`](skills/sensor/SKILL.md) | A recurring mistake becomes a check whose message tells the agent how to fix it |
| [`decide`](skills/decide/SKILL.md) | ADRs with Proposed / Validated / Accepted / Rejected and evidence |
| [`review`](skills/review/SKILL.md) | Fresh-context review from the acceptance criteria, deepest in red zones |
| [`garden`](skills/garden/SKILL.md) | Finds stale guidance, structural/context drift, due debt/exception reviews and security follow-up; proposes scoped fixes |
| [`measure`](skills/measure/SKILL.md) | Delivery, test reliability and maintainability/debt trends; optional routing usage and context-recovery trials, with evidence and uncertainty |
| [`operate`](skills/operate/SKILL.md) | The Operate module, O1 to O3: one contract, read-only until granted, attributed, safe retries, untrusted text, bounded outside load |

## Use it

**Claude Code**, as a plugin. This works wherever Claude Code runs: the desktop app's Code tab,
the terminal, the web, or an IDE.

```
/plugin marketplace add C:/path/to/agent804
/plugin install agent804@agent804
```

Then `/agent804:start` in an empty folder, or `/agent804:assess` in an existing
project.

**Codex** (in the ChatGPT or Codex desktop apps, the terminal or an IDE) reads a project's
`AGENTS.md` and its skills from `.agents/skills/`. Codex installs Agent804 as a plugin too, from
the same folder or marketplace: it reads the root `plugin.json`. Without plugins, point Codex at
`skills/<name>/SKILL.md` and tell it to follow the file. The hooks and permission
rules in `templates/claude-settings.json` are Claude Code's; Codex has its own approval and
sandbox settings. Follow the [Codex host recipe](framework/agents/codex.md) for Draft config,
paired stop adapter/engine, hook trust and actual-host verification. Preserve the intact kit
when linking local skills; copying skill folders alone breaks resource paths. Use
`python scripts/check_skill_resources.py <kit-root>` after relocation; this checks paths,
not native discovery. Do not install both plugin and local copies under colliding names.

**ChatGPT and custom API hosts:** use the [capability guidance](framework/agents/chatgpt.md).
A document-only chat can review supplied content; execution and enforced completion require
actual tools and controls. Record host/version, capabilities and gaps in the
[host record](templates/agent-host.md). A model name is not an execution guarantee.

**Grok Build CLI:** follow the [native host recipe](framework/agents/grok-build.md) for
`AGENTS.md`, intact skill discovery, project permission rules, separate user-layer settings
and paired native Stop adapter/shared engine. Inspect discovery with `grok inspect --json`
and review actual project trust before enabling hooks. Public and newer upstream Stop
documentation differ; adapter fixtures do not prove the installed client's continuation.
This Draft integration targets the coding CLI/TUI, not web/mobile Build Mode. No plugin or
model session is installed/launched by these templates; keep existing data/spend permissions.

**Other agents** (Cursor and others that read Agent Skills or plain instructions): the same, point
the agent at `skills/<name>/SKILL.md`. The skills use only the portable frontmatter fields and
refer to the framework by relative path.

## The loop, once set up

1. Resolve the current task, relevant contracts, debt and valid human decisions. `spec` sizes
   behavior changes and records agreed criteria; pure refactors use preservation criteria.
2. Use `context` or `route` only when useful. Preserve exact artifacts and unknowns; a model
   recommendation does not authorize another session, provider transfer or spending.
3. A separate acceptance context writes tests and preserves meaningful pre-change failure
   evidence. Pure structural work establishes a green baseline; do not manufacture red.
4. An implementation context builds the behavior, inspects/refactors after green and updates
   plan/PR evidence. Concurrent writers use isolated worktrees/resources; check the combined result.
5. `review` assesses criteria, risks and actual results in a fresh context; a human reviews
   before merge. A configured hook is not an exercised control. A reporting escape allows
   an honest failure report, never a false success claim.
6. A repeated mistake becomes a `sensor`. On the project's cadence, `garden`/`measure`
   revisit drift, security findings, test gaps and debt. Verify repayment before closure.

## What it does not do

- Decide what is worth building.
- Replace experienced maintainers or human review. Reviewers must understand the actual
  change; red-zone work receives the applicable deeper review.
- Guarantee correctness or complete context. Tests and reviews can miss misunderstood
  requirements; retrieved text, summaries and model agreement are not proof of completeness.
- Set itself up or enforce policy through prose alone. Setup, trust, tools and independent
  CI need exercise in the selected host; effort depends on project scope and existing controls.

## Status

**Version 0.3.0, unreleased preview.** Rules will change; see [CHANGELOG.md](CHANGELOG.md).

What has been tested:
- The repository check currently runs **48 regression tests**: eight shared/Claude stop-hook
  cases, thirteen Codex and thirteen Grok adapter cases, twelve mechanical approval cases and two skill-resource
  layout cases. These are fixture tests, not full application or host-enforcement trials.
- Codex adapter protocol, malformed events, reporting escape, missing engine and rendered
  commands from a subdirectory, plus shared Git/worktree/cache scenarios. Intact relocated
  skill resources resolve; a skills-only copy is rejected. A local CLI rule evaluation
  returned `prompt` for a direct Git push pattern without executing a push.
- Grok 1.0.70 isolated offline inspection discovered all twelve kit skills through a fixture
  user-layer path. The untrusted project did not load instructions, permissions or hooks;
  that inspection grants no evidence of active enforcement or a live model workflow.
- `assess` installed as a plugin in both Claude Code and Codex.
- `assess` on two real Django repositories, three rounds each by independent agents working
  from the playbook alone. Scores converged once ambiguous rule wording was fixed.
- The full flow on one real feature, from a one-line request: quality scenarios and ADRs read
  unprompted, a stop on a Proposed ADR (which caught a flaw in it), an agreed spec, tests from
  a separate context failing for the right reason, a tests-only commit, the build with the
  tests unchanged, review, and evidence recorded back on the ADR and the scenario.
- Automated stop-hook regressions: linked worktrees, private caches, staged edits before the
  first commit, changed check commands, path discovery and failure reporting. The repository
  check runs them; fixture commits are confined to disposable test repositories.
- Mechanical approval regression fixtures: schema/snapshots, scoped freshness, unrelated
  edits, revocation/supersession, dependencies, conditions/expiry, references and explicit
  provenance/authority disclaimers. These do not authenticate any real human decision.

What has not:
- Live Grok Build trust, project-policy enforcement, native Stop continuation and OS/network
  sandbox behavior. Thirteen adapter fixtures and offline discovery do not establish these;
  importing Claude configuration alone cannot prove the native event contract works.
- The MT-5 debt lifecycle on an adopting project: candidate confirmation, scoped human
  deferral, due review, partial repayment and verified closure. It remains a reported practice;
  no tracker automation, real risk acceptance or economic benefit is established by the kit.
- The context-management playbook and IN-8/WK-8 practices on representative retrieval/recovery
  maintenance tasks. MS-4 trials remain pending; integrity checks do not measure attention,
  retrieval recall or complete context. No universal model/context-size guarantee is claimed.
- Optional model routing and WK-7/MS-5 on actual single-model, same-family or cross-provider
  tasks. No budget optimization, adversarial-model effectiveness or savings is established
  by templates and integrity checks; these conditional practices add no scoring gates.
- The revised host capability workflow and live Codex hook loading/trust/continuation across
  clients. Adapter/resource fixtures and a CLI rule parse do not prove actual-host enforcement.
  Equivalent bug-fix/feature/refactor/review trials across hosts remain pending.
- The new `refactor` skill and MT-4 preservation workflow on full applications. MT-4 remains
  a reported practice pending trials, with no new rung or scoring gate.
- The revised [testing workflow](framework/testing.md), new TS gates and Draft native-runner
  evidence mappings on full applications. Sensitivity checks (TS-13) remain a practice;
  repository checks do not prove these workflows or update historic reference scores.
- `start` on an empty repository, the small-change path, and the `sensor`, `garden`,
  `measure` and `operate` skills.
- The full flow under Codex: only `assess` has been run there (installed as a plugin, in the
  ChatGPT desktop app). Codex shows the account that added a private plugin as its author.
- Any stack other than Django.
- The revised worktree lifecycle, retry contract and separate `docs/evidence/` model on a full
  application feature. Hook regression tests alone do not validate those end-to-end workflows.
- The new maintainability gates (MT-2 at rung 2, MT-1 at rung 4, MT-3 at rung 6), revised
  reference-project scores, or the draft Django mechanisms. Fresh-maintainer exercises (MS-4)
  remain a practice pending trials with experienced humans and fresh agent contexts.
- The six security baseline rules and revised gates, dependency/build verification, response
  workflow and new Django mappings on reference projects. The framework's own integrity check
  does not scan or certify the security of adopting applications or production environments.
- The new approval gates, trusted-source/host adapters, permitted administrative transitions
  and cross-session human approval reuse on a real project. Portable byte checks alone do
  not establish consent, reviewer authority, semantic trace coverage or action permission.

To validate this kit (Python 3.11+ and Git):

```bash
python scripts/check.py
```

It checks references/rule IDs, portable skill metadata, line budgets, matching manifests,
configuration syntax, approval-template structure and the regression suite. It does not
exercise every native stack, authenticate human consent or measure model/context quality.
Optional style tools are needed only when adopting their configurations; the kit does not
install or execute them implicitly. Keep the intact kit when distributing its skills.

For reusable project records, start from [maintainability](templates/maintainability.md),
[security](templates/security.md), [approvals](templates/approvals.md), [host capabilities](templates/agent-host.md),
[optional routing](templates/model-routing.md) and [debt](templates/debt.md). Existing equivalent
records qualify; do not create duplicate authorities or fictional approvals/findings.
See [ROADMAP.md](ROADMAP.md) for pending trials and [validation](framework/validation.md) for
consulted research, observed evidence and limits.

Böckeler's point that there are no unit tests for context applies here too: run it on real
repositories and change the rules that do not survive.

## License

[MIT](LICENSE), except [`templates/`](templates/), which is [MIT No Attribution](templates/LICENSE):
copy a template into your own project and change it freely, with no notice to keep.
