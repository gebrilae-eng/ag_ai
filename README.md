# ag_ai — AI Development Infrastructure

> Complete AI-powered dev environment. Install once, reuse across all projects.

[![GitHub](https://img.shields.io/badge/GitHub-ag__ai-blue?logo=github)](https://github.com/gebrilae-eng/ag_ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Quick Start

```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git C:\ag_ai
C:\ag_ai\run.bat
```

---

## Scripts (root — 8 files only)

| File | Purpose |
|------|---------|
| `run.bat` | **Main entry point** — menu for all operations |
| `agent.bat` | Launch OpenCode with agent selector menu |
| `setup_ai.py` | Installer engine (called by run.bat) |
| `wizard.py` | Context file generator (called by run.bat) |
| `validate.py` | Setup checker (called by run.bat) |
| `CLAUDE.md` | Claude Code entry point template |
| `README.md` | This file |
| `CHANGELOG.md` | Version history |

### run.bat — menu mode
```cmd
C:\ag_ai\run.bat
```
```
1) new-project    create + install + wizard
2) install        install agents into a project
3) wizard         fill context files
4) validate       check project setup
5) update         update ag_ai from GitHub
6) update-project update agents (keep context)
7) agent          launch OpenCode with agent menu
```

### run.bat — direct mode
```cmd
C:\ag_ai\run.bat install        D:\my-project
C:\ag_ai\run.bat wizard         D:\my-project
C:\ag_ai\run.bat validate       D:\my-project
C:\ag_ai\run.bat update-project D:\my-project
C:\ag_ai\run.bat agent
```

### Python flags
```cmd
python setup_ai.py D:\my-project --dry-run        :: preview
python setup_ai.py D:\my-project --update-agents  :: agents only
```

---

## Global OpenCode Config

Copy once to get all 18 agents in every project:
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

## Project Structure (after install)

```
your-project/
├── AGENTS.md                    ← OpenCode reads first
├── CLAUDE.md                    ← Claude Code reads first
├── specs/                       ← feature specs
├── .opencode/agents/            ← 18 YAML agent configs
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

---

## Repo Structure

```
ag_ai/
├── run.bat           ← single entry point
├── agent.bat         ← OpenCode agent launcher
├── setup_ai.py       ← installer engine
├── wizard.py         ← context file generator
├── validate.py       ← setup checker
├── CLAUDE.md         ← entry point template
├── README.md
├── CHANGELOG.md
├── .ai/              ← installed into projects
├── .opencode/agents/ ← 18 YAML configs
├── .claude/commands/ ← slash commands
└── .config/opencode/ ← global OpenCode config
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
