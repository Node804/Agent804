# Modules

The eight rungs are the **core**: every project built with agents needs them. Modules cover
problems a project has only in some situations: agents calling the system, sensitive data,
several agents writing at once. A module applies
when its trigger is true. Then it is scored, and a missing protection is a real finding. When
its trigger is false it costs nothing and the report shows `–`.

`assess` checks every trigger first and says which apply and why. `start` asks about them in
its interview.

## The modules

| Module | Applies when | Rules | Status |
|---|---|---|---|
| [Operate](#operate) | The project builds an MCP server, an API or tools for agents, or an embedded model feature (a chat, assistant, classifier, or generator). Scripts that call the system count | OP-1 to OP-11 | Scored, levels O1 to O3 |
| [Security](#security) | The system holds personal data beyond what sign-in needs (staff names and emails from sign-in do not count on their own), customer or business-sensitive data; handles money or safety; writes to another system of record; or people outside the development team can reach it | SE-1, SE-4, SE-5, SE-6 | Scored |
| [Parallel work](#parallel-work) | More than one agent or person writes to the repository at the same time: the instructions or tooling describe concurrent sessions, or history shows overlapping branches | WK-6 | Scored |
| [Maintenance](#maintenance) | The framework is adopted onto existing code, or the project carries known debt | MT-4, MT-5 | Trial |
| [Context](#context) | Work regularly spans several sessions or more than one context window | IN-8, WK-8 | Trial |
| [Routing](#routing) | More than one model is used for development, or development model spend is budgeted. A product that calls a model is Operate's concern | WK-7, MS-5 | Trial |

**Scored** modules are marked like the rungs: `✓`, `✓*`, `◐` or `✗` (see Scoring in
[rungs.md](rungs.md)). **Trial** modules have not yet been run on a real project, so the
assessment reports what it finds without a mark. A trial module becomes scored once a real
project has used it and the result is recorded in [validation](validation.md).

The core still applies inside every module. SE-2 and SE-3 (security checks in the check
command, reviewed dependencies) are core, and so are RV-1 (a human reads every change before
merge) and GR-7 (agents cannot supply consent; only a person accepts an ADR). A module adds
to them; it never replaces them.

## Reporting

One line after the core score, triggered modules first:

```
Modules: Operate O1✓ O2✓* O3◐ · Security ◐ · Parallel ✓ · Maintenance (trial) · Routing –
```

A triggered module applies whatever the project's target. For a prototype that will be thrown
away: Operate needs O1 and O2, Security needs SE-1, and the others apply as they would in
production. Everything else in a triggered module is a gap to close before production.

## Operate

This is how the project develops its AI-facing surface: an MCP server, an API or tools for
agents, or an embedded model feature. A mistake is a wrong write at machine speed, not a red
test. Guide: [operate.md](operate.md). Playbook: [`operate`](../skills/operate/SKILL.md).

| # | Level | Prevents | Gating rules | At it when |
|---|---|---|---|---|
| O1 | One contract | The UI, the API and agent tools disagreeing about what is allowed, and a tool list that is every function | OP-1, OP-5, OP-9 | Every action is declared once, with the same access rules, a designed name, schema, bound, and effect; credentials never travel in URLs |
| O2 | Safe by default | An agent with too much power, an unattributed or duplicated write, a foreign or session credential | OP-2 to OP-4, OP-11 | Agent access is read-only until a person grants write; writes name who acted; a repeat changes nothing; tokens were issued for this server, and a session is not a login |
| O3 | Bounded | Planted instructions, an embedded model that can approve itself, unbounded outside load, code nobody reviewed | OP-6 to OP-8, OP-10 | Data text is untrusted; an embedded model feature is specified and its output cannot approve or publish; outside calls have a budget; a person publishes definitions |

Levels are climbed in order: O2 means little without O1. Grade and mark every level, but
the level reached is the highest one with every level below it met or met with holes, as
with the foundation: `O1◐ O2✓` has reached no level. Start O1 with the first action: one
contract retrofitted over many hand-built endpoints is the expensive path.

## Security

The core keeps every project's checks honest: scanners in the check (SE-2) and reviewed
dependencies (SE-3). This module is for systems where a breach would hurt someone other than
the developer. It adds a threat model with versioned requirements (SE-1), safe runtime
defaults (SE-4), abuse tests for security-affecting changes (SE-5), and owned findings with
deadlines (SE-6). Guide: [security.md](security.md).

A rung or module mark assesses how the project is developed. It is not a security certificate
or permission to deploy, and settings checked locally say nothing about a deployed system.

## Parallel work

Two agents in one checkout trip each other's checks and share a test database. Each
concurrent writer gets its own checkout and its own databases, ports and storage; handoffs
name an exact revision; the combined result is checked again (WK-6). Guide:
[worktrees.md](worktrees.md).

## Maintenance

Bringing the harness to an existing codebase means refactoring code nobody fully remembers
and deciding which debt to carry. Refactors start from the maintenance problem, the affected
consumers and a green baseline, and report what they could not prove (MT-4). Confirmed debt
has an owner, a review date and verified closure; a debt ticket never waives a failing check
(MT-5). Guides: [maintainability.md](maintainability.md),
[technical-debt.md](technical-debt.md); playbook: [`refactor`](../skills/refactor/SKILL.md).

## Context

Long work loses its state to compaction, interruptions and handoffs. Decisions rest on
evidence with a known source and age (IN-8), and the approved scope, contracts and actual check
results can be rebuilt from files in the repository, not from chat (WK-8). Guide:
[context-management.md](context-management.md); playbook: [`context`](../skills/context/SKILL.md).

## Routing

Using several models, or paying for them, raises questions one model never does: which role
gets which model, what it may spend, and whether the cheaper route is actually cheaper once
rework is counted. Assignments are traceable (WK-7) and comparisons count total cost against
accepted outcomes (MS-5). One model in separate contexts is always enough. Guide:
[model-routing.md](model-routing.md); playbook: [`route`](../skills/route/SKILL.md).
