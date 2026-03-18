#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai - Project Validator
Checks context files for unfilled placeholders and verifies agents are installed.
Usage:
  python validate.py [project_path]
"""

import sys, re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

PLACEHOLDER_PATTERNS = [
    r"\[YOUR PROJECT NAME\]",
    r"\[your_db_name\]",
    r"FILL THIS FILE",
    r"\[PHP / Node",
    r"\[MySQL / PostgreSQL",
    r"Feature 1.*Planned",
    r"yourusername",
    r"\[your-project\]",
]

REQUIRED_FILES = {
    "CLAUDE.md":                       "Agent entry point",
    "AGENTS.md":                       "OpenCode agent routing",
    ".ai/context/PROJECT.md":          "Project description",
    ".ai/context/STACK.md":            "Tech stack details",
    ".ai/context/RULES.md":            "Coding rules",
    ".ai/spec/memory/constitution.md": "Project principles",
}

REQUIRED_AGENTS = [
    ".opencode/agents/orchestrator.yml",
    ".opencode/agents/coder.yml",
    ".opencode/agents/db-agent.yml",
    ".opencode/agents/api-agent.yml",
    ".opencode/agents/architect.yml",
    ".opencode/agents/tdd-guide.yml",
    ".opencode/agents/security-reviewer.yml",
    ".opencode/agents/code-reviewer.yml",
    ".opencode/agents/database-reviewer.yml",
    ".opencode/agents/refactor-cleaner.yml",
    ".opencode/agents/build-error-resolver.yml",
    ".opencode/agents/doc-updater.yml",
    ".opencode/agents/sql-helper.yml",
    ".opencode/agents/telegram-bot.yml",
    ".opencode/agents/n8n-workflow.yml",
    ".opencode/agents/debugger.yml",
    ".opencode/agents/test-writer.yml",
    ".opencode/agents/spec-workflow.yml",
]

def ok(msg):   print(f"  {GREEN}[OK]  {RESET}{msg}")
def warn(msg): print(f"  {YELLOW}[WARN]{RESET} {msg}")
def err(msg):  print(f"  {RED}[ERR] {RESET}{msg}")

def check_placeholders(filepath):
    try:
        content = Path(filepath).read_text(encoding="utf-8")
    except:
        return []
    return [p for p in PLACEHOLDER_PATTERNS if re.search(p, content)]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    project_path = Path(args[0]).resolve() if args else Path.cwd()

    print(f"\n{BOLD}  ag_ai - Validate{RESET}")
    print(f"  Project: {project_path}\n")
    issues = 0

    print(f"{BOLD}  Context files{RESET}")
    for rel, desc in REQUIRED_FILES.items():
        fp = project_path / rel
        if not fp.exists():
            err(f"{rel}  ({desc}) - MISSING")
            issues += 1
        else:
            placeholders = check_placeholders(fp)
            if placeholders:
                warn(f"{rel} - has unfilled placeholders")
                issues += 1
            else:
                ok(f"{rel}")

    print(f"\n{BOLD}  OpenCode agents{RESET}")
    missing = [a.split("/")[-1].replace(".yml","")
               for a in REQUIRED_AGENTS
               if not (project_path / a).exists()]
    if missing:
        warn(f"Missing agents: {', '.join(missing)}")
        warn("Run: python setup_ai.py [path] to install them")
        issues += 1
    else:
        ok(f"All {len(REQUIRED_AGENTS)} OpenCode agents installed")

    print(f"\n{BOLD}  Setup status{RESET}")
    if (project_path / ".ai/context/wizard-answers.json").exists():
        ok("Wizard has been run")
    else:
        warn("Wizard not run yet - run: python wizard.py [path]")
        issues += 1

    gi = project_path / ".gitignore"
    if gi.exists() and ".env" in gi.read_text(encoding="utf-8", errors="ignore"):
        ok(".gitignore has .env protection")
    else:
        warn(".gitignore missing .env entry")
        issues += 1

    print(f"\n{'─'*42}")
    if issues == 0:
        print(f"  {GREEN}{BOLD}All checks passed.{RESET} Project is ready.\n")
    else:
        print(f"  {YELLOW}{BOLD}{issues} issue(s) found.{RESET} Fix before using agents.\n")
    return 0 if issues == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
