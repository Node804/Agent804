---
name: plan
description: Divide agreed work spanning several changes into verifiable increments, with dependencies, integration checkpoints and resumable handoffs. Use for a larger feature or dependent delivery work; a small change keeps its short plan in spec. Trial workflow.
---

# Plan verifiable increments

**Trial:** written for 0.6; not yet exercised on a real project. Planning does not build,
launch workers, commit or publish anything. Use existing project records (WK-2).

**Templates:** Claude Code `${CLAUDE_PLUGIN_ROOT}/templates/plan.md`; other agents
`../../templates/plan.md` from this file. Extend an existing plan or tracker instead of
creating a competing backlog. Omit sections that add nothing for this work.

## 1. Establish the boundary

- Read the agreed criteria, relevant ADRs, risk zones and affected code/contracts. Preserve
  the developer's scope and current work. Identify the revision and any uncommitted inputs.
- Link the current behavior description and proposed deltas from `spec` (IN-5). Include
  description reconciliation in each delivered increment; pending increments remain proposed.
- If criteria are missing or unresolved, use `spec`: Claude Code
  `${CLAUDE_PLUGIN_ROOT}/skills/spec/SKILL.md`; otherwise `../spec/SKILL.md` from here
  (TS-1, TS-6). Do not invent answers to make a schedule. Planning resumes after resolution.
- Reuse prior agreement; ask only for choices still needed. A new hard-to-reverse choice
  goes through `decide`. Record unresolved external dependencies as blockers, not promises.

## 2. Slice by observable outcome

- Give increments stable IDs within the plan. Map each agreed criterion to an increment
  and its verification; flag uncovered criteria and work with no requirement before handoff.
- Prefer a thin complete journey early, extending the walking skeleton when available.
  Each increment has an observable outcome and an independent verification boundary.
  Necessary infrastructure or structural prerequisites get an explicit consumer, check and
  reason; avoid splitting everything into database, backend and UI tasks that prove no journey.
- For each increment record dependencies, affected contracts, test approach, completion
  evidence and status. Split work that cannot be reviewed or verified coherently.
- Keep structural and behaviour steps distinct. Note deployment/migration dependencies and
  safe intermediate states; a temporary state must not expose unfinished or forbidden actions.
  Record a fallback or recovery decision when an increment changes persistent state.

## 3. Coordinate handoffs and integration

- Order increments by dependencies and risk. Resolve an uncertain contract or exercise a
  risky boundary early. Label any investigation as such, with a question and exit condition;
  an experiment is not a completed feature. Block dependants on unresolved prerequisites.
- Name the responsible session/person where known; otherwise say unassigned. State shared
  contracts and when combined changes must be checked, including the full journey at the end.
- Each implementation handoff carries criterion IDs, files/revision or patch, independent
  acceptance tests and actual red evidence (TS-3, TS-9); `spec` owns that test-writing flow.
  After implementation, retain green/full-check evidence and fresh-context `review` findings.
- Concurrent writers require separate checkouts and mutable resources, exact handoff
  revisions and a check of the combined result (WK-6). Candidate parallel work is a proposal,
  not permission to start sessions or spend a model allowance.

## 4. Resume and revise

- Keep pending, blocked, active and verified increments distinguishable. Verified means the
  stated criteria and checks passed; a checked box or generated summary is not evidence (GR-4).
- Record completed increments, current dependencies, actual results and one next action in
  the existing plan. Preserve earlier evidence with its revision; do not reuse it as current
  verification after changes. A partial delivery is not the whole feature completed.
- When learning changes the plan, record why and revisit affected increments, contracts,
  tests and integration checks. Material criteria changes return to the developer (GR-7).
  Check that revised dependencies have no cycles or dangling IDs before another handoff.
- Report proposed order, blockers, verification limits and the next increment. Distinguish
  authorized implementation scope from proposed follow-ups; a plan supplies no consent for
  commits, pushes, deployments or migrations. Staffing and release governance stay with the
  developer's existing process.
