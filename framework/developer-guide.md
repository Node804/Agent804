# Using Agent804 as a developer

Agent804 helps you establish protections around agent work and use them during ordinary
development. You choose the scope, answer project-specific questions and review the result.
The agent can create configuration, checks, tests and documentation; your existing project
and its conventions are the starting point.

You can begin before earning a level. [Levels](levels.md) describe protections demonstrated
by evidence; they are not an entrance requirement. There is no one-time conversion that
makes a repository permanently compliant. Protections need to hold as the code changes.

## Choose a starting point

Install the intact kit using the [README](../README.md#1-install), then open the project in
your coding agent. Ask for the skill by name, or use your host's plugin command.

| Situation | Begin with | Result |
|---|---|---|
| Empty or nearly empty project | `start` | A running skeleton and exercised harness, or explicit setup gaps |
| Existing code; you want to understand its position | `assess` | A read-only assessment and one recommended next action |
| Existing code; you want help putting protections in place | `adopt` | One guided, implemented improvement and a continuation point |
| Already working with the harness | `spec` or `refactor` | A change sized to the task, with verification and review |
| Agreed work spans several changes | `plan` (Trial) | Verifiable increments, dependencies, integration checkpoints and a resume point |

`assess` does not install anything. `adopt` can use its findings, but a full assessment is
not required to begin. If you already know the missing piece, name it directly.

## Starting a new project

Try: **“Use start to set up this project. It is an internal scheduling tool.”**

Expect a short interview, one question at a time: what you are building, consequences of
failure, prototype or production, stack, who reviews, AI-facing surfaces and concurrent
writers. Answers already supplied do not need repeating. You remain responsible for the
product choices and for having someone able to review the code.

The agent creates a small running application, project instructions, one check command,
guardrails, CI and the records needed for its first change. It demonstrates that controls
actually work. The initial destination is Level 2 — Controlled; configured but unexercised
review or host controls remain explicit gaps, not an earned level.

Review the commands and evidence before accepting setup. Bootstrap and local checks should
be reproducible; a CI file alone does not show a successful CI run. Once setup is ready,
describe a small first feature and use the daily workflow below. Installing the kit and
setting up a project do not give the agent permission to commit, deploy or access production.

## Bringing an existing codebase into alignment

Try: **“Use adopt on this repository. Help me create the missing check command; keep the
existing tools and limit today's work to that setup.”**

The adoption workflow starts with what already works. Existing instructions, formatter
configuration, test runners and CI can satisfy the framework; their names do not need to
change. It will help you choose missing conventions and implement them, rather than hand
you a checklist to execute yourself.

You agree one useful increment and what proves it works. That increment can have several
dependent steps. Your time and change scope determine a stopping point; the target level
provides direction without making every gap part of today's assignment.

For a project missing style guidance and a check command, a possible sequence is:

| Increment | Questions you settle | What the agent creates or proves |
|---|---|---|
| Establish style | Keep an existing convention or use the language standard? Which languages are maintained? | Project-owned guidance/configuration, compatible formatter/linter, report and fix commands, evidence that checking does not rewrite files |
| Establish the check | Which commands already work, and what cannot run yet? | One runner around available checks, failure propagation, test counts and honest missing-scope reporting |
| Connect the controls | Which host and CI do you use? Who reviews? | Project integration and safe exercises; unavailable host controls remain gaps |
| Apply it to real work | What small feature or bug is next? | Criteria, focused tests, implementation and review using the new protections |

This order is illustrative. A missing test runner may need attention first; an exposed
credential may need an immediate response. A formatter migration across the repository is
a separate decision, not a side effect of adopting a convention.

Existing failures do not disappear. An initial runner can be useful while reporting missing
checks and an incomplete result. Do not read that as a green full check or Level 1. Narrow,
reviewed maintainability baselines can preserve specific legacy findings while preventing
new or worsening ones; they cannot excuse test failures or accept security exposure.

At the end, the project has a short continuation record, usually
`docs/agent804-adoption.md`, or a link in its existing plan. It records decisions made,
changes and evidence, remaining limits, and where to resume. It is not a second issue tracker.
Next time, say **“Continue adopt from the project record, with one more small increment.”**

Run `assess` when a broader view or an updated level would help. Its first recommendation
should explain one bounded next action; optional follow-ups are possibilities, not a demand
to fix the whole codebase. Urgent risks remain explicit. The full findings preserve evidence
without automatically becoming an implementation backlog.

## Daily development

The normal entry point is the affected area's [current behavior description](current-behavior.md),
which can be an existing README section or contract guide. It answers what the area does
without a tour of past changes. History explains how it got there; applicable decisions
still constrain changes. Adoption can establish one area at a time from inspected sources.

Start from the ordinary work you need to do. Tell the agent the outcome and relevant limits;
it should size the process to the change. The developer's decisions and handoffs matter more
than memorizing every skill name.

| Work | Your part | Agent work and evidence |
|---|---|---|
| Feature or bug fix | Describe the outcome; agree criteria before implementation | `spec` sizes the change; acceptance tests come from a separate context and show the intended failure before implementation |
| Larger delivery | Agree the outcome and decisions the evidence cannot settle | `plan` maps criteria to ordered increments, shared contracts and combined verification |
| Implementation | Resolve real uncertainties; keep the agreed outcome stable | Build from criteria and tests; preserve existing behavior; run relevant checks and record results |
| Refactoring | Agree the maintenance problem and preserved behavior | `refactor` traces consumers, captures a baseline and proves the exercised preservation scope |
| Review | Read and understand the final change before merge | `review` in a fresh context checks criteria, evidence and risk; findings are resolved or reported |

A small bug might begin: **“Fix the duplicate reminder. Agree a focused regression case,
keep the change local, and show it failing before the fix.”** A large feature needs more
questions and a written spec; a typo does not need the full interview. Acceptance-test
independence can use one model in separate contexts; multiple models are optional.

For a larger request, `spec` helps uncover missing requirements: current users and behaviour,
desired outcomes, constraints and consequential assumptions. Interaction changes include the
relevant journey, errors, refusal, recovery and accessibility needs. Existing answers and design
conventions keep the interview focused. Proposed assumptions remain visible until resolved.

Try: **“Use spec to clarify this request, then plan it as verifiable increments. Start with
one complete journey and show where the increments must be checked together.”** The Trial
`plan` skill extends the existing plan or tracker with criterion mappings, dependencies and
handoffs. A blocked prerequisite stays blocked; separate passing increments do not prove the
combined feature. [Planning rationale and limits](planning.md) explain the scope. Staffing
and release governance stay in your existing process; proposed parallel work starts no workers.

When changing contexts, pass the criteria, files/revision or patch, failing tests and actual
results. A red acceptance-test handoff is expected. Feature completion needs passing checks;
a summary saying tests ran is not execution evidence. A failing legacy check is reported,
not hidden or silently excluded to let the task finish.

You review the final behavior and diff; agent review and green checks support that judgment.
The delivered change also updates that area's maintained description with verified outcomes,
source/test links and evidence scope. Proposed changes remain in the spec/plan. Repository
checks do not prove what is deployed; known differences and unverified areas remain explicit.
Ask explicitly when you want a commit or push. Deployment, migrations and live settings have
their own authorization; agreeing to a feature does not authorize them automatically.

If adoption is still in progress, ordinary work can continue under the protections already
established and the developer's chosen risk limits. Missing protections and failed checks
remain visible; completing a feature does not make adoption complete.

## Keeping the protections useful

A recurring agent mistake is a candidate for `sensor`: turn a known failure into a check
that explains the fix. `garden` reviews drift and proposes scoped repairs. `measure` reports
whether the work holds using available evidence, without inventing missing metrics.

Choose a cadence appropriate to the project. Use `adopt` for the next missing protection,
`garden` for established guidance that has drifted, and `assess` to reconsider overall
position. Target satisfaction is a useful stopping point; further levels are optional when
the project's requirements do not demand them.

These journeys and `adopt` are new in 0.5. Fixture checks and scenario reviews establish
limited evidence only. Real-project adoption trials and reassessment remain pending.
The discovery and increment-planning extensions in 0.6 also await real-project trials.
