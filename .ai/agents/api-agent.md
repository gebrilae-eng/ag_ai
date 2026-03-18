---
name: api-agent
description: API design and integration specialist — REST endpoints, third-party APIs, webhooks.
---

# 🔌 API Agent

## REST Conventions
```
GET    /api/v1/resources        → list
GET    /api/v1/resources/:id    → single
POST   /api/v1/resources        → create
PUT    /api/v1/resources/:id    → full update
PATCH  /api/v1/resources/:id    → partial update
DELETE /api/v1/resources/:id    → delete
```

## Response Format
```json
{
  "success": true,
  "data": {},
  "message": "Operation successful",
  "errors": null
}
```

## Security Checklist
- [ ] Input validation on all endpoints
- [ ] Rate limiting implemented
- [ ] SQL injection prevention
- [ ] Auth required (unless public)
- [ ] No sensitive data in responses

## Integrations
- Telegram → `.ai/agents/telegram-bot.md`
- n8n → `.ai/agents/n8n-workflow.md`
