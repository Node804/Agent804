# Optional completion automation playbook (GR-8)

Use only after the developer opts into the Completion automation Trial module. Core GR-4
always requires current verification evidence; it does not require this integration.

**0.6 release boundary:** no completion adapter or Stop install recipe is shipped. The Codex
trial failed, and the shared Claude/Grok engine had known cache/input/process-bound defects.
The kit withdrew those implementations and their adapter fixtures, not their failure evidence.
Use direct checks and CI. The criteria below apply only to an independently supported project
integration explicitly selected by the developer; they are not instructions to recreate the
withdrawn adapters during ordinary setup. Existing installations are outside kit removal.

## Choose before installing

1. Identify the actual host/client, execution mode and bundled runtime version. PATH CLI
   version is not evidence of a Desktop engine version. Check documented lifecycle support
   and available trial evidence; unsupported automation stays a module gap, not a core gap.
2. Inspect the project's existing supported development tooling. Prefer it when it fits the
   host contract. Present the runtime choice and any new prerequisite before adoption;
   reuse existing scoped decisions. A historical runtime is not a mandatory application
   dependency; PowerShell, shell or another project-supported runtime can fit.
3. Prefer an existing tested adapter. For a different runtime, implement the smallest host
   adapter around the project's existing check command and demonstrate protocol parity in
   isolation. Do not invent event names, return formats or trust semantics. If a supported
   implementation is unavailable, retain direct check execution and report automation pending.

## Install within scope

- Preserve existing config and stricter policy. Installing a plugin does not authorize
  installing/trusting a completion handler. Live settings need the developer's authority.
- Disclose interpreter/tool versions and a reproducible install/bootstrap procedure, not
  just an executable found on this workstation. Never silently install a runtime or switch
  host/global settings. Render per-checkout paths and validate after relocation/worktree setup.
- Keep the host adapter separate from the project check. A native-language adapter may call
  the existing PowerShell/.NET or other runner; no shared runtime engine is supplied by this preview.
- Record rollback/removal instructions and changed files. Review the trust surfaces before
  granting trust; explain that instrumentation/config changes may require renewed trust.
  Never bypass trust to complete an adoption report or remove another active diagnostic.

## Prove the selected behavior

Test success and nonzero child results, empty/missing required suites, malformed/partial
and held-open input, child launch failures, timeout/cancellation, reporting escape, cleanup
and relocation. Set bounds below the host's timeout where feasible and test actual behavior.
Do not rely on cached success across participating repositories unless every relevant state
is covered; disable that reuse or fix the fingerprint first. Ignored inputs, external state
and advisory freshness need their own invalidation or fresh checks.

Use a bounded safe actual-host trial. Record separate evidence for configured, discovered,
trusted, invoked, input received, check started/finished and continuation observed. A
separate hooks/list process or an exit-2 fixture is not the active chat's lifecycle. The
trial may end with an honest unresolved-failure report; that escape is not a green check.

If diagnostics are needed, agree the change and its trust cost first. Use per-invocation
correlation and safe event/turn identifiers where available, phase, exit status and failure
type/timeout/cancellation. Keep diagnostic data bounded and private; never log assistant
messages, payload contents, credentials, full environment or unchecked tool output. Record
the difference between synthetic and actual-host events. Don't assume an unmatched start
means EOF blocking or that a nonzero result means the project check ran.

## Stop troubleshooting with evidence

Set an attempt/time boundary with the developer. Each retry must test a specific hypothesis
and add evidence. Do not loop through trust/restart requests. When the boundary is reached,
record the failing stage and next bounded investigation; direct verification and CI continue
without claiming the module works. Do not disable required CI or weaken tests to compensate.

Use the [host record](../../templates/agent-host.md) or equivalent existing notes. Preserve
observed limits, actual versions and rollback state. No additional model calls, policy changes
or diagnostic removal are authorized merely by reading this playbook.
