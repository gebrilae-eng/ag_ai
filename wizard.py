#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai - Project Setup Wizard
Run ONCE at the start of any new project.
Usage:
  python wizard.py
  python wizard.py D:\my-project
"""

import sys, os, json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

BOLD   = "\033[1m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
DIM    = "\033[2m"
RESET  = "\033[0m"

def title(t): print(f"\n{BOLD}{'─'*50}\n  {t}\n{'─'*50}{RESET}")

def ask(q, default=""):
    hint = f" [{default}]" if default else ""
    try:
        val = input(f"{CYAN}  → {q}{hint}: {RESET}").strip()
        return val if val else default
    except (EOFError, KeyboardInterrupt):
        return default

def ask_multi(q, options):
    print(f"\n{CYAN}  → {q}{RESET}")
    for i, o in enumerate(options, 1):
        print(f"     {BOLD}{i}{RESET}) {o}")
    print(f"     {BOLD}0{RESET}) {DIM}All{RESET}")
    try:
        raw = input("     Choose numbers (e.g. 1 3) or 0 for all: ").strip()
    except (EOFError, KeyboardInterrupt):
        return options
    if not raw or raw == "0":
        return options
    result = []
    for x in raw.split():
        try:
            idx = int(x) - 1
            if 0 <= idx < len(options):
                result.append(options[idx])
        except ValueError:
            pass
    return result if result else options

def get_project_path():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1]).resolve()
    else:
        print(f"\n{BOLD}  ag_ai — Project Setup Wizard{RESET}\n")
        raw = ask("Path to your project folder")
        p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists():
        p.mkdir(parents=True)
    return p

def collect_answers():
    a = {}
    title("1 / 4  —  Project Info")
    a["name"]         = ask("Project name", "My Project")
    a["description"]  = ask("What does it do?")
    a["type"]         = ask("Type (web / api / bot / automation)", "web")
    a["status"]       = ask("Status (new / development / production)", "new")
    a["out_of_scope"] = ask("What does it NOT do?", "Not defined yet")

    title("2 / 4  —  Tech Stack")
    a["backend"]   = ask("Backend (e.g. PHP vanilla / Laravel / Node.js)", "PHP vanilla")
    a["db_engine"] = ask("Database engine (e.g. MySQL 8 / PostgreSQL)", "MySQL 8")
    a["db_name"]   = ask("Database name", "my_db")
    a["db_user"]   = ask("DB username", "root")
    a["db_pass"]   = ask("DB password (blank if none)", "")
    a["frontend"]  = ask("Frontend (e.g. HTML/JS / React / Blade)", "HTML/CSS/JS")
    a["local"]     = ask("Local dev (e.g. Laragon / XAMPP / Docker)", "Laragon")
    a["integrations"] = ask_multi("Integrations?",
        ["Telegram bot", "n8n workflows", "REST APIs", "Email", "WhatsApp", "None"])

    title("3 / 4  —  Rules")
    a["hard_rules"] = ask("Hard business rules? (e.g. never delete records)", "")
    a["language"]   = ask("Docs language (English / Arabic / Both)", "Both")

    title("4 / 4  —  AI Tool")
    a["ai_tool"] = ask("AI tool (claude / opencode / both)", "both")
    return a

def write_project_md(path, a):
    integrations = "\n".join(f"- {i}" for i in a["integrations"])
    (path / ".ai/context/PROJECT.md").write_text(f"""# Project Overview

## Project Name
`{a["name"]}`

## Description
{a["description"]}

## Type
{a["type"].capitalize()}

## Status
{a["status"].capitalize()}

## Key Integrations
{integrations}

## Out of Scope
- {a["out_of_scope"]}
""", encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/PROJECT.md")

def write_stack_md(path, a):
    integrations = "\n".join(f"- {i}" for i in a["integrations"])
    app_name = a["name"].upper().replace(" ", "_")
    (path / ".ai/context/STACK.md").write_text(f"""# Tech Stack

## Backend
- Language / Framework: `{a["backend"]}`
- Local Server: `{a["local"]}`

## Database
- Engine: `{a["db_engine"]}`
- Name: `{a["db_name"]}`

## Frontend
- `{a["frontend"]}`

## Integrations
{integrations}

## Environment Variables
```env
APP_NAME={app_name}
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE={a["db_name"]}
DB_USERNAME={a["db_user"]}
DB_PASSWORD={a["db_pass"]}
```
""", encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/STACK.md")

def write_rules_md(path, a):
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules yet"
    (path / ".ai/context/RULES.md").write_text(f"""# Coding Rules

## Universal Rules
- NEVER hardcode credentials or API keys
- NEVER use SELECT * in production
- ALWAYS validate and sanitize all user inputs
- ALWAYS use parameterized SQL queries
- ALWAYS handle errors explicitly

## Project-Specific Rules
{hard}

## Documentation Language
{a["language"]}

## Security
- Parameterized queries for all DB operations
- Validate at input boundary
- Store secrets in .env only
""", encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/RULES.md")

def write_agents_md(path, a):
    """AGENTS.md - the key file OpenCode reads first"""
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules yet"
    integrations_str = ", ".join(a["integrations"])
    (path / "AGENTS.md").write_text(f"""# AGENTS.md — {a["name"]}

> Read this file first. It tells AI agents everything about this project.
> Also read `CLAUDE.md` and `.ai/context/` files.

## Project Reality
- Name: {a["name"]}
- Stack: {a["backend"]} + {a["db_engine"]} ({a["db_name"]}) + {a["frontend"]}
- Integrations: {integrations_str}
- Local server: {a["local"]}

## Build / Lint / Test Commands
- Document these here once the app is scaffolded.
- Expected PHP test: `vendor/bin/phpunit`
- Expected single test: `vendor/bin/phpunit --filter test_name`

## Agent Routing
| Task | Use Agent |
|------|-----------|
| Complex multi-step | `orchestrator` |
| Write / refactor code | `coder` |
| Database schema / queries | `db-agent` |
| API / integrations | `api-agent` |
| Spec-first planning | `spec-workflow` |
| System design | `architect` |
| TDD implementation | `tdd-guide` |
| Security audit | `security-reviewer` |
| Code review | `code-reviewer` |
| DB review | `database-reviewer` |
| Refactoring | `refactor-cleaner` |
| Build errors | `build-error-resolver` |
| Documentation | `doc-updater` |
| SQL generation | `sql-helper` |
| Telegram bot | `telegram-bot` |
| n8n workflows | `n8n-workflow` |
| Debugging | `debugger` |
| Writing tests | `test-writer` |

## Available Agents

### Core agents
`orchestrator` `coder` `db-agent` `api-agent` `spec-workflow`

### ECC agents
`architect` `tdd-guide` `security-reviewer` `code-reviewer`
`refactor-cleaner` `doc-updater` `database-reviewer` `build-error-resolver`

### Sub-agents
`sql-helper` `telegram-bot` `n8n-workflow` `debugger` `test-writer`

### Agent files
- Markdown instructions: `.ai/agents/` and `.ai/sub-agents/`
- OpenCode configs: `.opencode/agents/`
- Keep both in sync when adding or changing agents.

## How to Invoke Agents

### Claude Code
```
/tdd              implement test-first
/security         OWASP audit
/code-review      review code
/build-fix        fix build errors
/speckit.specify  start a new feature spec
```

### OpenCode
```
use orchestrator agent to build [feature]
use tdd-guide agent to implement [function]
use security-reviewer agent to audit [file or folder]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug]
```

## Non-Negotiable Rules
- NEVER hardcode credentials, tokens, or API keys
- NEVER use SELECT * in production
- ALWAYS validate user input at the boundary
- ALWAYS use parameterized SQL
- ALWAYS handle errors explicitly
{hard}

## Coding Style Summary
- Functions do one thing (~30 lines max)
- Files ~300 lines max
- PHP: PascalCase classes, camelCase methods
- DB tables: snake_case plural + soft deletes (deleted_at)
- Prefer clarity over cleverness
- No dead code or placeholder TODOs in finished work

## Workflow
1. Spec first → code second (`/speckit.specify` or `use spec-workflow agent`)
2. Tests first → TDD always
3. Small targeted changes over large rewrites
4. Summarize what changed after each task
""", encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  AGENTS.md")

def write_claude_md(path, a):
    tool = a["ai_tool"].lower()
    (path / "CLAUDE.md").write_text(f"""# AI Instructions — {a["name"]}

> Read `AGENTS.md` and `.ai/context/` first.

## Stack
`{a["backend"]}` + `{a["db_engine"]} / {a["db_name"]}` + `{a["frontend"]}`

## Quick Agent Reference
| Task | Agent |
|------|-------|
| Complex task | orchestrator |
| Code | coder |
| DB | db-agent |
| API | api-agent |
| TDD | tdd-guide |
| Security | security-reviewer |
| SQL | sql-helper |
| Telegram | telegram-bot |
| n8n | n8n-workflow |
| Bugs | debugger |

{"## Claude Code" if "claude" in tool or "both" in tool else ""}
{"```" if "claude" in tool or "both" in tool else ""}
{"/speckit.specify  new feature" if "claude" in tool or "both" in tool else ""}
{"/tdd              implement test-first" if "claude" in tool or "both" in tool else ""}
{"/verify           quality check" if "claude" in tool or "both" in tool else ""}
{"/security         audit" if "claude" in tool or "both" in tool else ""}
{"```" if "claude" in tool or "both" in tool else ""}

{"## OpenCode" if "open" in tool or "both" in tool else ""}
{"```" if "open" in tool or "both" in tool else ""}
{"use orchestrator agent to build [feature]" if "open" in tool or "both" in tool else ""}
{"use tdd-guide agent to implement [function]" if "open" in tool or "both" in tool else ""}
{"```" if "open" in tool or "both" in tool else ""}
""", encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  CLAUDE.md")

def write_constitution(path, a):
    (path / ".ai/spec/memory").mkdir(parents=True, exist_ok=True)
    hard = a["hard_rules"].strip() if a["hard_rules"].strip() else "No hard deletes — use soft-delete (deleted_at)"
    (path / ".ai/spec/memory/constitution.md").write_text(f"""# Constitution — {a["name"]}

**Version**: 1.0.0

## P1 — Data Integrity
All DB operations MUST use parameterized queries.
{hard}

## P2 — Security First
ALL user inputs MUST be validated before processing.
Secrets MUST live in .env — never in source code.

## P3 — Code Quality
Every function MUST do one thing only.
Tests MUST be written BEFORE implementation (TDD).
Coverage target: 80%+

## P4 — Language
Comments and docs: {a["language"]}

## P5 — Consistency
Follow .ai/context/RULES.md at all times.
When in doubt — ask, don't assume.
""", encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/spec/memory/constitution.md")

def main():
    print(f"\n{BOLD}{'='*50}")
    print(f"  ag_ai — Project Setup Wizard")
    print(f"{'='*50}{RESET}")

    project_path = get_project_path()
    print(f"\n  {YELLOW}Project:{RESET} {project_path}")

    answers = collect_answers()

    # Create dirs
    for d in [".ai/context", ".ai/spec/memory", ".ai/agents", ".ai/sub-agents", "specs"]:
        (project_path / d).mkdir(parents=True, exist_ok=True)

    title("Writing files...")
    write_agents_md(project_path, answers)       # NEW — AGENTS.md first
    write_claude_md(project_path, answers)
    write_project_md(project_path, answers)
    write_stack_md(project_path, answers)
    write_rules_md(project_path, answers)
    write_constitution(project_path, answers)

    # Save answers
    answers_copy = dict(answers)
    answers_copy["integrations"] = list(answers_copy["integrations"])
    (project_path / ".ai/context/wizard-answers.json").write_text(
        json.dumps(answers_copy, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  {GREEN}OK{RESET}  .ai/context/wizard-answers.json")

    tool = answers["ai_tool"].lower()
    print(f"\n{BOLD}{'='*50}")
    print(f"  Done! {answers['name']} is ready.")
    print(f"{'='*50}{RESET}\n")
    if "claude" in tool or "both" in tool:
        print(f"  Claude Code:  cd \"{project_path}\"  then  claude")
        print(f"                /speckit.specify  I want to build [feature]\n")
    if "open" in tool or "both" in tool:
        print(f"  OpenCode:     cd \"{project_path}\"  then  opencode")
        print(f"                use orchestrator agent to help me build [feature]\n")

if __name__ == "__main__":
    main()
