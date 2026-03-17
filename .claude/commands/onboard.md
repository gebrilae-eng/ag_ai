---
description: Interactive project onboarding — ask questions and auto-fill all context files
---

# /onboard — Project Setup Wizard

You are helping the developer set up their project's AI infrastructure.
Ask the questions below ONE SECTION AT A TIME, wait for answers, then fill all files.

---

## Step 1: Project Basics

Ask these questions together:

```
🚀 Let's set up your AI infrastructure!

1. What is your project name?
2. Describe your project in 1-2 sentences (what does it do? who uses it?)
3. What type is it?
   A) Web App    B) REST API    C) Automation/Bot    D) Library    E) Other
4. What is the current status?
   A) Just planning    B) In development    C) Already in production
```

---

## Step 2: Tech Stack

After getting project basics, ask:

```
🛠️ Now let's map your tech stack:

5. Backend language & framework?
   Examples: PHP + Laravel, PHP vanilla, Node.js + Express, Python + FastAPI
6. Database engine and name?
   Examples: MySQL 8 / pharmacy_db, PostgreSQL / myapp_db
7. Frontend? (or API-only?)
   Examples: Blade templates, React, Vue, HTML/JS, API only
8. Integrations? (select all that apply)
   A) Telegram bot    B) n8n workflows    C) WhatsApp    D) Email    E) None
9. AI tools you use?
   A) Claude Code    B) OpenCode    C) Cursor    D) Ollama local    E) Other
10. Local dev environment?
    Examples: Laragon on Windows, XAMPP, Docker, WSL
```

---

## Step 3: Agents & Rules

After getting stack info, ask:

```
🤖 Let's configure your agents:

11. Any domain-specific terminology I should know?
    (e.g., "we call customers 'members'", "invoices are called 'orders'")
12. Any critical business rules?
    (e.g., "never delete records, only soft-delete", "all amounts in EGP")
13. What are your DB column naming conventions? (or leave blank for defaults)
14. Any security requirements specific to your project?
    (e.g., "HIPAA compliant", "PCI-DSS for payments")
15. Preferred language for comments/docs? Arabic / English / Both
```

---

## After All Answers — Auto-Fill Files

Once you have all answers, do the following WITHOUT asking again:

### Fill `.ai/context/PROJECT.md`
Replace all placeholder text with real project details from answers 1-4.

### Fill `.ai/context/STACK.md`
Replace all placeholder text with real stack from answers 5-10.
Add actual env variable names if mentioned.

### Update `.ai/context/RULES.md`
Add domain-specific rules from answers 11-14.
Add language preference from answer 15.

### Update `CLAUDE.md` bottom section
Replace "Pharmacy Project Notes" with actual project notes.

### Generate `.ai/spec/memory/constitution.md`
Create a project constitution with principles derived from all answers.
Use the template at `.ai/spec/templates/constitution-template.md`.

---

## Completion Message

After filling all files, show:

```
✅ AI Infrastructure configured for [PROJECT NAME]!

Files updated:
  📄 .ai/context/PROJECT.md
  📄 .ai/context/STACK.md
  📄 .ai/context/RULES.md
  📄 CLAUDE.md
  📄 .ai/spec/memory/constitution.md

Next step — start your first feature:
  /speckit.specify [describe what you want to build]
```
