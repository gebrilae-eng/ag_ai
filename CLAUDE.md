# AI Instructions

> Read `AGENTS.md` and `.ai/context/` first.

## Agent Routing
| Task | Agent |
|------|-------|
| Complex multi-step | `orchestrator` (delegates only) |
| Write / refactor code | `coder` |
| DB schema / queries | `db-agent` |
| API / integrations | `api-agent` |
| Spec-first planning | `spec-workflow` |
| System design | `architect` |
| TDD | `tdd-guide` |
| Security audit | `security-reviewer` |
| Code review | `code-reviewer` |
| DB review | `database-reviewer` |
| Refactoring | `refactor-cleaner` |
| Build errors | `build-error-resolver` |
| Docs | `doc-updater` |
| SQL | `sql-helper` |
| Telegram | `telegram-bot` |
| n8n | `n8n-workflow` |
| Debugging | `debugger` |
| Tests | `test-writer` |

## Key Files
| File | Purpose |
|------|---------|
| `.ai/agents/*.md` | All agent instructions (18 agents) |
| `.ai/rules/common.md` | Universal coding style + security |
| `.ai/rules/php.md` | PHP architecture + security + testing |
| `.ai/spec/commands.md` | All speckit commands reference |
| `.ai/spec/templates/` | Spec, plan, tasks templates |
| `.ai/context/` | PROJECT.md, STACK.md, RULES.md |

## Claude Code Commands
```
/speckit.specify  → new feature spec
/speckit.plan     → technical plan
/speckit.tasks    → task breakdown
/speckit.implement → execute
/tdd              → test-first
/verify           → quality gate
/security         → OWASP audit
```
