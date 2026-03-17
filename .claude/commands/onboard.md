---
description: Interactive project onboarding wizard — asks about your project and auto-fills all context files.
---

# /onboard — Project Setup Wizard

You are setting up the AI infrastructure for a new project.
Ask ALL questions below in ONE message, then wait for answers, then fill all files silently.

---

## Ask These Questions (all at once)

```
🚀 Welcome to ag_ai! Let's configure your project.
Answer the questions below and I'll set everything up automatically.

── PROJECT ──────────────────────────────────────
1. Project name?
2. What does it do? (1-2 sentences)
3. Type: A) Web App  B) REST API  C) Bot/Automation  D) CLI Tool  E) Other
4. Status: A) New project  B) In development  C) Production

── TECH STACK ───────────────────────────────────
5. Backend language + framework?
   Examples: PHP vanilla, PHP + Laravel, Node.js + Express, Python + FastAPI
6. Database engine + name?
   Examples: MySQL 8 + my_db, PostgreSQL + app_db, SQLite, None
7. Frontend?
   Examples: HTML/CSS/JS, React, Vue, Blade, API only
8. Integrations? (all that apply)
   A) Telegram bot  B) n8n workflows  C) WhatsApp  D) Email  E) REST APIs  F) None
9. Local dev setup?
   Examples: Laragon, XAMPP, Docker, WSL, MAMP

── CONVENTIONS ──────────────────────────────────
10. Any domain-specific terms I should know?
    Examples: "we call customers members", "invoices are called orders"
11. Any hard business rules?
    Examples: "never hard-delete records", "all prices in EGP", "Arabic UI"
12. Preferred language for comments and docs?
    A) English  B) Arabic  C) Both
```

---

## After Getting Answers — Do This Silently

### 1. Fill `.ai/context/PROJECT.md`
Replace all placeholder text with real answers from questions 1-4.
Remove all template comments and placeholder sections.

### 2. Fill `.ai/context/STACK.md`
Replace all placeholder text with real answers from questions 5-9.
Add actual env variable names based on the stack mentioned.
Remove unused sections entirely.

### 3. Update `.ai/context/RULES.md`
Add domain rules from questions 10-11 under a new section:
```markdown
## Project-Specific Rules
- [rule from answer 10]
- [rule from answer 11]
```
Add language preference from question 12 at the bottom.

### 4. Update `CLAUDE.md` — bottom section
Replace the generic "Core Rules" notes with project-specific ones derived from answers.

### 5. Generate `.ai/spec/memory/constitution.md`
Use `.ai/spec/templates/constitution-template.md` as base.
Derive 3-5 principles from the answers. Examples:
- Data integrity principle (from hard-delete rule)
- Language principle (from Arabic/English preference)
- Security principle (based on stack)
- Performance principle (based on project type)

Fill all placeholders. Remove all template comments.

---

## Completion — Show This Summary

```
✅ ag_ai configured for [PROJECT NAME]!

Files updated:
  📄 .ai/context/PROJECT.md    — project overview
  📄 .ai/context/STACK.md      — tech stack
  📄 .ai/context/RULES.md      — coding rules
  📄 CLAUDE.md                 — agent entry point
  📄 .ai/spec/memory/constitution.md — project principles

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next — pick your workflow:

  New feature (spec-first):
  → /speckit.specify I want to build [describe feature]

  Jump straight to coding:
  → Just describe what you need

  Establish project principles first:
  → /speckit.constitution
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
