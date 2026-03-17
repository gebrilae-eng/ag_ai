#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai - Project Setup Wizard
Run ONCE at the start of any new project.
Asks questions and fills all AI context files automatically.

Usage:
  python wizard.py                    (asks for project path)
  python wizard.py D:\my-project      (direct path)
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

def title(t):
    print(f"\n{BOLD}{'─'*50}\n  {t}\n{'─'*50}{RESET}")

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
        print(f"\n{BOLD}  ag_ai — Project Setup Wizard{RESET}")
        print(f"  {DIM}Fills all AI context files before you start coding{RESET}\n")
        raw = ask("Path to your project folder")
        p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists():
        p.mkdir(parents=True)
    return p

def collect_answers():
    a = {}

    title("1 / 4  —  Project Info")
    a["name"]        = ask("Project name", "My Project")
    a["description"] = ask("What does it do? (1-2 sentences)")
    a["type"]        = ask("Type (web / api / bot / automation / other)", "web")
    a["status"]      = ask("Status (new / development / production)", "new")
    a["out_of_scope"] = ask("What does this project NOT do?", "")

    title("2 / 4  —  Tech Stack")
    a["backend"]   = ask("Backend (e.g. PHP vanilla / PHP+Laravel / Node.js)", "PHP vanilla")
    a["db_engine"] = ask("Database engine (e.g. MySQL 8 / PostgreSQL / none)", "MySQL 8")
    a["db_name"]   = ask("Database name (e.g. pharmacy_db / my_db)", "my_db")
    a["db_user"]   = ask("DB username", "root")
    a["db_pass"]   = ask("DB password (leave blank if none)", "")
    a["frontend"]  = ask("Frontend (e.g. HTML/JS / React / Blade / API only)", "HTML/CSS/JS")
    a["local"]     = ask("Local dev tool (e.g. Laragon / XAMPP / Docker)", "Laragon")
    a["integrations"] = ask_multi(
        "Integrations?",
        ["Telegram bot", "n8n workflows", "REST APIs", "Email", "WhatsApp", "None"]
    )

    title("3 / 4  —  Rules & Conventions")
    a["hard_rules"] = ask("Hard business rules? (e.g. never delete records)", "")
    a["naming"]     = ask("Special naming conventions? (Enter = defaults)", "")
    a["language"]   = ask("Docs language (English / Arabic / Both)", "Both")

    title("4 / 4  —  AI Tool")
    a["ai_tool"] = ask("AI tool (claude / opencode / both)", "both")

    return a

def write_project_md(path, a):
    out_of_scope = a.get("out_of_scope", "").strip()
    if not out_of_scope:
        out_of_scope = "Nothing defined yet"
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
- {out_of_scope}
"""
    (path / ".ai/context/PROJECT.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/PROJECT.md")

def write_stack_md(path, a):
    integrations = "\n".join(f"- {i}" for i in a["integrations"])
    db_pass_line = a["db_pass"] if a["db_pass"] else ""
    app_name = a["name"].upper().replace(" ", "_")
    content = f"""# Tech Stack

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
DB_PASSWORD={db_pass_line}
```
"""
    (path / ".ai/context/STACK.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/context/STACK.md")

def write_rules_md(path, a):
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules defined"
    naming = f"- {a['naming']}" if a["naming"].strip() else "- snake_case for DB tables, camelCase for functions"
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
    claude_section = ""
    if "claude" in tool or "both" in tool:
        claude_section = """
## Claude Code
```
/speckit.specify  I want to build [feature]
/tdd              implement test-first
/verify           quality check
/security         security audit
```
"""
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
    content = f"""# AI Agent Instructions — {a["name"]}

> Entry point for Claude Code & OpenCode.

## Project Context
- Stack: `{a["backend"]}` + `{a["db_engine"]} / {a["db_name"]}` + `{a["frontend"]}`
- Read `.ai/context/PROJECT.md`, `.ai/context/STACK.md`, `.ai/context/RULES.md` before any task

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
- ALWAYS use parameterized SQL
"""
    (path / "CLAUDE.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  CLAUDE.md")

def write_constitution(path, a):
    (path / ".ai/spec/memory").mkdir(parents=True, exist_ok=True)
    lang_rule = a["language"]
    hard = a["hard_rules"].strip() if a["hard_rules"].strip() else "No hard deletes — use soft-delete (deleted_at)"
    content = f"""# Project Constitution — {a["name"]}

**Version**: 1.0.0

## P1 — Data Integrity
All DB operations MUST use parameterized queries.
{hard}

## P2 — Security First
ALL user inputs MUST be validated before processing.
Secrets MUST live in .env — never in source code.
Run security audit before every release.

## P3 — Code Quality
Every function MUST do one thing only.
Tests MUST be written BEFORE implementation (TDD).
Coverage target: 80%+

## P4 — Language & Documentation
Comments and docs language: {lang_rule}

## P5 — Consistency
Follow .ai/context/RULES.md at all times.
When in doubt — ask, don't assume.
Small targeted changes over large rewrites.
"""
    (path / ".ai/spec/memory/constitution.md").write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK{RESET}  .ai/spec/memory/constitution.md")

def main():
    print(f"\n{BOLD}{'='*50}")
    print(f"  ag_ai — Project Setup Wizard")
    print(f"{'='*50}{RESET}")

    project_path = get_project_path()
    print(f"\n  {YELLOW}Project folder:{RESET} {project_path}")

    answers = collect_answers()

    # Create required dirs
    for d in [".ai/context", ".ai/spec/memory", ".ai/agents", ".ai/sub-agents", "specs"]:
        (project_path / d).mkdir(parents=True, exist_ok=True)

    title("Writing files...")
    write_project_md(project_path, answers)
    write_stack_md(project_path, answers)
    write_rules_md(project_path, answers)
    write_claude_md(project_path, answers)
    write_constitution(project_path, answers)

    # Save answers for re-run
    answers_copy = dict(answers)
    answers_copy["integrations"] = list(answers_copy["integrations"])
    (project_path / ".ai/context/wizard-answers.json").write_text(
        json.dumps(answers_copy, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  {GREEN}OK{RESET}  .ai/context/wizard-answers.json")

    # Done
    tool = answers["ai_tool"].lower()
    print(f"\n{BOLD}{'='*50}")
    print(f"  Done! {answers['name']} is ready.")
    print(f"{'='*50}{RESET}\n")

    if "claude" in tool or "both" in tool:
        print(f"  Claude Code:")
        print(f'    cd "{project_path}"')
        print(f"    claude")
        print(f"    /speckit.specify  I want to build [feature]\n")
    if "open" in tool or "both" in tool:
        print(f"  OpenCode:")
        print(f'    cd "{project_path}"')
        print(f"    opencode")
        print(f"    use orchestrator agent to help me build [feature]\n")

if __name__ == "__main__":
    main()
