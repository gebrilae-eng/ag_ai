#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai - Project Setup Wizard
Run this ONCE at the start of any new project.
It asks you questions and fills all AI context files automatically.

Usage:
  python wizard.py                    (asks for project path)
  python wizard.py D:\my-project      (direct path)
"""

import sys
import os
import json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

# ─────────────────────────────────────────────
BOLD  = "\033[1m"
GREEN = "\033[92m"
CYAN  = "\033[96m"
YELLOW= "\033[93m"
DIM   = "\033[2m"
RESET = "\033[0m"

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
    try:
        raw = input(f"     اختار أرقام (مثال: 1 3) أو Enter للكل: ").strip()
    except (EOFError, KeyboardInterrupt):
        return options
    if not raw:
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

# ─────────────────────────────────────────────
def get_project_path():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1]).resolve()
    else:
        print(f"\n{BOLD}  ag_ai — Project Setup Wizard{RESET}")
        print(f"  {DIM}Fills all AI context files before you start coding{RESET}\n")
        raw = ask("Path to your project folder")
        p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists():
        print(f"\n  Creating folder: {p}")
        p.mkdir(parents=True)
    return p

def collect_answers():
    answers = {}

    title("1 / 4  —  Project Info")
    answers["name"]        = ask("Project name", "My Project")
    answers["description"] = ask("What does it do? (1-2 sentences)")
    answers["type"]        = ask("Type (web / api / bot / automation / other)", "web")
    answers["status"]      = ask("Status (new / development / production)", "new")

    title("2 / 4  —  Tech Stack")
    answers["backend"]  = ask("Backend (e.g. PHP vanilla / PHP+Laravel / Node.js / Python)", "PHP vanilla")
    answers["database"] = ask("Database (e.g. MySQL 8 + my_db / PostgreSQL / none)", "MySQL 8")
    answers["frontend"] = ask("Frontend (e.g. HTML/JS / React / Blade / API only)", "HTML/CSS/JS")
    answers["local"]    = ask("Local dev tool (e.g. Laragon / XAMPP / Docker)", "Laragon")
    answers["integrations"] = ask_multi(
        "Integrations?",
        ["Telegram bot", "n8n workflows", "REST APIs", "Email", "WhatsApp", "None"]
    )

    title("3 / 4  —  Rules & Conventions")
    answers["hard_rules"] = ask("Any hard business rules? (e.g. never delete records)", "")
    answers["naming"]     = ask("Any special naming? (or press Enter for defaults)", "")
    answers["language"]   = ask("Docs language (English / Arabic / Both)", "Both")

    title("4 / 4  —  AI Tool")
    answers["ai_tool"] = ask("AI tool (claude / opencode / both)", "both")

    return answers


# ─────────────────────────────────────────────
def write_project_md(path, a):
    integrations = "\n".join(f"- {i}" for i in a["integrations"])
    content = f"""# Project Overview

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
- [Add what this project does NOT do]
"""
    (path / ".ai/context/PROJECT.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/PROJECT.md")

def write_stack_md(path, a):
    content = f"""# Tech Stack

## Backend
- Language / Framework: `{a["backend"]}`
- Local Server: `{a["local"]}`

## Database
- Engine: `{a["database"]}`

## Frontend
- `{a["frontend"]}`

## Integrations
{chr(10).join(f"- {i}" for i in a["integrations"])}

## Environment Variables
```env
APP_NAME={a["name"].replace(" ", "_").upper()}
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=
DB_USERNAME=root
DB_PASSWORD=
```
"""
    (path / ".ai/context/STACK.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/STACK.md")

def write_rules_md(path, a):
    hard = f"\n- {a['hard_rules']}" if a["hard_rules"] else "\n- [Add project-specific rules]"
    naming = f"\n- {a['naming']}" if a["naming"] else "\n- snake_case for DB tables, camelCase for functions"
    content = f"""# Coding Rules & Conventions

## Universal Rules
- NEVER hardcode credentials or API keys
- NEVER use SELECT * in production queries
- ALWAYS validate and sanitize all user inputs
- ALWAYS use parameterized SQL queries
- ALWAYS handle errors explicitly

## Project-Specific Rules
{hard}

## Naming Conventions
{naming}

## Documentation Language
{a["language"]}

## Security
- Parameterized queries for all DB operations
- Validate at input boundary
- Store secrets in .env only
"""
    (path / ".ai/context/RULES.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/RULES.md")


def write_claude_md(path, a):
    tool = a["ai_tool"].lower()
    oc_section = ""
    if "open" in tool or "both" in tool:
        oc_section = """
## OpenCode
```
use orchestrator agent to help me build [feature]
use tdd-guide agent to implement [function]
use security-reviewer agent to audit [file]
```
"""
    claude_section = ""
    if "claude" in tool or "both" in tool:
        claude_section = """
## Claude Code
```
/onboard          ← first time setup
/speckit.specify  ← new feature
/tdd              ← implement test-first
/verify           ← quality check
/security         ← security audit
```
"""
    content = f"""# AI Agent Instructions — {a["name"]}

> Entry point for Claude Code & OpenCode.

## Read First
- `.ai/context/PROJECT.md` — what we're building
- `.ai/context/STACK.md`   — tech stack: {a["backend"]} + {a["database"]}
- `.ai/context/RULES.md`   — coding rules (mandatory)

## Agent Routing
| Task | Agent |
|------|-------|
| Complex multi-step | `.ai/agents/orchestrator.md` |
| Write / refactor code | `.ai/agents/coder.md` |
| Database | `.ai/agents/db-agent.md` |
| API / integrations | `.ai/agents/api-agent.md` |
| TDD | `.ai/agents/ecc/tdd-guide.md` |
| Security | `.ai/agents/ecc/security-reviewer.md` |
| SQL queries | `.ai/sub-agents/sql-helper.md` |
| Telegram | `.ai/sub-agents/telegram-bot.md` |
| n8n | `.ai/sub-agents/n8n-workflow.md` |
| Bugs | `.ai/sub-agents/debugger.md` |
{claude_section}{oc_section}
## Core Rules
- Spec first → code second
- Tests first → TDD always
- NEVER SELECT * in production
- NEVER hardcode credentials
- ALWAYS validate user input
"""
    (path / "CLAUDE.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  CLAUDE.md")

def write_constitution(path, a):
    (path / ".ai/spec/memory").mkdir(parents=True, exist_ok=True)
    content = f"""# Project Constitution — {a["name"]}

**Version**: 1.0.0

## P1 — Data Integrity
All data operations MUST use parameterized queries.
Hard deletes are FORBIDDEN — use soft deletes (deleted_at).

## P2 — Security First  
ALL user inputs MUST be validated before processing.
Secrets MUST live in .env — never in source code.

## P3 — Code Quality
Every function MUST do one thing only.
Tests MUST be written BEFORE implementation (TDD).
Coverage target: 80%+

## P4 — Language
{f'Code comments and docs in: {a["language"]}'}

## P5 — Consistency
Follow conventions in .ai/context/RULES.md at all times.
When in doubt — ask, don't assume.
"""
    (path / ".ai/spec/memory/constitution.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/spec/memory/constitution.md")


# ─────────────────────────────────────────────
def main():
    print(f"\n{BOLD}{'='*50}")
    print(f"  ag_ai — Project Setup Wizard")
    print(f"  Fills all AI context files automatically")
    print(f"{'='*50}{RESET}")

    project_path = get_project_path()
    print(f"\n  {YELLOW}Project:{RESET} {project_path}")

    # Collect answers
    answers = collect_answers()

    # Ensure required dirs exist
    for d in [".ai/context", ".ai/spec/memory", ".ai/agents",
              ".ai/sub-agents", "specs"]:
        (project_path / d).mkdir(parents=True, exist_ok=True)

    # Write all files
    title("Writing files...")
    write_project_md(project_path, answers)
    write_stack_md(project_path, answers)
    write_rules_md(project_path, answers)
    write_claude_md(project_path, answers)
    write_constitution(project_path, answers)

    # Save answers as JSON for reference
    answers_copy = answers.copy()
    answers_copy["integrations"] = list(answers_copy["integrations"])
    (project_path / ".ai/context/wizard-answers.json").write_text(
        json.dumps(answers_copy, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"  {GREEN}OK{RESET}  .ai/context/wizard-answers.json  (re-run wizard to update)")

    # Final summary
    tool = answers["ai_tool"].lower()
    print(f"\n{BOLD}{'='*50}")
    print(f"  Done! {answers['name']} is configured.")
    print(f"{'='*50}{RESET}")

    if "claude" in tool or "both" in tool:
        print(f"""
  Claude Code:
    cd "{project_path}"
    claude
    /speckit.specify  I want to build [feature]
""")
    if "open" in tool or "both" in tool:
        print(f"""
  OpenCode:
    cd "{project_path}"
    opencode
    use orchestrator agent to help me build [feature]
""")

if __name__ == "__main__":
    main()
