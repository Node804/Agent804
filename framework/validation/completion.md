# 0.6 completion evidence and optional automation

The developer approved this separation after the [0.5 Desktop trial](codex-desktop.md).
That trial did not establish correlated automatic continuation and exposed an inappropriate
implicit Python prerequisite in a project with existing PowerShell/.NET tooling. It also
produced useful fixture/discovery evidence and independently reproduced cache/EOF limitations.
These are agent-harness concerns, not reasons to require the same hook runtime everywhere.

## Design decision and compatibility

Core GR-4 now grades actual verification evidence for current changed state and honest
success claims. Failed, skipped, stale or missing required checks cannot support completion.
Core gate membership remains 38 IDs; the meaning of GR-4 changes. Earlier hook-based findings
need reassessment, not automatic score translation. CK-1, CK-8, testing and human review stay.

GR-8 belongs only to the developer-opted-in Completion automation module, initially Trial.
No opt-in means not applicable. Unsupported or unsuccessful opted-in automation produces a
module finding, not a core penalty merely for a missing hook. Historical Claude evidence
does not prove Codex, Grok or new host/runtime implementations; all retain observed limits.
An attempted field trial alone no longer implies a Trial module is ready for scored promotion.

## 0.6 release disposition

The Codex trial failed to auto-continue despite attempted remedies. The supplied Claude/Grok
shared engine also had dirty-gitlink cache reuse, EOF-dependent input and unbounded child
execution. The developer authorized resolving these risks by fixing or withdrawing the
recipes; the release withdraws all supplied adapters, hook starters and enabling flags.
Claude's action-permission starter remains, with no Stop handler. Direct checks and CI stay.

Adapter fixtures are retired because their runtime is no longer shipped, not to turn a
failing runtime green. Historical trial/regression observations are preserved here and in
the linked records; they do not establish current support. The kit's remaining tests cover
scoring, context estimates, resource layout and integrity. No runtime fix or live continuation
success is claimed, and existing project installations are not automatically changed.

GR-8 remains a Trial property for independently supported project integrations selected by
the developer. The [shared criteria](../agents/completion.md) retain runtime/installation,
input/child bounds, cache scope, lifecycle evidence and bounded troubleshooting requirements.
They are not instructions to recreate withdrawn adapters during ordinary adoption.

## References and evidence

- [Official Codex hooks](https://learn.chatgpt.com/docs/hooks), read during the trial review:
  Stop requests continuation, reports can escape after a prior block, and turn fields can
  support correlation. Configuration and a fixture exit code are not live-host evidence.
- [Official app server](https://learn.chatgpt.com/docs/app-server), read during the review:
  hooks/list describes discovery, distinct from a different process's active lifecycle.
- Historical Claude reference evidence remains in [validation](../validation.md); revised
  setup has not been exercised on every host/runtime, so no general enforcement claim follows.

This core/module choice is the developer's local framework design, not a guarantee from a
provider or a new published maturity standard. The kit check verifies gate/module separation,
rule alignment, references, budgets, version parity and remaining kit regressions. It cannot
establish truthful project claims, runtime acceptance or real continuation. Project-native
adapter parity, reproducible bootstrap/relocation and bounded actual-host trials remain pending.
