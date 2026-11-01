---
name: route
description: Recommend which model and effort setting should handle each development role (design, acceptance tests, implementation, review, search) using the models the user actually has, and plan independent review. Use when choosing models for a task or project, when an allowance is running low, or when setting up separate test, code and review contexts. Recommends only; never launches a model or spends allowance.
---

# Route work to models

Routing is a trial module; one model in separate contexts is always enough.

This skill recommends. It does not launch models or agents, change accounts or settings,
probe paid APIs, or send the project to another provider.

## 1. Find out what is available

- Read the project's `docs/model-routing.md` if there is one, and its security record for
  providers allowed to receive the code.
- Ask the user which models they have and which account pays for each, if unknown. Never ask
  for credentials. A model in a public catalogue is not proof the user can use it.
- Note the host each model runs in (`docs/agent-host.md`): a model without the tools a
  role needs cannot fill that role.

## 2. Recommend tiers for the task's roles

Map the user's models to the Strongest, Mid and Fast tiers, then assign the roles the task
needs. Starting points:

| Role | Tier |
|---|---|
| Design, specification, architecture | Strongest |
| Review | Strongest, a different model from the author where available |
| Acceptance tests | Strong or mid; pass independent validity checks; identify expected missing-interface diagnostics (TS-7) |
| Implementation | Mid, raised for security, concurrency or cross-module work |
| Search, running checks, mechanical edits | Fast |

Name tiers, not models, in anything kept in the kit; model names belong only in the
project's `docs/model-routing.md`. For each, give the model, its effort setting and one line
on why. Raise a tier for security, concurrency or cross-module work; lower one only where
results have shown the cheaper tier produces the same accepted outcomes.

Put review on a different model from the author when one is available, and say so when it
is not. Keep a reserve for review and the final check. If the allowance cannot cover the
roles at their tiers, say which step is at risk; recommend waiting or a blocked handoff,
never a silent paid fallback or a lower tier.

## 3. Prepare the handoffs

For each separate context, list exactly what it receives: the approved criteria, the
revision, the relevant files and commands. The acceptance-test context gets no
implementation; the review context gets the diff and real check results before the author's
explanation. Concurrent writers need separate worktrees (WK-6).

## Report

- The tier mapping and role table, with reasons and anything unknown.
- Which steps are at risk if an allowance runs out, and the plan for that.
- The handoffs.
- What to record afterwards (WK-7, MS-5): the actual model per role, accepted outcome,
  retries and rework. Mark everything as a recommendation, not something that has run.
