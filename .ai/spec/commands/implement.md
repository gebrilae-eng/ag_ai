---
description: Execute all tasks from tasks.md in correct order.
---

# /speckit.implement

1. Read `tasks.md` from current feature directory
2. Validate prerequisites: constitution, spec, plan, tasks all exist
3. Execute tasks in order, respecting `[P]` parallel markers
4. After each user story phase: pause and confirm independently testable
5. Handle errors: report and ask how to proceed
6. On completion: run `/verify` quality gate

## Delegate By Task Type
- Code implementation → `.ai/agents/coder.md`
- DB changes → `.ai/agents/db-agent.md`
- API → `.ai/agents/api-agent.md`
- Tests → `.ai/sub-agents/test-writer.md`
