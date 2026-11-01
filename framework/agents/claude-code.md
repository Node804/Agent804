# Host: Claude Code

Historical reference workflow exists; revised setup still requires application trials.
Use the shared [host checklist](README.md) and record actual version/platform/tool scope.
This profile does not claim parity with every Claude client or deployment mode.

Keep `CLAUDE.md` as `@AGENTS.md`, with the shared rules in `AGENTS.md`. Inspect nested
instructions and effective settings; importing the root does not prove every source agrees.
Installed skills use `${CLAUDE_PLUGIN_ROOT}` paths; other hosts use the accompanying relative
paths from the intact kit. Validate installed resources and the skill selector in the host.

For supported Claude Code project setup, merge [claude-settings.json](../../templates/claude-settings.json)
into `.claude/settings.json` and copy [stop_check.py](../../templates/stop_check.py) to
`.claude/hooks/stop_check.py`. Select the actual interpreter/check command and review command
patterns for the project. Do not copy this configuration into Codex. Preserve existing scope,
trust and stricter settings. File deny patterns supplement real credential/data isolation.

Exercise passing/failing checks and the reporting escape in the actual host; shared engine
regressions do not establish hook registration. Verify each worktree's settings, resources
and private check state. The success cache excludes ignored files and external/time-dependent
state; refresh it when these change and run independent final/CI checks.

Separate acceptance and implementation contexts and fresh review use the same handoff contract
as other hosts. Do not assume every subagent starts without inherited implementation context.
Record actual inputs and preserve independent expected outcomes. Human design/review decisions
remain distinct from permission prompts and mechanical metadata. No additional action
authority follows from a plugin installation or successful hook.
