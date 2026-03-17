# Common Security Rules

## Universal Rules (All Languages)
- NEVER hardcode credentials, API keys, or tokens in source code
- NEVER log passwords, tokens, or PII
- ALWAYS validate and sanitize all external input
- ALWAYS use HTTPS in production
- ALWAYS use parameterized queries — no string concatenation in SQL
- ALWAYS store secrets in environment variables or secret manager

## Rate Limiting
- Apply rate limiting to all public endpoints and bot commands
- Default: 10 requests per minute per user/IP
- Stricter on auth endpoints: 5 attempts per 15 minutes

## CORS
- Whitelist specific origins — never `*` in production
- Only allow necessary HTTP methods

## Dependencies
- Review new dependencies before adding
- Run security audit regularly (`composer audit`, `npm audit`)
- Remove unused dependencies

## Logging
- Log security events: failed auth, rate limit hits, suspicious input
- Never log: passwords, tokens, credit card numbers, full request bodies
- Rotate logs, set retention policy
