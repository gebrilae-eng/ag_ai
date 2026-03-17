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

**مثال:**
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

### أول مرة في المشروع — Onboarding
```
/onboard
```
يسألك 12 سؤال ويملي كل الملفات تلقائياً:
- `.ai/context/PROJECT.md`
- `.ai/context/STACK.md`
- `.ai/context/RULES.md`
- `CLAUDE.md`
- `.ai/spec/memory/constitution.md`

---

## 5️⃣ الاستخدام مع OpenCode

### افتح المشروع
```cmd
cd C:\path\to\your-project
opencode
```

### أول مرة في المشروع — Onboarding
OpenCode مفيش فيه slash commands — اكتب مباشرة:
```
Read CLAUDE.md then ask me the onboarding questions to fill the context files
```

### تشغيل أمر مباشر بدون TUI
```cmd
opencode run "Read CLAUDE.md and help me build [feature]"
```

---

## 6️⃣ Workflow — Feature جديدة

### الطريقة الكاملة (Spec-First)
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

### الطريقة السريعة
```
/tdd                ← ابدأ مباشرة بـ TDD
/build-fix          ← صلّح build errors
/refactor-clean     ← نظّف الكود
/quality-gate       ← فحص سريع
```

### أول مرة في مشروع جديد
```
/speckit.constitution  ← اعمل مبادئ المشروع (مرة واحدة)
```

---

## 7️⃣ Slash Commands — مرجع كامل

### Spec Kit — التخطيط
| Command | الوظيفة |
|---------|---------|
| `/speckit.constitution` | مبادئ المشروع |
| `/speckit.specify` | تعريف الـ feature |
| `/speckit.clarify` | توضيح المتطلبات |
| `/speckit.plan` | خطة التنفيذ التقنية |
| `/speckit.tasks` | تقسيم لـ tasks |
| `/speckit.implement` | تنفيذ الـ tasks |
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

## 8️⃣ الـ Agents المتاحة

### Agents رئيسية
| الملف | الدور |
|-------|-------|
| `orchestrator.md` | يوزّع المهام على الـ agents |
| `coder.md` | يكتب الكود |
| `db-agent.md` | متخصص قواعد البيانات |
| `api-agent.md` | API والـ integrations |
| `spec-workflow.md` | يربط Spec Kit بالـ agents |

### ECC Agents
| الملف | الدور |
|-------|-------|
| `ecc/architect.md` | تصميم النظام (يشتغل على Opus) |
| `ecc/tdd-guide.md` | test-first development |
| `ecc/security-reviewer.md` | OWASP Top 10 audit |
| `ecc/code-reviewer.md` | مراجعة جودة الكود |
| `ecc/refactor-cleaner.md` | تنظيف الكود |
| `ecc/build-error-resolver.md` | إصلاح build errors |
| `ecc/database-reviewer.md` | مراجعة الـ DB |
| `ecc/doc-updater.md` | تحديث الـ docs |

### Sub-Agents
| الملف | الدور |
|-------|-------|
| `sql-helper.md` | توليد SQL queries |
| `telegram-bot.md` | Telegram HTML formatting |
| `n8n-workflow.md` | n8n automation |
| `debugger.md` | تحقيق منهجي في الـ bugs |
| `test-writer.md` | كتابة الـ tests |

---

## 9️⃣ بنية الملفات بعد التثبيت

```
your-project/
├── CLAUDE.md                    ← entry point للـ AI
├── specs/                       ← specs الـ features
└── .ai/
    ├── agents/
    │   ├── orchestrator.md
    │   ├── coder.md
    │   ├── db-agent.md
    │   ├── api-agent.md
    │   ├── spec-workflow.md
    │   └── ecc/                 ← 8 ECC agents
    ├── sub-agents/              ← 5 specialists
    ├── rules/
    │   ├── php/                 ← security, patterns, testing
    │   └── common/              ← security, coding-style
    ├── context/
    │   ├── PROJECT.md           ← يتملى بـ /onboard
    │   ├── STACK.md             ← يتملى بـ /onboard
    │   └── RULES.md             ← يتملى بـ /onboard
    └── spec/
        ├── commands/            ← /speckit.* commands
        ├── templates/           ← spec/plan/tasks/constitution
        └── memory/
            └── constitution.md  ← يتملى بـ /onboard
```

---

## 🔟 نصائح عملية

**افتح Claude Code من داخل المشروع دايماً:**
```cmd
cd C:\path\to\your-project
claude
```

**لو عندك مشروع موجود وعاوز تبدأ spec-first:**
```
/speckit.specify أريد إضافة [وصف الـ feature]
```

**لو عاوز تقفز للكود مباشرة:**
```
/tdd [وصف الـ function اللي عاوز تعملها]
```

**لو الـ build بيفشل:**
```
/build-fix
```

**لو عاوز تعمل security review على ملف:**
```
/security [path/to/file.php]
```

---

## 🔗 روابط مفيدة

- **الريبو:** https://github.com/gebrilae-eng/ag_ai
- **Spec Kit:** https://github.com/github/spec-kit
- **ECC:** https://github.com/affaan-m/everything-claude-code
- **Claude Code:** https://www.anthropic.com/claude-code
- **OpenCode:** https://opencode.ai
