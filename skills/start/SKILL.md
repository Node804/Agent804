---
name: start
description: Set up an empty project with instructions, checks, guardrails, a walking skeleton, CI and decisions before features. Existing code uses adopt; assess diagnoses read-only.
---

# Start a project

Target Level 2 — Controlled before the first feature, or report explicit gaps. No commit,
push, deploy or migration without the developer's specific instruction (GR-7).

**Resources:** Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/` and
`${CLAUDE_PLUGIN_ROOT}/templates/`; other agents `../../framework/` and `../../templates/`
from this file. Read only the sections/resources needed for the current step; do not preload
all profiles, templates, host recipes or historical records.

## 1. Establish the starting point and target

- Inspect files, branch and dirty work. Existing application code uses `adopt` (Claude Code
  `${CLAUDE_PLUGIN_ROOT}/skills/adopt/SKILL.md`; otherwise `../adopt/SKILL.md`) or read-only
  `assess`. Preserve changes; never automatically reset or stash.
- Initialize Git if needed; reuse an appropriate task branch or create one (GR-3), even
  for an empty repository on its default branch. Do not commit to enable worktrees.
- Read `framework/levels.md`: Practices, Scoring and How much a project needs. Read the
  trigger table in `framework/modules.md`; then only triggered module sections.
- Reuse known answers; ask remaining questions one at a time, offering a default:
  purpose/users; impact if it breaks; prototype or production; stack; who can review code;
  any MCP/agent API/tools or embedded model feature; concurrent writers. Sign-in names alone
  do not trigger Security; use the actual module triggers. Mark disposable prototypes in README.
- Recommend an established typed stack with a profile if no preference exists. If nobody
  can read the code, explain the remaining reviewer need and recommend small red zones.
  Set the target/additions and triggered modules with their cost in two or three sentences.
  Explain protections and consequential choices plainly; no rule/tool study is prerequisite.

## 2. Select mechanisms

Read `framework/profiles/README.md` and only the applicable stack profile. Without one,
copy `_template.md` into `docs/stack-profile.md`, agree actual mappings/versions and mark
Draft. Record missing mechanisms. Agree public-interface scope, complexity/file-size/
duplication limits and exception review before building (MT-2).

Use the shared host checklist, Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`,
otherwise `../../framework/agents/README.md`, and only the selected host profile. Record
actual version/capabilities using `templates/agent-host.md`; file presence is not enforcement.
For concurrent writers only, follow Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/worktrees.md`,
otherwise `../../framework/worktrees.md`. Before a baseline commit, work sequentially;
otherwise isolate checkout/resources and check state (WK-6).

Every project needs core scanners/dependency trust (SE-2, SE-3). If Security triggers, agree
owner, assets, trust boundaries, credible abuse cases, versioned requirements and finding
deadlines (SE-1, SE-6). Use the language's standard formatter/linter unless the developer
chooses another convention; record why (ST-1). Offer `templates/editorconfig` and
`templates/gitattributes`. Choose one debt record, initially empty. Only on routing opt-in
use `templates/model-routing.md`; setup launches no models or account probes.

## 3. Build in this order

1. **Tools:** use the profile's pinned package manager/lock file, formatter/linter, type/test
   runner, complexity/size/duplication checks and documentation/example/unused-code checks
   (MT-2). Keep judgment reports visible. Review dependency sources and build execution
   before installing (SE-3). Security checks show freshness, safe detection evidence and
   error/skip handling (SE-2). Format/lint checks report; separate commands fix (ST-1).
   Editor/pre-commit integrations use the same config; CI still runs the full check (CK-6).
2. **One check (CK-1):** wrap all applicable checks, document the actual command in
   instructions. `.agent-check` is optional completion-adapter configuration.
3. **Skeleton (SK-1, SK-2):** one rerunnable fresh-clone bootstrap, a running page/endpoint
   behind access control and a representative end-to-end test in CI (TS-5). Environment
   configuration has no hard-coded paths/hosts (SK-4). Show allowed/refused requests, the
   refusal with no effect (AR-1). When target requires AR-1, check entry points missing access
   rules; diagnostics tell the agent how to fix them (CK-4). Validate writes once (AR-4),
   parse input at boundaries and encode for destinations (AR-6). Document public contracts,
   failures/side effects (MT-1) and scoped navigation/test commands (IN-4).
   If Operate applies, use `operate` for O1/O2: one action declaration serves UI/API/tools
   under the same access rules, machine credentials start read-only, results are bounded
   and effect is server-enforced (OP-9). No production credential reaches a local process
   (OP-11); embedded prompts/allowed actions live in the repo and output cannot approve or
   publish (OP-10). Security-triggered projects demonstrate safe defaults (SE-4).
4. **Instructions:** merge `templates/AGENTS.md` as shared authority (IN-1), actual check
   first (CK-2), line budget enforced (IN-3). Keep the `spec` discovery instruction portable;
   verify resolution in the selected host without embedding local install/cache paths.
   Keep only otherwise-missed guidance; plain
   statements (IN-6), repeated procedures in skills (IN-7), area rules scoped. Preserve dry-run
   scripts (GR-6) and done criteria (WK-5). Link applicable security/worktree/routing records.
   Explain growth: a correction repeated twice becomes guidance; enforceable guidance moves
   to a check. For Claude Code, `CLAUDE.md` contains `@AGENTS.md`; verify actual host loading.
5. **Guardrails (GR-1 to GR-4, GR-7):** require human consent, task branches and current
   check commands/scope/results. Failed or missing checks remain incomplete. Isolate test
   credentials/data; no production secrets, except a GR-1 development exception the person
   decides and records in `docs/security.md`. Preserve stricter settings/trust when merging
   authorized action controls. Core needs no completion hook. Only for opted-in GR-8 and
   a supported host, use Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/completion.md`,
   otherwise `../../framework/agents/completion.md`; agree runtime/prerequisites first.
   No Stop adapter ships in 0.6; do not recreate withdrawn integrations during setup.
   Headless work states done/check/scope/stop/sign-off and runs sandboxed (GR-5).
6. **CI:** run the same check from committed state in a clean environment, blocking red
   merges (CK-8). Use `templates/pull_request_template.md`; a person reviews every merge.
7. **Records:** create only records needed for the selected scope, from the templates:
   ADR 0001 (Proposed) holds interview/stack/target answers with linked evidence (DC-1 to
   DC-3); `docs/specs/`, `docs/plans/`, `docs/evidence/` hold later work. Keep ADR/evidence
   templates as `0000-template.md`. Draw `docs/risk-zones.md` with the developer.
   Describe the running skeleton in an existing README/contract or `current-behavior.md`
   (IN-5). Replace the instructions' `<path>` with that location, and cite sources/tests,
   revision/patch and gaps. Unbuilt
   features stay proposed; local tests do not prove deployment. Add the profile's changelog
   mechanism (WK-4). Create `docs/maintainability.md` with checks, limits, interfaces and
   exceptions; no invented legacy baseline. Retain initial complexity, size, duplication and
   boundary-exception reports from installed checks in its Measurements index (MS-1), with
   date, revision/patch, command/tool version, scope, report links and unavailable coverage.
   Capture actual skeleton observations after fixture cleanup; snapshots approve no exceptions
   and do not establish trends. Create `docs/security.md` with core scanner/trust
   evidence and applicable exception/module sections, without secrets or sensitive incidents.
   For concurrent work, copy the worktree playbook to `docs/worktrees.md` and fill actual
   bootstrap/resource/cleanup commands. README links commands, policies, tests and evidence;
   instructions retain independent test contexts, truthful red handoffs and human review.

## 4. Prove and report

Run bootstrap and the full check; preserve actual output. Exercise negative fixtures through
the ordinary project check, preserving nonzero failures. In isolation, demonstrate:

- Selected host instruction/skill/resource discovery, effective controls and relevant refusals;
  configuration/fixture success alone cannot establish live host behavior.
- A missing access rule fails where AR-1 is implemented; each MT-2 violation fails; maintained
  examples run and unmapped mechanisms remain gaps. Exercise forbidden dependencies and
  undeclared cycles where AR-3 is implemented. For representative failures, inspect diagnostics
  for the offending location, violated constraint and concrete correction under the project's
  declared architecture (CK-4); a rule ID alone is insufficient. Show correction passes the
  exercised check, restore fixtures and report unrelated failures separately.
- A representative security detection (SE-2); `.env`/secrets ignored in Git status.
- A formatting violation fails without rewriting; targeted fix then an idempotent second fix.
- Test discovery/counts/skips/exclusions, nonzero propagation and unexpected empty-suite
  failure, isolated data and real skeleton integration (TS-10 to TS-12). Record environment,
  revision and results; unexercised mechanisms stay untrialled.
- Current completion evidence (GR-4); only opted-in supported GR-8 needs an actual correlated
  lifecycle trial. Unsupported/unverified automation is a Trial finding, not a core hook gap.
  Worktrees retain isolated resources and private state.

Report what exists and earned level/name against target. Apply `levels.md` Scoring: partial
or missing gates block; unresolved evidence permits only a separately named provisional level
with assumptions. A new skeleton cannot demonstrate historical review/TDD. Name unverified
CI/branch protection and other gaps. Suggest the first feature through `spec`; setup is not
security certification or deployment approval. Ask before any first commit; a suggested
message is “Project harness: check, guardrails, walking skeleton”.
