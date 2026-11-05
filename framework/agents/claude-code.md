# Host: Claude Code

Historical reference workflow exists; revised setup still requires application trials.
Use the shared [host checklist](README.md) and record actual version/platform/tool scope.
This profile does not claim parity with every Claude client or deployment mode.

GR-4 requires current verification evidence. The supplied Stop integration is withdrawn
in 0.6 because the shared engine has known cache/input/process-bound limitations. Historical
Claude evidence does not validate that engine or other hosts. Use direct checks and CI.
GR-8 remains an opt-in Trial design for independently supported project integrations; the
[playbook](completion.md) supplies criteria, not a shipped runtime.

Keep `CLAUDE.md` as `@AGENTS.md`, with the shared rules in `AGENTS.md`. Inspect nested
instructions and effective settings; importing the root does not prove every source agrees.
Installed skills use `${CLAUDE_PLUGIN_ROOT}` paths; other hosts use the accompanying relative
paths from the intact kit. Validate installed resources and the skill selector in the host.

For project action controls, merge [claude-settings.json](../../templates/claude-settings.json)
into `.claude/settings.json`; review command patterns for the project. The starter contains
permission settings only, with no Stop handler. Preserve existing scope, trust and stricter
settings. File deny patterns supplement real credential/data isolation.

Run the declared check directly against the current changes and retain actual results.
CI runs independently; no automatic completion blocking is supplied by this release.
Removing kit files does not uninstall handlers already copied into another project. Review
those separately within the developer's authorized scope; do not remove existing diagnostics
or unrelated settings automatically.

Separate acceptance and implementation contexts and fresh review use the same handoff contract
as other hosts. Do not assume every subagent starts without inherited implementation context.
Record actual inputs and preserve independent expected outcomes. Human design/review decisions
remain distinct from permission prompts and mechanical metadata. No additional action
authority follows from a plugin installation or successful hook.
