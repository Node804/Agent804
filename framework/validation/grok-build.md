# Grok Build integration evidence and limits

Historical evidence: the 0.6 preview withdraws the supplied Grok Stop adapter and its
fixtures with the shared engine. Results below describe earlier tests, not current support
or an active install/trial plan. Action settings and skill-discovery guidance remain.

Primary sources checked 2026-11-01; no xAI model or account endpoint was invoked.

| Reference consulted | Informed | Limits and choices |
|---|---|---|
| [Overview](https://docs.x.ai/build/overview), [instructions](https://docs.x.ai/build/features/project-rules), [skills/plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces) | Native root/scoped guidance, skill sources and Claude plugin compatibility | Metadata discovery is not execution. No third plugin manifest or extra routing frontmatter is needed; keep intact relative resources |
| [Public hooks](https://docs.x.ai/build/features/hooks) versus [upstream hook guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/10-hooks.md) | Older public page says Stop is passive; newer guide specifies blocking Stop, native camelCase flags, exit-2 feedback, trust and fail-open errors/caps | Historical adapter followed newer contract; it is withdrawn. Core GR-4 now grades current check evidence; opt-in automation is Trial GR-8. Never infer parity from Claude-compatible configuration |
| [Configuration scopes](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/05-configuration.md) and [permissions](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/22-permissions-and-safety.md) | Project permission rules versus user-only settings; merged ask/deny/allow and imported compatibility sources | Native prompt patterns are supplementary, not complete action authority. No global/user settings changed; no actual permission refusal was tested |
| [Sandbox](https://docs.x.ai/build/features/sandbox) and [settings reference](https://docs.x.ai/build/settings/reference) | Separate sandbox/action controls, platform/network limits and effort/config scope | No claim that a profile name protects every platform, credential path or in-process tool |

Local `grok --version` reports 1.0.70 (f50904eaee6c), stable; its extracted public hook guide
also describes Stop blocking and `stopHookActive`. `--help` exposes inspect, worktree,
permission-mode, sandbox, model and reasoning-effort options. Help/docs are not runtime proof.

In disposable project/user-home fixtures with updates disabled and credentials removed from
the child environment, `grok inspect --json` completed without a model call. A user-layer
`skills.paths` entry discovered all twelve kit skills. The normalized project root matched
the fixture; its untrusted state omitted project instructions, permissions and hooks. No
folder was trusted and no plugin loaded/invoked. This establishes offline skill metadata
discovery and the observed untrusted omission, not effective settings, authorization or trust.

Thirteen Python/Git fixtures exercise the native adapter/shared-engine pair: changed content
and commands, unborn commits, independent linked worktree caches, subdirectory discovery,
failed/missing checks, Git errors, invalid/malformed or foreign events, missing engine,
camelCase reporting escape and a rendered command from a subdirectory. Stdlib TOML/JSON
parsing and Python compilation cover starter integrity. No new runtime dependency on Grok
is required by the repository check; the CLI inspection is recorded separately.

Still pending: trusted actual-client loading, successful/failed Stop dispatch/continuation,
timeouts/caps, permission refusal and wrapper coverage, sandbox/credential/network controls,
installed-plugin invocation, subagent completion coverage, account model/effort entitlement
and complete feature/refactor/review workflows. Draft support is not a Reference promotion.
Web/mobile Build Mode and custom API access do not inherit this CLI evidence. Use the host
capability record and preserve missing applicable controls as explicit scoring gaps.
