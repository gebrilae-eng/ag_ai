#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ag_ai v5 -- wizard.py
Ask 4 questions about your project, generate everything automatically:
  - .ai/context/ files (PROJECT, STACK, RULES, constitution)
  - AGENTS.md + CLAUDE.md + PRD.md
  - .claude/settings.json  (stack-aware hooks)
  - .claude/skills/        (SKILL.md files for your framework)
  - .claude/commands/      (/learn /verify /security /checkpoint /evolve)
  - .claude/security/      (security-audit.js)
  - wizard-answers.json

Usage:
  python wizard.py
  python wizard.py D:\\my-project
"""

import sys, json, shutil
from pathlib import Path
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

BOLD   = "\033[1m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
DIM    = "\033[2m"
RESET  = "\033[0m"

SCRIPT_DIR = Path(__file__).parent.resolve()

def title(t): print(f"\n{BOLD}{'─'*52}\n  {t}\n{'─'*52}{RESET}")
def ok(msg):  print(f"  {GREEN}OK  {msg}{RESET}")
def warn(msg): print(f"  {YELLOW}--  {msg}{RESET}")

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
    print(f"     {BOLD}0{RESET}) All")
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

# ================================================================
# 1. COLLECT ANSWERS
# ================================================================
def collect_answers():
    a = {}
    title("1 / 4  --  Project Info")
    a["name"]         = ask("Project name", "My Project")
    a["description"]  = ask("What does it do?")
    a["type"]         = ask("Type (web / api / bot / automation / cli)", "web")
    a["status"]       = ask("Status (new / development / production)", "new")
    a["out_of_scope"] = ask("What does it NOT do?", "Not defined yet")

    title("2 / 4  --  Tech Stack")
    a["backend"]   = ask("Backend (e.g. PHP vanilla / Laravel / Node.js / Python+Django)", "PHP vanilla")
    a["db_engine"] = ask("Database (e.g. MySQL 8 / PostgreSQL / MongoDB / SQLite / None)", "MySQL 8")
    a["db_name"]   = ask("Database name", "my_db")
    a["db_user"]   = ask("DB username", "root")
    a["db_pass"]   = ask("DB password (.env only)", "")
    a["frontend"]  = ask("Frontend (e.g. HTML/JS / React / Vue / Blade / None)", "HTML/CSS/JS")
    a["local"]     = ask("Local dev env (e.g. Laragon / Docker / XAMPP / venv)", "Laragon")
    a["integrations"] = ask_multi("Integrations?",
        ["Telegram bot", "n8n workflows", "REST APIs", "WhatsApp", "Email", "Docker", "None"])

    title("3 / 4  --  Rules")
    a["hard_rules"] = ask("Hard business rules? (e.g. no hard delete, prices in EGP)", "")
    a["language"]   = ask("Docs language (English / Arabic / Both)", "Both")
    a["ai_tool"]    = ask("AI tool (claude / opencode / both)", "both")
    return a

# ================================================================
# 2. CONTEXT FILE GENERATORS
# ================================================================
def gen_project_md(a):
    integ = "\n".join(f"- {i}" for i in a["integrations"])
    return f"""# Project Overview
## Project Name
`{a['name']}`
## Description
{a['description']}
## Type / Status
{a['type'].capitalize()} / {a['status'].capitalize()}
## Key Integrations
{integ}
## Out of Scope
- {a['out_of_scope']}
"""

def gen_stack_md(a):
    integ = "\n".join(f"- {i}" for i in a["integrations"])
    app = a["name"].upper().replace(" ", "_")
    return f"""# Tech Stack
## Backend
- Language / Framework: `{a['backend']}`
- Local Server: `{a['local']}`
## Database
- Engine: `{a['db_engine']}`  Name: `{a['db_name']}`
## Frontend
- `{a['frontend']}`
## Integrations
{integ}
## Environment Variables
```env
APP_NAME={app}
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE={a['db_name']}
DB_USERNAME={a['db_user']}
DB_PASSWORD={a['db_pass']}
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
- ALWAYS handle errors explicitly — never silently fail
## Project-Specific Rules
{hard}
## Documentation Language
{a['language']}
## Security
- Parameterized queries for all DB operations
- Validate at input boundary — never trust external input
- Secrets in .env only — never in source code
"""

def gen_constitution_md(a):
    hard = a["hard_rules"].strip() or "No hard deletes -- use soft-delete (deleted_at)"
    return f"""# Constitution -- {a['name']}
**Version**: 1.0.0
**Created**: {datetime.now().strftime('%Y-%m-%d')}

## P1 -- Data Integrity
All DB operations MUST use parameterized queries.
{hard}

## P2 -- Security First
ALL user inputs MUST be validated before processing.
Secrets MUST live in .env -- never in source code.

## P3 -- Code Quality
Every function MUST do one thing only.
Tests MUST be written BEFORE implementation (TDD).
Coverage target: 80%+

## P4 -- Language
Comments and docs: {a['language']}

## P5 -- Consistency
Follow .ai/context/RULES.md at all times.
When in doubt -- ask, don't assume.
"""

def gen_agents_md(a):
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules yet"
    integ = ", ".join(a["integrations"])
    return f"""# AGENTS.md -- {a['name']}

> Read this first. Then CLAUDE.md and .ai/context/ files.

## Project
- Stack: {a['backend']} + {a['db_engine']} ({a['db_name']}) + {a['frontend']}
- Integrations: {integ}
- Local: {a['local']}

## Agent Routing
| Task | Agent |
|------|-------|
| Complex multi-step | `orchestrator` (delegates only) |
| Write / refactor code | `coder` |
| DB schema / queries | `db-agent` |
| API / integrations | `api-agent` |
| Spec-first planning | `spec-workflow` |
| System design | `architect` |
| TDD | `tdd-guide` |
| Security audit | `security-reviewer` |
| Code review | `code-reviewer` |
| DB review | `database-reviewer` |
| Debugging | `debugger` |
| Telegram bot | `telegram-bot` |
| n8n workflows | `n8n-workflow` |

## Non-Negotiable Rules
- NEVER hardcode credentials, tokens, or API keys
- NEVER use SELECT * in production
- ALWAYS validate user input at the boundary
- ALWAYS use parameterized SQL
{hard}

## Workflow
1. Spec first then code
2. Tests first (TDD)
3. /verify before every commit
4. /security before deploy
"""

def gen_claude_md(a):
    tool = a["ai_tool"].lower()
    lines = [
        f"# AI Instructions -- {a['name']}", "",
        "> Reading chain: PRD.md -> AGENTS.md -> .ai/context/STACK.md -> .ai/context/RULES.md", "",
        f"## Stack: `{a['backend']}` + `{a['db_engine']}/{a['db_name']}` + `{a['frontend']}`", "",
        "## Commands", "| Command | Purpose |", "|---------|---------|",
        "| `/learn` | Extract patterns from session |",
        "| `/verify` | Quality gate before commit |",
        "| `/security` | Security audit |",
        "| `/checkpoint` | Save session state |",
        "| `/instinct-status` | View learned instincts |",
        "| `/evolve` | Turn instincts into skills |", "",
        "## Agent Routing", "| Task | Agent |", "|------|-------|",
        "| Complex task | `orchestrator` |",
        "| Code | `coder` |",
        "| DB | `db-agent` |",
        "| API | `api-agent` |",
        "| Spec | `spec-workflow` |",
        "| TDD | `tdd-guide` |",
        "| Debug | `debugger` |", "",
    ]
    if "claude" in tool or "both" in tool:
        lines += ["## Claude Code", "```",
                  "/speckit.specify  -- new feature spec",
                  "/tdd              -- test-first development",
                  "/verify           -- quality check",
                  "/security         -- OWASP audit", "```", ""]
    if "open" in tool or "both" in tool:
        lines += ["## OpenCode", "```",
                  "use orchestrator agent to manage: [task]",
                  "use coder agent to implement: [feature]", "```", ""]
    return "\n".join(lines)

def gen_prd_md(a):
    integ = "\n".join(f"- {i}" for i in a["integrations"])
    hard = f"- {a['hard_rules']}" if a["hard_rules"].strip() else "- No additional rules"
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""# PRD -- {a['name']}
> Generated by ag_ai wizard on {today}.

## 1. Product Overview
| Field | Value |
|-------|-------|
| **Name** | {a['name']} |
| **Type** | {a['type'].capitalize()} |
| **Status** | {a['status'].capitalize()} |
| **Description** | {a['description']} |
| **Out of Scope** | {a['out_of_scope']} |
| **Docs Language** | {a['language']} |

## 2. Tech Stack
| Layer | Technology |
|-------|-----------|
| **Backend** | `{a['backend']}` |
| **Database** | `{a['db_engine']}` -- `{a['db_name']}` |
| **Frontend** | `{a['frontend']}` |
| **Local Dev** | `{a['local']}` |

### Integrations
{integ}

## 3. Business Rules
{hard}

## 4. Features & Specs
- No features yet -- run `/speckit.specify` to add features.

## 5. Reading Chain
PRD.md -> AGENTS.md -> .ai/context/STACK.md -> .ai/context/RULES.md -> constitution.md
"""

# ================================================================
# 3. HOOKS GENERATOR
# ================================================================
def _pre_hook(desc, js):
    cmd = ('node -e "let d=\'\';process.stdin.on(\'data\',c=>d+=c);'
           'process.stdin.on(\'end\',()=>{'
           'const i=JSON.parse(d);const cmd=(i.tool_input?.command||\'\');'
           f'{js}'
           'console.log(d)})"')
    return {"matcher": "Bash", "hooks": [{"type": "command", "command": cmd}], "description": desc}

def _post_hook(desc, js):
    cmd = ('node -e "let d=\'\';process.stdin.on(\'data\',c=>d+=c);'
           'process.stdin.on(\'end\',()=>{'
           'const i=JSON.parse(d);'
           'const fp=(i.tool_input?.file_path||\'\');'
           'const content=(i.tool_input?.new_string||i.tool_input?.content||\'\');'
           f'{js}'
           'console.log(d)})"')
    return {"matcher": "Write|Edit", "hooks": [{"type": "command", "command": cmd}], "description": desc}

def generate_hooks(a):
    backend = a.get("backend", "").lower()
    db      = a.get("db_engine", "").lower()
    integ   = [i.lower() for i in a.get("integrations", [])]
    pre, post, stop = [], [], []

    # Universal
    pre.append(_pre_hook("Block git push --force",
        r"if(/git push.*--force|git push.*-f/.test(cmd)){console.error('[HOOK] git push --force blocked');process.exit(2)}"))
    post.append(_post_hook("Detect hardcoded secrets",
        r"const sec=[/sk-[a-zA-Z0-9]{48}/,/ghp_[a-zA-Z0-9]{36}/,/AKIA[0-9A-Z]{16}/,/-----BEGIN.*PRIVATE KEY/];"
        r"if(sec.some(r=>r.test(content)))console.error('[HOOK] Possible hardcoded secret!');"))
    stop.append({"hooks": [{"type": "command", "command":
        'node -e "process.stdin.resume();process.stdin.on(\'data\',()=>{});'
        'process.stdin.on(\'end\',()=>{console.error(\'[HOOK] Session ended -- run /verify before commit\');'
        'process.stdout.write(\'{}\')})"'}], "description": "Session end reminder"})

    # DB
    if any(k in db for k in ["mysql","postgres","sqlite","mariadb"]):
        pre.append(_pre_hook("Block dangerous DB commands",
            r"const d=['DROP TABLE','DROP DATABASE','TRUNCATE'];"
            r"const f=d.filter(p=>cmd.toUpperCase().includes(p));"
            r"if(f.length){console.error('[HOOK] Dangerous DB: '+f.join(', '));process.exit(2)}"))
        pre.append(_pre_hook("Block DELETE without WHERE",
            r"if(/DELETE\s+FROM/i.test(cmd)&&!/WHERE/i.test(cmd)){console.error('[HOOK] DELETE without WHERE');process.exit(2)}"))

    # PHP
    if "php" in backend:
        post.append(_post_hook("PHP security checks",
            r"if(fp.endsWith('.php')){"
            r"const p=[];"
            r"if(/md5\s*\([^)]*pass/i.test(content))p.push('MD5 password->use password_hash()');"
            r"if(/SELECT\s+\*/i.test(content))p.push('SELECT * ->specify columns');"
            r"if(/\$_(GET|POST)\[/.test(content)&&!content.includes('prepare'))p.push('Unvalidated input->prepared statement');"
            r"if(p.length)console.error('[HOOK] PHP: '+p.join(' | '));}"))

    # Python
    if any(k in backend for k in ["python","django","fastapi","flask"]):
        post.append(_post_hook("Python security checks",
            r"if(fp.endsWith('.py')){"
            r"const p=[];"
            r"if(/\beval\s*\(/.test(content))p.push('eval() is dangerous');"
            r"if(/os\.system\s*\(/.test(content))p.push('os.system()->use subprocess');"
            r"if(p.length)console.error('[HOOK] Python: '+p.join(' | '));}"))

    # Node / JS
    if any(k in backend for k in ["node","express","next","nuxt","react","vue"]):
        post.append(_post_hook("JS security checks",
            r"if(['.js','.ts','.jsx','.tsx'].some(e=>fp.endsWith(e))){"
            r"const p=[];"
            r"if(/\beval\s*\(/.test(content))p.push('eval() dangerous');"
            r"if(/innerHTML\s*=\s*[^'\"` ]/.test(content))p.push('innerHTML= XSS risk');"
            r"if(/console\.log\(/.test(content))p.push('console.log->remove before commit');"
            r"if(p.length)console.error('[HOOK] JS: '+p.join(' | '));}"))

    # n8n
    if any("n8n" in i for i in integ):
        post.append(_post_hook("n8n: no template literals",
            r"if(content.includes('$input.all()')||content.includes('$json')){"
            r"if(/`[^`]*\$\{/.test(content))console.error('[HOOK] n8n: template literals->use string concat');}"))

    # Telegram
    if any("telegram" in i for i in integ):
        post.append(_post_hook("Telegram: enforce HTML parse_mode",
            r"if(content.includes('parse_mode')&&content.includes('Markdown'))"
            r"console.error('[HOOK] Telegram: use HTML not Markdown (breaks Arabic)');"))

    # Background observer (async)
    post.append({"matcher": "Write|Edit|Bash",
        "hooks": [{"type": "command",
                   "command": "node ~/.claude/hooks/scripts/session-observer.js",
                   "async": True, "timeout": 10}],
        "description": "Background observer -- logs patterns for /learn"})

    hooks = {}
    if pre:  hooks["PreToolUse"]  = pre
    if post: hooks["PostToolUse"] = post
    if stop: hooks["Stop"]        = stop
    return {"$schema": "https://json.schemastore.org/claude-code-settings.json", "hooks": hooks}

# ================================================================
# 4. SKILLS GENERATOR
# ================================================================
SKILL_TEMPLATES = {

"security-core": lambda a: f"""---
name: security-core
description: >
  Core security patterns for {a['name']}.
  Use for any code handling input, auth, secrets, or DB queries.
---
# Security Core -- {a['name']}
## Non-Negotiables
- Never hardcode secrets -- use env vars
- Always validate external input at the boundary
- Always use parameterized queries -- no string concat in SQL
- Never expose stack traces or DB details in error responses
- .env must be in .gitignore
## Input Validation
Validate at the first point of entry: Type -> sanitize -> use.
## Error Handling
```python
try:
    result = process(data)
except Exception as e:
    log.error(str(e))           # internal only
    return {{"error": "Failed"}} # safe for user
```
## Security Checklist
- [ ] No hardcoded secrets
- [ ] .env in .gitignore
- [ ] All user inputs validated
- [ ] Errors don't expose internals
- [ ] Dependencies audited
""",

"sql-patterns": lambda a: f"""---
name: sql-patterns
description: >
  SQL patterns for {a.get('db_engine','the database')} in {a['name']}.
  Parameterized queries, soft delete, safe pagination, division safety.
---
# SQL Patterns -- {a.get('db_engine','Database')}
## Always Parameterized
```sql
SELECT id, name FROM users WHERE id = ? AND active = 1
```
## Soft Delete
```sql
UPDATE users SET deleted_at = NOW() WHERE id = ?;
-- Always filter: WHERE deleted_at IS NULL
```
## Safe Division
```sql
SELECT quantity / NULLIF(avg_consumption, 0) AS months_stock FROM inventory;
```
## Pagination
```sql
SELECT id, name FROM items ORDER BY created_at DESC LIMIT ? OFFSET ?;
```
## Schema Conventions
- Every table: id, created_at, updated_at, deleted_at
- Charset: utf8mb4 (Arabic + emoji support)
- FK columns: always indexed
""",

"git-workflow": lambda a: f"""---
name: git-workflow
description: >
  Git workflow for {a['name']}. Commit format, branching, pre-commit checklist.
---
# Git Workflow -- {a['name']}
## Commit Format
```
type: description (max 72 chars)
feat / fix / refactor / docs / test / chore
```
## Before Every Commit
1. /verify  -- quality gate
2. /security -- security audit
3. git status -- confirm no .env staged
## Never Commit
.env, vendor/, node_modules/, __pycache__/, *.log
""",

"tdd-workflow": lambda a: f"""---
name: tdd-workflow
description: >
  TDD cycle for {a['name']}. Red -> Green -> Refactor.
---
# TDD Workflow -- {a['name']}
## Cycle
1. RED    -- write failing test
2. GREEN  -- minimal code to pass
3. REFACTOR -- clean up, keep green
## Always Test Edge Cases
- Null / empty / boundary inputs
- Error paths (DB failure, network, bad auth)
- Special characters (Arabic, emoji, SQL chars)
## Coverage Target
General: 80%+ | Financial / auth: 100%
""",

"n8n-patterns": lambda a: f"""---
name: n8n-patterns
description: >
  n8n Code node patterns for {a['name']}.
  Use when writing or editing any n8n workflow.
---
# n8n Patterns -- {a['name']}
## Code Node Rules
```javascript
const items = $input.all();
if (items.length === 0) return [{{ json: {{ message: 'No data' }} }}];
const value = parseFloat(item.json.field) || 0;  // null-safe
const msg = 'Hello ' + name + '!';               // string concat only -- no template literals
```
## Error Handler
```javascript
for (const item of items) {{
    try {{
        results.push({{ json: {{ ...item.json, processed: true }} }});
    }} catch (e) {{
        results.push({{ json: {{ error: e.message, original: item.json }} }});
    }}
}}
```
## MCP Tool Order
1. search_workflows -> 2. get_workflow_details -> 3. execute_workflow
""",

"telegram-bot": lambda a: f"""---
name: telegram-bot
description: >
  Telegram bot patterns for {a['name']}.
  HTML formatting, message splitting, Arabic RTL, rate limiting.
---
# Telegram Bot -- {a['name']}
## Hard Rules
1. Always parse_mode: HTML -- never Markdown (breaks Arabic)
2. Split at 3800 chars -- never send > 4096 chars
3. Escape <, >, & in all DB/user content
4. Rate limit: 10 commands/min/user
## Allowed Tags Only
<b> <i> <code> <a href=""> -- never <pre> for Arabic text
## Split Function
```javascript
function splitMessage(text, maxLen) {{
    maxLen = maxLen || 3800;
    if (text.length <= maxLen) return [text];
    const chunks = []; let current = '';
    for (const line of text.split('\\n')) {{
        if ((current + line + '\\n').length > maxLen) {{ chunks.push(current.trim()); current = ''; }}
        current += line + '\\n';
    }}
    if (current.trim()) chunks.push(current.trim());
    return chunks;
}}
```
""",

"api-design": lambda a: f"""---
name: api-design
description: >
  REST API conventions for {a['name']}.
  Endpoints, response format, error codes, security checklist.
---
# API Design -- {a['name']}
## URL Conventions
GET/POST/PUT/PATCH/DELETE /api/v1/resources/:id
## Response Format
```json
{{ "success": true, "data": {{}}, "message": "OK", "errors": null }}
```
## Status Codes
200 OK | 201 Created | 400 Bad Request | 401 Unauth | 403 Forbidden
404 Not Found | 422 Business Error | 429 Rate Limit | 500 Server Error
## Security Per Endpoint
Auth checked | Input validated | Rate limited | No secrets in response
""",
}

def select_skills(a):
    backend = a.get("backend", "").lower()
    db      = a.get("db_engine", "").lower()
    integ   = [i.lower() for i in a.get("integrations", [])]
    selected = ["security-core", "git-workflow", "tdd-workflow"]
    if any(k in db for k in ["mysql","postgres","sqlite","mariadb"]):
        selected.append("sql-patterns")
    if any("n8n" in i for i in integ):
        selected.append("n8n-patterns")
    if any("telegram" in i for i in integ):
        selected.append("telegram-bot")
    if any(k in backend for k in ["api","rest","express","fastapi","laravel","rails","django"]):
        selected.append("api-design")
    return selected

# ================================================================
# 5. SECURITY AUDIT GENERATOR
# ================================================================
def generate_security_audit(a):
    name    = a.get("name", "Project")
    backend = a.get("backend", "").lower()
    db      = a.get("db_engine", "").lower()
    integ   = [i.lower() for i in a.get("integrations", [])]

    exts = [".env", ".json", ".yaml", ".yml"]
    if "php" in backend:                                              exts += [".php"]
    if any(k in backend for k in ["python","django","fastapi","flask"]): exts += [".py"]
    if any(k in backend for k in ["node","express","next","react","vue","nuxt"]): exts += [".js",".ts",".jsx",".tsx"]

    req_env = ["SECRET_KEY"]
    if any(k in db for k in ["mysql","postgres","mariadb"]):
        req_env = ["DB_HOST","DB_DATABASE","DB_USERNAME","DB_PASSWORD"]
    if any("telegram" in i for i in integ): req_env.append("TELEGRAM_BOT_TOKEN")
    if any("n8n" in i for i in integ):      req_env.append("N8N_WEBHOOK_URL")

    lang_fns, lang_calls = "", ""

    if "php" in backend:
        lang_fns += """
function checkPhp(fp, content) {
    if (!fp.endsWith('.php')) return;
    content.split('\\n').forEach((line, idx) => {
        if (line.trim().startsWith('//') || line.trim().startsWith('*')) return;
        if (/md5\\s*\\([^)]*pass/i.test(line)) flag('critical',fp,idx+1,'MD5 password','Use password_hash(PASSWORD_BCRYPT)');
        if (/\\$_(GET|POST|REQUEST)\\[/.test(line)&&/SELECT|INSERT|UPDATE|DELETE/i.test(line)&&!line.includes('prepare')) flag('critical',fp,idx+1,'SQL with user input','Use PDO prepared statements');
        if (/SELECT\\s+\\*/i.test(line)) flag('medium',fp,idx+1,'SELECT *','Specify columns');
        if (/\\beval\\s*\\(/.test(line)) flag('high',fp,idx+1,'eval()','Refactor');
        if (/DELETE\\s+FROM/i.test(line)&&!/WHERE/i.test(line)) flag('high',fp,idx+1,'DELETE without WHERE','Add WHERE or use soft delete');
    });
}"""
        lang_calls += "\n    checkPhp(fp, content);"

    if any(k in backend for k in ["python","django","fastapi","flask"]):
        lang_fns += """
function checkPython(fp, content) {
    if (!fp.endsWith('.py')) return;
    content.split('\\n').forEach((line, idx) => {
        if (line.trim().startsWith('#')) return;
        if (/\\beval\\s*\\(/.test(line)) flag('critical',fp,idx+1,'eval()','Refactor');
        if (/os\\.system\\s*\\(/.test(line)) flag('high',fp,idx+1,'os.system()','Use subprocess.run()');
        if (/execute\\s*\\(\\s*f['"]/.test(line)) flag('critical',fp,idx+1,'f-string in SQL execute()','Use parameterized: execute(sql,[param])');
    });
}"""
        lang_calls += "\n    checkPython(fp, content);"

    if any(k in backend for k in ["node","express","next","react","vue","nuxt"]):
        lang_fns += """
function checkJs(fp, content) {
    if (!['.js','.ts','.jsx','.tsx'].some(e=>fp.endsWith(e))) return;
    content.split('\\n').forEach((line, idx) => {
        if (line.trim().startsWith('//')) return;
        if (/\\beval\\s*\\(/.test(line)) flag('critical',fp,idx+1,'eval()','Refactor');
        if (/innerHTML\\s*=/.test(line)&&!/innerHTML\\s*=\\s*['"]/.test(line)) flag('high',fp,idx+1,'innerHTML= XSS risk','Use textContent or sanitize');
        if (/console\\.log\\(/.test(line)) flag('info',fp,idx+1,'console.log','Remove before production');
    });
}"""
        lang_calls += "\n    checkJs(fp, content);"

    if any("n8n" in i for i in integ):
        lang_fns += """
function checkN8n(fp, content) {
    if (!content.includes('$input')&&!content.includes('$json')) return;
    content.split('\\n').forEach((line, idx) => {
        if (/`[^`]*\\$\\{/.test(line)) flag('high',fp,idx+1,'Template literal in n8n Code node',"Use string concat: 'a' + var + 'b'");
    });
}"""
        lang_calls += "\n    checkN8n(fp, content);"

    exts_json   = json.dumps(exts)
    reqenv_json = json.dumps(req_env)

    return f"""#!/usr/bin/env node
// security-audit.js -- {name}
// Generated by ag_ai wizard.py | Run: node security-audit.js [project-path]
const fs=require('fs'),path=require('path');
const C={{red:s=>`\\x1b[31m${{s}}\\x1b[0m`,yellow:s=>`\\x1b[33m${{s}}\\x1b[0m`,green:s=>`\\x1b[32m${{s}}\\x1b[0m`,bold:s=>`\\x1b[1m${{s}}\\x1b[0m`,dim:s=>`\\x1b[2m${{s}}\\x1b[0m`}};
const projectPath=process.argv[2]||process.cwd();
const findings={{critical:[],high:[],medium:[],info:[]}};
let filesScanned=0;
function flag(level,file,line,issue,fix){{findings[level].push({{file:path.relative(projectPath,file),line,issue,fix}});}}
function walkDir(dir,exts,cb){{
  if(!fs.existsSync(dir))return;
  const skip=['node_modules','vendor','.git','__pycache__','.cache'];
  let entries;try{{entries=fs.readdirSync(dir);}}catch(_){{return;}}
  for(const e of entries){{
    if(skip.includes(e))continue;
    const full=path.join(dir,e);
    let stat;try{{stat=fs.statSync(full);}}catch(_){{continue;}}
    if(stat.isDirectory())walkDir(full,exts,cb);
    else if(exts.some(x=>full.endsWith(x))){{try{{cb(full,fs.readFileSync(full,'utf8'));filesScanned++;}}catch(_){{}}}}
  }}
}}
function checkSecrets(fp,content){{
  if(path.basename(fp)==='.env')return;
  const patterns=[
    {{re:/sk-[a-zA-Z0-9]{{48}}/,name:'OpenAI key'}},
    {{re:/ghp_[a-zA-Z0-9]{{36}}/,name:'GitHub token'}},
    {{re:/AKIA[0-9A-Z]{{16}}/,name:'AWS key'}},
    {{re:/TELEGRAM_BOT_TOKEN\\s*=\\s*[\\d]+:[A-Za-z0-9_-]{{35}}/,name:'Telegram token'}},
    {{re:/['"]password['"]\\s*[:=]\\s*['"][^'"']{{4,}}['"]/,name:'Hardcoded password'}},
    {{re:/-----BEGIN.*PRIVATE KEY-----/,name:'Private key'}},
    {{re:/mysql:\\/\\/[^:]+:[^@]+@/,name:'MySQL connection with password'}},
  ];
  content.split('\\n').forEach((line,idx)=>{{
    if(line.trim().startsWith('//')||line.trim().startsWith('#'))return;
    for(const p of patterns)if(p.re.test(line))flag('critical',fp,idx+1,`Hardcoded secret: ${{p.name}}`,'Move to .env');
  }});
}}
{lang_fns}
function checkConfig(){{
  const envPath=path.join(projectPath,'.env');
  const giPath=path.join(projectPath,'.gitignore');
  const required={reqenv_json};
  if(!fs.existsSync(envPath))flag('high',envPath,0,'.env missing','Create .env');
  else{{
    const env=fs.readFileSync(envPath,'utf8');
    for(const k of required)if(!env.includes(k+'='))flag('medium',envPath,0,`.env missing: ${{k}}`,`Add ${{k}}=value`);
  }}
  if(!fs.existsSync(giPath))flag('high',giPath,0,'.gitignore missing','Create .gitignore');
  else if(!fs.readFileSync(giPath,'utf8').includes('.env'))flag('critical',giPath,0,'.env not in .gitignore',"Add '.env' to .gitignore");
}}
console.log(C.bold(`\\n  Security Audit -- {name}`));
console.log(C.dim(`  ${{projectPath}}\\n`));
walkDir(projectPath,{exts_json},(fp,content)=>{{checkSecrets(fp,content);{lang_calls}}});
checkConfig();
const c=findings.critical.length,h=findings.high.length,m=findings.medium.length,i=findings.info.length;
const grade=c>0?'F':h>2?'D':h>0?'C':m>0?'B':'A';
const gc=['A','B'].includes(grade)?C.green:['C','D'].includes(grade)?C.yellow:C.red;
console.log('  '+'─'.repeat(48));
for(const [level,items] of Object.entries(findings)){{
  if(!items.length)continue;
  const icon=level==='critical'?C.red('[CRITICAL]'):level==='high'?C.red('[HIGH]    '):level==='medium'?C.yellow('[MEDIUM]  '):C.dim('[INFO]    ');
  for(const f of items){{
    console.log(`  ${{icon}} ${{f.line>0?f.file+':'+f.line:f.file}}`);
    console.log(`          ${{C.bold('Issue:')}} ${{f.issue}}`);
    console.log(`          ${{C.dim('Fix:  ')}} ${{f.fix}}\\n`);
  }}
}}
console.log('  '+'─'.repeat(48));
console.log(`  Files: ${{filesScanned}} | C:${{C.red(c)}} H:${{C.red(h)}} M:${{C.yellow(m)}} I:${{C.dim(i)}}`);
console.log(`  Grade: ${{gc(C.bold(grade))}}`);
console.log('  '+'─'.repeat(48));
if(c>0||h>0){{console.log(C.red('\\n  Fix issues before deploy\\n'));process.exit(1);}}
else{{console.log(C.green('\\n  Safe to deploy\\n'));process.exit(0);}}
"""

# ================================================================
# 6. COMMANDS CONTENT
# ================================================================
COMMANDS = {
"learn.md": """\
Extract reusable patterns from this session and save as instincts.

Review this conversation for any behavior that appeared 2+ times:
corrections, conventions confirmed, anti-patterns flagged by hooks.

Save each to ~/.claude/instincts/personal/{id}.yaml:
```yaml
---
id: short-kebab-id
trigger: "when {situation}"
confidence: 0.3-0.9
domain: code-style|sql|api|security|testing|git|other
source: session-observation
observed: {YYYY-MM-DD}
---
## Action
{One clear sentence: what to do}
## Evidence
- {Observation from this session}
## Examples
{correct code example}
```
Confidence: 0.9=hard rule | 0.7=strong | 0.5=moderate | 0.3=tentative
After: run /instinct-status to review.
""",

"instinct-status.md": """\
Show all instincts grouped by domain with confidence scores.

Read ~/.claude/instincts/personal/*.yaml, group by domain, display:
```
Instincts -- {N} total
─────────────────────
── {domain} ({count}) ──
  ████████░░  0.9  {id} -> {trigger}
  ███████░░░  0.7  {id} -> {trigger}
```
Confidence bar: round(confidence * 10) filled blocks.
Run /evolve when a domain has 3+ instincts with confidence >= 0.7.
""",

"evolve.md": """\
Cluster instincts into reusable SKILL.md files or commands.

1. Read all ~/.claude/instincts/personal/*.yaml
2. Group by domain -- clusters with 3+ instincts -> evolve
3. Coding patterns -> SKILL.md in ~/.claude/skills/{name}/
4. Workflow -> command.md in ~/.claude/commands/
5. Mark evolved instincts with evolved: true and evolved_into: {path}
6. Report what was created and what is still pending.
""",

"checkpoint.md": """\
Save current session state to ~/.claude/checkpoints/{YYYY-MM-DD}-{desc}.md

Format:
# Checkpoint: {desc}
Date: {YYYY-MM-DD HH:MM}

## Completed
- {task}

## In Progress
- {task}: done {x}, remaining {y}

## Pending
- {task}

## Files Modified
- {path} -- {change}

## Resume
{One sentence to restore context}
""",

"verify.md": """\
Quality gate before committing. Check .ai/context/STACK.md for the project
stack, then run relevant checks.

## Universal (all projects)
- [ ] No hardcoded secrets | .env in .gitignore | All .env keys set
- [ ] No TODO/FIXME in committed code | Errors do not expose internals

## Stack checks
Read ~/.claude/skills/ for installed skills -- each has a checklist.
Common: no SELECT * | parameterized SQL | no eval() | no console.log in prod

## Report
```
Quality Gate
────────────
Universal ........ OK / N issues
{Stack} .......... OK / N warnings
Issues: {file}:{line} -- {issue} -> Fix: {fix}
Overall: PASS / FAIL
```
For each failure show the bad code and corrected version.
""",

"security.md": """\
Run the security audit for this project.

```bash
node ~/.claude/security/security-audit.js {project-path}
```

The script was generated for this project stack by wizard.py.
If missing, re-run: python C:\\ag_ai\\wizard.py {project-path}

For each CRITICAL or HIGH finding:
- Show the vulnerable code
- Show the corrected version
- Apply the fix (ask first for significant changes)

Grades: A=clean | B=info only | C=medium | D=high | F=critical (do NOT deploy)
""",
}

# ================================================================
# 7. SESSION OBSERVER
# ================================================================
SESSION_OBSERVER = r"""#!/usr/bin/env node
// session-observer.js -- background hook, async:true, never blocks Claude
const fs=require('fs'),path=require('path'),os=require('os');
const OBS=path.join(os.homedir(),'.claude','sessions','observations.jsonl');
const dir=path.dirname(OBS);
if(!fs.existsSync(dir))fs.mkdirSync(dir,{recursive:true});
let raw='';
process.stdin.on('data',c=>raw+=c);
process.stdin.on('end',()=>{
  try{
    const input=JSON.parse(raw);
    const content=input.tool_input?.new_string||input.tool_input?.content||'';
    const fp=input.tool_input?.file_path||'';
    const obs=[];
    if(fp.endsWith('.php')){
      if(/password_hash\s*\(.*BCRYPT/.test(content))obs.push({pattern:'php-bcrypt',domain:'php',signal:'correct'});
      if(/md5\s*\([^)]*pass/i.test(content))obs.push({pattern:'php-md5',domain:'security',signal:'anti-pattern'});
    }
    if(content.includes('$input.all()')||content.includes('$json')){
      if(/`[^`]*\$\{/.test(content))obs.push({pattern:'n8n-template-literal',domain:'n8n',signal:'anti-pattern'});
      if(/parseFloat.*\|\|\s*0/.test(content))obs.push({pattern:'n8n-null-safe',domain:'n8n',signal:'correct'});
    }
    if(content.includes('parse_mode')){
      if(content.includes('HTML'))obs.push({pattern:'telegram-html',domain:'telegram',signal:'correct'});
      if(content.includes('Markdown'))obs.push({pattern:'telegram-markdown',domain:'telegram',signal:'anti-pattern'});
    }
    if(content.includes('NULLIF'))obs.push({pattern:'sql-nullif',domain:'sql',signal:'correct'});
    if(obs.length>0){
      const ts=new Date().toISOString();
      fs.appendFileSync(OBS,obs.map(o=>JSON.stringify({ts,file:fp,...o})).join('\n')+'\n','utf8');
    }
  }catch(_){}
  process.stdout.write(raw);
});
"""

# ================================================================
# 8. WRITE ALL FILES
# ================================================================
def write_file(path_obj, content, label, overwrite_all=False):
    if path_obj.exists() and not overwrite_all:
        if not ask_yes(f"  {label} already exists. Overwrite?", default=True):
            warn(f"Skipped: {label}"); return
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    path_obj.write_text(content, encoding="utf-8")
    ok(label)

def install_all(project_path, answers, overwrite_all=False):

    title("Writing project files...")
    ctx = project_path / ".ai" / "context"
    write_file(ctx / "PROJECT.md",         gen_project_md(answers),   ".ai/context/PROJECT.md",  overwrite_all)
    write_file(ctx / "STACK.md",           gen_stack_md(answers),     ".ai/context/STACK.md",    overwrite_all)
    write_file(ctx / "RULES.md",           gen_rules_md(answers),     ".ai/context/RULES.md",    overwrite_all)
    write_file(project_path / ".ai" / "spec" / "memory" / "constitution.md",
               gen_constitution_md(answers), "constitution.md",        overwrite_all)
    write_file(project_path / "AGENTS.md", gen_agents_md(answers),    "AGENTS.md",               overwrite_all)
    write_file(project_path / "CLAUDE.md", gen_claude_md(answers),    "CLAUDE.md",               overwrite_all)
    write_file(project_path / "PRD.md",    gen_prd_md(answers),       "PRD.md",                  overwrite_all)

    # Save answers
    ans_copy = dict(answers)
    ans_copy["integrations"] = list(ans_copy["integrations"])
    (ctx / "wizard-answers.json").write_text(
        json.dumps(ans_copy, ensure_ascii=False, indent=2), encoding="utf-8")
    ok(".ai/context/wizard-answers.json")

    title("Generating Hooks...")
    hooks_data = generate_hooks(answers)
    settings_p = project_path / ".claude" / "settings.json"
    settings_p.parent.mkdir(parents=True, exist_ok=True)
    if settings_p.exists():
        try:
            existing = json.loads(settings_p.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
        existing["hooks"] = hooks_data["hooks"]
        settings_p.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
        ok(".claude/settings.json (merged)")
    else:
        settings_p.write_text(json.dumps(hooks_data, ensure_ascii=False, indent=2), encoding="utf-8")
        ok(".claude/settings.json (created)")
    pre_c  = len(hooks_data["hooks"].get("PreToolUse",  []))
    post_c = len(hooks_data["hooks"].get("PostToolUse", []))
    ok(f"  Hooks: {pre_c} PreToolUse + {post_c} PostToolUse")

    title("Generating Skills...")
    selected = select_skills(answers)
    for dest in [Path.home()/".claude"/"skills", project_path/".claude"/"skills"]:
        for name in selected:
            if name not in SKILL_TEMPLATES: continue
            skill_dir = dest / name
            if skill_dir.exists(): shutil.rmtree(skill_dir)
            skill_dir.mkdir(parents=True, exist_ok=True)
            (skill_dir / "SKILL.md").write_text(SKILL_TEMPLATES[name](answers), encoding="utf-8")
    ok(f"Skills ({len(selected)}): {', '.join(selected)}")

    title("Installing Commands...")
    for dest in [Path.home()/".claude"/"commands", project_path/".claude"/"commands"]:
        dest.mkdir(parents=True, exist_ok=True)
        for fname, content in COMMANDS.items():
            (dest / fname).write_text(content, encoding="utf-8")
    ok("Commands: /learn /instinct-status /evolve /checkpoint /verify /security")

    title("Session Observer...")
    obs_dir = Path.home() / ".claude" / "hooks" / "scripts"
    obs_dir.mkdir(parents=True, exist_ok=True)
    (obs_dir / "session-observer.js").write_text(SESSION_OBSERVER, encoding="utf-8")
    ok("session-observer.js (background learning)")

    title("Generating Security Audit...")
    audit = generate_security_audit(answers)
    for dest in [Path.home()/".claude"/"security", project_path/".claude"/"security"]:
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "security-audit.js").write_text(audit, encoding="utf-8")
    ok("security-audit.js")

    # .gitignore
    gi = project_path / ".gitignore"
    entries = [".env","*.log","node_modules/","__pycache__/","vendor/"]
    existing_gi = gi.read_text(encoding="utf-8") if gi.exists() else ""
    new_entries = [e for e in entries if e not in existing_gi]
    if new_entries:
        with open(gi, "a", encoding="utf-8") as f:
            f.write("\n# ag_ai\n" + "\n".join(new_entries) + "\n")
        ok(".gitignore updated")

    for d in ["specs",".ai/agents",".ai/rules",".ai/spec/templates",".claude/agents"]:
        (project_path / d).mkdir(parents=True, exist_ok=True)

# ================================================================
# 9. MAIN
# ================================================================
def get_project_path():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args: return Path(args[0]).resolve()
    print(f"\n{BOLD}  ag_ai v5 -- Project Wizard{RESET}\n")
    raw = ask("Project folder path")
    p = Path(raw).resolve() if raw else Path.cwd()
    if not p.exists(): p.mkdir(parents=True)
    return p

def print_summary(a):
    title("Summary -- Review before writing")
    print(f"""
  Project:      {a['name']}
  Description:  {a['description']}
  Type:         {a['type']} / {a['status']}
  Backend:      {a['backend']}
  DB:           {a['db_engine']} / {a['db_name']}
  Frontend:     {a['frontend']}
  Local server: {a['local']}
  Integrations: {', '.join(a['integrations'])}
  Hard rules:   {a['hard_rules'] or '(none)'}
  Language:     {a['language']}
""")

def main():
    print(f"\n{BOLD}{'='*52}")
    print(f"   ag_ai v5 -- Project Wizard")
    print(f"{'='*52}{RESET}")

    project_path = get_project_path()
    print(f"\n  {YELLOW}Project:{RESET} {project_path}")

    answers = collect_answers()
    print_summary(answers)

    if not ask_yes("Everything correct? Start generating", default=True):
        print(f"\n  {YELLOW}Cancelled.{RESET}"); sys.exit(0)

    overwrite_all = False
    existing = [f for f in ["CLAUDE.md","AGENTS.md","PRD.md"] if (project_path/f).exists()]
    if existing:
        overwrite_all = ask_yes(f"Found {len(existing)} existing file(s). Overwrite all?", default=True)

    install_all(project_path, answers, overwrite_all)

    # Final summary
    tool = answers["ai_tool"].lower()
    print(f"\n{BOLD}{'='*52}")
    print(f"  Done! {answers['name']} is ready.")
    print(f"{'='*52}{RESET}\n")
    print(f"  Generated:")
    print(f"    - .ai/context/    -- PROJECT, STACK, RULES, constitution")
    print(f"    - AGENTS.md, CLAUDE.md, PRD.md")
    print(f"    - .claude/settings.json -- hooks for {answers['backend']}")
    print(f"    - .claude/skills/       -- {', '.join(select_skills(answers))}")
    print(f"    - .claude/commands/     -- /learn /verify /security /checkpoint /evolve")
    print(f"    - .claude/security/     -- security-audit.js")
    print(f"    - session-observer.js   -- background learning\n")
    if "claude" in tool or "both" in tool:
        print(f"  Claude Code:")
        print(f"    cd \"{project_path}\" && claude")
        print(f"    /speckit.specify I want to build [feature]\n")
    if "open" in tool or "both" in tool:
        print(f"  OpenCode:")
        print(f"    cd \"{project_path}\" && opencode")
        print(f"    use orchestrator agent to manage: [task]\n")
    print(f"  After each session:")
    print(f"    /learn -> /instinct-status -> /verify -> /security\n")

if __name__ == "__main__":
    main()
