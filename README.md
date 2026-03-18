# ag_ai — AI Development Infrastructure

> Complete AI-powered dev environment. Install once, reuse across all projects.

[![GitHub](https://img.shields.io/badge/GitHub-ag__ai-blue?logo=github)](https://github.com/gebrilae-eng/ag_ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Quick Start

```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git C:\ag_ai
C:\ag_ai\install.bat D:\my-project
C:\ag_ai\wizard.bat  D:\my-project
```

Or all in one: `C:\ag_ai\new-project.bat`

---

## Scripts

| Script | Purpose |
|--------|---------|
| `install.bat / .ps1` | Install agents into a project |
| `wizard.bat / .ps1` | Fill context files interactively |
| `update.bat / .ps1` | Pull latest ag_ai from GitHub |
| `update-project.bat` | Update agents only, keep context |
| `validate.bat` | Check setup completeness |
| `agent.bat / .ps1` | Launch OpenCode with agent menu |
| `new-project.bat` | Create + install + wizard in one shot |

```cmd
python setup_ai.py D:\my-project --dry-run        :: preview
python setup_ai.py D:\my-project --update-agents  :: agents only
```

---

## Global OpenCode Config

Copy `.config/opencode/opencode.json` to enable all 18 agents globally
(works in every project, even without `.opencode/agents/`):

```cmd
copy C:\ag_ai\.config\opencode\opencode.json ^
     C:\Users\%USERNAME%\.config\opencode\opencode.json
```

---

## Using Agents in OpenCode

```
use orchestrator agent to manage: [complex multi-step task]
use coder agent to implement [function or feature]
use tdd-guide agent to write tests for [function]
use security-reviewer agent to audit [file or folder]
use db-agent agent to design schema for [entity]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug or error]
use architect agent to design [system or feature]
use spec-workflow agent to specify: I want to add [feature]
use telegram-bot agent to implement [command or message]
use n8n-workflow agent to design workflow for [task]
```

Or use the menu: `C:\ag_ai\agent.bat`

---

## All 18 Agents

### Planning
| Agent | Role | Tools |
|-------|------|-------|
| `orchestrator` | Delegates only — never writes code | read, glob, grep, task |
| `spec-workflow` | specify → clarify → plan → tasks | full |
| `architect` | System design, trade-offs (Opus) | read, write, glob, grep |

### Development
| Agent | Role | Tools |
|-------|------|-------|
| `coder` | Write and refactor PHP/JS/SQL | full |
| `tdd-guide` | Red→Green→Refactor | full |
| `db-agent` | MySQL schema, migrations, indexes | full |
| `api-agent` | REST endpoints, webhooks | full |
| `refactor-cleaner` | Improve structure | full |
| `build-error-resolver` | Fix build/runtime errors | full |

### Review
| Agent | Role | Tools |
|-------|------|-------|
| `code-reviewer` | Correctness, performance, style | read, write, glob, grep |
| `security-reviewer` | OWASP Top 10 | full |
| `database-reviewer` | Schema quality, query safety | read, write, glob, grep |
| `doc-updater` | Docs in sync with code | read, write, edit, glob, grep |

### Specialists
| Agent | Role | Tools |
|-------|------|-------|
| `sql-helper` | Optimized MySQL queries | full |
| `telegram-bot` | HTML formatting, Arabic RTL | full |
| `n8n-workflow` | Workflow design, code nodes | full |
| `debugger` | Reproduce → Isolate → Fix | full |
| `test-writer` | Unit, integration, E2E | full |

> All `mode: primary`. `orchestrator` = read/glob/grep/task only.
> `architect` uses `claude-opus-4-6`. All others use `claude-sonnet-4-6`.

---

## Project File Structure

```
your-project/
├── AGENTS.md                    ← OpenCode reads first
├── CLAUDE.md                    ← Claude Code reads first
├── specs/                       ← feature specs
├── .opencode/agents/            ← 18 project-level YAML agents
├── .claude/commands/            ← Claude Code slash commands
└── .ai/
    ├── agents/                  ← 18 agent instruction .md files
    ├── rules/
    │   ├── common.md            ← coding style + security
    │   └── php.md               ← PHP architecture + security + testing
    ├── spec/
    │   ├── commands.md          ← all speckit commands reference
    │   ├── templates/           ← spec, plan, tasks templates
    │   └── memory/              ← constitution.md (per project)
    └── context/                 ← PROJECT.md, STACK.md, RULES.md
```

**Flat structure — no nested sub-agents/ or rules/php/ or rules/common/ folders.**

---

## Repo Structure

```
ag_ai/
├── .ai/                         ← installed into projects
├── .opencode/agents/            ← 18 YAML agent configs
├── .claude/commands/            ← slash commands
├── .config/opencode/
│   └── opencode.json            ← global OpenCode config (copy manually)
├── agent.bat / agent.ps1        ← agent launcher menu
├── install.bat / .ps1           ← project installer
├── wizard.bat / .ps1 + wizard.py ← context setup
├── update.bat / .ps1            ← update ag_ai
├── update-project.bat           ← update project agents
├── validate.bat + validate.py   ← verify setup
├── new-project.bat              ← one-shot setup
├── setup_ai.py                  ← installer engine
├── CLAUDE.md                    ← Claude Code entry point template
├── CHANGELOG.md
└── README.md
```

---

## Claude Code Slash Commands

| Command | Purpose |
|---------|---------|
| `/speckit.specify` | New feature spec |
| `/speckit.clarify` | Resolve ambiguities |
| `/speckit.plan` | Technical plan |
| `/speckit.tasks` | Ordered task list |
| `/speckit.implement` | Execute |
| `/tdd` | Test-first |
| `/verify` | Quality gate |
| `/security` | OWASP audit |
| `/code-review` | Review |
| `/build-fix` | Fix errors |
| `/refactor-clean` | Refactor |
| `/update-docs` | Sync docs |

---

## Requirements
- Python 3.6+, Git
- [Claude Code](https://www.anthropic.com/claude-code) and/or [OpenCode](https://opencode.ai/)

---

## Credits
- [Spec Kit](https://github.com/github/spec-kit) by GitHub
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) by @affaan-m

MIT License
