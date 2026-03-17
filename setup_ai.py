#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai -- AI Infrastructure Setup Script
Usage:
  python setup_ai.py [project_path]         interactive
  python setup_ai.py [project_path] --auto  install everything silently
"""

import os, sys, shutil
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent.resolve()
AUTO_MODE  = "--auto" in sys.argv

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
    if AUTO_MODE: return True
    hint = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"  ? {question} {hint}: ").strip().lower()
        return default if ans == "" else ans in ("y", "yes")
    except: return default

def ask_choice(question, options):
    if AUTO_MODE:
        return list(range(len(options)))  # select all
    print(f"\n  ? {question}")
    print(f"  {'─' * 50}")
    for i, (label, desc) in enumerate(options, 1):
        print(f"  {BOLD}{i}{RESET}) {label:<22} {DIM}{desc}{RESET}")
    print(f"  {BOLD}0{RESET}) All  {DIM}(install everything){RESET}")
    print()
    try:
        raw = input("  Select numbers (e.g. 1 3 4) or 0 for all: ").strip()
    except: raw = "0"
    if raw == "0" or raw == "":
        return list(range(len(options)))
    selected = []
    for x in raw.split():
        try:
            idx = int(x) - 1
            if 0 <= idx < len(options): selected.append(idx)
        except: pass
    return selected if selected else list(range(len(options)))

def get_target():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        p = Path(args[0]).resolve()
    else:
        raw = input("  Project path (Enter = current dir): ").strip()
        p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists():
        p.mkdir(parents=True)
        ok(f"Created: {p}")
    if p.resolve() == SCRIPT_DIR.resolve():
        err("Cannot install ag_ai into itself!")
        err("Use a different project path.")
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

def install_ai_folder(target):
    ai_src  = SCRIPT_DIR / ".ai"
    ai_dest = target / ".ai"
    if not ai_src.exists():
        warn("Source .ai/ not found"); return False
    if ai_dest.exists():
        if not ask_yes(".ai/ folder exists. Overwrite?", default=True):
            warn("Skipped: .ai/"); return False
        shutil.rmtree(ai_dest)
    shutil.copytree(ai_src, ai_dest)
    ok("Installed: .ai/")
    return True

def make_dirs(target, use_opencode=True, use_speckit=True):
    dirs = ["specs", ".ai/context", ".ai/agents/ecc", ".ai/sub-agents",
            ".ai/skills", ".ai/rules/php", ".ai/rules/common", ".claude/commands"]
    if use_opencode: dirs.append(".opencode/agents")
    if use_speckit:  dirs += [".ai/spec/memory", ".ai/spec/commands", ".ai/spec/templates"]
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
    if AUTO_MODE:
        print(f"\n{BOLD}  ag_ai -- Installing (auto mode)...{RESET}")
    else:
        print(f"\n{BOLD}{'='*50}\n   ag_ai -- AI Infrastructure Setup\n{'='*50}{RESET}")

    target = get_target()
    info(f"Target: {target}")

    # Questions (skipped in auto mode)
    tool_options = [
        ("Claude Code",  "slash commands: /tdd  /security  /speckit.*"),
        ("OpenCode",     "YAML agents: use orchestrator agent to ..."),
        ("Both",         "Claude Code + OpenCode"),
    ]
    tool_idx     = ask_choice("Which AI tool?", tool_options)
    use_claude   = (0 in tool_idx or 2 in tool_idx)
    use_opencode = (1 in tool_idx or 2 in tool_idx)

    comp_options = [
        ("Core Agents",   "orchestrator, coder, db-agent, api-agent"),
        ("ECC Agents",    "architect, tdd-guide, security-reviewer, code-reviewer"),
        ("Sub-Agents",    "sql-helper, telegram-bot, n8n-workflow, debugger"),
        ("PHP Rules",     "security + patterns + testing"),
        ("Common Rules",  "security + coding-style"),
        ("Spec Kit",      "speckit.* commands + templates"),
    ]
    comp_idx        = ask_choice("Which components?", comp_options)
    install_ecc     = (1 in comp_idx)
    install_sub     = (2 in comp_idx)
    install_php     = (3 in comp_idx)
    install_common  = (4 in comp_idx)
    install_speckit = (5 in comp_idx)

    header("Installing...")

    copy_item(SCRIPT_DIR / "CLAUDE.md", target / "CLAUDE.md", "CLAUDE.md")
    install_ai_folder(target)
    if use_claude:   copy_item(SCRIPT_DIR / ".claude",   target / ".claude",   ".claude/")
    if use_opencode: copy_item(SCRIPT_DIR / ".opencode", target / ".opencode", ".opencode/")

    ai_path = target / ".ai"
    if not install_ecc    and (ai_path/"agents"/"ecc").exists(): shutil.rmtree(ai_path/"agents"/"ecc");    warn("Skipped: ECC agents")
    if not install_sub    and (ai_path/"sub-agents").exists():   shutil.rmtree(ai_path/"sub-agents");      warn("Skipped: sub-agents")
    if not install_php    and (ai_path/"rules"/"php").exists():  shutil.rmtree(ai_path/"rules"/"php");     warn("Skipped: PHP rules")
    if not install_common and (ai_path/"rules"/"common").exists():shutil.rmtree(ai_path/"rules"/"common"); warn("Skipped: common rules")
    if not install_speckit and (ai_path/"spec").exists():        shutil.rmtree(ai_path/"spec");            warn("Skipped: Spec Kit")

    make_dirs(target, use_opencode=use_opencode, use_speckit=install_speckit)
    update_gitignore(target)

    md_count = len(list(ai_path.rglob("*.md"))) if ai_path.exists() else 0
    oc_count = len(list((target/".opencode"/"agents").glob("*.yml"))) if (target/".opencode"/"agents").exists() else 0

    parts = [f"{md_count} MD files"]
    if oc_count: parts.append(f"{oc_count} OpenCode agents")
    print(f"\n{GREEN}{BOLD}  Done! {' + '.join(parts)} installed.{RESET}\n")

if __name__ == "__main__":
    main()
