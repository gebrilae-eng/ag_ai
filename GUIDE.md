# 📖 ag_ai — دليل التنصيب والاستخدام

> كل اللي محتاجه في ملف واحد

---

## الخطوات الـ 3 لأي مشروع جديد

```
1. install  ← ثبّت الـ agents والـ commands في المشروع
2. wizard   ← أجاوب على أسئلة عن المشروع وهيملي الملفات
3. claude / opencode ← ابدأ الشغل
```

---

## 1️⃣ أول مرة على الجهاز — Clone

في **أي مكان على أي drive**:
```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git D:\tools\ag_ai
git clone https://github.com/gebrilae-eng/ag_ai.git F:\ag_ai
git clone https://github.com/gebrilae-eng/ag_ai.git C:\Users\AG\ag_ai
```

---

## 2️⃣ تثبيت في مشروع

```cmd
D:\tools\ag_ai\install.bat  C:\laragon\www\my-project
F:\ag_ai\install.bat        D:\projects\new-app
F:\ag_ai\install.bat        .
```

النقطة `.` = الـ folder الحالي.
الـ `install.bat` بيسألك سؤالين:
- بتستخدم Claude Code / OpenCode / الاتنين؟
- إيه المكونات اللي تثبّتها؟

---

## 3️⃣ Wizard — امل الملفات قبل ما تبدأ

بعد الـ install، شغّل الـ wizard على نفس المشروع:

```cmd
D:\tools\ag_ai\wizard.bat  C:\laragon\www\my-project
F:\ag_ai\wizard.bat        D:\projects\new-app
```

أو من PowerShell:
```powershell
F:\ag_ai\wizard.ps1 -ProjectPath D:\projects\new-app
```

### الـ Wizard هيسألك 4 sections:

```
1 / 4  Project Info
  → Project name
  → What does it do?
  → Type (web / api / bot / automation)
  → Status (new / development / production)

2 / 4  Tech Stack
  → Backend (PHP vanilla / Laravel / Node.js / Python)
  → Database (MySQL 8 + db_name / PostgreSQL / none)
  → Frontend (HTML/JS / React / Blade / API only)
  → Local dev (Laragon / XAMPP / Docker)
  → Integrations (Telegram / n8n / REST APIs / ...)

3 / 4  Rules & Conventions
  → Hard business rules (never delete records / ...)
  → Naming conventions
  → Docs language (English / Arabic / Both)

4 / 4  AI Tool
  → claude / opencode / both
```

### الملفات اللي بيكتبها تلقائياً:
```
.ai/context/PROJECT.md              ← وصف المشروع
.ai/context/STACK.md                ← الـ tech stack
.ai/context/RULES.md                ← قواعد الكود
CLAUDE.md                           ← entry point للـ AI
.ai/spec/memory/constitution.md     ← مبادئ المشروع
.ai/context/wizard-answers.json     ← إجاباتك (للـ re-run)
```

---

## 4️⃣ ابدأ الشغل

### Claude Code
```cmd
cd C:\path\to\your-project
claude
```
بعدين ابدأ أي feature:
```
/speckit.specify  I want to build [feature description]
```

### OpenCode
```cmd
cd C:\path\to\your-project
opencode
```
بعدين:
```
use orchestrator agent to help me build [feature description]
```

---

## 5️⃣ تحديث ag_ai

```cmd
F:\ag_ai\update.bat     ← CMD
F:\ag_ai\update.ps1     ← PowerShell
```

---

## 6️⃣ Workflow — Feature جديدة

### Claude Code
```
/speckit.specify    ← وصّف إيه اللي عاوز تبنيه
/speckit.clarify    ← وضّح أي غموض (اختياري)
/speckit.plan       ← حدد الـ tech stack والـ architecture
/speckit.tasks      ← قسّم لـ tasks منظمة
/tdd                ← implement test-first
/verify             ← quality gate
/code-review        ← review قبل الـ commit
/security           ← security audit
```

### OpenCode
```
use orchestrator agent to help me build [feature]
use tdd-guide agent to implement [function]
use security-reviewer agent to audit [file]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug]
```

---

## 7️⃣ الـ Agents المتاحة

### Claude Code — `.ai/agents/`
| Agent | الـ Command | الدور |
|-------|------------|-------|
| orchestrator | تلقائي | يوزّع المهام |
| coder | تلقائي | كتابة الكود |
| db-agent | تلقائي | قواعد البيانات |
| api-agent | تلقائي | API و integrations |
| spec-workflow | `/speckit.*` | Spec-Driven workflow |
| ecc/architect | تلقائي | تصميم النظام |
| ecc/tdd-guide | `/tdd` | test-first |
| ecc/security-reviewer | `/security` | OWASP audit |
| ecc/code-reviewer | `/code-review` | مراجعة الكود |
| ecc/refactor-cleaner | `/refactor-clean` | تنظيف الكود |
| ecc/build-error-resolver | `/build-fix` | إصلاح errors |
| ecc/database-reviewer | تلقائي | مراجعة DB |
| ecc/doc-updater | `/update-docs` | تحديث docs |

### OpenCode — `.opencode/agents/`
| Agent | الاستدعاء | الدور |
|-------|-----------|-------|
| orchestrator | `use orchestrator agent` | يوزّع المهام |
| architect | `use architect agent` | تصميم النظام |
| coder | `use coder agent` | كتابة الكود |
| db-agent | `use db-agent agent` | قواعد البيانات |
| tdd-guide | `use tdd-guide agent` | test-first |
| security-reviewer | `use security-reviewer agent` | OWASP audit |
| sql-helper | `use sql-helper agent` | SQL queries |
| telegram-bot | `use telegram-bot agent` | Telegram |
| n8n-workflow | `use n8n-workflow agent` | n8n automation |
| debugger | `use debugger agent` | debugging |

### Sub-Agents — `.ai/sub-agents/`
| Agent | الدور |
|-------|-------|
| sql-helper | MySQL query generation |
| telegram-bot | HTML formatting + splitting |
| n8n-workflow | n8n automation patterns |
| debugger | systematic bug investigation |
| test-writer | PHPUnit / Jest test writing |

---

## 8️⃣ Slash Commands (Claude Code)

| Command | الوظيفة |
|---------|---------|
| `/speckit.constitution` | مبادئ المشروع |
| `/speckit.specify` | تعريف الـ feature |
| `/speckit.clarify` | توضيح المتطلبات |
| `/speckit.plan` | خطة التنفيذ |
| `/speckit.tasks` | تقسيم لـ tasks |
| `/speckit.implement` | تنفيذ الـ tasks |
| `/tdd` | TDD |
| `/verify` | فحص شامل |
| `/quality-gate` | فحص سريع |
| `/code-review` | مراجعة الكود |
| `/security` | OWASP audit |
| `/build-fix` | إصلاح build errors |
| `/refactor-clean` | تنظيف الكود |
| `/learn` | استخلاص patterns |
| `/checkpoint` | حفظ الجلسة |
| `/update-docs` | تحديث الـ docs |

---

## 9️⃣ ملخص الملفات في الـ Repo

```
ag_ai/
├── install.bat      ← تثبيت (CMD)
├── install.ps1      ← تثبيت (PowerShell)
├── update.bat       ← تحديث ag_ai (CMD)
├── update.ps1       ← تحديث ag_ai (PowerShell)
├── wizard.bat       ← wizard ملي الملفات (CMD)
├── wizard.ps1       ← wizard ملي الملفات (PowerShell)
├── setup_ai.py      ← installer script
├── wizard.py        ← wizard script
├── CLAUDE.md        ← template
├── README.md        ← شرح إنجليزي
├── GUIDE.md         ← دليل عربي (الملف ده)
├── .ai/             ← agents + rules + skills
├── .claude/         ← Claude Code commands
└── .opencode/       ← OpenCode agents
```

---

## 🔗 روابط

- **الريبو:** https://github.com/gebrilae-eng/ag_ai
- **Spec Kit:** https://github.com/github/spec-kit
- **ECC:** https://github.com/affaan-m/everything-claude-code
- **Claude Code:** https://www.anthropic.com/claude-code
- **OpenCode:** https://opencode.ai
