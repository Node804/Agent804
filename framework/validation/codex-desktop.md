# Codex Desktop completion trial: unsuccessful

This records 0.5 behavior and historical follow-ups. The developer subsequently confirmed
that Codex did not auto-continue and none of the approaches tried enabled it. In 0.6 the
Codex adapter, hook starter, enabling flag and adapter fixtures are removed; the follow-ups
below are historical, not an active setup or retry plan. Existing project installations
are outside this kit-only removal. In 0.6, [completion automation](completion.md) moves to Trial GR-8;
the old hook outcome must not be treated as a new core GR-4 failure without reassessment.

Trial feedback received and reviewed 2026-11-03 against kit 0.5.0. A reference project used
the installed adoption playbook to add a partial check and project-only Codex integration.
The application had existing PowerShell/.NET tooling and a participating Git submodule.
Project identities, private paths and original logs remain outside the published kit.

## Scope and provenance

The developer described the host as ChatGPT Desktop; the chat context identified Codex
desktop. Do not extend this evidence to every Desktop surface. The trial report identified
PATH CLI 0.141.0 and a different bundled Desktop engine, 0.166.0-alpha.5.1. UI version and
actual model were not established. PATH version alone cannot identify the active runtime.

The report is the source for the live conversation outcome, approvals and app-server probe.
This review independently inspected the trace's limited fields, matched the installed
configuration hash to the supplied hash, and confirmed the two copied adapters match this
kit byte-for-byte. It did not independently replay the Desktop conversation or model turn.

The project check intentionally remains nonzero while required tests/style/security/CI and
runtime evidence are missing. Partial app/harness builds do not establish application,
installer, live-system or complete adoption success. Existing security findings remain open;
they were not accepted by this trial. No application behavior change was claimed.

## Evidence states

| State | Evidence and limit |
|---|---|
| Configured | Reported project-only config/handler installation with explicit developer approval; no global permission change |
| Discovered/trusted | Reported read-only bundled app-server initialize/hooks/list probe returned the correct handler enabled/trusted, without warnings/errors. A modified handler required renewed trust. This was a separate process, not the active chat's lifecycle |
| Fixture-tested | Reported six contracts pass for both unchanged adapter and temporary wrapper; first twelve trace records are synthetic and excluded from live conclusions |
| Wrapper entered/exited | Review found twenty records: after the synthetic baseline, three start/finish pairs return 2 and two starts lack a finish. Minimal fields cannot authenticate originating event/process/turn |
| Payload received | Not established by the wrapper trace; it logs started before reading stdin |
| Check started/finished | Not established by code 2. A separately reported restricted-shell probe fails on Git metadata access before the project check starts |
| Host continuation | Not visible in the trial report after ordinary stop attempts; later inputs were user-authored. Treat completion enforcement as unsuccessful/unverified, not passed |

The completed exit-2 pairs in the inspected trace were 12:34:51–12:34:54, 13:17:03–13:17:06,
and 13:17:48–13:17:51 UTC. Unmatched starts were at 12:32:20 and 13:22:24 UTC. Trace content
may grow after review. A discovery-only repeat reportedly left the earlier count unchanged;
that excludes one hypothesis for that probe, not every possible invocation source.

No decisive lifecycle correlation was found in the reported log patterns. Missing matches
do not prove a hook did not launch. Conversely, some code-2 invocations do not prove that the
active chat received a Stop block. The exact failure boundary remains unresolved.

## Independently reproduced implementation limitations

**Dirty gitlink caching:** a disposable nested repository tracked as a mode-160000 gitlink
was changed to one dirty content state, checked successfully, then changed again. Both
fingerprints were identical and the check counter remained one after the second request.
The outer diff represents a dirty gitlink without hashing its working files. This confirms
a cache-validity defect for checks covering participating nested repositories. The fixture
was not a complete registered-submodule integration trial. No stale success occurred in the
reference project's deliberately failing runner, which creates no successful cache entry.

**Held-open stdin:** a disposable adapter process received a complete valid JSON Stop object
with an active reporting escape. It remained running after 0.5 seconds with stdin open;
closing stdin allowed exit 0 with JSON output. `json.load(sys.stdin)` reads to EOF, and the
trial wrapper also calls `sys.stdin.read()` before launching the adapter. This confirms
EOF dependence, not that Desktop actually held the pipe open or caused an unmatched start.

The shared engine also has no internal child timeout, and the current contract fixtures
close stdin through subprocess input. A host timeout/cancellation can therefore lose a
completed adapter result; that specific live cause has not been demonstrated.

## Required follow-up, not completed fixes

- Select hook runtime with the developer from existing tooling. Python is this adapter's
  tooling prerequisite, not an application dependency or universal framework requirement.
  Its presence on one workstation is not portable bootstrap. Native runtime adapters or an
  explicitly installed supported runtime need parity evidence and per-checkout rendering.
- Disable cache reuse across participating repositories until all relevant states are
  fingerprinted or safe invalidation is demonstrated. Ignored config, outside services and
  advisory freshness remain separate limitations even with recursive tracked-file hashing.
- Add bounded diagnostics with a per-invocation identifier, event/turn correlation where
  available, input-received, check-started/check-finished, result and failure phase/type.
  Retain timestamps and cancellation/timeout outcomes. Do not record message/payload contents,
  environment, credentials or full check output; review identifier sensitivity/retention.
- Test held-open/partial input, launch exceptions, cancellation, timeouts, child cleanup,
  registered submodules and relocation. Use a fresh safe failing fixture to correlate a
  real Stop invocation to an observed continuation; if missing, record the exact boundary.
- Bound troubleshooting attempts and explain trust invalidation before changing handlers.
  Do not repeatedly request trust/restart without a hypothesis and new evidence. Preserve
  prior results and supply rollback/cleanup steps; no fixture authorizes live policy changes.

The installed diagnostic remains active according to the trial report. This review changed
neither that project nor its hook/trust state, and did not authorize cleanup/removal. The
untracked field-trial plan in this kit was preserved. Runtime/cache/diagnostic fixes and a
new correlated Desktop trial remain pending. GR-4 is not established by this evidence; the
reporting escape is intentionally bounded and independent CI/merge review remain separate.

## Official contract consulted

[Hooks](https://learn.chatgpt.com/docs/hooks) documents exit 2/stderr or a blocking JSON
decision as Stop continuation requests and supplies turn identifiers. The observed lack of
correlated continuation does not establish which side failed that contract.
[App server](https://learn.chatgpt.com/docs/app-server) describes hooks/list as discovery;
successful listing is not evidence of dispatch by a different active process.
