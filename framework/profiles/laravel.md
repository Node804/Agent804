# Profile: Laravel

- **Status:** Draft extension; no full application trial.
- **Applies to:** A supported pinned Laravel/PHP combination with Composer and selected frontend tooling.
- **Extends:** [PHP](php.md) plus the [shared baseline](README.md#shared-baseline). Read both first.

## Explicit overrides and baseline

Use Laravel's own project structure, bootstrap, configuration and HTTP-test facilities rather
than inventing a parallel framework. Choose PHPUnit or Pest and lock it. Pint's chosen preset
replaces the parent's standalone PHP-CS-Fixer pipeline; do not run both over the same files.
Blade has separate grammar ownership; frontend assets need independently scoped JS/TS checks.
Use PHPStan with a reviewed Laravel-aware extension if required for the project's dynamic
features; document accepted limits rather than suppressing the whole application.

## Check, bootstrap and skeleton

Generate `composer check` to orchestrate Pint `--test`, the chosen Blade/frontend checks,
syntax/static analysis, architecture and docs checks, current security checks, and
`php artisan test`. Propagate every failure; the parent generic test recipe is replaced by
the selected Laravel runner. Tests must verify resource selection before destructive setup.
Generate bootstrap/doctor scripts for reviewed Composer/frontend locked installs and isolated
dev/test config. Database migration requires existing explicit authorization; never migrate
an inherited production URL. Use the supported Laravel development run command for the
selected version, one protected route/action, authorized/refused HTTP acceptance cases and CI.

## Rule mapping overrides/additions

| Rules | Laravel mechanism to generate |
|---|---|
| ST-1 to ST-3 | [Pint](../../templates/style/laravel/pint.json) plus [Blade config](../../templates/style/laravel/.bladeformatterrc.json); explicit frontend scope and convergence tests |
| SK-1, SK-2 | Bootstrap/doctor and real HTTP/browser scenario, not only isolated class tests |
| AR-1 | Discover route declarations and require explicit public or access metadata; policies/gates and service authorization enforce object/tenant permissions. Test direct URLs, APIs, jobs and command paths |
| AR-2, OP-1 | Action/operation declarations serve controllers, tools and jobs; policies and validation are shared behind adapters |
| AR-3 | Namespace/AST contracts around modules and their public services; test forbidden imports and dynamic lookup bypasses |
| AR-4 to AR-6 | Actor-aware transactional services/history, integration-only clients, ORM/prepared queries, validated requests and escaped Blade output; inspect raw output and mass-assignment boundaries |
| WK-6 | Unique database, session/cache/queue prefixes and ports; test config/cache must not point to another checkout or production |
| SE-4, SE-5 | Deployment-shaped config checks, safe secrets/debug/session/CSRF policy and refusal/tenant/injection/upload tests; actual deployment verification is separate |
| OP-2 to OP-8 | Scoped machine credentials, attributed writes, deduplication/reconciliation and bounded integrations; policies must hold for every adapter |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Inherit PHP evidence; record selected suites and actual discovered/executed counts. Isolate
databases, queue/cache/storage and parallel workers. HTTP tests must identify simulated
services versus real middleware/database/worker boundaries; report skips and backend gaps.

## Gaps and gotchas

Choose and exercise the actual auth/token package, database, queue/cache drivers, architecture
checker, complexity limits and deployment verification. A policy class existing is not proof
it is called on every route or job. Review cached configuration and test environment variables
before DB-refresh helpers execute. An in-memory database may not cover production engine
semantics; add representative throwaway-engine tests where needed. Blade custom directives,
frontend parsers and browser tests remain explicit gaps until trialled. All other PHP/shared
baseline obligations remain; no inherited Reference status or automatic dependency authority.

## Sources

- [Laravel testing](https://laravel.com/docs/12.x/testing)
- [Laravel authorization](https://laravel.com/docs/12.x/authorization)
- [Laravel Pint](https://laravel.com/docs/12.x/pint)
