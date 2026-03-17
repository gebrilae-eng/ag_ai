#!/usr/bin/env python3
"""
ag_ai — AI Infrastructure Setup Script
Installs complete AI dev environment into any project.
Usage: python setup_ai.py [project_path]
"""

import os
import sys
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BLUE   = "\033[94m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def ok(msg):     print(f"{GREEN}  OK  {msg}{RESET}")
def warn(msg):   print(f"{YELLOW}  --  {msg}{RESET}")
def err(msg):    print(f"{RED}  XX  {msg}{RESET}")
def info(msg):   print(f"{BLUE}  >>  {msg}{RESET}")
def header(msg): print(f"\n{BOLD}{msg}{RESET}")

def get_target():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1]).resolve()
    else:
        raw = input(f"\n{BOLD}Project path (Enter = current dir): {RESET}").strip()
        p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists():
        err(f"Path not found: {p}")
        sys.exit(1)
    return p

def copy_item(src, dest, label):
    src, dest = Path(src), Path(dest)
    if not src.exists():
        warn(f"Source not found, skipping: {label}")
        return False
    if dest.exists():
        ch = input(f"{YELLOW}  ?? {label} exists. Overwrite? (y/N): {RESET}").strip().lower()
        if ch != 'y':
            warn(f"Skipped: {label}")
            return False
        shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
    shutil.copytree(src, dest) if src.is_dir() else shutil.copy2(src, dest)
    ok(f"Installed: {label}")
    return True

def make_dirs(target):
    dirs = [
        "specs",
        ".ai/spec/memory",
        ".claude/commands",
        ".ai/agents/ecc",
        ".ai/sub-agents",
        ".ai/skills",
        ".ai/rules/php",
        ".ai/rules/common",
        ".ai/context",
    ]
    for d in dirs:
        (target / d).mkdir(parents=True, exist_ok=True)
    ok("Created directory structure")

def update_gitignore(target):
    entries = [".env", "*.log", "node_modules/", "__pycache__/", "*.pyc"]
    gi = target / ".gitignore"
    existing = gi.read_text(encoding="utf-8") if gi.exists() else ""
    new_entries = [e for e in entries if e not in existing]
    if new_entries:
        with open(gi, "a", encoding="utf-8") as f:
            f.write("\n# ag_ai\n" + "\n".join(new_entries) + "\n")
        ok("Updated .gitignore")

def show_tree(target):
    header("Installed Files:")
    for root, dirs, files in os.walk(target / ".ai"):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        level = len(Path(root).relative_to(target).parts) - 1
        ind = "  " + "  " * level
        print(f"{BLUE}{ind}{Path(root).name}/{RESET}")
        for f in sorted(files):
            print(f"{ind}  {f}")
    for extra in [".claude/commands", "specs", "CLAUDE.md"]:
        p = target / extra
        if p.exists():
            icon = "[dir]" if p.is_dir() else "[file]"
            print(f"{BLUE}  {icon} {extra}{RESET}")

def show_next_steps():
    header("Next Steps:")
    print(f"""
  1. Fill project context:
     {YELLOW}.ai/context/PROJECT.md{RESET}  -- what you are building
     {YELLOW}.ai/context/STACK.md{RESET}    -- your tech stack
     {YELLOW}.ai/context/RULES.md{RESET}    -- coding conventions

  2. Open Claude Code or OpenCode:
     {BOLD}claude{RESET}   or   {BOLD}opencode{RESET}

  3. Run onboarding wizard (auto-fills all context files):
     {GREEN}/onboard{RESET}

  4. Start your first feature:
     {GREEN}/speckit.specify  I want to build [describe feature]{RESET}

  5. Full workflow:
     {BLUE}/speckit.specify -> /speckit.plan -> /speckit.tasks -> /tdd -> /verify{RESET}
""")

def main():
    print(f"\n{BOLD}{'=' * 50}{RESET}")
    print(f"{BOLD}  ag_ai — AI Infrastructure Setup{RESET}")
    print(f"{BOLD}  Custom Agents + Spec Kit + ECC{RESET}")
    print(f"{BOLD}{'=' * 50}{RESET}")

    target = get_target()
    info(f"Target project: {target}")

    header("Installing...")

    # Core files
    copy_item(SCRIPT_DIR / ".ai",      target / ".ai",      ".ai/ (agents + skills + rules)")
    copy_item(SCRIPT_DIR / ".claude",  target / ".claude",  ".claude/ (ECC commands)")
    copy_item(SCRIPT_DIR / "CLAUDE.md", target / "CLAUDE.md", "CLAUDE.md")

    # Create any missing dirs
    make_dirs(target)

    # Gitignore
    update_gitignore(target)

    # Count installed md files
    md_count = len(list((target / ".ai").rglob("*.md"))) if (target / ".ai").exists() else 0

    show_tree(target)
    show_next_steps()

    print(f"{GREEN}{BOLD}  Done! {md_count} agent/skill/rule files installed.{RESET}\n")


if __name__ == "__main__":
    main()
