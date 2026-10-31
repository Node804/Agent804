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

A few ideas run through all of it:
- **A ladder you can score a project against**, so you always know where you stand and what to
  do next.
- **Nothing is done until a test proves it.** What the system must always do leads to the
  decisions that achieve it, then to specs and tests, and passing tests are what mark each one
  met.
- **Process sized to the change.** A one-line fix gets a test or two; a change that touches
  access or other people's systems gets the full treatment.
- **Agents using the system, not just building it.** Once an AI assistant can call what you
  built, it needs the same access rules as a person, read-only until someone grants more.

## Two halves

- **Build: how agents build the software.** Eight rungs, from an instructions file to
  measurement, each a few hours of work and each preventing a named failure.
- **Operate: how agents use the software.** Three levels: one contract for people and agents;
  safe by default (read-only until granted, every write attributed, repeats harmless); and
  bounded (untrusted text, outside load, a person publishes). Most guidance stops at the first
  half. Once an AI assistant can call your system, the second matters as much.

## What is in it

| Path | What |
|---|---|
| [framework/rungs.md](framework/rungs.md) | The eight Build rungs and three Operate levels, what each prevents, how a project is scored and how much it needs |
| [framework/rules.md](framework/rules.md) | The rules, each with an ID, its source and how to check it |
| [framework/profiles/](framework/profiles/) | How each stack enforces the rules; Django is the reference |
| [templates/](templates/) | `AGENTS.md`, ADR, spec, plan, risk zones, agent settings, stop hook, PR template |
| [skills/](skills/) | The skills below, as plain playbooks any agent can follow |

| Skill | Does |
|---|---|
| `start` | New project: interview, then a running skeleton with one check command, guardrails, CI, decisions and risk zones, before any feature; if agents will use it, the first action goes through one contract |
| `assess` | Existing project: Build foundation and coverage, Operate level, with evidence, and the next three steps. Read-only |
| `spec` | Acceptance criteria sized to the change; tests from a separate session, written first |
| `sensor` | A recurring mistake becomes a check whose message tells the agent how to fix it |
| `decide` | ADRs with Proposed / Validated / Accepted / Rejected and evidence |
| `review` | Fresh-context review from the acceptance criteria, deepest in red zones |
| `garden` | Finds docs, plans and decisions that no longer match the code |
| `measure` | Lead time, first-pass check rate, interventions, rework, escaped defects |
| `operate` | Agents using the system (Operate O1 to O3): one contract, read-only until granted, attributed, safe retries, untrusted text, bounded outside load |

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
`AGENTS.md` and its skills from `.agents/skills/`. Recent versions also have plugins and can
list a Claude marketplace as a source, so the same install may work there; that is not yet
tested with Agent804. Otherwise, point Codex at `skills/<name>/SKILL.md` and tell it to follow
the file. The hooks and permission
rules in `templates/claude-settings.json` are Claude Code's; Codex has its own approval and
sandbox settings, which need setting to match.

**Other agents** (Cursor and others that read Agent Skills or plain instructions): the same, point
the agent at `skills/<name>/SKILL.md`. The skills use only the portable frontmatter fields and
refer to the framework by relative path.

## The loop, once set up

1. Describe a feature. `spec` sizes it and writes acceptance criteria.
2. A separate session writes the tests and sees them fail.
3. A fresh session implements until the check is green; the stop hook will not let it finish
   earlier.
4. `review` in a fresh context; a person reads the diff and merges.
5. The same mistake twice: `sensor`. Weekly: `garden` and `measure`.

## What it does not do

- Decide what is worth building.
- Remove the need for someone who can read the code. It lowers the skill needed; red-zone
  changes still need a reviewer who understands them.
- Guarantee correctness. No check catches a misunderstood requirement; the acceptance criteria
  are where that is caught, so a person has to read them.
- Come free. Setup is about an hour; each feature carries a little ceremony, scaled to its size.

## Status

**Version 0.2, preview.** Rules will change; see [CHANGELOG.md](CHANGELOG.md).

What has been tested:
- `assess` on two real Django repositories, three rounds each by independent agents working
  from the playbook alone. Scores converged once ambiguous rule wording was fixed.
- The full flow on one real feature, from a one-line request: quality scenarios and ADRs read
  unprompted, a stop on a Proposed ADR (which caught a flaw in it), an agreed spec, tests from
  a separate context failing for the right reason, a tests-only commit, the build with the
  tests unchanged, review, and evidence recorded back on the ADR and the scenario.

What has not:
- `start` on an empty repository, the small-change path, and the `sensor`, `garden`,
  `measure` and `operate` skills.
- Any agent other than Claude following the playbooks, and any stack other than Django: the
  Django profile is the only one.

Böckeler's point that there are no unit tests for context applies here too: run it on real
repositories and change the rules that do not survive.

## License

[MIT](LICENSE), except [`templates/`](templates/), which is [MIT No Attribution](templates/LICENSE):
copy a template into your own project and change it freely, with no notice to keep.
