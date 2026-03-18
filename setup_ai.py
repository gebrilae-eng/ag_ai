#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai -- AI Infrastructure Setup Script
Usage:
  python setup_ai.py [project_path]                  interactive
  python setup_ai.py [project_path] --auto           install everything silently
  python setup_ai.py [project_path] --dry-run        preview changes only
  python setup_ai.py [project_path] --update-agents  update agents only, preserve context
"""

import os, sys, shutil
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR  = Path(__file__).parent.resolve()
AUTO_MODE   = "--auto"          in sys.argv
DRY_RUN     = "--dry-run"       in sys.argv
AGENTS_ONLY = "--update-agents" in sys.argv

GREEN  = "\033[92m"; YELLOW = "\033[93m"; RED    = "\033[91m"
BLUE   = "\033[94m"; CYAN   = "\033[96m"; RESET  = "\033[0m"
BOLD   = "\033[1m";  DIM    = "\033[2m"

def ok(msg):     print(f"{GREEN}  OK  {msg}{RESET}")
def warn(msg):   print(f"{YELLOW}  --  {msg}{RESET}")
def dry(msg):    print(f"{CYAN}  DRY {msg}{RESET}")
def err(msg):    print(f"{RED}  XX  {msg}{RESET}")
def info(msg):   print(f"{BLUE}  >>  {msg}{RESET}")
def header(msg): print(f"\n{BOLD}{msg}{RESET}")

def ask_yes(question, default=True):
    if AUTO_MODE or AGENTS_ONLY: return True
    hint = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"  ? {question} {hint}: ").strip().lower()
        return default if ans == "" else ans in ("y", "yes")
    except: return default

def ask_choice(question, options):
    if AUTO_MODE or AGENTS_ONLY:
        return list(range(len(options)))
    print(f"\n  ? {question}")
    print(f"  {'─' * 50}")
    for i, (label, desc) in enumerate(options, 1):
        print(f"  {BOLD}{i}{RESET}) {label:<28} {DIM}{desc}{RESET}")
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
        if DRY_RUN:
            info(f"[DRY-RUN] Would create: {p}"); return p
        p.mkdir(parents=True); ok(f"Created: {p}")
    if p.resolve() == SCRIPT_DIR.resolve():
        err("Cannot install ag_ai into itself!"); sys.exit(1)
    return p

def copy_item(src, dest, label, overwrite_all=False):
    src, dest = Path(src), Path(dest)
    if not src.exists():
        warn(f"Source not found, skipping: {label}"); return False
    if DRY_RUN:
        dry(f"{'WOULD OVERWRITE' if dest.exists() else 'WOULD CREATE'}: {label}"); return True
    if dest.exists() and not overwrite_all:
        if not ask_yes(f"{label} exists. Overwrite?", default=True):
            warn(f"Skipped: {label}"); return False
        shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
    elif dest.exists():
        shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
    shutil.copytree(src, dest) if src.is_dir() else shutil.copy2(src, dest)
    ok(f"Installed: {label}"); return True

def install_ai_folder(target, overwrite_all=False):
    ai_src  = SCRIPT_DIR / ".ai"
    ai_dest = target / ".ai"
    if not ai_src.exists():
        warn("Source .ai/ not found"); return False
    if DRY_RUN:
        dry(f"{'WOULD OVERWRITE' if ai_dest.exists() else 'WOULD CREATE'}: .ai/"); return True
    if ai_dest.exists() and not overwrite_all:
        if not ask_yes(".ai/ folder exists. Overwrite?", default=True):
            warn("Skipped: .ai/"); return False
        shutil.rmtree(ai_dest)
    elif ai_dest.exists():
        shutil.rmtree(ai_dest)
    shutil.copytree(ai_src, ai_dest)
    ok("Installed: .ai/"); return True

def update_agents_only(target):
    """Update only agent files, preserve all context files."""
    header("Updating agents only (preserving context)...")
    for subdir in [".opencode", ".claude"]:
        src = SCRIPT_DIR / subdir
        if src.exists():
            copy_item(src, target / subdir, f"{subdir}/", overwrite_all=True)
    for subdir in ["agents", "sub-agents", "rules", "spec/commands", "spec/templates"]:
        src = SCRIPT_DIR / ".ai" / subdir
        dst = target / ".ai" / subdir
        if src.exists():
            copy_item(src, dst, f".ai/{subdir}/", overwrite_all=True)
    if not (target / ".ai/context/wizard-answers.json").exists():
        copy_item(SCRIPT_DIR / "CLAUDE.md", target / "CLAUDE.md", "CLAUDE.md", overwrite_all=True)
    info("Context files preserved: PROJECT.md, STACK.md, RULES.md, constitution.md")

def make_dirs(target, use_opencode=True, use_speckit=True):
    dirs = ["specs", ".ai/context", ".ai/agents/ecc", ".ai/sub-agents",
            ".ai/rules/php", ".ai/rules/common", ".claude/commands"]
    if use_opencode: dirs.append(".opencode/agents")
    if use_speckit:  dirs += [".ai/spec/memory", ".ai/spec/commands", ".ai/spec/templates"]
    if not DRY_RUN:
        for d in dirs: (target / d).mkdir(parents=True, exist_ok=True)
    ok("Directory structure ready")

def update_gitignore(target):
    entries = [".env", "*.log", "node_modules/", "__pycache__/", "*.pyc"]
    gi = target / ".gitignore"
    existing = gi.read_text(encoding="utf-8") if gi.exists() else ""
    new_entries = [e for e in entries if e not in existing]
    if new_entries and not DRY_RUN:
        with open(gi, "a", encoding="utf-8") as f:
            f.write("\n# ag_ai\n" + "\n".join(new_entries) + "\n")
        ok("Updated .gitignore")
    elif new_entries and DRY_RUN:
        dry(f"WOULD ADD to .gitignore: {', '.join(new_entries)}")

def main():
    if DRY_RUN:       print(f"\n{BOLD}  ag_ai -- DRY RUN (no files written){RESET}")
    elif AGENTS_ONLY: print(f"\n{BOLD}  ag_ai -- Update Agents Only{RESET}")
    elif AUTO_MODE:   print(f"\n{BOLD}  ag_ai -- Installing (auto mode)...{RESET}")
    else:             print(f"\n{BOLD}{'='*50}\n   ag_ai -- AI Infrastructure Setup\n{'='*50}{RESET}")

    target = get_target()
    info(f"Target: {target}")

    if AGENTS_ONLY:
        update_agents_only(target)
        print(f"\n{GREEN}{BOLD}  Agents updated.{RESET}\n"); return

    overwrite_all = AUTO_MODE or DRY_RUN
    if not AUTO_MODE and not DRY_RUN:
        existing_check = [f for f in ["CLAUDE.md","AGENTS.md"] if (target/f).exists()]
        if existing_check:
            overwrite_all = ask_yes("Found existing files. Overwrite all?", default=True)

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
    install_ecc     = (1 in comp_idx); install_sub     = (2 in comp_idx)
    install_php     = (3 in comp_idx); install_common  = (4 in comp_idx)
    install_speckit = (5 in comp_idx)
    header("Installing...")
    copy_item(SCRIPT_DIR/"CLAUDE.md", target/"CLAUDE.md", "CLAUDE.md", overwrite_all=overwrite_all)
    install_ai_folder(target, overwrite_all=overwrite_all)
    if use_claude:   copy_item(SCRIPT_DIR/".claude",   target/".claude",   ".claude/",   overwrite_all=overwrite_all)
    if use_opencode: copy_item(SCRIPT_DIR/".opencode", target/".opencode", ".opencode/", overwrite_all=overwrite_all)
    if not DRY_RUN:
        ai_path = target / ".ai"
        if not install_ecc    and (ai_path/"agents"/"ecc").exists():     shutil.rmtree(ai_path/"agents"/"ecc")
        if not install_sub    and (ai_path/"sub-agents").exists():       shutil.rmtree(ai_path/"sub-agents")
        if not install_php    and (ai_path/"rules"/"php").exists():      shutil.rmtree(ai_path/"rules"/"php")
        if not install_common and (ai_path/"rules"/"common").exists():   shutil.rmtree(ai_path/"rules"/"common")
        if not install_speckit and (ai_path/"spec").exists():            shutil.rmtree(ai_path/"spec")
    make_dirs(target, use_opencode=use_opencode, use_speckit=install_speckit)
    update_gitignore(target)
    if not DRY_RUN:
        ai_path = target / ".ai"
        md_count = len(list(ai_path.rglob("*.md"))) if ai_path.exists() else 0
        oc_count = len(list((target/".opencode"/"agents").glob("*.yml"))) if (target/".opencode"/"agents").exists() else 0
        parts = [f"{md_count} MD files"]
        if oc_count: parts.append(f"{oc_count} OpenCode agents")
        print(f"\n{GREEN}{BOLD}  Done! {' + '.join(parts)} installed.{RESET}\n")
    else:
        print(f"\n{CYAN}{BOLD}  Dry run complete. No files were written.{RESET}\n")

if __name__ == "__main__":
    main()
