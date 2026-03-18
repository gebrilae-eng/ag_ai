#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai - Project Setup Wizard
Usage:
  python wizard.py
  python wizard.py D:\my-project
"""

import sys, json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

BOLD="\033[1m"; GREEN="\033[92m"; CYAN="\033[96m"
YELLOW="\033[93m"; DIM="\033[2m"; RESET="\033[0m"

def title(t): print(f"\n{BOLD}{'─'*50}\n  {t}\n{'─'*50}{RESET}")

def ask(q, default=""):
    hint = f" [{default}]" if default else ""
    try:
        val = input(f"{CYAN}  -> {q}{hint}: {RESET}").strip()
        return val if val else default
    except (EOFError, KeyboardInterrupt): return default

def ask_yes(q, default=True):
    hint = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"{CYAN}  -> {q} {hint}: {RESET}").strip().lower()
        return default if ans == "" else ans in ("y", "yes")
    except (EOFError, KeyboardInterrupt): return default

def ask_multi(q, options):
    print(f"\n{CYAN}  -> {q}{RESET}")
    for i, o in enumerate(options, 1):
        print(f"     {BOLD}{i}{RESET}) {o}")
    print(f"     {BOLD}0{RESET}) {DIM}All{RESET}")
    try:
        raw = input("     Choose numbers (e.g. 1 3) or 0 for all: ").strip()
    except (EOFError, KeyboardInterrupt): return options
    if not raw or raw == "0": return options
    result = []
    for x in raw.split():
        try:
            idx = int(x) - 1
            if 0 <= idx < len(options): result.append(options[idx])
        except ValueError: pass
    return result if result else options
def get_project_path():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1]).resolve()
    else:
        print(f"\n{BOLD}  ag_ai - Project Setup Wizard{RESET}\n")
        raw = ask("Path to your project folder")
        p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists():
        p.mkdir(parents=True)
    return p

def safe_write(path_obj, content, label, overwrite_all=False):
    if path_obj.exists() and not overwrite_all:
        if not ask_yes(f"  {label} exists. Overwrite?", default=False):
            print(f"  {YELLOW}--  Skipped: {label}{RESET}")
            return False
    path_obj.write_text(content, encoding="utf-8")
    print(f"  {GREEN}OK  {label}{RESET}")
    return True

def collect_answers():
    a = {}
    title("1 / 4  -  Project Info")
    a["name"]         = ask("Project name", "My Project")
    a["description"]  = ask("What does it do?")
    a["type"]         = ask("Type (web / api / bot / automation)", "web")
    a["status"]       = ask("Status (new / development / production)", "new")
    a["out_of_scope"] = ask("What does it NOT do?", "Not defined yet")
    title("2 / 4  -  Tech Stack")
    a["backend"]   = ask("Backend (e.g. PHP vanilla / Laravel / Node.js)", "PHP vanilla")
    a["db_engine"] = ask("Database engine (e.g. MySQL 8 / PostgreSQL)", "MySQL 8")
    a["db_name"]   = ask("Database name", "my_db")
    a["db_user"]   = ask("DB username", "root")
    a["db_pass"]   = ask("DB password (blank if none)", "")
    a["frontend"]  = ask("Frontend (e.g. HTML/JS / React / Blade)", "HTML/CSS/JS")
    a["local"]     = ask("Local dev (e.g. Laragon / XAMPP / Docker)", "Laragon")
    a["integrations"] = ask_multi("Integrations?",
        ["Telegram bot", "n8n workflows", "REST APIs", "Email", "WhatsApp", "None"])
    title("3 / 4  -  Rules")
    a["hard_rules"] = ask("Hard business rules? (e.g. never delete records)", "")
    a["language"]   = ask("Docs language (English / Arabic / Both)", "Both")
    title("4 / 4  -  AI Tool")
    a["ai_tool"] = ask("AI tool (claude / opencode / both)", "both")
    return a

def print_summary(a):
    title("Summary - Review before writing")
    print(f"""
  Project:      {a['name']}
  Description:  {a['description']}
  Type / Status: {a['type']} / {a['status']}
  Backend:      {a['backend']}
  Database:     {a['db_engine']} / {a['db_name']}
  Frontend:     {a['frontend']}
  Local server: {a['local']}
  Integrations: {', '.join(a['integrations'])}
  Hard rules:   {a['hard_rules'] or '(none)'}
  Docs lang:    {a['language']}
  AI tool:      {a['ai_tool']}
""")

def gen_agents_md(a):
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules yet"
    integ = ", ".join(a["integrations"])
    return f"""# AGENTS.md - {a["name"]}

> Read this file first. Also read CLAUDE.md and .ai/context/ files.

## Project Reality
- Name: {a["name"]}
- Stack: {a["backend"]} + {a["db_engine"]} ({a["db_name"]}) + {a["frontend"]}
- Integrations: {integ}
- Local server: {a["local"]}

## Build / Test Commands
- PHP: `vendor/bin/phpunit`
- Single test: `vendor/bin/phpunit --filter test_name`

## Agent Routing
| Task | Use Agent |
|------|-----------|
| Complex multi-step | `orchestrator` (delegates only, never codes) |
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

## Non-Negotiable Rules
- NEVER hardcode credentials, tokens, or API keys
- NEVER use SELECT * in production
- ALWAYS validate user input at the boundary
- ALWAYS use parameterized SQL
{hard}

## Workflow
1. Spec first then code
2. Tests first (TDD)
3. Small targeted changes over large rewrites
"""

def gen_claude_md(a):
    tool = a["ai_tool"].lower()
    use_claude   = "claude" in tool or "both" in tool
    use_opencode = "open"   in tool or "both" in tool
    lines = [
        f"# AI Instructions - {a['name']}", "",
        "> Read AGENTS.md and .ai/context/ first.", "",
        "## Stack",
        f"`{a['backend']}` + `{a['db_engine']} / {a['db_name']}` + `{a['frontend']}`", "",
        "## orchestrator = delegate only, never writes code",
        "| Task | Agent |", "|------|-------|",
        "| Complex task | orchestrator |", "| Code | coder |",
        "| DB | db-agent |", "| API | api-agent |",
        "| TDD | tdd-guide |", "| Security | security-reviewer |",
        "| SQL | sql-helper |", "| Telegram | telegram-bot |",
        "| n8n | n8n-workflow |", "| Bugs | debugger |", "",
    ]
    if use_claude:
        lines += ["## Claude Code", "```",
                  "/speckit.specify  new feature",
                  "/tdd              implement test-first",
                  "/verify           quality check",
                  "/security         audit", "```", ""]
    if use_opencode:
        lines += ["## OpenCode", "```",
                  "use orchestrator agent to manage: [complex task]",
                  "use coder agent to implement [function]",
                  "use tdd-guide agent to write tests for [function]",
                  "```", ""]
    return "\n".join(lines)

def gen_project_md(a):
    integ = "\n".join(f"- {i}" for i in a["integrations"])
    return f"""# Project Overview
## Project Name
`{a["name"]}`
## Description
{a["description"]}
## Type / Status
{a["type"].capitalize()} / {a["status"].capitalize()}
## Key Integrations
{integ}
## Out of Scope
- {a["out_of_scope"]}
"""

def gen_stack_md(a):
    integ = "\n".join(f"- {i}" for i in a["integrations"])
    app   = a["name"].upper().replace(" ", "_")
    return f"""# Tech Stack
## Backend
- Language / Framework: `{a["backend"]}`
- Local Server: `{a["local"]}`
## Database
- Engine: `{a["db_engine"]}`  Name: `{a["db_name"]}`
## Frontend
- `{a["frontend"]}`
## Integrations
{integ}
## Environment Variables
```env
APP_NAME={app}
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE={a["db_name"]}
DB_USERNAME={a["db_user"]}
DB_PASSWORD={a["db_pass"]}
```
"""

def gen_rules_md(a):
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules yet"
    return f"""# Coding Rules
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
"""

def gen_constitution_md(a):
    hard = a["hard_rules"].strip() if a["hard_rules"].strip() else "No hard deletes - use soft-delete (deleted_at)"
    return f"""# Constitution - {a["name"]}
**Version**: 1.0.0
## P1 - Data Integrity
All DB operations MUST use parameterized queries.
{hard}
## P2 - Security First
ALL user inputs MUST be validated before processing.
Secrets MUST live in .env - never in source code.
## P3 - Code Quality
Every function MUST do one thing only.
Tests MUST be written BEFORE implementation (TDD).
Coverage target: 80%+
## P4 - Language
Comments and docs: {a["language"]}
## P5 - Consistency
Follow .ai/context/RULES.md at all times.
When in doubt - ask, don't assume.
"""

def main():
    print(f"\n{BOLD}{'='*50}\n  ag_ai - Project Setup Wizard\n{'='*50}{RESET}")
    project_path = get_project_path()
    print(f"\n  {YELLOW}Project:{RESET} {project_path}")

    if (project_path / "CLAUDE.md").exists():
        print(f"\n  {YELLOW}Project already has ag_ai configured.{RESET}")
        if not ask_yes("Re-run wizard? Existing files reviewed before overwrite", default=False):
            print("  Cancelled."); sys.exit(0)

    answers = collect_answers()
    print_summary(answers)
    if not ask_yes("Everything correct? Proceed to write files", default=True):
        print(f"\n  {YELLOW}Cancelled. Re-run wizard when ready.{RESET}"); sys.exit(0)

    overwrite_all = False
    existing = [f for f in ["CLAUDE.md","AGENTS.md",".ai/context/PROJECT.md"] if (project_path/f).exists()]
    if existing:
        print(f"\n  Found {len(existing)} existing file(s).")
        overwrite_all = ask_yes("Overwrite all existing files without prompting?", default=True)

    for d in [".ai/context",".ai/spec/memory",".ai/agents",".ai/sub-agents","specs"]:
        (project_path / d).mkdir(parents=True, exist_ok=True)

    title("Writing files...")
    files = {
        "AGENTS.md":                       gen_agents_md(answers),
        "CLAUDE.md":                       gen_claude_md(answers),
        ".ai/context/PROJECT.md":          gen_project_md(answers),
        ".ai/context/STACK.md":            gen_stack_md(answers),
        ".ai/context/RULES.md":            gen_rules_md(answers),
        ".ai/spec/memory/constitution.md": gen_constitution_md(answers),
    }
    for rel_path, content in files.items():
        target_file = project_path / rel_path
        target_file.parent.mkdir(parents=True, exist_ok=True)
        safe_write(target_file, content, rel_path, overwrite_all=overwrite_all)

    answers_copy = dict(answers)
    answers_copy["integrations"] = list(answers_copy["integrations"])
    (project_path / ".ai/context/wizard-answers.json").write_text(
        json.dumps(answers_copy, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  {GREEN}OK  .ai/context/wizard-answers.json{RESET}")

    tool = answers["ai_tool"].lower()
    print(f"\n{BOLD}{'='*50}\n  Done! {answers['name']} is ready.\n{'='*50}{RESET}\n")
    if "claude" in tool or "both" in tool:
        print(f"  Claude Code:  cd \"{project_path}\"  then  claude")
        print(f"                /speckit.specify  I want to build [feature]\n")
    if "open"  in tool or "both" in tool:
        print(f"  OpenCode:     cd \"{project_path}\"  then  opencode")
        print(f"                use orchestrator agent to manage: build [feature]\n")

if __name__ == "__main__":
    main()
