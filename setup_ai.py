#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai -- AI Infrastructure Setup Script (Interactive)
Usage: python setup_ai.py [project_path]
"""

import os
import sys
import shutil
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    os.environ["PYTHONIOENCODING"] = "utf-8"

SCRIPT_DIR = Path(__file__).parent.resolve()

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"

def ok(msg):     print(f"{GREEN}  OK  {msg}{RESET}")
def warn(msg):   print(f"{YELLOW}  --  {msg}{RESET}")
def err(msg):    print(f"{RED}  XX  {msg}{RESET}")
def info(msg):   print(f"{BLUE}  >>  {msg}{RESET}")
def header(msg): print(f"\n{BOLD}{msg}{RESET}")

def ask_yes(question, default=True):
    hint = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"  ? {question} {hint}: ").strip().lower()
    except (EOFError, UnicodeDecodeError):
        return default
    if ans == "":
        return default
    return ans in ("y", "yes")

def ask_choice(question, options):
    print(f"\n  ? {question}")
    print(f"  {'─' * 48}")
    for i, (label, desc) in enumerate(options, 1):
        print(f"  {BOLD}{i}{RESET}) {label:<22} {DIM}{desc}{RESET}")
    print(f"  {BOLD}0{RESET}) All (install everything)")
    print()
    try:
        raw = input("  Select numbers separated by spaces (e.g. 1 3 4): ").strip()
    except (EOFError, UnicodeDecodeError):
        raw = ""

    if raw == "0" or raw == "":
        return list(range(len(options)))

    selected = []
    for x in raw.split():
        try:
            idx = int(x) - 1
            if 0 <= idx < len(options):
                selected.append(idx)
        except ValueError:
            pass
    return selected if selected else list(range(len(options)))

def get_target():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1]).resolve()
    else:
        raw = input("  Project path (Enter = current dir): ").strip()
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
        if not ask_yes(f"{label} exists. Overwrite?", default=True):
            warn(f"Skipped: {label}")
            return False
        shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
    shutil.copytree(src, dest) if src.is_dir() else shutil.copy2(src, dest)
    ok(f"Installed: {label}")
    return True

def make_dirs(target, use_opencode=True, use_speckit=True):
    dirs = ["specs", ".ai/context", ".ai/agents/ecc",
            ".ai/sub-agents", ".ai/skills",
            ".ai/rules/php", ".ai/rules/common",
            ".claude/commands"]
    if use_opencode:
        dirs.append(".opencode/agents")
    if use_speckit:
        dirs += [".ai/spec/memory", ".ai/spec/commands", ".ai/spec/templates"]
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

def main():
    print(f"\n{BOLD}{'=' * 52}{RESET}")
    print(f"{BOLD}   ag_ai -- AI Infrastructure Setup{RESET}")
    print(f"{BOLD}   Custom Agents + Spec Kit + ECC{RESET}")
    print(f"{BOLD}{'=' * 52}{RESET}")

    target = get_target()
    info(f"Target project: {target}")

    # ── Question 1: AI Tool ────────────────────────────────────
    tool_options = [
        ("Claude Code",   "slash commands: /tdd  /security  /speckit.*"),
        ("OpenCode",      "YAML agents: use orchestrator agent to ..."),
        ("Both",          "install Claude Code + OpenCode support"),
    ]
    tool_idx = ask_choice("Which AI tool do you use?", tool_options)
    use_claude   = (0 in tool_idx or 2 in tool_idx)
    use_opencode = (1 in tool_idx or 2 in tool_idx)

    # ── Question 2: Components ─────────────────────────────────
    comp_options = [
        ("Core Agents",    "orchestrator, coder, db-agent, api-agent (always recommended)"),
        ("ECC Agents",     "architect, tdd-guide, security-reviewer, code-reviewer"),
        ("Sub-Agents",     "sql-helper, telegram-bot, n8n-workflow, debugger, test-writer"),
        ("PHP Rules",      "security + patterns + testing (auto-apply to .php files)"),
        ("Common Rules",   "security + coding-style (universal rules)"),
        ("Spec Kit",       "speckit.* commands + spec/plan/tasks templates"),
    ]
    comp_idx = ask_choice("Which components to install?", comp_options)

    install_ecc     = (1 in comp_idx)
    install_sub     = (2 in comp_idx)
    install_php     = (3 in comp_idx)
    install_common  = (4 in comp_idx)
    install_speckit = (5 in comp_idx)

    # ── Install ────────────────────────────────────────────────
    header("Installing...")
    results = []

    # CLAUDE.md
    r = copy_item(SCRIPT_DIR / "CLAUDE.md", target / "CLAUDE.md", "CLAUDE.md")
    results.append(("CLAUDE.md", r))

    # .ai/ folder
    ai_src = SCRIPT_DIR / ".ai"
    ai_dest = target / ".ai"
    if ai_src.exists():
        if ai_dest.exists():
            if ask_yes(".ai/ folder exists. Overwrite?", default=True):
                shutil.rmtree(ai_dest)
                shutil.copytree(ai_src, ai_dest)
                ok("Installed: .ai/ (agents + rules + context)")
                results.append((".ai/", True))
            else:
                warn("Skipped: .ai/")
                results.append((".ai/", False))
        else:
            shutil.copytree(ai_src, ai_dest)
            ok("Installed: .ai/ (agents + rules + context)")
            results.append((".ai/", True))

    # Claude Code commands
    if use_claude:
        r = copy_item(SCRIPT_DIR / ".claude", target / ".claude", ".claude/ (slash commands)")
        results.append((".claude/", r))

    # OpenCode agents
    if use_opencode:
        r = copy_item(SCRIPT_DIR / ".opencode", target / ".opencode", ".opencode/ (OpenCode agents)")
        results.append((".opencode/", r))

    # Remove unselected components
    ai_path = target / ".ai"

    if not install_ecc and (ai_path / "agents" / "ecc").exists():
        shutil.rmtree(ai_path / "agents" / "ecc")
        warn("Skipped: ECC agents")

    if not install_sub and (ai_path / "sub-agents").exists():
        shutil.rmtree(ai_path / "sub-agents")
        warn("Skipped: sub-agents")

    if not install_php and (ai_path / "rules" / "php").exists():
        shutil.rmtree(ai_path / "rules" / "php")
        warn("Skipped: PHP rules")

    if not install_common and (ai_path / "rules" / "common").exists():
        shutil.rmtree(ai_path / "rules" / "common")
        warn("Skipped: common rules")

    if not install_speckit and (ai_path / "spec").exists():
        shutil.rmtree(ai_path / "spec")
        warn("Skipped: Spec Kit")

    make_dirs(target, use_opencode=use_opencode, use_speckit=install_speckit)
    update_gitignore(target)

    # ── Summary ────────────────────────────────────────────────
    header("Installed:")
    for label, status in results:
        icon = f"{GREEN}OK{RESET}" if status else f"{YELLOW}--{RESET}"
        print(f"  [{icon}] {label}")

    md_count = len(list(ai_path.rglob("*.md"))) if ai_path.exists() else 0
    oc_count = len(list((target / ".opencode" / "agents").glob("*.yml"))) \
               if (target / ".opencode" / "agents").exists() else 0

    header("Next Steps:")
    if use_claude:
        print(f"  Claude Code:  cd project && claude  →  /onboard")
    if use_opencode:
        print(f"  OpenCode:     cd project && opencode  →  use orchestrator agent to ...")

    parts = [f"{md_count} MD files"]
    if oc_count:
        parts.append(f"{oc_count} OpenCode agents")
    print(f"\n{GREEN}{BOLD}  Done! {' + '.join(parts)} installed.{RESET}\n")


if __name__ == "__main__":
    main()
