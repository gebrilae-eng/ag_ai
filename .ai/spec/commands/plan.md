---
description: Create technical implementation plan from the feature spec.
---

# /speckit.plan

1. Find current feature spec in `specs/`
2. Load spec.md and `.ai/spec/memory/constitution.md`
3. Load `.ai/spec/templates/plan-template.md`
4. Fill: tech stack, architecture decisions, phases
5. Generate `data-model.md` for any DB entities
6. Generate `contracts/api-spec.md` if API endpoints needed
7. Check constitution compliance — flag violations
8. Write `plan.md` to feature directory
9. Report: file path, artifacts created, ready for `/speckit.tasks`

## Arguments
$ARGUMENTS — tech stack and architecture preferences
