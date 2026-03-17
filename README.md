# 🤖 ag_ai — AI Development Infrastructure

> **One command installs a complete AI-powered dev environment into any project.**
> Combines three battle-tested systems: Custom Agents + Spec Kit + Everything Claude Code (ECC)

[![GitHub](https://img.shields.io/badge/GitHub-ag__ai-blue?logo=github)](https://github.com/gebrilae-eng/ag_ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ⚡ Quick Start

**First time — clone anywhere you want:**
```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git D:\tools\ag_ai
git clone https://github.com/gebrilae-eng/ag_ai.git F:\ag_ai
git clone https://github.com/gebrilae-eng/ag_ai.git C:\Users\AG\ag_ai
```

**Install into any project (any drive, any path):**
```cmd
D:\tools\ag_ai\install.bat C:\laragon\www\my-project
F:\ag_ai\install.bat D:\projects\new-app
F:\ag_ai\install.bat .
```

The installer asks you **2 questions** before installing:
1. Which AI tool? (Claude Code / OpenCode / Both)
2. Which components? (Core Agents / ECC / Sub-Agents / PHP Rules / Spec Kit)

---

## 🧠 What's Inside

### 3 Systems, Fully Merged

| System | What it brings |
|--------|---------------|
| **Custom Agents** | Specialized roles: SQL, Telegram, n8n, API, debugging |
| **[Spec Kit](https://github.com/github/spec-kit)** | Spec-driven development — write specs before code |
| **[ECC](https://github.com/affaan-m/everything-claude-code)** | Battle-tested agents: TDD, security, architecture, review |

---

## 📁 Structure — Installed Files

```
your-project/
├── CLAUDE.md                        ← AI entry point
├── specs/                           ← feature specs
├── .claude/commands/                ← Claude Code slash commands
│   ├── onboard.md
│   ├── tdd.md
│   ├── verify.md
│   ├── security.md
│   └── ...
├── .opencode/agents/                ← OpenCode YAML agents
│   ├── orchestrator.yml
│   ├── architect.yml
│   ├── coder.yml
│   ├── db-agent.yml
│   ├── tdd-guide.yml
│   ├── security-reviewer.yml
│   ├── sql-helper.yml
│   ├── telegram-bot.yml
│   ├── n8n-workflow.yml
│   └── debugger.yml
└── .ai/
    ├── agents/
    │   ├── orchestrator.md
    │   ├── coder.md
    │   ├── db-agent.md
    │   ├── api-agent.md
    │   ├── spec-workflow.md
    │   └── ecc/            ← 8 ECC agents
    ├── sub-agents/         ← 5 specialists
    ├── rules/php/          ← security, patterns, testing
    ├── rules/common/       ← security, coding-style
    ├── context/            ← filled by /onboard
    └── spec/               ← Spec Kit commands + templates
```

---

## 🚀 Workflow

### Claude Code
```
/onboard              ← first time: fills all context files
/speckit.specify      ← define WHAT to build
/speckit.plan         ← define HOW (tech stack)
/speckit.tasks        ← break into tasks
/tdd                  ← implement test-first
/verify               ← quality gate
/security             ← OWASP audit
/code-review          ← review before commit
```

### OpenCode
```
use orchestrator agent to build [feature]
use tdd-guide agent to implement [function]
use security-reviewer agent to audit [file]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug]
```

Or from command line:
```cmd
opencode --agent orchestrator "build a daily sales report"
opencode run --agent tdd-guide "implement calculateProfit function"
```

---

## 📋 All Slash Commands (Claude Code)

| Command | Purpose |
|---------|---------|
| `/onboard` | Interactive wizard — fills all context files |
| `/speckit.constitution` | Create project principles (once per project) |
| `/speckit.specify` | Define what to build |
| `/speckit.clarify` | Resolve ambiguous requirements |
| `/speckit.plan` | Technical implementation plan |
| `/speckit.tasks` | Break plan into ordered tasks |
| `/speckit.implement` | Execute all tasks |
| `/speckit.analyze` | Cross-check consistency |
| `/tdd` | Test-first implementation |
| `/verify` | Full quality gate |
| `/quality-gate` | Quick quality scan |
| `/code-review` | Code review |
| `/security` | OWASP security audit |
| `/build-fix` | Fix build errors |
| `/refactor-clean` | Refactor without changing behavior |
| `/learn` | Extract patterns from session |
| `/checkpoint` | Save session state |
| `/update-docs` | Sync documentation with code |

---

## 🔄 Update ag_ai

```cmd
D:\tools\ag_ai\install.bat C:\path\to\project
```

`install.bat` always pulls latest from GitHub before installing.
Works from **any drive or folder** — no hardcoded paths.

---

## ⚙️ Requirements

- Python 3.6+ (no extra packages)
- Git
- [Claude Code](https://www.anthropic.com/claude-code) or [OpenCode](https://opencode.ai/)

---

## 📚 Credits

- **[Spec Kit](https://github.com/github/spec-kit)** by GitHub
- **[Everything Claude Code](https://github.com/affaan-m/everything-claude-code)** by [@affaan-m](https://github.com/affaan-m)

---

## 📄 License

MIT — use freely in any project.
