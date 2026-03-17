---
description: Clarify underspecified requirements before planning.
---

# /speckit.clarify

1. Read current `spec.md`
2. Find all `[NEEDS CLARIFICATION]` markers
3. For each (max 3), present options:
   ```
   ## Q[N]: [Topic]
   Context: [quote from spec]
   Options:
   A) [option] — [implication]
   B) [option] — [implication]
   C) Custom answer
   ```
4. Wait for user responses
5. Update spec replacing markers with chosen answers
6. Confirm spec ready for `/speckit.plan`
