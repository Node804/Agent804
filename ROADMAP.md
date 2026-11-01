# Roadmap

**Status:** 0.3.0, preview, not yet released. What has and hasn't been tested is in the
README's Status section; this page is what's next and why things are the way they are.

## Before the first public release

- [ ] Trial the revised [testing workflow](framework/testing.md) on an application: preserved
      red/green handoff without a commit, compiled missing-interface diagnostic, bug regression,
      discovery failure, isolated parallel fixtures and owned flake/quarantine remediation.
      Exercise selected TS-13 sensitivity cases before considering any new gate; re-score
      reference projects under the TS-10/TS-12, TS-11 and TS-8/TS-9 gates.
- [ ] Clearance to publish (private details in `HANDOVER.local.md`).
- [ ] First commit, and a remote under the Node 804 organisation.
- [ ] Install the plugin in Claude Code from a clean machine (`/plugin marketplace add`, then
      `/plugin install agent804@agent804`). Codex install is already tested.
- [ ] Rebuild the zip package after the last edits.

## Trials before 1.0

Each is one session. Record the result in the README's Status section, and fix whatever the
trial shows is unclear before moving on.

- [ ] Trial Grok Build CLI with actual trusted project instructions/skills/permissions and
      passing/failing native Stop continuation, reporting escape, timeouts and worktrees.
      Reconcile the public/upstream hook-doc discrepancy for the tested client; verify actual
      OS/network isolation and keep web/mobile Build Mode separate from CLI capability claims.
- [ ] Trial MT-5 debt management: confirm/reject candidates, reuse scoped deferral, revisit
      overdue/triggered review, repay in authorized feature/refactor work and verify closure.
      Include partial repayment and renamed items; prove ticket creation does not waive a
      defect, unmet criterion, failing check or security acceptance requirement. Keep MT-5
      a reported practice until real adoption evidence supports a change.
- [ ] Trial scoped context and recovery on equivalent maintenance tasks: stale/current
      authority, cross-file constraints, superseding decisions, truncated evidence, dirty
      work missing from an index and insufficient evidence. Predefine expected outcomes;
      record missed contracts, actual recovery, unnecessary reads and overhead under MS-4.
      IN-8/WK-8 remain practices; no extra model sessions are authorized by this checklist.
- [ ] Trial optional routing with one model/separate contexts, multiple classes in one family,
      and multiple providers where access/data/spend policy permits. Record native effort,
      shared/unknown/exhausted allowances, bounded escalation and adversarial input boundaries;
      compare equivalent accepted outcomes including retries/transfer/rework. Actual calls
      and paid trials require applicable authorization; WK-7/MS-5 remain conditional practices.
- [ ] Exercise host capability records and equivalent bug-fix/feature/refactor/review fixtures
      in Claude Code and Codex. Verify actual instruction discovery, nested overrides, intact
      relocated skill resources, hook trust/loading/failure continuation and missing-control
      reporting on the tested clients/OS; don't infer other surfaces from one CLI trial.
- [ ] Trial `refactor` on a scoped existing-code change: capture consumers/contracts and
      baseline, add immediately passing characterization tests where needed, restructure in
      small steps and verify final preservation/retirement. Exercise a hidden behavior-change
      case and an unknown consumer without claiming equivalence. MT-4 stays a practice.
- [ ] `start` on an empty repository, through to a green check and a walking skeleton.
- [ ] One small change end to end, to prove the light path really is light.
- [ ] The full flow under Codex: spec, separate test session, build, review, evidence. Work out
      Codex's equivalents for the stop hook and the commit/push/migrate approvals (GR-2 to GR-4).
- [ ] Exercise a non-Django Draft profile on a real application before considering Reference
      promotion; record its resolved mappings, bootstrap/check/CI, refusal evidence and gaps.
- [ ] Someone other than the author runs `assess` cold on their own repository.
- [ ] Run `sensor`, `garden`, `measure` and `operate` once each on a real project.
- [ ] Trial two concurrent worktrees with separate databases and ports, an explicit test
      handoff, combined-change verification and cleanup; exercise the strengthened retry
      contract and append evidence without editing an Accepted ADR.
- [ ] Reassess reference projects against the revised maintainability gates; trial the Django
      complexity and contract checks, gradual adoption baseline and retirement review. Record
      an MS-4 maintenance exercise with an unfamiliar human and a fresh agent context before
      considering it as a gate.
- [ ] Trial SE-1 to SE-6 and revised reference-project scores: versioned requirement mapping,
      scanner detection/error/staleness, dependency trust and isolated builds, secure skeleton,
      abuse tests, expiry-aware human decisions and a safe response exercise. Verify one
      authorized release/environment readiness record independently of its Build score.
- [ ] Trial ST-1 to ST-3 with custom and default styles, staged adoption and tool upgrades.
      Exercise all optional language starters, error/skip handling and repeated-pass stability;
      include Laravel Blade, WPF XAML and WinForms designer/resource round-trips. Reassess
      reference scores without treating style-only recommendations as complete stack profiles.
- [ ] Trial AP-1 to AP-4 and RV-1 at the revised gates: original human sources/authority,
      scoped cross-session reuse, material changes, permitted status transitions, requirement
      trace and actual host stale-review enforcement. Validate native/source adapters; byte
      freshness and synthetic records alone do not establish human approval.

## Known gaps

- The guardrail mechanisms (stop hook, permission rules) are Claude Code's; Codex needs its own.
- Under Codex, skill names show without a prefix (`spec`, `start`), so they can clash with
  other skills.
- Items marked † in `framework/profiles/django.md` have not run on a real project.
- All other stack profiles are Draft, including Laravel's PHP and WPF/WinForms' .NET
  inheritance. Their recipes still require project implementation and application trials.
- Not yet read, so not relied on: arc42 §10 and the SEI's quality attribute scenarios (the
  quality scenarios follow their form); StrongDM's "software factory" write-up; the DORA 2025 AI
  report; METR's 2025 developer productivity study.
- The scoring rules are sensitive to wording. Any change to `rungs.md` or a rule's Check column
  should be followed by a fresh `assess` run on the reference projects.

## Decisions so far, and why

- **Name: Agent804.** Ties to the Node 804 organisation. "Harness" names clash with Harness
  Inc.; "Node" reads as Node.js; "Factory" clashes with Factory.ai and "AI factory" hardware.
  The tagline, "build the harness before the app", says what it is.
- **Licence: MIT, with `templates/` under MIT No Attribution.** Templates are meant to be copied
  into other projects and edited, so they shouldn't carry a notice.
- **Credit: Node 804.** Copyright, manifests and the framework's origin name the organisation,
  not a person.
- **Voice: plain.** "I built this, then checked it against and reinforced it with these
  references." `framework/validation.md` records what each reference reinforced and why
  Agent804 chose differently where it did, without per-rule citations, academic framing or
  claims about going further. Agreement is never presented as origin.
- **Two plugin manifests.** `.claude-plugin/plugin.json` for Claude Code, root `plugin.json` for
  Codex; the check fails if they drift. Codex labels a privately added plugin with the account
  that added it, whatever the manifest says.
- **Scoring.** Build rungs 1–4 are strict and cumulative (the foundation); 5–8 are independent.
  A rule with a hole is "partly met" and leaves the rung "met with holes"; only a missing
  protection fails a rung. Operate (O1–O3) is scored the same way, separately. Earlier versions
  failed a rung on any partial rule and swung scores on trivia; three assessment rounds settled
  this form.
- **GR-1 judges impact.** Production secrets in the agent's reach fail it; production reachable
  with no credential at all is an outside risk, not a failure. Never infer a secret from a
  placeholder.
- **Quality scenarios above decisions and specs (DC-5).** Status changes only when tests pass;
  evidence flows back from specs to ADRs to scenarios.

## Changing the framework

1. Read `AGENTS.md` and `framework/validation.md` before changing a rule.
2. Run `python scripts/check.py`.
3. For scoring or rule-wording changes, re-run `assess` on the reference projects with fresh
   agents that follow the playbook alone, and compare with the previous scores.
4. Add a line to `CHANGELOG.md`.
