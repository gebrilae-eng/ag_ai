---
description: Create or update the feature specification from a natural language description.
---

# /speckit.specify

Given the feature description in `$ARGUMENTS`:

1. Generate a concise 2-4 word short name (action-noun format)
2. Create feature directory: `specs/###-short-name/`
3. Load `.ai/spec/templates/spec-template.md`
4. Fill spec with user stories, requirements, success criteria
5. Max 3 `[NEEDS CLARIFICATION]` markers — make informed guesses for the rest
6. Write to `specs/###-short-name/spec.md`
7. Report: branch name, file path, readiness for `/speckit.plan`

## Rules
- Focus on WHAT and WHY — no tech stack details
- Written for business stakeholders, not developers
- Every requirement must be testable
- Success criteria: measurable, technology-agnostic

## Arguments
$ARGUMENTS
