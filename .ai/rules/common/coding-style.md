# Common Coding Style Rules

## Universal
- Functions do ONE thing — if you need "and" to describe it, split it
- Max function length: 30 lines (guideline, not hard limit)
- Max file length: 300 lines — if longer, consider splitting
- No commented-out code in commits
- No `TODO` comments in commits — create an issue instead
- Constants over magic numbers/strings

## Naming
- Names should explain WHY not WHAT
- Boolean names: `is_`, `has_`, `can_` prefix — `$isOverstocked`
- Avoid abbreviations unless universally understood (`id`, `url`, `api`)

## Error Handling
- Never silently swallow exceptions
- Log with context: file, function, input that caused error
- Return meaningful error messages to callers

## Code Review Mindset
- Write code for the next developer (could be you in 6 months)
- Prefer clarity over cleverness
- A comment that explains WHY is valuable; one that explains WHAT is noise

## Git
- Commit messages: `type: short description` (feat, fix, refactor, docs, test)
- One logical change per commit
- Never commit `.env`, `vendor/`, `node_modules/`
