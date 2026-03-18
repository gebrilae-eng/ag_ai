# Spec Kit Commands

## Workflow Order
```
/speckit.constitution  → project principles (once per project)
/speckit.specify       → WHAT to build
/speckit.clarify       → resolve ambiguities
/speckit.plan          → HOW to build
/speckit.tasks         → executable task list
/speckit.implement     → execute
```

## File Structure
```
specs/{###-feature-name}/
  spec.md        ← WHAT (requirements, user stories)
  plan.md        ← HOW (tech decisions, phases)
  data-model.md  ← DB entities
  tasks.md       ← ordered task list
  discovery.md   ← research (optional)
```

---

## /speckit.constitution
Create `.ai/spec/memory/constitution.md` from `constitution-template.md`.
1. Load existing constitution if present
2. Derive 3-5 principles from project context
3. Each principle: name + MUST/MUST NOT rules + rationale
4. Write file, report version + principles defined

---

## /speckit.specify
Given `$ARGUMENTS` (feature description):
1. Generate 2-4 word short name (action-noun format)
2. Create `specs/###-short-name/`
3. Fill spec with user stories, requirements, success criteria
4. Max 3 `[NEEDS CLARIFICATION]` markers — guess the rest
5. Write `spec.md`, report branch name + readiness

Rules: WHAT and WHY only — no tech details. Every requirement testable.

---

## /speckit.clarify
1. Read current `spec.md`
2. Find all `[NEEDS CLARIFICATION]` markers (max 3)
3. For each, present options: A) B) C) Custom
4. Wait for user responses
5. Update spec, confirm ready for `/speckit.plan`

---

## /speckit.plan
1. Load `spec.md` + `constitution.md`
2. Fill tech stack, architecture decisions, phases
3. Generate `data-model.md` for DB entities
4. Generate `contracts/api-spec.md` if API endpoints needed
5. Check constitution compliance
6. Write `plan.md`, report artifacts created

---

## /speckit.tasks
1. Read `plan.md`, `spec.md`, `data-model.md`
2. Generate tasks organized by user story (US1, US2...)
3. Mark parallel tasks with `[P]`
4. Order: models → services → endpoints
5. Add checkpoints after each user story
6. Write `tasks.md`

---

## /speckit.implement
1. Read `tasks.md`
2. Validate: constitution + spec + plan + tasks all exist
3. Execute tasks in order, respecting `[P]` parallel markers
4. After each user story: pause + confirm independently testable
5. On completion: run `/verify`

Delegate by task type:
- Code → coder
- DB → db-agent
- API → api-agent
- Tests → test-writer
