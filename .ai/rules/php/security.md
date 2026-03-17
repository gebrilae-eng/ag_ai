---
paths:
  - "**/*.php"
  - "**/composer.json"
---
# PHP Security Rules

## Input & Output
- Validate ALL request input at the controller boundary
- Escape output in templates — treat raw HTML as exception requiring justification
- Never trust `$_GET`, `$_POST`, `$_COOKIE`, `$_FILES` without validation

## Database Safety
- PDO prepared statements for ALL dynamic queries — no string concatenation
- Scope ORM mass-assignment — whitelist writable fields explicitly
- Never expose DB structure in error messages

## Passwords & Sessions
- `password_hash()` with `PASSWORD_BCRYPT` — never MD5, SHA1, or plain text
- `password_verify()` for comparison — never direct string compare
- `session_regenerate_id(true)` after login and privilege changes
- CSRF token on all state-changing requests (POST/PUT/PATCH/DELETE)

## Secrets & Dependencies
- Secrets in `.env` or secret manager — never in committed config files
- Run `composer audit` in CI
- Pin major versions in `composer.json`

## Error Handling
- Never expose stack traces or DB errors to end users
- Log errors server-side with context — sanitize before logging (no passwords/tokens)
- Return generic error messages to clients
