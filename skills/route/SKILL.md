---
name: route
description: Recommend model, host and supported effort assignments for development roles using actual access, project evidence and optional subscription/API budgets. Use when choosing or budgeting models or planning independent test/code/review roles; recommendations only, without launching agents or spending allowance.
---

# Route development work (optional)

Read routing guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/model-routing.md`,
otherwise `../../framework/model-routing.md` from this file. Host capabilities are in Claude
Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`, otherwise
`../../framework/agents/README.md`. WK-7/MS-5 are conditional practices, not rung gates.

This skill recommends assignments and handoffs. Do not launch models/agents, probe paid APIs,
scrape account dashboards, install plugins, change settings/accounts or transfer project
content to another provider. Preparing a recommendation uses available evidence; execution
and spending remain separately authorized. Do not expose credentials/private billing details.

## Establish constraints

Read project approval, security/data policy, risk zones and any existing model-routing record.
Identify the task's required outcomes, relevant contracts, execution tools and minimum quality.
Single-model use is valid: retain separate contexts for acceptance authorship and review.
No new routing document or extra subscription is needed merely to follow existing workflows.

Inspect provided model/host inventory and existing evidence first. Use current official
provider guidance for model-specific claims and effort support. Verify account entitlement
from available source evidence; a public catalog is not proof of access. Preserve explicit
user selections and identify missing values as unknown, not a guessed replacement model.
Ask for material missing access/budget/data constraints while continuing independent analysis;
never require credentials. A provisional recommendation must label its unresolved conditions.

## Recommend an eligible route

1. Filter candidates by permitted provider/data scope, actual access/host capabilities and
   task quality/risk. If none qualify, report a blocked recommendation and missing decision.
2. Assign roles, not permanent vendor rankings: triage, specification, acceptance author,
   implementer, adversarial reviewer and integration verifier as useful for this task.
3. Select native effort supported by that model/host, using project evidence or a labelled
   provisional default. Effort names are not equivalent across models. Distinguish power
   modes that spawn agents from single-model reasoning; never enable them implicitly.
4. Compare total expected overhead including retries, transfer, review and rework. Keep
   subscription pools/windows/units and API spending separate; do not invent remaining quota
   or equate messages/credits/percentages across providers. Prefer measured data; label estimates.
5. Set finite retry/time/usage bounds, verification reserve and evidence-based escalation.
   Fix context/setup/criteria problems before reflexively raising effort. Exhaustion means
   wait, an eligible authorized fallback or a blocked handoff; never silent paid fallback or
   dropping required quality. Unknown budget does not grant unlimited usage.

Use the optional template for non-trivial recurring policy: Claude Code
`${CLAUDE_PLUGIN_ROOT}/templates/model-routing.md`, otherwise
`../../templates/model-routing.md`. A small task may use existing plan/PR fields instead.

## Prepare independent handoffs

Use context guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/context-management.md`,
otherwise `../../framework/context-management.md`. Keep necessary contracts, source/freshness,
unknowns and actual verification state when changing models; fewer transferred tokens alone
does not demonstrate a better route. Compacted summaries need critical source revalidation.

Acceptance role A gets approved criteria and baseline contracts, not the proposed
implementation's expected answers. B implements from criteria/tests/red evidence. C reviews
criteria, contracts, tests, diff and real results before reading author conclusions. A/B/C
may use the same model in separate contexts or different models; record actual input boundaries.
Don't claim independence from a model/fork label or compaction. No finding quota, majority-vote
correctness or model replacement for deterministic checks/human review. Ambiguous criteria
need the responsible human; confirmed failures need bounded correction and verification.

Identify exact revision/patch, approved scope, checkout/resources, contracts and relevant
files, commands/results, known failures and next verification. Concurrent writers require
separate worktrees/resources (WK-6); sequential roles can reuse a checkout. Never fabricate
future execution results, actual model selections or approval sources in the proposed trace.

## Report

- Available evidence and unknown access/allowance/effort values.
- Recommended role/model/host/effort table, reasons and minimum quality constraints.
- Pool/spend assumptions, bounds, reserves and eligible fallback/escalation conditions.
- Exact handoffs and outstanding decisions; clearly mark recommendations as unexecuted.
- What to measure under MS-5: accepted outcomes, native usage/API cost, latency, retries,
  transfer/rework, human interventions and defects. Missing data remains missing; evaluation
  itself is not authorized by recommending it. No guaranteed saving or superiority claim.
