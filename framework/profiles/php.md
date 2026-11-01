# Profile: PHP

- **Status:** Draft; no full application trial. Mechanisms must be generated and exercised.
- **Applies to:** Supported pinned PHP, Composer-based CLI/library/service projects.
- **Inherits:** [Shared baseline](README.md#shared-baseline); [Laravel](laravel.md) overrides framework-specific choices.

## Baseline

| Concern | Proposed mechanism |
|---|---|
| Dependencies | Composer with committed lock, platform requirements and reviewed plugins/scripts |
| Style | Project choice; offer explicit PER preset through PHP-CS-Fixer |
| Types/lint | PHP syntax checks and PHPStan at an agreed enforced level |
| Tests | Pinned PHPUnit with subprocess/HTTP acceptance tests and throwaway resources |
| Architecture | Namespace/public-interface rules checked by project AST/import tests |
| Security | Secret scan, static security rules, `composer audit` and effective runtime config/abuse tests |

## Check, bootstrap and skeleton

Generate a `composer check` script that runs the declared non-mutating fixer check, syntax
checks, PHPStan, architecture/docs checks, current security checks and PHPUnit, propagating
all failures. Pin any additional analyzer and define actual paths/config rather than relying
on tools' incidental defaults. A check never runs dependency updates or automatic fixes.
Generate `composer bootstrap` and `composer doctor` scripts: install reviewed locked inputs,
verify PHP/extensions, provision test/dev resources safely and identify actionable failures.
Add one executable command or endpoint and a real CLI/HTTP acceptance test, plus CI and docs.
Composer scripts/plugins and analyzer config execute code; bootstrap is not a safe audit of
an untrusted manifest. Review inputs before installation and isolate execution.

## Rule mapping beyond the shared baseline

| Rules | Mechanism to generate |
|---|---|
| ST-1 to ST-3 | [PHP fixer starter](../../templates/style/php/.php-cs-fixer.dist.php), pinned preset support, dry-run/fix/convergence proof and precise Finder scope |
| SK-1, SK-2 | Rerunnable bootstrap/doctor and real executable/endpoint test against the installed project |
| MT-1, IN-5 | Public PHPDoc/types, command/help and maintained example/link checks; review side effects/failures |
| MT-2, MT-3 | Adopt an explicit complexity rule/limit and report tool; PHPStan/AST/reference reports guide scoped retirement, not automatic deletion |
| AR-1, AR-2 | Authoritative operation registry with explicit public/access policy; structural tests discover real commands/routes and reject missing declarations |
| AR-3 | Namespace/import contracts reject internal cross-module dependencies and unapproved cycles |
| AR-4 to AR-6 | Services validate writes/actor/history; one integration package; prepared queries, safe paths/commands and contextual output handling |
| SE-2 to SE-5 | Audit the complete locked set and reviewed origins/scripts; secret/code/config checks plus effective authorization, input and disclosure tests |
| WK-6 | Separate dev/test database, sessions/cache prefix, queues and ports per checkout; verify the runner's actual resource selection |
| OP-1 to OP-8 | Shared registry adapters and scoped machine credentials; test attribution, concurrent retry behavior, untrusted data and external load |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Record selected suites and discovery/execution counts with the chosen runner. Isolate
filesystem/database fixtures and prove installed CLI or HTTP/persistence boundaries. Report
skips, retries and unavailable PHP version/extension/backend coverage.

## Gaps to resolve before scoring

Select the actual framework, authentication, persistence, complexity/static-security tools,
architecture checker, deployment config and supported extensions. This general profile does
not validate a specific web framework or tenant model. Reflection, dynamic service lookup and
external consumers require targeted discovery evidence. Current audit results do not prove
package publisher trust or absence of vulnerabilities. Agent enforcement/host CI need proof.

## Sources

- [PHPStan setup](https://phpstan.org/user-guide/getting-started)
- [Composer command reference](https://getcomposer.org/doc/03-cli.md)
- [Style starter commands](../../templates/style/README.md)
