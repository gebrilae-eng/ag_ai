# 📖 ag_ai — دليل التنصيب والاستخدام

> كل اللي محتاجه في ملف واحد — من التنصيب لأول سطر كود

---

## 1️⃣ التنصيب — أول مرة على الجهاز

```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git C:\temp\ag_ai
```

يعمل مرة واحدة بس على كل جهاز.

---

## 2️⃣ تثبيت في مشروع

```cmd
C:\temp\ag_ai\install.bat C:\path\to\your-project
```

**أمثلة:**
```cmd
C:\temp\ag_ai\install.bat C:\laragon\www\my-project
C:\temp\ag_ai\install.bat C:\Users\AG\Desktop\new-app
C:\temp\ag_ai\install.bat .
```

النقطة `.` تثبّت في الـ folder الحالي.
المسار مش مرتبط بـ Laragon — أي مسار على الجهاز يشتغل.

---

## 3️⃣ تحديث ag_ai

```cmd
C:\temp\ag_ai\install.bat C:\path\to\your-project
```

نفس أمر التثبيت — الـ `install.bat` دايماً يعمل `git pull` أولاً.

---

## 4️⃣ الاستخدام مع Claude Code

### افتح المشروع
```cmd
cd C:\path\to\your-project
claude
```

### أول مرة — Onboarding
```
/onboard
```
يسألك 12 سؤال ويملي كل الملفات تلقائياً.

### Workflow — Feature جديدة
```
/speckit.specify    ← وصّف إيه اللي عاوز تبنيه
/speckit.clarify    ← وضّح أي غموض (اختياري)
/speckit.plan       ← حدد الـ tech stack
/speckit.tasks      ← قسّم لـ tasks
/tdd                ← implement test-first
/verify             ← quality gate
/code-review        ← review قبل الـ commit
/security           ← security audit
```

---

## 5️⃣ الاستخدام مع OpenCode

### افتح المشروع
```cmd
cd C:\path\to\your-project
opencode
```

### أول مرة — Onboarding
OpenCode مفيش فيه slash commands — اكتب مباشرة:
```
Read CLAUDE.md then ask me the onboarding questions to fill the context files
```

### تفعيل الـ Agents في OpenCode

**الطريقة الأولى — من داخل الـ TUI:**
```
use orchestrator agent to help me build [feature description]
use tdd-guide agent to implement [function name]
use security-reviewer agent to audit [file path]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug description]
```

**الطريقة التانية — من command line مباشرة:**
```cmd
opencode --agent orchestrator "build a daily sales Telegram report"
opencode --agent tdd-guide "implement calculateProfit function"
opencode --agent security-reviewer "audit controllers/SaleController.php"
opencode --agent sql-helper "top 10 selling drugs this month"
opencode --agent debugger "Telegram bot stops sending after 5 messages"
```

**الطريقة التالتة — run بدون TUI:**
```cmd
opencode run --agent coder "add pagination to the drugs list API"
```

---

## 6️⃣ الـ Agents المتاحة

### Claude Code — `.ai/agents/`
| Agent | الاستدعاء | الدور |
|-------|-----------|-------|
| orchestrator | تلقائي عبر CLAUDE.md | يوزّع المهام |
| coder | تلقائي | كتابة الكود |
| db-agent | تلقائي | قواعد البيانات |
| api-agent | تلقائي | API والـ integrations |
| spec-workflow | `/speckit.*` | Spec-Driven workflow |
| ecc/architect | تلقائي | تصميم النظام |
| ecc/tdd-guide | `/tdd` | test-first |
| ecc/security-reviewer | `/security` | OWASP audit |
| ecc/code-reviewer | `/code-review` | مراجعة الكود |
| ecc/refactor-cleaner | `/refactor-clean` | تنظيف الكود |
| ecc/build-error-resolver | `/build-fix` | إصلاح build errors |
| ecc/database-reviewer | تلقائي | مراجعة DB |
| ecc/doc-updater | `/update-docs` | تحديث docs |

### OpenCode — `.opencode/agents/`
| Agent | الاستدعاء | الدور |
|-------|-----------|-------|
| orchestrator | `use orchestrator agent` | يوزّع المهام |
| architect | `use architect agent` | تصميم النظام (Opus) |
| coder | `use coder agent` | كتابة الكود |
| db-agent | `use db-agent agent` | قواعد البيانات |
| tdd-guide | `use tdd-guide agent` | test-first |
| security-reviewer | `use security-reviewer agent` | OWASP audit |
| sql-helper | `use sql-helper agent` | SQL queries |
| telegram-bot | `use telegram-bot agent` | Telegram |
| n8n-workflow | `use n8n-workflow agent` | n8n automation |
| debugger | `use debugger agent` | debugging |

### Sub-Agents المشتركة — `.ai/sub-agents/`
| Agent | الدور |
|-------|-------|
| sql-helper | توليد MySQL queries |
| telegram-bot | HTML formatting + splitting |
| n8n-workflow | n8n automation patterns |
| debugger | تحقيق منهجي في الـ bugs |
| test-writer | كتابة PHPUnit/Jest tests |

---

## 7️⃣ Slash Commands — مرجع كامل (Claude Code)

### Spec Kit — التخطيط
| Command | الوظيفة |
|---------|---------|
| `/speckit.constitution` | مبادئ المشروع (مرة واحدة) |
| `/speckit.specify` | تعريف الـ feature |
| `/speckit.clarify` | توضيح المتطلبات |
| `/speckit.plan` | خطة التنفيذ التقنية |
| `/speckit.tasks` | تقسيم لـ tasks منظمة |
| `/speckit.implement` | تنفيذ الـ tasks بالترتيب |
| `/speckit.analyze` | فحص التناسق |

### ECC — جودة الكود
| Command | الوظيفة |
|---------|---------|
| `/tdd` | TDD — اكتب الـ test أولاً |
| `/verify` | فحص شامل: build + lint + tests |
| `/quality-gate` | فحص سريع |
| `/code-review` | مراجعة الكود |
| `/security` | OWASP security audit |
| `/build-fix` | تشخيص وإصلاح build errors |
| `/refactor-clean` | تنظيف بدون تغيير الـ behavior |
| `/learn` | استخلاص patterns من الجلسة |
| `/checkpoint` | حفظ حالة الجلسة |
| `/update-docs` | تحديث الـ documentation |

### Onboarding
| Command | الوظيفة |
|---------|---------|
| `/onboard` | wizard يملي كل الملفات |

---

## 8️⃣ بنية الملفات بعد التثبيت

```
your-project/
├── CLAUDE.md                        ← entry point للـ AI
├── specs/                           ← specs الـ features
├── .claude/
│   └── commands/                    ← Claude Code slash commands
│       ├── onboard.md
│       ├── tdd.md
│       ├── verify.md
│       ├── security.md
│       └── ...
├── .opencode/
│   └── agents/                      ← OpenCode YAML agents
│       ├── orchestrator.yml
│       ├── architect.yml
│       ├── coder.yml
│       ├── db-agent.yml
│       ├── tdd-guide.yml
│       ├── security-reviewer.yml
│       ├── sql-helper.yml
│       ├── telegram-bot.yml
│       ├── n8n-workflow.yml
│       └── debugger.yml
└── .ai/
    ├── agents/
    │   ├── orchestrator.md
    │   ├── coder.md
    │   ├── db-agent.md
    │   ├── api-agent.md
    │   ├── spec-workflow.md
    │   └── ecc/                     ← 8 ECC agents
    ├── sub-agents/                  ← 5 specialists
    ├── rules/
    │   ├── php/                     ← security, patterns, testing
    │   └── common/                  ← security, coding-style
    ├── context/
    │   ├── PROJECT.md               ← يتملى بـ /onboard
    │   ├── STACK.md                 ← يتملى بـ /onboard
    │   └── RULES.md                 ← يتملى بـ /onboard
    └── spec/
        ├── commands/                ← /speckit.* commands
        ├── templates/               ← spec/plan/tasks/constitution
        └── memory/
            └── constitution.md      ← يتملى بـ /onboard
```

---

## 9️⃣ نصائح عملية

**افتح Claude Code أو OpenCode من داخل المشروع دايماً:**
```cmd
cd C:\path\to\your-project
claude        ← Claude Code
opencode      ← OpenCode
```

**لو عندك مشروع موجود وعاوز تبدأ spec-first:**
```
/speckit.specify أريد إضافة [وصف الـ feature]
```

**لو عاوز تقفز للكود مباشرة:**
```
/tdd [وصف الـ function]
```

**لو الـ build بيفشل:**
```
/build-fix
```

**لو عاوز security review على ملف:**
```
/security path/to/file.php
```

**في OpenCode — لو مش عارف تبدأ:**
```
use orchestrator agent — I want to [describe what you need]
```

---

## 🔟 أمثلة عملية

### مثال ١ — Feature جديدة (Claude Code)
```
/speckit.specify أريد تقرير يومي على Telegram يعرض المبيعات والأرباح
/speckit.plan PHP + MySQL, n8n workflow, Telegram HTML
/speckit.tasks
/tdd
/verify
```

### مثال ٢ — Feature جديدة (OpenCode)
```
use orchestrator agent to help me build a daily Telegram sales report
using PHP, MySQL, and n8n workflow
```

### مثال ٣ — إصلاح bug
```
/build-fix                               ← Claude Code
use debugger agent — [وصف المشكلة]      ← OpenCode
```

### مثال ٤ — Security audit
```
/security                                ← Claude Code
use security-reviewer agent to audit the entire controllers/ folder
```

---

## 🔗 روابط مفيدة

- **الريبو:** https://github.com/gebrilae-eng/ag_ai
- **Spec Kit:** https://github.com/github/spec-kit
- **ECC:** https://github.com/affaan-m/everything-claude-code
- **Claude Code:** https://www.anthropic.com/claude-code
- **OpenCode:** https://opencode.ai
