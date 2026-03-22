#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai x agency-agents -- Merged Installer v3.0
================================================
Usage:
  python setup_ai.py [project_path]
  python setup_ai.py [project_path] --auto
  python setup_ai.py [project_path] --dry-run
  python setup_ai.py [project_path] --update-agents
  python setup_ai.py [project_path] --all-divisions
  python setup_ai.py [project_path] --divisions engineering,design,testing
  python setup_ai.py [project_path] --ag-only
  python setup_ai.py [project_path] --no-agency
"""

import os, sys, shutil, subprocess, json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR   = Path(__file__).parent.resolve()
AGENCY_CACHE = SCRIPT_DIR / ".agency-agents-cache"
AGENCY_REPO  = "https://github.com/msitarzewski/agency-agents.git"

AUTO_MODE   = "--auto"          in sys.argv
DRY_RUN     = "--dry-run"       in sys.argv
AGENTS_ONLY = "--update-agents" in sys.argv
AG_ONLY     = "--ag-only"       in sys.argv
NO_AGENCY   = "--no-agency"     in sys.argv
ALL_DIVS    = "--all-divisions" in sys.argv


# Dev-relevant divisions (default)
DEV_DIVISIONS = [
    "engineering", "design", "product",
    "project-management", "testing", "support"
]

ALL_DIVISIONS = [
    "engineering", "design", "marketing", "sales",
    "product", "project-management", "testing", "support",
    "spatial-computing", "specialized", "game-development", "academic",
    "paid-media", "strategy", "integrations"
]

GREEN="\033[92m"; YELLOW="\033[93m"; RED="\033[91m"
BLUE="\033[94m";  CYAN="\033[96m";   RESET="\033[0m"
BOLD="\033[1m";   DIM="\033[2m"

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

def get_divisions():
    """Parse --divisions flag or return defaults."""
    for arg in sys.argv:
        if arg.startswith("--divisions="):
            return [d.strip() for d in arg.split("=", 1)[1].split(",")]
    # Check next arg after --divisions
    for i, arg in enumerate(sys.argv):
        if arg == "--divisions" and i + 1 < len(sys.argv):
            return [d.strip() for d in sys.argv[i+1].split(",")]
    if ALL_DIVS:
        return ALL_DIVISIONS
    return DEV_DIVISIONS

def ensure_agency_cache():
    """Clone or update agency-agents cache. Returns Path or None."""
    if AGENCY_CACHE.exists():
        info("agency-agents cache found — checking for updates...")
        result = subprocess.run(
            ["git", "-C", str(AGENCY_CACHE), "pull", "--ff-only"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            ok(f"agency-agents cache updated")
        else:
            warn("Could not update cache (offline?) — using existing")
        return AGENCY_CACHE

    info(f"Cloning agency-agents (first time — may take 30s)...")
    result = subprocess.run(
        ["git", "clone", "--depth=1", AGENCY_REPO, str(AGENCY_CACHE)],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        ok("agency-agents cloned successfully")
        return AGENCY_CACHE
    else:
        err(f"Clone failed: {result.stderr.strip()[:200]}")
        warn("Continuing with ag_ai agents only")
        return None


def install_agency_agents(target, agency_root, divisions, overwrite_all=False):
    """Copy agency-agents .md files into .opencode/agents/ and .claude/agents/"""
    oc_dest = target / ".opencode" / "agents"
    cl_dest = Path.home() / ".claude" / "agents"

    if not DRY_RUN:
        oc_dest.mkdir(parents=True, exist_ok=True)
        cl_dest.mkdir(parents=True, exist_ok=True)

    total = 0
    for div in divisions:
        div_path = agency_root / div
        if not div_path.exists():
            warn(f"Division not found in cache: {div}"); continue
        agents = list(div_path.glob("*.md"))
        for agent_file in agents:
            if not DRY_RUN:
                shutil.copy2(agent_file, oc_dest / agent_file.name)
                shutil.copy2(agent_file, cl_dest / agent_file.name)
            total += 1
        ok(f"  {div:25s} → {len(agents):3d} agents")

    return total

def build_agents_md(target, divisions, agency_root, overwrite_all=False):
    """Generate AGENTS.md with combined routing for ag_ai + agency-agents."""
    lines = [
        "# AGENTS.md\n",
        "> **Read this first.** Then read CLAUDE.md and .ai/context/ files.\n",
        "---\n",
        "## 🏗 ag_ai — Core 18 Agents\n",
        "| Task | Agent |",
        "|------|-------|",
        "| Complex multi-step task | `orchestrator` — delegates only, never codes |",
        "| Write / refactor code | `coder` |",
        "| Database schema + queries | `db-agent` |",
        "| REST endpoints / webhooks | `api-agent` |",
        "| Spec-first planning | `spec-workflow` |",
        "| System design | `architect` |",
        "| TDD implementation | `tdd-guide` |",
        "| Security audit | `security-reviewer` |",
        "| Code review | `code-reviewer` |",
        "| DB quality review | `database-reviewer` |",
        "| Refactoring | `refactor-cleaner` |",
        "| Build / runtime errors | `build-error-resolver` |",
        "| Documentation | `doc-updater` |",
        "| SQL generation | `sql-helper` |",
        "| Telegram bot | `telegram-bot` |",
        "| n8n workflows | `n8n-workflow` |",
        "| Debugging | `debugger` |",
        "| Writing tests | `test-writer` |",
        "",
        "---\n",
        "## 🏢 agency-agents — Specialist Divisions\n",
    ]

    if agency_root:
        for div in divisions:
            div_path = agency_root / div
            if not div_path.exists(): continue
            agents = sorted(div_path.glob("*.md"))
            if not agents: continue
            lines.append(f"### {div.replace('-', ' ').title()}\n")
            lines.append("| Agent | Role |")
            lines.append("|-------|------|")
            for a in agents:
                name = a.stem
                role = name.replace(f"{div}-", "").replace("-", " ").title()
                lines.append(f"| `{name}` | {role} |")
            lines.append("")
    else:
        lines.append("_agency-agents not installed_\n")

    lines += [
        "---\n",
        "## Non-Negotiable Rules\n",
        "- NEVER hardcode credentials, tokens, or API keys",
        "- NEVER use SELECT * in production",
        "- ALWAYS validate user input at the boundary",
        "- ALWAYS use parameterized SQL",
        "",
        "## Workflow\n",
        "1. Spec first → then code",
        "2. Tests first (TDD)",
        "3. Small targeted changes over large rewrites",
        "4. Use orchestrator to coordinate multi-agent tasks",
    ]

    content = "\n".join(lines)
    out = target / "AGENTS.md"
    if not DRY_RUN:
        out.write_text(content, encoding="utf-8")
        ok("AGENTS.md → combined routing table written")
    else:
        dry("WOULD WRITE: AGENTS.md")


def update_agents_only(target):
    """Update agents, rules, templates — preserve all context files."""
    header("Updating agents only (preserving context)...")
    for subdir in [".opencode", ".claude"]:
        src = SCRIPT_DIR / subdir
        if src.exists():
            copy_item(src, target / subdir, f"{subdir}/", overwrite_all=True)
    for item in ["agents", "rules", "spec/templates"]:
        src = SCRIPT_DIR / ".ai" / item
        dst = target / ".ai" / item
        if src.exists():
            copy_item(src, dst, f".ai/{item}/", overwrite_all=True)
    for f in ["spec/commands.md"]:
        src = SCRIPT_DIR / ".ai" / f
        dst = target / ".ai" / f
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            copy_item(src, dst, f".ai/{f}", overwrite_all=True)
    # Also update agency-agents
    if not AG_ONLY and not NO_AGENCY:
        divisions = get_divisions()
        agency_root = ensure_agency_cache()
        if agency_root:
            header("Updating agency-agents...")
            total = install_agency_agents(target, agency_root, divisions, overwrite_all=True)
            ok(f"agency-agents updated: {total} agents")
            build_agents_md(target, divisions, agency_root, overwrite_all=True)
    info("Context files preserved: PROJECT.md, STACK.md, RULES.md, constitution.md")

def make_dirs(target, use_opencode=True, use_speckit=True):
    dirs = ["specs", ".ai/agents", ".ai/rules", ".ai/context", ".claude/commands", ".claude/agents"]
    if use_opencode: dirs.append(".opencode/agents")
    if use_speckit:  dirs += [".ai/spec/memory", ".ai/spec/templates"]
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

def main():
    if DRY_RUN:       print(f"\n{BOLD}  ag_ai x agency-agents -- DRY RUN{RESET}")
    elif AGENTS_ONLY: print(f"\n{BOLD}  ag_ai x agency-agents -- Update Agents Only{RESET}")
    elif AUTO_MODE:   print(f"\n{BOLD}  ag_ai x agency-agents -- Installing (auto)...{RESET}")
    else:
        print(f"\n{BOLD}{'='*54}")
        print(f"   ag_ai x agency-agents -- Merged Installer v3.0")
        print(f"{'='*54}{RESET}")

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

    # ── Step 1: ag_ai core files ────────────────────────────────────────────
    header("Installing ag_ai core files...")
    copy_item(SCRIPT_DIR/"CLAUDE.md", target/"CLAUDE.md", "CLAUDE.md", overwrite_all=overwrite_all)
    install_ai_folder(target, overwrite_all=overwrite_all)
    copy_item(SCRIPT_DIR/".claude",   target/".claude",   ".claude/",   overwrite_all=overwrite_all)
    copy_item(SCRIPT_DIR/".opencode", target/".opencode", ".opencode/", overwrite_all=overwrite_all)
    make_dirs(target)
    update_gitignore(target)

    # ── Step 2: agency-agents ───────────────────────────────────────────────
    agency_root  = None
    agency_total = 0
    divisions    = []

    if not AG_ONLY and not NO_AGENCY:
        divisions   = get_divisions()
        agency_root = ensure_agency_cache()
        if agency_root:
            header(f"Installing agency-agents ({len(divisions)} divisions)...")
            agency_total = install_agency_agents(target, agency_root, divisions, overwrite_all)
            ok(f"Total agency-agents installed: {agency_total}")

    # ── Step 3: AGENTS.md ───────────────────────────────────────────────────
    header("Generating AGENTS.md...")
    build_agents_md(target, divisions, agency_root, overwrite_all)

    # ── Summary ─────────────────────────────────────────────────────────────
    ag_count = len(list((target/".opencode"/"agents").glob("*.yml"))) if not DRY_RUN else 18
    print(f"\n{GREEN}{BOLD}{'='*54}")
    print(f"  Done! ag_ai installed successfully.")
    print(f"{'='*54}{RESET}")
    print(f"  {CYAN}ag_ai agents:{RESET}     {ag_count} YAML agents")
    if agency_total:
        print(f"  {CYAN}agency-agents:{RESET}    {agency_total} agents ({len(divisions)} divisions)")
        print(f"  {CYAN}Divisions:{RESET}        {', '.join(divisions)}")
    print(f"\n  {YELLOW}Next steps:{RESET}")
    print(f"  1. C:\\ag_ai\\run.bat wizard \"{target}\"")
    print(f"  2. cd \"{target}\" && opencode")
    print(f"     use orchestrator agent to manage: [task]\n")

if __name__ == "__main__":
    main()
