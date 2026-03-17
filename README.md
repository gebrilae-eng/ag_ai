# 🤖 ag_ai — AI Development Infrastructure

> **One command installs a complete AI-powered dev environment into any project.**
> Combines three battle-tested systems: Custom Agents + Spec Kit + Everything Claude Code (ECC)

[![GitHub](https://img.shields.io/badge/GitHub-ag__ai-blue?logo=github)](https://github.com/gebrilae-eng/ag_ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ⚡ Quick Start

**First time on a new machine:**
```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git C:\temp\ag_ai
```

**Install into any project:**
```cmd
C:\temp\ag_ai\install.bat C:\path\to\your-project
```

Then open Claude Code or OpenCode and run:
```
/onboard
```
The wizard asks questions about your project and auto-fills all context files.

---

## 🧠 What's Inside

### 3 Systems, Fully Merged

| System | What it brings |
|--------|---------------|
| **Custom Agents** | Specialized roles: SQL, Telegram, n8n, API, debugging |
| **[Spec Kit](https://github.com/github/spec-kit)** | Spec-driven development — define specs before writing code |
| **[ECC](https://github.com/affaan-m/everything-claude-code)** | Battle-tested agents: TDD, security, architecture, code review |

---

## 📁 Structure — 36 Files Installed

```
.ai/
├── agents/
│   ├── orchestrator.md        🧠 Routes tasks to right agent
│   ├── coder.md               💻 Writes production code
│   ├── db-agent.md            🗄️  Database specialist
│   ├── api-agent.md           🔌 API & integrations
│   ├── spec-workflow.md       📋 Spec-driven workflow bridge
│   └── ecc/
│       ├── architect.md           System design (runs on Opus)
│       ├── tdd-guide.md           Test-first development
│       ├── security-reviewer.md   OWASP Top 10 audit
│       ├── code-reviewer.md       Quality review
│       ├── refactor-cleaner.md    Code cleanup
│       ├── build-error-resolver.md Fix build errors
│       ├── database-reviewer.md   DB schema + query review
│       └── doc-updater.md         Documentation sync
├── sub-agents/
│   ├── sql-helper.md          SQL query generation
│   ├── telegram-bot.md        Telegram HTML formatting + splitting
│   ├── n8n-workflow.md        n8n automation patterns
│   ├── debugger.md            Systematic bug investigation
│   └── test-writer.md         Unit / integration test writing
├── rules/
│   ├── php/                   PHP security, patterns, testing
│   └── common/                Universal security, coding style
├── context/
│   ├── PROJECT.md    ← filled by /onboard
│   ├── STACK.md      ← filled by /onboard
│   └── RULES.md      ← filled by /onboard
└── spec/
    ├── commands/     Spec Kit slash commands
    ├── templates/    spec / plan / tasks / constitution
    └── memory/       constitution.md lives here

.claude/commands/
└── onboard.md        ← interactive setup wizard
```

---

## 🚀 The Full Workflow

### New Feature — Every Time
```
/speckit.specify    → describe WHAT to build (no tech details)
/speckit.clarify    → resolve any ambiguity (optional)
/speckit.plan       → define HOW — tech stack + architecture
/speckit.tasks      → break into ordered, executable tasks
/tdd                → implement test-first (Red → Green → Refactor)
/verify             → full quality gate check
/code-review        → review before committing
/security           → OWASP security audit
```

### Quick Commands
```
/build-fix          → diagnose and fix build errors
/refactor-clean     → clean up code without changing behavior
/learn              → extract reusable patterns from the session
/checkpoint         → save session context before compacting
/update-docs        → keep documentation in sync with code
```

### First Time (new project)
```
/speckit.constitution  → create project principles (once per project)
```

---

## 📋 Slash Commands Reference

### Spec Kit (Planning)
| Command | Purpose |
|---------|---------|
| `/speckit.constitution` | Create project governing principles |
| `/speckit.specify` | Define what to build (requirements + user stories) |
| `/speckit.clarify` | Resolve underspecified requirements |
| `/speckit.plan` | Technical implementation plan |
| `/speckit.tasks` | Break plan into ordered task list |
| `/speckit.implement` | Execute all tasks in correct order |
| `/speckit.analyze` | Cross-check spec ↔ plan consistency |

### ECC (Development Quality)
| Command | Purpose |
|---------|---------|
| `/tdd` | Implement with test-first methodology |
| `/verify` | Full quality gate: build + lint + tests + coverage |
| `/quality-gate` | Quick quality scan on a file or directory |
| `/code-review` | Comprehensive code review |
| `/security` | Security vulnerability audit (OWASP Top 10) |
| `/build-fix` | Diagnose and fix build errors |
| `/refactor-clean` | Refactor without changing behavior |
| `/learn` | Extract reusable patterns from current session |
| `/checkpoint` | Save session state before context compaction |
| `/update-docs` | Sync documentation with code changes |

### Onboarding
| Command | Purpose |
|---------|---------|
| `/onboard` | Interactive wizard — auto-fills all context files |

---

## 🔄 Update ag_ai

To get the latest agents and commands:

```cmd
C:\temp\ag_ai\install.bat C:\path\to\your-project
```

`install.bat` always pulls the latest from GitHub before installing.

---

## 🛠️ How It Works

```
install.bat
    │
    ├── git fetch + reset --hard   ← always gets latest version
    │
    └── setup_ai.py [project path]
            │
            ├── copies .ai/        ← all agents, rules, skills
            ├── copies .claude/    ← slash commands
            ├── copies CLAUDE.md   ← entry point for AI
            └── creates dirs       ← specs/, .ai/spec/memory/, etc.
```

---

## ⚙️ Requirements

- Python 3.6+ (no extra packages needed)
- Git
- [Claude Code](https://www.anthropic.com/claude-code) or [OpenCode](https://opencode.ai/)

Works on any project path — not tied to any specific framework or directory structure.

---

## 📚 Credits

- **[Spec Kit](https://github.com/github/spec-kit)** — spec-driven development by GitHub
- **[Everything Claude Code](https://github.com/affaan-m/everything-claude-code)** — battle-tested agents by [@affaan-m](https://github.com/affaan-m)

---

## 📄 License

MIT — use freely in any project.
