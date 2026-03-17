---
description: Break implementation plan into ordered executable tasks.
---

# /speckit.tasks

1. Read `plan.md`, `spec.md`, `data-model.md` from current feature
2. Load `.ai/spec/templates/tasks-template.md`
3. Generate tasks organized by user story (US1, US2, ...)
4. Mark parallel tasks with `[P]`
5. Include dependency order: models → services → endpoints
6. Add checkpoints after each user story
7. Write `tasks.md` to feature directory
8. Report: task count, phases, ready for `/speckit.implement` or `/tdd`
