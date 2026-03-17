# 🤖 AI Agent Instructions

> Entry point for Claude Code & OpenCode.
> **ai-dev-kit** — Custom Agents + Spec Kit + ECC

---

## 🚀 New Feature Workflow

```
1. /speckit.specify    → define WHAT to build
2. /speckit.clarify    → resolve gaps (optional)
3. /speckit.plan       → define HOW (tech stack)
4. /speckit.tasks      → break into ordered tasks
5. /tdd                → implement test-first
6. /verify             → quality gate check
```

---

## 📁 Read First

| File | Purpose |
|------|---------|
| `.ai/context/PROJECT.md` | What we're building |
| `.ai/context/STACK.md`   | Tech stack details |
| `.ai/context/RULES.md`   | Coding rules (mandatory) |

---

## 🧠 Agent Routing

### Planning
| Task | Agent |
|------|-------|
| Complex multi-step | `.ai/agents/orchestrator.md` |
| System design | `.ai/agents/ecc/architect.md` |
| Feature planning | `.ai/agents/ecc/planner.md` |
| Spec workflow | `.ai/agents/spec-workflow.md` |

### Development
| Task | Agent |
|------|-------|
| Write / refactor code | `.ai/agents/coder.md` |
| TDD implementation | `.ai/agents/ecc/tdd-guide.md` |
| Fix build errors | `.ai/agents/ecc/build-error-resolver.md` |
| Refactor & clean | `.ai/agents/ecc/refactor-cleaner.md` |

### Review & Quality
| Task | Agent |
|------|-------|
| Code review | `.ai/agents/ecc/code-reviewer.md` |
| Security audit | `.ai/agents/ecc/security-reviewer.md` |
| Database review | `.ai/agents/ecc/database-reviewer.md` |
| Documentation | `.ai/agents/ecc/doc-updater.md` |

### Specialists
| Task | Agent |
|------|-------|
| MySQL queries | `.ai/sub-agents/sql-helper.md` |
| Telegram bot | `.ai/sub-agents/telegram-bot.md` |
| n8n workflows | `.ai/sub-agents/n8n-workflow.md` |
| Test writing | `.ai/sub-agents/test-writer.md` |
| Debugging | `.ai/sub-agents/debugger.md` |

---

## 📋 Commands

### Spec Kit
`/speckit.constitution` `/speckit.specify` `/speckit.clarify`
`/speckit.plan` `/speckit.tasks` `/speckit.implement` `/speckit.analyze`

### ECC
`/tdd` `/verify` `/quality-gate` `/code-review`
`/security` `/build-fix` `/refactor-clean` `/learn` `/checkpoint`

---

## ⚡ Core Rules
- **Spec first** → write spec before code
- **Tests first** → TDD always
- **NEVER** `SELECT *` in production
- **NEVER** hardcode credentials
- **ALWAYS** validate + sanitize user input
- **ALWAYS** parameterized SQL queries
