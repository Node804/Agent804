# Stack profiles

`rules.md` says what must be true; a profile says how one stack makes it true. `start` and
`sensor` read the profile for the project's stack; `assess` uses it to know where to look.

A profile is one file, `<stack>.md`, copied from `_template.md`. It has:

1. **Baseline**: the tools a new project gets (package manager, formatter, linter, type checker,
   test runner, architecture checker, task runner), with one line each on why.
2. **The check command**, in the order the steps run.
3. **Rule mapping**: for each rule that needs a mechanism, how this stack enforces it. A rule the
   stack cannot enforce is listed under **Gaps** with what to do instead. Never drop it silently.
4. **Skeleton**: what `start` generates for a walking skeleton.
5. **Gotchas**: things in this stack that pass every check and still break.

Rules that are pure process (decisions, review, measurement) need no mapping.

| Profile | Status |
|---|---|
| [django.md](django.md) | Reference: every rule mapped, used on a real project |
| Others | Not written. `start` on another stack writes a draft profile from `_template.md` with the user, marked Draft, and lists unmapped rules as gaps |

A profile is promoted from Draft to Reference only after a real project has run on it.
