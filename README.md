# ag_ai — AI Development Infrastructure

> Complete AI-powered dev environment for any project.
> Install once, reuse across all projects.

[![GitHub](https://img.shields.io/badge/GitHub-ag__ai-blue?logo=github)](https://github.com/gebrilae-eng/ag_ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Quick Start — 3 Steps

### Step 1 — Clone once per machine
```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git C:\ag_ai
```

### Step 2 — Install into your project
```cmd
C:\ag_ai\install.bat D:\my-new-project
```

### Step 3 — Fill project context
```cmd
C:\ag_ai\wizard.bat D:\my-new-project
```

Or all three steps in one:
```cmd
C:\ag_ai\new-project.bat
```

---

## All Scripts

| Script | What it does |
|--------|-------------|
| `install.bat / .ps1` | Install agents into a project |
| `wizard.bat / .ps1` | Fill PROJECT.md, STACK.md, RULES.md interactively |
| `update.bat / .ps1` | Pull latest ag_ai from GitHub + show changelog |
| `update-project.bat` | Update agents only — preserves your context files |
| `validate.bat` | Check context files and verify all agents installed |
| `agent.bat / .ps1` | Launch OpenCode with a specific agent from a menu |
| `new-project.bat` | Create + install + wizard in one shot |

### New in v2.1
```cmd
:: Preview what would change before installing
python setup_ai.py D:\my-project --dry-run

:: Update agents only, never touches your context files
python setup_ai.py D:\my-project --update-agents
C:\ag_ai\update-project.bat D:\my-project

:: Verify project is correctly configured
C:\ag_ai\validate.bat D:\my-project
```

---

## Agent System

### How to invoke agents in OpenCode
```
use orchestrator agent to manage: [complex multi-step task]
use coder agent to implement [function or feature]
use tdd-guide agent to write tests for [function] test-first
use security-reviewer agent to audit [file or folder]
use db-agent agent to design schema for [entity]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug or error]
use code-reviewer agent to review [file or change]
use architect agent to design [system or feature]
use telegram-bot agent to implement [command or message]
use n8n-workflow agent to design workflow for [task]
use test-writer agent to write tests for [function]
use refactor-cleaner agent to refactor [file]
use doc-updater agent to update docs for [change]
use build-error-resolver agent to fix [error message]
use spec-workflow agent to specify: I want to add [feature]
use database-reviewer agent to review [schema or migration]
```

### Agent launcher menu
```cmd
C:\ag_ai\agent.bat    (CMD)
C:\ag_ai\agent.ps1    (PowerShell)
```

---

## All 18 Agents

### Planning and Architecture
| Agent | Role | Tools |
|-------|------|-------|
| `orchestrator` | Delegates only — **never writes code itself** | read, glob, grep, task |
| `spec-workflow` | Spec-first: specify → clarify → plan → tasks | full |
| `architect` | System design, trade-offs, ADRs (Opus model) | read, write, glob, grep |

### Development
| Agent | Role | Tools |
|-------|------|-------|
| `coder` | Write and refactor PHP/JS/SQL | full |
| `tdd-guide` | Red→Green→Refactor, runs tests | full |
| `refactor-cleaner` | Improve structure, keep tests green | full |
| `build-error-resolver` | Diagnose and fix build/runtime errors | full |
| `db-agent` | MySQL schema, migrations, indexes | full |
| `api-agent` | REST endpoints, webhooks, integrations | full |

### Review and Quality
| Agent | Role | Tools |
|-------|------|-------|
| `code-reviewer` | Correctness, performance, style | read, write, glob, grep |
| `security-reviewer` | OWASP Top 10 audit | full |
| `database-reviewer` | Schema quality, query safety | read, write, glob, grep |
| `doc-updater` | Keep docs in sync with code | read, write, edit, glob, grep |

### Specialists
| Agent | Role | Tools |
|-------|------|-------|
| `sql-helper` | Generate optimized MySQL queries | full |
| `telegram-bot` | HTML formatting, Arabic RTL, splits | full |
| `n8n-workflow` | Workflow design, code nodes | full |
| `debugger` | Reproduce → Isolate → Fix → Verify | full |
| `test-writer` | Unit, integration, E2E tests | full |

> All agents are `mode: primary`.
> `orchestrator` is the only agent that **delegates only** — read/grep/task tools, never write or bash.

---

## Feature Workflow

### Spec-first (recommended for new features)
```
use spec-workflow agent to specify: I want to add [feature]
use orchestrator agent to manage: plan and implement [feature]
```

Or with Claude Code slash commands:
```
/speckit.specify  I want to add [feature]
/speckit.plan
/speckit.tasks
/speckit.implement
/verify
/security
```

### Quick implementation (small tasks)
```
use coder agent to implement [specific function]
use test-writer agent to write tests for [function]
use security-reviewer agent to audit [file]
```

### Spec folder structure
```
specs/
└── 001-feature-name/
    ├── spec.md        <- WHAT (user stories, requirements)
    ├── plan.md        <- HOW (tech decisions, phases)
    ├── data-model.md  <- DB schema and entities
    ├── tasks.md       <- ordered tasks with [P] parallel markers
    └── discovery.md   <- research findings (optional)
```

---

## What Gets Installed

```
your-project/
├── AGENTS.md                     <- OpenCode reads this first
├── CLAUDE.md                     <- Claude Code reads this first
├── specs/                        <- feature specs go here
├── .opencode/agents/             <- 18 OpenCode YAML agents
├── .claude/commands/             <- Claude Code slash commands
└── .ai/
    ├── agents/                   <- agent markdown instructions
    │   └── ecc/                  <- ECC specialist agents
    ├── sub-agents/               <- sql, telegram, n8n, debugger...
    ├── rules/
    │   ├── php/                  <- PHP security + patterns + testing
    │   └── common/               <- universal security + coding style
    ├── context/                  <- PROJECT.md, STACK.md, RULES.md
    └── spec/                     <- Spec Kit commands + templates
```

Files generated by `wizard.bat`:

| File | Content |
|------|---------|
| `AGENTS.md` | Agent routing + coding style for OpenCode |
| `CLAUDE.md` | Agent routing + slash commands for Claude Code |
| `.ai/context/PROJECT.md` | Project name, description, integrations |
| `.ai/context/STACK.md` | Backend, DB, frontend, env variables |
| `.ai/context/RULES.md` | Coding rules + project-specific rules |
| `.ai/spec/memory/constitution.md` | Project principles |
| `.ai/context/wizard-answers.json` | Saved answers for re-runs |

---

## Claude Code Slash Commands

| Command | Purpose |
|---------|---------|
| `/speckit.specify` | Define what to build |
| `/speckit.clarify` | Resolve ambiguities |
| `/speckit.plan` | Technical plan |
| `/speckit.tasks` | Break into ordered tasks |
| `/speckit.implement` | Execute with specialist agents |
| `/tdd` | Test-first implementation |
| `/verify` | Full quality gate |
| `/security` | OWASP audit |
| `/code-review` | Review code |
| `/build-fix` | Fix build errors |
| `/refactor-clean` | Refactor code |
| `/update-docs` | Sync docs with code |
| `/learn` | Extract patterns from session |
| `/checkpoint` | Save session state |

---

## Requirements
- Python 3.6+ (no extra packages)
- Git
- [Claude Code](https://www.anthropic.com/claude-code) and/or [OpenCode](https://opencode.ai/)

Works on any drive, any path — no hardcoded locations.

---

## Credits
- [Spec Kit](https://github.com/github/spec-kit) by GitHub
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) by @affaan-m

---
MIT License
