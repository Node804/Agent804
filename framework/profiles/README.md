# Stack profiles

`rules.md` says what must be true; a profile says how one stack makes it true. `start` and
`sensor` read the profile for the project's stack; `assess` uses it to know where to look.
Agent-host setup (instructions, skills, hooks) is separate: see [agents](../agents/README.md).

A profile is one file, `<stack>.md`, copied from `_template.md`. It has:

1. **Baseline**: the tools a new project gets (package manager, formatter, linter, type checker,
   test runner, architecture checker, task runner), with one line each on why.
2. **The check command**, in the order the steps run.
3. **Rule mapping**: for each rule that needs a mechanism, how this stack enforces it. A rule the
   stack cannot enforce is listed under **Gaps** with what to do instead. Never drop it silently.
4. **Skeleton**: what `start` generates for a walking skeleton, including safe defaults,
   an allowed and a refused request, and who owns security findings.
5. **Gotchas**: things in this stack that pass every check and still break.

Rules that are pure process (decisions, review, measurement) need no mapping.

## What exists

| Profile | Status |
|---|---|
| [Django](django.md) | Reference: run on two real projects. Mappings marked † have not run yet |

That is the only one, on purpose. A profile written ahead of time, for no project, guesses
at versions and mechanisms and goes stale. For any other stack, `start` copies
`_template.md` into the project as `docs/stack-profile.md` and fills it in with the user,
against the real project and its real versions. It stays **Draft** until it has run.

A profile is added to this kit only after it has been used on a real project: bootstrap,
check and CI working, a refused request shown to fail safely, and the gaps written down in
[validation](../validation.md) and the README status.

## What a new profile maps

Use this table when filling in `_template.md`. Each row needs a mechanism or a listed gap.

| Rules | Mechanism to set up and exercise |
|---|---|
| IN-1, IN-3 to IN-5, CK-2 | Agent instructions, plus checks for line budgets, paths and links |
| CK-1, CK-4, CK-6, CK-8 | One check command with useful messages, editor or pre-commit feedback, CI from committed state, merge protection |
| ST-1 | The language's standard style through its usual formatter and linter, configured and pinned, run by the check without rewriting files |
| RV-1 | How a person's review before merge is required and recorded |
| GR-1 to GR-4, GR-7 | Test credentials and data, a task branch per change, human approval for commit/push/deploy, a completion check the agent cannot skip, and instructions that only a person approves |
| GR-5, GR-6 | Sandboxed unattended runs; data scripts dry-run by default |
| MT-1 to MT-3 | Interface documentation checks, complexity, file-size and duplication limits, unused-code reports |
| TS-1 to TS-12 | See [testing](../testing.md): separate acceptance tests, red then green, isolated test data, real integration boundaries, full test discovery |
| WK-4, WK-6 | Changelog check; a database, port and storage per checkout |
| SE-1 to SE-6 | Secret, code and dependency scanners in the check; reviewed dependency sources; safe defaults; abuse tests; an owner for findings |
| AR-1 to AR-6 | Access declared on every entry point, one write layer, import boundaries, one place for outside systems |
| OP-1 to OP-8 | When machines use the system: one operation contract, narrowed credentials, attribution, safe retries, bounded outside load |

Mixed stacks combine their mechanisms under one check. A profile grants no install,
production or deployment authority.
