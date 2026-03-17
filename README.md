# 🤖 ai-dev-kit

> Complete AI-powered development infrastructure.
> Combines: **Custom Agents** + **Spec Kit** + **Everything Claude Code (ECC)**

## Install into any project

```bash
python setup_ai.py C:\path\to\your-project
```

## What's included

- **16 specialized agents** (orchestrator, architect, TDD guide, security reviewer, etc.)
- **Spec-Driven workflow** (`/speckit.*` commands) — define specs before writing code
- **ECC commands** (`/tdd`, `/verify`, `/security`, `/quality-gate`, etc.)
- **PHP + common rules** — auto-applied to `.php` files
- **Skills** — laravel, tdd-workflow, security-review, database-migrations, and more

## Workflow

```
/speckit.specify → /speckit.plan → /speckit.tasks → /tdd → /verify
```

## Sources
- Custom Agents — pharmacy-specific roles, SQL, Telegram, n8n
- [Spec Kit](https://github.com/github/spec-kit) — spec-driven development
- [ECC](https://github.com/affaan-m/everything-claude-code) — battle-tested agents + skills
