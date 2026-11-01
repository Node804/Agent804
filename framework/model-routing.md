# Optional model routing and independent verification

Select the least total usage/cost that reliably meets the project's quality requirements,
including retries, context transfer, review and corrective work. This is an optional layer,
not a new rung. WK-7 and MS-5 are conditional practices pending trials, never scoring gates.
Single-model users can meet every rung through separate contexts and actual verification.

Use the [routing template](../templates/model-routing.md) only when useful, or equivalent
fields in an existing plan. The [route skill](../skills/route/SKILL.md) recommends assignments
and prepares handoffs; it does not launch models, switch accounts or spend allowance.
Host capabilities remain separate: see [agent hosts](agents/README.md). A suitable model in
a host without required execution tools cannot satisfy an execution role merely by name.

## Inventory and eligibility

Record provider, exact model/alias and observed revision where available, host/client,
supported effort settings, context/tool needs, access mode (subscription or API), and the
source/date of availability. Catalog access is not account entitlement. Unavailable or
unverified values remain explicit; don't replace a user's selected model without agreement.
Avoid model names in rules or permanent "best at coding/tests" claims. Current official
guidance is a starting point; representative project evidence informs role assignments.

Identify providers/hosts permitted to receive the project's code/data and any restrictions
before transferring artifacts. Access to a subscription does not itself approve disclosure.
Don't place credentials, account identifiers or private billing data in shared records.
Filter by data policy, actual tool/access capability and task quality/risk before cost.
An exhausted allowance does not authorize a weaker route below required protection.

## Roles and effort

| Role | Evaluate for the actual project |
|---|---|
| Triage/navigation | Accurate scope and evidence retrieval at low total overhead |
| Architecture/specification | Constraints, ambiguity, tradeoffs and measurable criteria |
| Acceptance author | Independent expected outcomes, boundary/refusal cases and meaningful red evidence |
| Implementer | Relevant language/tools, coherent edits and reliable execution |
| Adversarial reviewer | Concrete counterexamples and confirmed contract/criteria violations |
| Integration verifier | Actual combined-state checks, scope, discovery and failure interpretation |

One model may fill every role in separate contexts; different classes within a family or
multiple providers may fill them too. No fixed model count, provider diversity or particular
family/class is required. More agents or more opinions are not automatically better.

Route on role, task risk, model, native effort, host capability and budget together. Record
the actual supported effort value; labels are not equivalent across models/providers.
Start from the client's appropriate default or a project-tested setting. Narrow tasks may
need modest effort; ambiguity, security/concurrency and cross-module reasoning may justify
more. Maximum effort is not universal policy and more reasoning cannot replace missing
requirements, tools or evidence. Some host power modes can launch agents; don't treat them
as just another scalar effort value or enable them implicitly.

Escalate when concrete failures, unresolved contradictions or task complexity justify it.
First distinguish bad context, environment failure, unclear criteria and model limitations.
Set bounded attempts, elapsed-time/usage caps and an escalation trigger before expensive
cycles. A stronger model, more effort, narrower scope or a human decision may be appropriate;
no automatic retry storm or endless agent debate. Report unresolved blockers honestly.

## Subscription and usage budgets

Keep each allowance in its provider's actual unit/window, with source/time and confidence:
observed, user-reported, estimated or unknown. Name shared pools to avoid counting one balance
for each model separately. Do not convert messages, credits or allowance percentages into
fictional interchangeable token balances. Track input/output/reasoning/cache usage only
where exposed, and keep estimates separate from measured charges or quota consumption.

Subscription capacity and separately billed API access are distinct. Record allowed spend,
fallbacks, reset times with timezone, reserve for difficult work/final verification, and what
to do when exhausted: wait, use an eligible authorized route or return a blocked handoff.
Never buy credits, change plans or silently fall back to paid API access. Unused subscription
capacity may guide selection but does not establish that a low-quality route is cheaper.

Use focused context and exact artifact references, preserving necessary contracts and safety
constraints. Use deterministic tools for formatting/discovery/checks; avoid duplicating broad
repository reads and rerunning model reviews without new evidence. Account for transfers,
retries, verification and rework, not just the initial prompt. Host caching may reduce usage
but must not be assumed across providers or counted twice. Do not evade service limits.

## Optional adversarial workflow

1. Human-approved criteria and relevant existing contracts go to acceptance context A.
   It derives expected behavior independently of proposed implementation and preserves red
   evidence. Characterization for pure refactors follows MT-4 rather than invented red.
2. Implementation context B receives criteria, tests and exact baseline/handoff, implements
   and records actual green results. Test corrections follow TS-4 and affected approval.
3. Review context C inspects criteria/contracts, tests, revision/diff and actual check results.
   It forms an initial assessment without the author's conclusions; then explanations can
   help resolve findings. It seeks reproducible failures/counterexamples, not a finding quota.
4. Deterministic checks verify the combined result and a human reviews before merge (RV-1).
   Review may request new tests for missing protection, preserving their provenance.

A/B/C are roles, not required distinct models. Record the actual model/context per role and
any inherited inputs; same-model separate contexts satisfy the independence requirement.
Different models may share errors. Agreement is not correctness, a majority vote does not
override criteria, and a third model cannot establish an unexecuted check passed. Ambiguous
requirements go to the responsible human under existing approval policy; confirmed defects
receive bounded corrective work. Model review never becomes human architecture/merge consent.

Sequential roles may reuse a checkout. Concurrent writers use [worktrees](worktrees.md)
and isolated resources. Handoffs identify exact revision/patch, dirty work, approved scope,
contracts, permitted role/actions, results, known failures and remaining verification. Routing
recommendations do not grant permission to spawn agents, transmit code or change host policy.

Follow [context management](context-management.md) for role-specific retrieval and recovery:
retain authoritative references, scope/freshness and unknowns when changing models. Reduce
transfer overhead without dropping required contracts or treating summaries as approvals.

## Evidence and adoption

Evaluate representative tasks with equivalent starting artifacts, permissions, tests and
acceptance thresholds. Record model/host/version, effort, role, inputs, usage source/units,
latency, retries, interventions, unrelated edits, review findings and escaped defects.
Compare accepted changes and quality first, then total usage/cost and elapsed time. Include
failed attempts and switching overhead. Model aliases, releases and host changes may require
re-evaluation; no universal brand ranking or guaranteed saving is claimed.

For MS-5, distinguish marginal API spend, quota consumed and subscription fees. Do not add
unlike currencies/units or allocate a whole subscription fee to one task without a stated
method. Missing telemetry stays missing. Small samples and different task/host mixes limit
comparisons; observed association is not proof a model caused the outcome. No paid evaluation
or additional model session is authorized merely by enabling the policy.

Keep routing disabled by default. An existing scoped task can use an approved route without
repeated permission prompts; changing provider/data scope, spending authority or required
quality needs an affected decision. No automatic orchestrator, live quota scraper or vendor
connector is shipped. Templates/playbooks are Draft until real adoption trials.

## References

- [OpenAI model/effort guidance](https://learn.chatgpt.com/docs/models)
- [OpenAI usage factors and pricing](https://learn.chatgpt.com/docs/pricing?codex-pricing-plans=individual)

These inform native effort and usage interpretation, not cross-vendor rankings. Read current
official documentation for every selected provider and verify actual account/host support.
