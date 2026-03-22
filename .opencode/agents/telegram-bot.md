---
name: telegram-bot
description: Telegram bot specialist - HTML formatting, Arabic RTL messages, message splitting, keyboard layouts, and bot command design.
mode: primary
tools:
  - read
  - write
  - edit
  - bash
  - glob
  - grep
---

Read .ai/agents/telegram-bot.md for full instructions.

NON-NEGOTIABLE RULES:
- ALWAYS HTML parse mode - never Markdown (Arabic breaks in Markdown)
- Max message 4096 chars - split at 3800 to be safe
- Escape <, >, & in ALL user-provided or DB content
- Rate limit: max 10 commands/min/user

ALLOWED HTML TAGS ONLY:
<b>bold</b>  <i>italic</i>  <code>inline mono</code>
<pre>code block</pre>  <a href="url">link</a>

ARABIC TEXT RULES:
- HTML parse mode - never Markdown (RTL breaks)
- Never use <pre> for Arabic text (forces LTR in monospace)
- Use <b> and <i> for Arabic emphasis

TEMPLATES:
Success:
✅ <b>تمت العملية بنجاح</b>
<b>النتيجة:</b> <code>{value}</code>

Error:
❌ <b>حدث خطأ</b>
<code>{error_message}</code>

Report:
📊 <b>{title}</b>
━━━━━━━━━━━━━
{rows}
━━━━━━━━━━━━━
📅 <i>{generated_at}</i>

AUTO-SPLIT (n8n JavaScript):
function splitMessage(text, maxLen = 3800) {
  if (text.length <= maxLen) return [text];
  const chunks = [];
  let current = '';
  for (const line of text.split('\n')) {
    if ((current + line).length > maxLen) {
      chunks.push(current.trim()); current = '';
    }
    current += line + '\n';
  }
  if (current.trim()) chunks.push(current.trim());
  return chunks;
}

New command: always include rate limiting + input validation.
