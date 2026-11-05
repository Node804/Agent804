# Agent hosts and capability evidence

Stack [profiles](../profiles/README.md) select language mechanisms; host profiles describe
how an agent discovers instructions/skills, executes tools and applies controls. Models do
not define host capabilities. Keep the five domain policies shared across hosts.
Optional [model routing](../model-routing.md) selects role/model/effort within these host
capabilities; it does not install tools or establish permissions. One model remains sufficient.

| Host | Guidance | Evidence status |
|---|---|---|
| Claude Code | [claude-code.md](claude-code.md) | Historical feature trial; Stop integration withdrawn; action-control setup still needs trials |
| Codex | [codex.md](codex.md) | Desktop completion trial failed; Stop integration removed; direct checks and action-control setup remain |
| Grok Build CLI | [grok-build.md](grok-build.md) | Draft action settings and isolated skill discovery; Stop integration withdrawn, live action-control trials pending |
| ChatGPT and custom API hosts | [chatgpt.md](chatgpt.md) | Capability-specific guidance; no general execution/enforcement claim |

## Capability check before claiming protection

Record results in `docs/agent-host.md` using the [template](../../templates/agent-host.md),
or an existing equivalent. Record host/client version, model identifier where available,
OS/shell, orchestration/execution location, date, policy source and limitations. Never invent
an unavailable version. Distinguish configured, fixture-tested and exercised in the actual host.

| Capability | Evidence to obtain safely | Missing evidence means |
|---|---|---|
| Instructions | Inventory effective root/nested/override guidance and startup scope; resolve conflicts and loading limits | IN-1/IN-4 protection is not established from file presence |
| Skills/resources | Invoke intended skill, resolve its framework/templates after installation, check name collisions | Installed metadata alone does not prove a usable workflow |
| Check execution | Run an isolated passing and intended-failing check; inspect actual status/results | No claim of executed tests without tool output |
| Verification claims | Match current state, commands, scope/results and declared gaps to completion claims | GR-4 requires evidence, not automatic host blocking |
| Guardrails | Inspect effective action permissions and exercise applicable safe refusals | GR-2 remains a gap where applicable action controls are missing |
| Optional completion automation | Only after opt-in, follow the [playbook](completion.md) and record GR-8 runtime/lifecycle evidence | Trial module findings do not block core merely because hooks are absent/unsupported |
| Worktrees | Use the [lifecycle](../worktrees.md); verify installed paths, private state and isolated mutable resources in each checkout | A separate chat or branch alone is not concurrent isolation |
| Independent contexts | Supply criteria/contracts and exact artifacts to a separate test/review context; record its input boundary | Compaction or inherited implementation reasoning alone does not establish independence |
| Human approval | Approval comes from the person directing the work, in their own words (GR-7) | Tool permission and automatic approval are not consent to a design, a feature or a review |

`start` generates the host-specific setup and exercises it; `assess` inspects existing
evidence read-only. Neither may change user/global/admin policy, grant network access, install
plugins or run a paid host session merely to close a gap without applicable authorization.
Record unavailable facilities. A chat-only review can be useful without an executable harness;
it must not receive claims that require repository execution or blocking controls.

Automatic completion checks are opt-in Trial integrations. The [completion playbook](completion.md)
owns runtime selection/setup: existing project tooling first, new prerequisites explicit,
current check evidence still required. No completion adapter is shipped in 0.6; host recipes cover action settings and direct checks.

## Fresh context and handoff

For TS-3, WK-3 and RV-2, a separate chat or genuinely isolated agent context receives approved
criteria, relevant contracts, tests and exact revision/patch. Acceptance authors do not derive
expected behavior from the new implementation. Reviewers can inspect implementation/diff but
should form their assessment without the implementing context's conclusions. A fork/subagent
may inherit history; verify its actual inputs instead of inferring independence from its name.
Context compaction and a plan-mode switch are not evidence of a separate context. No subagent
or particular host command is mandatory; sequential separate chats may reuse one checkout.

Keep a compact handoff in the [plan](../../templates/plan.md): approved scope/decisions,
revision/patch and dirty work, checkout/resources, relevant files/contracts, commands/results
and known failures, unresolved decisions and next verification. Recover valid consent rather
than asking again merely because the context changed. Recheck artifacts before resuming;
chat summaries, memory and compacted history are pointers, not execution or approval evidence.

For scoped retrieval, incomplete output and post-compaction recovery, use
[context management](../context-management.md). Revalidate critical sources and dirty-state
changes; summaries do not promote hypotheses to facts or attempted checks to passes.

## Cross-host trials

Run equivalent isolated fixtures for a small bug fix, feature, refactor and fresh review.
Record initial artifact/revision, permitted inputs/actions, check/environment, client/model,
approval decisions, defects, human interventions, verification completeness and unrelated
changes. Include hook failure, missing trust/config, relocated resources and handoff recovery.
Do not compare generated lines or attribute differences solely to a model when host/tool
conditions differ. Actual host sessions and installation/trust changes need existing scope
or explicit authorization. Until exercised, recipes stay Draft; see [validation](../validation.md).
