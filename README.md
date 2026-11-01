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
| **Security** | The system holds sensitive data, handles money or safety, writes to other systems of record, or is reachable beyond the team. Threat model, safe defaults, abuse tests and owned findings |
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

## What is in it

| Path | Read by | What |
|---|---|---|
| [framework/rules.md](framework/rules.md) | Both | Every rule, with an ID and how to grade it |
| [framework/rungs.md](framework/rungs.md) | Both | The eight core rungs, how a project is scored, and how much it needs |
| [framework/modules.md](framework/modules.md) | Both | The modules and their triggers, and the Operate levels |
| [framework/profiles/](framework/profiles/) | Both | The Django profile, and the template `start` fills in for any other stack |
| [framework/agents/](framework/agents/) | Both | Host recipes: Claude Code, Codex, Grok Build CLI, ChatGPT and custom hosts |
| [framework/worktrees.md](framework/worktrees.md) | Both | Separate checkouts for agents or people writing at the same time |
| [testing](framework/testing.md), [maintainability](framework/maintainability.md), [security](framework/security.md), [debt](framework/technical-debt.md), [context](framework/context-management.md), [routing](framework/model-routing.md) | People | Why the rules on each topic exist, and their trade-offs |
| [framework/validation.md](framework/validation.md) | People | The published work the framework was checked against, and where it chose differently |
| [templates/](templates/) | Agents | `AGENTS.md`, specs, plans, pull requests, ADRs and evidence, project records, host settings and stop hooks |
| [skills/](skills/) | Agents | The twelve skills below |

**Two readers.** The pages marked "People" explain; skills and templates instruct, because an
agent pays for every line it loads. Skills send agents into `framework/` only for the pages
marked "Both", and the check enforces that, keeps each skill within a size budget, and fails
any rule that no skill or template acts on.

The kit ships one language profile, Django, because it is the only stack it has been run
on. For any other stack, `start` writes a Draft profile for the project from the template,
against the real code. A profile joins the kit once it has been used on a real project; see
[profiles](framework/profiles/README.md).

| Skill | Does |
|---|---|
| [`start`](skills/start/SKILL.md) | New project: an interview, then a running skeleton with one check command, guardrails, CI, decisions and risk zones, before any feature |
| [`assess`](skills/assess/SKILL.md) | Existing project: the score, which modules apply, the gaps with evidence and the next three steps. Read-only |
| [`spec`](skills/spec/SKILL.md) | Acceptance criteria sized to the change, then tests written first in a separate context |
| [`review`](skills/review/SKILL.md) | A fresh-context review from the criteria and the real check output, deepest in red zones |
| [`refactor`](skills/refactor/SKILL.md) | Restructuring with no behaviour change: callers traced, tests green before and after |
| [`decide`](skills/decide/SKILL.md) | ADRs, and the evidence recorded back once a feature is built |
| [`sensor`](skills/sensor/SKILL.md) | A recurring mistake becomes a check whose message says how to fix it |
| [`garden`](skills/garden/SKILL.md) | Finds stale instructions, drift and overdue follow-ups; proposes small fixes |
| [`measure`](skills/measure/SKILL.md) | Whether agent work holds: corrections, rework, escaped defects, test reliability and maintainability trends |
| [`operate`](skills/operate/SKILL.md) | The Operate module: one contract for people and agents, read-only until granted, every write attributed |
| [`route`](skills/route/SKILL.md) | Optional: which model and effort for each role, without launching anything |
| [`context`](skills/context/SKILL.md) | Optional: gathers or recovers the evidence a long task needs, from the repository |

## Use it

### 1. Install

Until Agent804 is in a plugin marketplace, download it from GitHub: get the latest
`agent804-<version>.zip` from the repository's Releases page and unzip it somewhere it can
stay, for example `C:\tools\agent804` or `~/tools/agent804`. Keep the folder whole: skills
find the templates and tables by relative path, so a skill folder copied on its own breaks.

| Host | Install from the unzipped folder | Run a skill |
|---|---|---|
| **Claude Code** (desktop Code tab, terminal, web, IDE) | `/plugin marketplace add C:/tools/agent804`, then `/plugin install agent804@agent804`. The folder carries its own marketplace file | `/agent804:start` |
| **Codex** (desktop app, terminal, IDE) | Add the folder as a local plugin (it reads the root `plugin.json`), or link its skills into the project's `.agents/skills/`. Not both | Ask for the skill by name |
| **Grok Build CLI** | Follow the [Grok recipe](framework/agents/grok-build.md); confirm with `grok inspect --json` that the skills are found | Ask for the skill by name |
| **Cursor and others** | Nothing to install | "Follow `<folder>/skills/start/SKILL.md`" |
| **ChatGPT or an API chat** | See [chat hosts](framework/agents/chatgpt.md): without tools it can review what you paste, not run the check | — |

To update, replace the folder's contents with the new release (delete the old files first,
so removed ones do not linger), then in Claude Code run `/plugin marketplace update agent804`.
The stop hook and
permission settings differ per host; `start` installs the right ones from the
[host recipes](framework/agents/README.md). After moving the folder,
`python scripts/check_skill_resources.py <folder>` confirms the paths still resolve.

### 2. First run

**New project:** run `start` in an empty folder. It asks seven questions, one at a time
(what it is, what happens if it breaks, prototype or production, stack, who reviews, whether
agents will call it, how many write at once). Then it builds a running skeleton with one check command,
guardrails, CI, risk zones and a first ADR, and proves each control by making it fail once.
It asks before the first commit.

**Existing project:** run `assess`. It changes nothing. The first lines of its report are the
score, the three most serious gaps and the next three steps with rough sizes; the evidence
follows. Work the next steps, then run it again.

### 3. Every change

1. **`spec`** sizes the change. A small fix gets one or two criteria in the plan; a large one
   gets an interview and a spec. You agree the criteria before any code.
2. **Tests first, in a separate context**: a fresh session or subagent writes the acceptance
   tests from the criteria and shows them failing.
3. **Build** in another fresh context until the check is green, without editing those tests.
4. **`review`** in a fresh context, from the criteria and the real check output. Then a person
   reviews before merge.

Restructuring with no behaviour change uses `refactor` instead of steps 1 and 2.

### 4. Every so often

- A mistake the agent makes twice becomes a check, with `sensor`.
- `garden` finds stale instructions, drift and overdue follow-ups, and proposes small fixes.
- `measure` shows whether agent work holds: corrections, rework, escaped defects and test
  reliability, against the last period.

Optional: `route` when you have several models or an allowance to plan; `context` when a task
spans many sessions or the evidence is incomplete.

## What it does not do

- Decide what is worth building.
- Replace experienced maintainers or human review. Reviewers must understand the change;
  red-zone work gets deeper review.
- Guarantee correctness. Tests and reviews can miss a misunderstood requirement, and agreement
  between models is not proof.
- Enforce anything by prose alone. A hook or setting protects nothing until it has been seen
  working in the host you use.

## Status

**Unreleased; the last preview was 0.3.0.** Rules still change; see [CHANGELOG.md](CHANGELOG.md)
and [ROADMAP.md](ROADMAP.md).

Tried on real projects:
- `assess` on two real Django repositories by independent agents working from the skill
  alone: three rounds under 0.2, and again under 0.4. Scores converged once ambiguous wording
  was fixed; the 0.4 round found the defects fixed since (GR-1 wording, guessed evidence) and
  others still open in the roadmap.
- The full flow on one real feature, from a one-line request: quality scenarios and ADRs read
  unprompted, a stop on a Proposed ADR (which caught a flaw in it), an agreed spec, tests from
  a separate context failing for the right reason, the build with the tests unchanged, review,
  and evidence recorded back on the ADR and the scenario.
- The Operate module, graded on one reference project.
- `assess` installed as a plugin in Claude Code and in Codex (ChatGPT desktop app).

Not tried yet:
- `start` on an empty repository, and the `refactor`, `sensor`, `garden` and `measure` skills.
- The small-change path of `spec`.
- The 0.4 skills, which now carry their own instructions, on a real feature.
- The Security and Parallel work modules on a project where they apply.
- The trial modules (Maintenance, Context, Routing); `assess` reports them without a score.
- The full flow under Codex or Grok Build, and live hook enforcement in either. Grok's
  offline inspection found all twelve skills; that is discovery, not enforcement.
- Any stack other than Django.

The kit's own check (Python 3.11+ and Git):

```bash
python scripts/check.py
```

It runs 50 regression tests (stop hooks for each host in disposable Git repositories, skill
paths, private names, read budgets and rule alignment) and checks
links, rule IDs, budgets and configuration syntax. It proves the kit is consistent, not that
it works in your project: run it on real repositories and change the rules that do not survive.

## License

[MIT](LICENSE), except [`templates/`](templates/), which is [MIT No Attribution](templates/LICENSE):
copy a template into your own project and change it freely, with no notice to keep.
