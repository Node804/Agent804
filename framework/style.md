# Project-owned coding style

Each project chooses its conventions. Agent804 requires an explicit, coherent policy and
reproducible enforcement (ST-1 to ST-3), not a particular formatter or indentation preference.
The [style defaults](recommendations/style-defaults.md) and [starter templates](../templates/style/README.md)
are optional recommendations. Adopting or customizing them does not reduce compliance.

## Choose and record

Inspect existing configuration first, including nested files, editor settings and CI. Preserve
declared conventions unless a change is agreed. For a new project, apply user preferences;
where none exist, offer the profile's defaults and record the agreed choice. Later agents
follow project configuration; they do not replace it with framework defaults.

Keep a small language matrix in the project stack profile or style document. For each row,
identify language/grammar, maintained paths, convention, authoritative config, pinned runtime
and tool versions, check/fix commands, exclusions and remaining manual review. Config values
stay in their real files rather than being copied into prose. See the stack profile template.

A project normally has one policy per language. Independent applications in a monorepo may
have distinct policies with explicit boundaries and ownership. Nested overrides reflect
syntax or a deliberate project choice; a task or directory is not permission to invent one.

## Cover the real source

Inventory application code, tests, scripts, build/config files and maintained examples. Detect
new languages and grammars during review, including files without extensions. A formatter
for a base language may not understand embedded template syntax. Record unsupported areas as
gaps; an editor setting alone does not prove their formatting is enforced.

Generated and vendored files may have precise exclusions and reasons. Identify the generator
and its authored inputs; do not exclude hand-written wrappers or code-behind merely because
they sit beside generated files. If generated output must obey a style, fix its generation
pipeline rather than hand-editing the output. Review designer round-trips for UI code.

## Assign responsibilities

One authoritative formatter owns layout for an overlapping syntax scope. Import organization
or other fixers may be separate stages with declared responsibilities and order. Disable
conflicting layout rules; prove the whole chain converges instead of alternating its output.
Linters enforce additional adopted conventions; humans review naming, contracts and clarity
where automation cannot judge meaning. Formatting conformity alone is not code quality.

Keep editor configuration compatible with the CLI and CI. Shared encoding, line endings and
indentation settings help but do not replace syntax-aware checks. Select language/toolchain
editions and supported syntax explicitly where they affect output. Pin tools through the
project's lock files, manifests or verified build inputs; a moving latest alias is not a pin.

## Check and fix separately

The full project check runs all declared formatting and lint checks without rewriting source.
A separate command applies supported fixes within its documented scope. Development
integrations may format edited files; they must not rewrite unrelated user work. CI verifies
the complete declared scope independently and fails on violations, parser errors, missing
tools or unexpected skipped coverage. Printing diagnostics without failure is not enforcement.

Some tools report differences without a failing exit status, or lack a read-only mode. The
project wrapper must translate diagnostics into failure or format temporary copies and
compare them, preserving path/config context and leaving source untouched. Test the wrapper;
do not assume every command containing "check" enforces the policy.

Prove the adopted pipeline with a safe isolated fixture:

1. Introduce a layout violation in each claimed syntax scope and confirm a non-mutating check
   fails for the right reason, without changing the source.
2. Apply the declared fix pipeline and confirm the checks pass.
3. Run the full pipeline again and compare content; there must be no further change.
4. Verify local/editor/CI versions and settings agree, and that authored tests and scripts
   are included. Include a syntax-error fixture where exit-status handling needs a wrapper.

Record commands, versions, scope and results. A copied config does not establish ST-2.

## Exceptions, adoption and upgrades

Record exclusions and suppressions by exact path, rule or construct, with a reason and
reviewer. Add a review condition for temporary exceptions. A broad exclusion cannot hide a
missing language, an unsupported formatter or an unfinished migration.

Keep established coherent conventions. For an existing repository, prefer a reviewed
formatting-only change; for a large migration, record covered paths, remaining scope, owner
and completion plan. New and migrated files follow the chosen policy. Report partial
adoption as partial rather than claiming full scope; a maintainability baseline alone does
not waive style coverage. Avoid reformatting the whole repository during an ordinary feature.

Upgrade formatter versions, presets and shared configuration deliberately. Inspect output,
rerun convergence checks and the project check, then update the pinned environment and CI.
Keep formatting changes separate from unrelated behavior changes. Presets may change with
their tool version even when the config text stays unchanged.

Changes that also weaken security linting, CI gates or approvals retain their security review
requirements (GR-2, RV-3). An ordinary formatting preference does not need a new architecture
decision; use an ADR only when the choice is hard to reverse.

## Assess and maintain

At rung 2, ST-1 needs declared scope and real config, ST-2 needs exercised stable enforcement,
and ST-3 needs justified exceptions and controlled change/migration evidence. No exceptions
can be a valid result; no policy for exclusions is a gap. Unsupported scopes remain explicit.
Use the same criteria for custom project styles and framework defaults.

Review new languages, changed config, broad suppressions and unrelated reformatting in normal
review. Gardening finds drift between editors, local commands and CI and follows staged
migrations. Defaults and starters are draft until trialled; they are style support, not full
stack profiles establishing architecture, security, bootstrap or test coverage.
