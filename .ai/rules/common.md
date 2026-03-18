# Common Rules

## Coding Style

- Functions do ONE thing — if you need "and" to describe it, split it
- Max function length: 30 lines (guideline, not hard limit)
- Max file length: 300 lines — split if longer
- No commented-out code in commits
- No `TODO` comments in commits — create an issue instead
- Constants over magic numbers/strings

### Naming
- Names should explain WHY not WHAT
- Boolean names: `is_`, `has_`, `can_` prefix
- Avoid abbreviations unless universal (`id`, `url`, `api`)

### Error Handling
- Never silently swallow exceptions
- Log with context: file, function, input that caused error
- Return meaningful error messages to callers

### Git
- Commit messages: `type: short description` (feat, fix, refactor, docs, test)
- One logical change per commit
- Never commit `.env`, `vendor/`, `node_modules/`

---

## Security

- NEVER hardcode credentials, API keys, or tokens in source code
- NEVER log passwords, tokens, or PII
- ALWAYS validate and sanitize all external input
- ALWAYS use HTTPS in production
- ALWAYS use parameterized queries — no string concatenation in SQL
- ALWAYS store secrets in environment variables

### Rate Limiting
- All public endpoints and bot commands: 10 req/min/user
- Auth endpoints: 5 attempts per 15 minutes

### CORS
- Whitelist specific origins — never `*` in production
- Only allow necessary HTTP methods

### Dependencies
- Review new dependencies before adding
- Run `composer audit` / `npm audit` regularly
- Remove unused dependencies

### Logging
- Log security events: failed auth, rate limit hits, suspicious input
- Never log: passwords, tokens, credit card numbers, full request bodies
