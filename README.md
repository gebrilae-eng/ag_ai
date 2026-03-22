# ag_ai v3 — AI Development Infrastructure

> Install once. Run the wizard. Everything generates automatically for any project.

[![GitHub](https://img.shields.io/badge/GitHub-ag__ai-blue?logo=github)](https://github.com/gebrilae-eng/ag_ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What It Does

Run one command and `wizard.py` asks 4 questions about your project,
then generates everything automatically based on your stack:

| What gets generated | How it adapts |
|---------------------|---------------|
| `.ai/context/` files | Project name, description, rules |
| `AGENTS.md` + `CLAUDE.md` + `PRD.md` | Stack + integrations |
| `.claude/settings.json` | Stack-aware hooks (PHP/Python/Node/MySQL/n8n/Telegram) |
| `.claude/skills/` | SKILL.md files for your framework |
| `.claude/commands/` | 6 slash commands |
| `.claude/security/` | `security-audit.js` for your stack |
| `session-observer.js` | Background pattern logger |

Works with **PHP, Python, Node.js** and any combination of
**MySQL, PostgreSQL, MongoDB, SQLite, n8n, Telegram, Docker**.

---

## Quick Start

```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git C:\ag_ai
python C:\ag_ai\wizard.py D:\my-project
```

That is it. The wizard handles everything else.

---

## Scripts

| File | Purpose |
|------|---------|
| `wizard.py` | **Main entry point** -- asks questions, generates everything |
| `run.bat` | Menu launcher for all operations |
| `setup_ai.py` | Installs 18 agents + agency-agents into a project |
| `validate.py` | Checks project setup completeness |
| `agent.bat` | Launches OpenCode with agent selector |
| `CLAUDE.md` | Claude Code entry point template |

### wizard.py -- the core command

```cmd
python C:\ag_ai\wizard.py D:\my-project
```

Asks 4 groups of questions, then generates in one pass:

```
1/4  Project info  (name, description, type, status)
2/4  Tech stack    (backend, DB, frontend, integrations)
3/4  Rules         (hard rules, language, AI tool)
  -> generates everything
```

### run.bat -- menu mode

```cmd
C:\ag_ai\run.bat
```

```
1) new-project    wizard + install + agents
2) install        install 18 agents into project
3) wizard         run wizard only
4) validate       check project setup
5) update         update ag_ai from GitHub
6) update-project update agents (keep context)
7) agent          launch OpenCode with agent menu
```

### run.bat -- direct mode

```cmd
C:\ag_ai\run.bat wizard   D:\my-project
C:\ag_ai\run.bat install  D:\my-project
C:\ag_ai\run.bat validate D:\my-project
```

---

## What the Wizard Generates

### Hooks (`.claude/settings.json`)

Hooks run automatically on every Edit/Write/Bash -- no manual trigger needed.

| Hook | Triggers on | Blocks when |
|------|-------------|-------------|
| Universal | All projects | git push --force, hardcoded secrets |
| MySQL / PostgreSQL | DB detected | DROP TABLE, DELETE without WHERE |
| PHP | PHP backend | MD5 passwords, SELECT *, SQL concat |
| Python | Python backend | eval(), os.system(), f-string in SQL |
| Node.js | Node backend | eval(), innerHTML=, console.log |
| n8n | n8n integration | Template literals in Code nodes |
| Telegram | Telegram integration | Markdown parse_mode instead of HTML |
| Observer | All (async) | Silent -- logs patterns for /learn |

### Skills (`.claude/skills/`)

SKILL.md files Claude Code reads automatically before working on your project.

| Skill | When included |
|-------|--------------|
| `security-core` | Always |
| `git-workflow` | Always |
| `tdd-workflow` | Always |
| `sql-patterns` | MySQL / PostgreSQL / SQLite detected |
| `n8n-patterns` | n8n integration detected |
| `telegram-bot` | Telegram integration detected |
| `api-design` | API / REST / Express / Django / Laravel detected |

### Commands (`.claude/commands/`)

Installed globally in `~/.claude/commands/` and per-project.

| Command | Purpose |
|---------|---------|
| `/learn` | Extract patterns from session -> save as instincts |
| `/instinct-status` | View all instincts by domain with confidence |
| `/evolve` | Cluster instincts into new SKILL.md or command |
| `/checkpoint` | Save session state for resuming |
| `/verify` | Quality gate before committing |
| `/security` | Run the generated security audit |

### Security Audit (`.claude/security/security-audit.js`)

Generated for your specific stack. Run directly:

```cmd
node ~/.claude/security/security-audit.js D:\my-project
```

Checks: hardcoded secrets (14 patterns) | SQL injection | stack-specific
anti-patterns | .env protection | .gitignore completeness.
Grades A to F. Exits with code 1 if critical/high issues found (CI-compatible).

---

## Continuous Learning Loop

After every session:

```
Session ends
  -> /learn             extract patterns, save as instincts
  -> /instinct-status   review what was captured
  -> /evolve            cluster into new SKILL.md when ready
  -> /verify            quality gate before commit
  -> /security          security audit before deploy
```

Instincts accumulate in `~/.claude/instincts/personal/`.
The background `session-observer.js` logs patterns silently during work.

---

## 18 Agents (installed via setup_ai.py)

### Planning
| Agent | Role |
|-------|------|
| `orchestrator` | Delegates only -- never writes code |
| `spec-workflow` | specify -> clarify -> plan -> tasks -> implement |
| `architect` | System design and trade-offs |

### Development
| Agent | Role |
|-------|------|
| `coder` | Write and refactor code |
| `tdd-guide` | Red -> Green -> Refactor |
| `db-agent` | MySQL schema, migrations, indexes |
| `api-agent` | REST endpoints, webhooks |
| `refactor-cleaner` | Improve structure without behavior change |
| `build-error-resolver` | Fix build and runtime errors |

### Review
| Agent | Role |
|-------|------|
| `code-reviewer` | Correctness, performance, style |
| `security-reviewer` | OWASP Top 10 audit |
| `database-reviewer` | Schema quality, query safety |
| `doc-updater` | Keep docs in sync with code |

### Specialists
| Agent | Role |
|-------|------|
| `sql-helper` | Optimized MySQL queries |
| `telegram-bot` | HTML formatting, Arabic RTL |
| `n8n-workflow` | Workflow design, code nodes |
| `debugger` | Reproduce -> Isolate -> Fix |
| `test-writer` | Unit, integration, E2E tests |

---

## Project Structure (after wizard.py)

```
your-project/
├── AGENTS.md                       <- agent routing table
├── CLAUDE.md                       <- Claude Code entry point
├── PRD.md                          <- product requirements
├── specs/                          <- feature specs
├── .claude/
│   ├── settings.json               <- hooks (auto-generated)
│   ├── commands/                   <- /learn /verify /security ...
│   ├── skills/                     <- SKILL.md files (auto-generated)
│   ├── security/                   <- security-audit.js (auto-generated)
│   └── agents/
├── .opencode/agents/               <- 18 YAML agent configs
└── .ai/
    ├── agents/                     <- 18 agent instruction files
    ├── rules/
    │   ├── common.md
    │   └── php.md
    ├── spec/
    │   ├── commands.md
    │   ├── templates/
    │   └── memory/constitution.md
    └── context/
        ├── PROJECT.md
        ├── STACK.md
        ├── RULES.md
        └── wizard-answers.json
```

---

## Repo Structure

```
ag_ai/
├── wizard.py         <- main entry point (all-in-one generator)
├── run.bat           <- menu launcher
├── setup_ai.py       <- agent installer engine
├── validate.py       <- setup checker
├── agent.bat         <- OpenCode agent launcher
├── CLAUDE.md         <- entry point template
├── README.md
├── CHANGELOG.md
├── .ai/              <- installed into projects
├── .opencode/agents/ <- 18 YAML agent configs
├── .claude/commands/ <- slash command templates
└── .config/opencode/ <- global OpenCode config
```

---

## Global OpenCode Config

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
use debugger agent to investigate [bug or error]
use spec-workflow agent to specify: I want to add [feature]
use telegram-bot agent to implement [command or message]
use n8n-workflow agent to design workflow for [task]
```

---

## Claude Code Slash Commands

| Command | Purpose |
|---------|---------|
| `/learn` | Extract patterns from session |
| `/instinct-status` | View learned instincts |
| `/evolve` | Turn instincts into skills |
| `/checkpoint` | Save session state |
| `/verify` | Quality gate before commit |
| `/security` | Run security audit |
| `/speckit.specify` | New feature spec |
| `/speckit.clarify` | Resolve ambiguities |
| `/speckit.plan` | Technical plan |
| `/speckit.tasks` | Ordered task list |
| `/speckit.implement` | Execute spec |
| `/tdd` | Test-first development |
| `/code-review` | Code review |
| `/build-fix` | Fix build errors |
| `/refactor-clean` | Refactor |
| `/update-docs` | Sync documentation |

---

## Requirements

- Python 3.6+, Git, Node.js (for hooks and security audit)
- [Claude Code](https://www.anthropic.com/claude-code) and/or [OpenCode](https://opencode.ai/)

---

## Credits

- [Spec Kit](https://github.com/github/spec-kit) by GitHub
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) by @affaan-m
- [agency-agents](https://github.com/msitarzewski/agency-agents) by @msitarzewski

MIT License
