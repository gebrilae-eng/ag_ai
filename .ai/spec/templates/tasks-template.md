# Tasks: [FEATURE NAME]

**Input**: specs/[###-feature-name]/plan.md
**Format**: `[ID] [P?] [US?] Description`
- `[P]` = can run in parallel
- `[US1]` = belongs to User Story 1

---

## Phase 1: Setup

- [ ] T001 Create project/feature structure
- [ ] T002 [P] Install/verify dependencies

---

## Phase 2: Foundation ⚠️ Blocks all stories

- [ ] T003 Database migrations / schema changes
- [ ] T004 [P] Base models and relationships
- [ ] T005 [P] Auth / middleware setup (if needed)

**Checkpoint**: Foundation done → stories can start

---

## Phase 3: User Story 1 — [Title] (P1) 🎯 MVP

- [ ] T006 [P] [US1] Create [Entity] model
- [ ] T007 [US1] Implement [Service]
- [ ] T008 [US1] Implement [endpoint/feature]
- [ ] T009 [US1] Validation and error handling

**Checkpoint**: US1 independently testable ✓

---

## Phase 4: User Story 2 — [Title] (P2)

- [ ] T010 [P] [US2] Create [Entity] model
- [ ] T011 [US2] Implement [Service]
- [ ] T012 [US2] Implement [endpoint/feature]

**Checkpoint**: US2 independently testable ✓

---

## Phase N: Polish

- [ ] TXXX [P] Update documentation
- [ ] TXXX Code cleanup
- [ ] TXXX Run quality gate: `/verify`

---

## Execution Notes
- Models before services, services before endpoints
- Commit after each logical group
- Stop at each checkpoint to validate independently
