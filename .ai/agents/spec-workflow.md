---
name: spec-workflow
description: Spec-first planning — specify, clarify, plan, tasks, implement.
---

# Spec Workflow Agent

## Workflow Order
```
/speckit.specify    → WHAT to build
/speckit.clarify    → resolve ambiguities
/speckit.plan       → HOW to build
/speckit.tasks      → executable task list
/speckit.implement  → execute
```
Full command reference: `.ai/spec/commands.md`

## Spec File Structure
```
specs/{###-feature-name}/
  spec.md        ← WHAT (requirements, user stories)
  plan.md        ← HOW (tech decisions, phases)
  data-model.md  ← DB entities
  tasks.md       ← ordered task list with [P] markers
  discovery.md   ← research (optional)
```

## Delegation When Implementing
| Task | Agent |
|------|-------|
| DB schema | `db-agent` |
| API endpoints | `api-agent` |
| Business logic | `coder` |
| SQL | `sql-helper` |
| Telegram | `telegram-bot` |
| n8n | `n8n-workflow` |
| Tests | `test-writer` |

## Quality Gates
- Before plan: no `[NEEDS CLARIFICATION]` markers remain
- Before implement: `tasks.md` organized by user story
