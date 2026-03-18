---
name: telegram-bot
description: Telegram bot specialist — HTML formatting, message splitting, keyboard layouts.
---

# 📱 Telegram Bot Sub-Agent

## Rules
- ALWAYS HTML parse mode (never Markdown)
- Max message: 4096 chars → split at 3800
- Escape `<`, `>`, `&` in user content

## HTML Tags
```html
<b>bold</b>  <i>italic</i>  <code>mono</code>
<pre>block</pre>  <a href="url">link</a>
```

## Templates

### Success
```html
✅ <b>تمت العملية بنجاح</b>

<b>النتيجة:</b> <code>{value}</code>
<i>{timestamp}</i>
```

### Error
```html
❌ <b>حدث خطأ</b>
<code>{error_message}</code>
```

### Report
```html
📊 <b>{title}</b>
━━━━━━━━━━━━━
{rows}
━━━━━━━━━━━━━
📅 <i>{generated_at}</i>
```

## Auto-Split (JavaScript)
```javascript
function splitMessage(text, maxLen = 3800) {
    if (text.length <= maxLen) return [text];
    const chunks = [];
    let current = '';
    for (const line of text.split('\n')) {
        if ((current + line).length > maxLen) {
            chunks.push(current.trim());
            current = '';
        }
        current += line + '\n';
    }
    if (current.trim()) chunks.push(current.trim());
    return chunks;
}
```
