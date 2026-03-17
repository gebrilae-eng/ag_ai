---
name: spec-workflow
description: Bridges Spec Kit commands with specialized agents. Ensures spec-first development.
---

# 📋 Spec Workflow Agent

## The Workflow
```
/speckit.constitution  → project principles (once)
/speckit.specify       → WHAT to build (no tech details)
/speckit.clarify       → resolve ambiguities
/speckit.plan          → HOW to build (tech + architecture)
/speckit.analyze       → cross-check consistency
/speckit.tasks         → executable task list
/speckit.implement     → execute
```

## File Locations
```
specs/{feature-branch}/
  spec.md         ← what to build
  plan.md         ← how to build
  data-model.md   ← DB entities
  tasks.md        ← task breakdown
  research.md     ← tech decisions
```

## After Planning → Delegate
| Task type in tasks.md | Agent |
|-----------------------|-------|
| DB models/schema | `db-agent.md` |
| API endpoints | `api-agent.md` |
| Business logic | `coder.md` |
| SQL | `sub-agents/sql-helper.md` |
| Telegram | `sub-agents/telegram-bot.md` |
| n8n | `sub-agents/n8n-workflow.md` |
| Tests | `sub-agents/test-writer.md` |

## Quality Gates
Before `/speckit.plan`: no `[NEEDS CLARIFICATION]` markers remain
Before `/speckit.implement`: `tasks.md` organized by user story
