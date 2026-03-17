# 📖 ag_ai — دليل التنصيب والاستخدام

> كل اللي محتاجه في ملف واحد

---

## الخطوات لكل مشروع جديد

```
1. install  ← ثبّت الـ agents والـ commands
2. wizard   ← امل الملفات بمعلومات مشروعك
3. opencode / claude ← ابدأ الشغل
```

---

## 1️⃣ أول مرة على الجهاز
```cmd
git clone https://github.com/gebrilae-eng/ag_ai.git F:\ag_ai
```

---

## 2️⃣ مشروع جديد — خطوتين بس
```cmd
F:\ag_ai\install.bat  D:\my-project
F:\ag_ai\wizard.bat   D:\my-project
```

أو أمر واحد:
```cmd
F:\ag_ai\new-project.bat
```

---

## 3️⃣ ابدأ الشغل
```cmd
cd D:\my-project
opencode        ← OpenCode
claude          ← Claude Code
```

---

## 4️⃣ الـ Workflow الكامل في OpenCode

### أول مرة في مشروع جديد
```
use orchestrator agent to manage the project and set up agents
```
بيراجع المشروع ويضبط الـ AGENTS.md تلقائياً.

### Feature جديدة — 4 خطوات
```
# 1. اكتب الـ spec (إيه اللي عاوز تبنيه)
use spec-workflow agent to specify: I want to add [feature description]

# 2. خطة التنفيذ
use orchestrator agent to plan and manage adding [feature]

# 3. نفّذ كل task
use [agent] agent to implement [specific task]

# 4. راجع الشغل
use code-reviewer agent to review the changes
use security-reviewer agent to audit the implementation
```

### مثال حقيقي — إضافة n8n
```
use spec-workflow agent to specify: I want to add n8n automation
use orchestrator agent to plan and manage adding n8n
use architect agent to design the PHP to n8n integration
use api-agent agent to implement the webhook client
use n8n-workflow agent to design the first workflow
use tdd-guide agent to write tests for the integration
use security-reviewer agent to audit the n8n integration
```

---

## 5️⃣ الـ Workflow الكامل في Claude Code

### Feature جديدة
```
/speckit.specify  I want to add [feature]
/speckit.plan     tech stack: [your stack]
/speckit.tasks
/speckit.implement
/verify
/security
```

---

## 6️⃣ الـ Specs — إزاي تستخدمها وتحدّثها

### بنية الـ spec
```
specs/
└── feature-name/
    ├── spec.md        ← WHAT (requirements, user stories)
    ├── plan.md        ← HOW (tech decisions, phases)
    ├── data-model.md  ← DB schema
    ├── tasks.md       ← ordered task list
    └── discovery.md   ← research findings (optional)
```

### إنشاء spec جديدة
```
use spec-workflow agent to specify: I want to add [feature]
```

### تحويل spec لـ plan
```
use orchestrator agent to plan and manage adding [feature]
```

### تحديث spec موجودة
```
use spec-workflow agent to update specs/feature-name/spec.md
[describe what changed]
```

### مراجعة progress
```
use spec-workflow agent to review progress on specs/feature-name/
```

---

## 7️⃣ الـ Agents — كل agent ومتى تستخدمه

### OpenCode — استدعاء مباشر بالاسم
```
use orchestrator agent to [complex multi-step task]
use spec-workflow agent to specify: [feature]
use architect agent to design [system or feature]
use coder agent to implement [function or file]
use db-agent agent to design schema for [entity]
use api-agent agent to implement [endpoint]
use tdd-guide agent to write tests for [function]
use security-reviewer agent to audit [file or folder]
use code-reviewer agent to review [file or change]
use database-reviewer agent to review [schema or query]
use refactor-cleaner agent to refactor [file]
use build-error-resolver agent to fix [error message]
use doc-updater agent to update docs for [change]
use sql-helper agent to write a query for [description]
use telegram-bot agent to format [message or feature]
use n8n-workflow agent to design workflow for [task]
use debugger agent to investigate [bug or issue]
use test-writer agent to write tests for [function]
```

### Claude Code — Slash Commands
| Command | متى |
|---------|-----|
| `/speckit.specify` | feature جديدة |
| `/speckit.plan` | بعد الـ spec |
| `/speckit.tasks` | بعد الـ plan |
| `/speckit.implement` | تنفيذ |
| `/tdd` | TDD |
| `/verify` | quality check |
| `/security` | audit |
| `/code-review` | مراجعة |
| `/build-fix` | إصلاح errors |
| `/refactor-clean` | تنظيف |
| `/learn` | استخلاص patterns |
| `/checkpoint` | حفظ الجلسة |

---

## 8️⃣ الـ Scripts

| Script | الوظيفة |
|--------|---------|
| `install.bat / .ps1` | تثبيت في مشروع |
| `wizard.bat / .ps1` | ملي الملفات |
| `update.bat / .ps1` | تحديث ag_ai |
| `new-project.bat` | كل حاجة في أمر واحد |

---

## 9️⃣ تحديث ag_ai
```cmd
F:\ag_ai\update.bat      (CMD)
F:\ag_ai\update.ps1      (PowerShell)
```

---

## 🔗 روابط
- **الريبو:** https://github.com/gebrilae-eng/ag_ai
- **Claude Code:** https://www.anthropic.com/claude-code
- **OpenCode:** https://opencode.ai
- **Spec Kit:** https://github.com/github/spec-kit
- **ECC:** https://github.com/affaan-m/everything-claude-code
