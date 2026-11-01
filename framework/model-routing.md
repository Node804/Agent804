# Model routing

Which model does which job changes the software, not just the bill. Three reasons:

1. **Capability matched to judgement.** Design, specification and review need the strongest
   model available. Searching the code, running checks and mechanical edits do not. A weak
   model on design gives worse architecture; the strongest model on everything spends the
   allowance before the work that needs it.
2. **Independent review.** A fresh context is always required (RV-2), but a reviewer of the
   same model shares the author's training, so its blind spots are likely to overlap. A
   different model, ideally from a different family, may catch different mistakes. This is
   plausible rather than measured; MS-5 is how a project finds out.
3. **Running out cuts the wrong steps.** When an allowance runs out mid-task, what gets
   skipped is the separate test context, the review and the final check: the steps the rest
   of the framework depends on. Plan so those are never the ones cut.

Routing is the Routing [module](modules.md#routing), a trial. One model in separate contexts
meets every rung; nothing here is required to climb them. The
[`route`](../skills/route/SKILL.md) skill recommends assignments; it never launches a model
or spends allowance.

## Roles and tiers

Write routing in roles and capability tiers, never model names: names date within months,
tiers do not. Map tiers to the models you actually have, and record the actual model used for
each role in the plan or PR (WK-7).

| Role | Starting tier | Why |
|---|---|---|
| Design, specification, architecture | Strongest | Ambiguity, trade-offs and constraints are where mistakes are most expensive |
| Review | Strongest, and a different model from the author where available | Judgement, plus independence |
| Acceptance tests | Strong or mid | Needs to reason from criteria, not from code; check its output types and lints before handover (TS-7) |
| Implementation | Mid, raised for security, concurrency or cross-module work | Most code is routine once criteria and tests exist |
| Search, running checks, mechanical edits | Fast | Speed and cost; deterministic tools do the checking |

These are starting points. Move a role up a tier when its results show it needs one, and down
when a cheaper tier produces the same accepted outcomes. Use each model's own effort setting
the same way: more for ambiguity and risk, not maximum everywhere. More effort cannot replace
missing requirements or evidence.

## Independent roles

Three contexts, whatever the models: **A** writes acceptance tests from the approved criteria
without seeing an implementation and shows them failing; **B** implements until they pass,
never editing them to fit; **C** reviews the criteria, tests, diff and real check results
before reading B's explanation. A, B and C may be one model in three contexts or three
models. Agreement between models is not correctness: deterministic checks and a human
reviewer (RV-1) still decide.

## Budgets and data

- Know which allowance or account pays for each role, and keep a reserve for review and the
  final check.
- When an allowance runs out, wait or hand off the work as blocked. Never silently fall back
  to paid API usage, buy credits, or drop to a tier below the role's minimum.
- Send code only to providers allowed to receive it. Access to a model is not permission to
  disclose the project to it.

## Measuring it (MS-5)

Compare routes on comparable tasks: accepted outcomes and defects first, then total cost
including retries, rework and review. Keep each provider's own units; do not convert
messages, credits and tokens into one number. Small samples suggest, they do not prove.

Re-check the tier mapping when models change (MS-3). A route that was right for last
quarter's models may not be right now.
