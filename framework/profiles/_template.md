# Profile: <stack>

- **Status:** Draft
- **Applies to:** <language and framework, versions>

## Baseline

| Concern | Tool | Why |
|---|---|---|
| Package manager and lock file | | |
| Formatter | | |
| Linter (with security rules) | | |
| Type checker | | |
| Test runner | | |
| End-to-end tests | | |
| Architecture / boundary checker | | |
| Task runner | | |
| Changelog | | |

## The check command

```
<one command>
```

Runs, in order: format check, lint, types, architecture, framework checks, tests.

## Rule mapping

| Rule | Mechanism |
|---|---|
| IN-3, IN-5 | |
| CK-1 | |
| CK-6 | |
| GR-1, GR-2, GR-4 | |
| SK-1 | |
| SK-2 | |
| TS-4 | |
| AR-1 | |
| AR-2 | |
| AR-3 | |
| AR-4 | |
| AR-5 | |
| WK-4 | |
| OP-1 to OP-5 | |

## Gaps

| Rule | Why it cannot be enforced here | Instead |
|---|---|---|

## Skeleton

What `start` generates: <files and the one end-to-end test>.

## Gotchas
