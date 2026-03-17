# 📖 ag_ai — دليل التنصيب والاستخدام

> كل اللي محتاجه في ملف واحد

---

## 1️⃣ التنصيب — أول مرة على الجهاز

Clone في **أي مكان على أي drive**:
```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git D:\tools\ag_ai
git clone https://github.com/gebrilae-eng/ag_ai.git F:\ag_ai
git clone https://github.com/gebrilae-eng/ag_ai.git C:\Users\AG\ag_ai
```

يعمل مرة واحدة بس على كل جهاز.

---

## 2️⃣ تثبيت في مشروع

```cmd
D:\tools\ag_ai\install.bat C:\laragon\www\my-project
F:\ag_ai\install.bat D:\projects\new-app
F:\ag_ai\install.bat .
```

- المسار مش مرتبط بـ drive معين — أي مكان يشتغل
- النقطة `.` تثبّت في الـ folder الحالي
- الـ `install.bat` يشتغل من أي مكان تحطه فيه

### الـ Installer هيسألك سؤالين:

**السؤال الأول — بتستخدم إيه؟**
```
  1) Claude Code    slash commands: /tdd  /security  /speckit.*
  2) OpenCode       YAML agents: use orchestrator agent to ...
  3) Both           Claude Code + OpenCode
  0) All
```

**السؤال التاني — إيه المكونات؟**
```
  1) Core Agents    orchestrator, coder, db-agent, api-agent
  2) ECC Agents     architect, tdd-guide, security-reviewer, code-reviewer
  3) Sub-Agents     sql-helper, telegram-bot, n8n-workflow, debugger
  4) PHP Rules      security + patterns + testing
  5) Common Rules   security + coding-style
  6) Spec Kit       speckit.* commands + templates
  0) All
```

اختار بأرقام مفصولة بـ space:
```
0          ← كل حاجة (الأسهل)
1 2 3      ← Core + ECC + Sub-Agents بس
1 4 6      ← Core + PHP Rules + Spec Kit بس
```

---

## 3️⃣ تحديث ag_ai

```cmd
D:\tools\ag_ai\install.bat C:\path\to\your-project
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
يسألك 12 سؤال ويملي كل الملفات تلقائياً:
- `.ai/context/PROJECT.md`
- `.ai/context/STACK.md`
- `.ai/context/RULES.md`
- `CLAUDE.md`
- `.ai/spec/memory/constitution.md`

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

### Quick Commands
```
/build-fix          ← إصلاح build errors
/refactor-clean     ← تنظيف الكود
/learn              ← استخلاص patterns من الجلسة
/checkpoint         ← حفظ حالة الجلسة
/update-docs        ← تحديث الـ docs
```

---

## 5️⃣ الاستخدام مع OpenCode

### افتح المشروع
```cmd
cd C:\path\to\your-project
opencode
```

### أول مرة — Onboarding
```
Read CLAUDE.md then ask me the onboarding questions to fill the context files
```

### تفعيل الـ Agents

**من داخل الـ TUI:**
```
use orchestrator agent to help me build [feature]
use tdd-guide agent to implement [function]
use security-reviewer agent to audit [file path]
use sql-helper agent to write a query for [description]
use debugger agent to investigate [bug description]
use architect agent to design [system/feature]
```

**من command line:**
```cmd
opencode --agent orchestrator "build a daily sales Telegram report"
opencode --agent tdd-guide "implement calculateProfit function"
opencode --agent security-reviewer "audit controllers/SaleController.php"
opencode run --agent coder "add pagination to the drugs list API"
```

---

## 6️⃣ الـ Agents المتاحة

### Claude Code — `.ai/agents/`
| Agent | الـ Command | الدور |
|-------|------------|-------|
| orchestrator | تلقائي | يوزّع المهام |
| coder | تلقائي | كتابة الكود |
| db-agent | تلقائي | قواعد البيانات |
| api-agent | تلقائي | API و integrations |
| spec-workflow | `/speckit.*` | Spec-Driven workflow |
| ecc/architect | تلقائي | تصميم النظام (Opus) |
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

### Sub-Agents — `.ai/sub-agents/`
| Agent | الدور |
|-------|-------|
| sql-helper | MySQL query generation |
| telegram-bot | HTML formatting + splitting |
| n8n-workflow | n8n automation patterns |
| debugger | systematic bug investigation |
| test-writer | PHPUnit / Jest test writing |

---

## 7️⃣ Slash Commands — مرجع كامل (Claude Code)

### Spec Kit
| Command | الوظيفة |
|---------|---------|
| `/speckit.constitution` | مبادئ المشروع (مرة واحدة) |
| `/speckit.specify` | تعريف الـ feature |
| `/speckit.clarify` | توضيح المتطلبات |
| `/speckit.plan` | خطة التنفيذ التقنية |
| `/speckit.tasks` | تقسيم لـ tasks منظمة |
| `/speckit.implement` | تنفيذ الـ tasks بالترتيب |
| `/speckit.analyze` | فحص التناسق |

### ECC
| Command | الوظيفة |
|---------|---------|
| `/tdd` | TDD — اكتب الـ test أولاً |
| `/verify` | فحص شامل |
| `/quality-gate` | فحص سريع |
| `/code-review` | مراجعة الكود |
| `/security` | OWASP audit |
| `/build-fix` | إصلاح build errors |
| `/refactor-clean` | تنظيف الكود |
| `/learn` | استخلاص patterns |
| `/checkpoint` | حفظ الجلسة |
| `/update-docs` | تحديث الـ docs |

### Onboarding
| Command | الوظيفة |
|---------|---------|
| `/onboard` | wizard يملي كل الملفات |

---

## 8️⃣ بنية الملفات بعد التثبيت

```
your-project/
├── CLAUDE.md
├── specs/
├── .claude/commands/      ← Claude Code commands
├── .opencode/agents/      ← OpenCode YAML agents
└── .ai/
    ├── agents/
    │   ├── orchestrator.md
    │   ├── coder.md
    │   ├── db-agent.md
    │   ├── api-agent.md
    │   ├── spec-workflow.md
    │   └── ecc/           ← 8 ECC agents
    ├── sub-agents/        ← 5 specialists
    ├── rules/php/         ← security, patterns, testing
    ├── rules/common/      ← security, coding-style
    ├── context/           ← PROJECT.md, STACK.md, RULES.md
    └── spec/              ← commands + templates + memory
```

---

## 9️⃣ أمثلة عملية

### مثال — Feature جديدة (Claude Code)
```
/speckit.specify  أريد تقرير يومي على Telegram للمبيعات والأرباح
/speckit.plan     PHP + MySQL, n8n workflow, Telegram HTML
/speckit.tasks
/tdd
/verify
```

### مثال — Feature جديدة (OpenCode)
```
use orchestrator agent to build a daily Telegram sales report
using PHP, MySQL, and n8n workflow
```

### مثال — إصلاح bug
```
/build-fix                                    ← Claude Code
use debugger agent — [وصف المشكلة]            ← OpenCode
```

### مثال — Security audit
```
/security                                     ← Claude Code
use security-reviewer agent to audit controllers/
```

---

## 🔗 روابط

- **الريبو:** https://github.com/gebrilae-eng/ag_ai
- **Spec Kit:** https://github.com/github/spec-kit
- **ECC:** https://github.com/affaan-m/everything-claude-code
- **Claude Code:** https://www.anthropic.com/claude-code
- **OpenCode:** https://opencode.ai
