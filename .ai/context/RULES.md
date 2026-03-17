# 📏 Coding Rules & Conventions

## 🚫 Never Do
- Never use `SELECT *` in production queries
- Never hardcode credentials, tokens, or passwords
- Never delete data without soft-delete option first
- Never write SQL string concatenation (use parameterized queries)
- Never push untested code to production
- Never assume input is safe — always validate

## ✅ Always Do
- Validate all user inputs before processing
- Use environment variables for sensitive config
- Write error messages that help debugging
- Test with edge cases: empty, null, very large numbers
- Add comments for non-obvious logic

## 📁 Naming Conventions
| Type | Convention | Example |
|------|-----------|---------|
| PHP classes | PascalCase | `DrugInventory` |
| PHP functions | camelCase | `calculateProfit()` |
| DB tables | snake_case plural | `drug_items` |
| DB columns | snake_case | `created_at` |
| JS functions | camelCase | `splitMessage()` |
| Constants | UPPER_SNAKE | `MAX_CHUNK_SIZE` |

## 🔒 Security Rules
- Rate limit all bot commands (max 10 req/min/user)
- Sanitize all HTML before displaying in Telegram
- Use PDO prepared statements for all DB queries
- Never expose DB structure in error messages

## 🌍 Arabic / RTL Support
- Store Arabic text as UTF-8
- Set DB charset to `utf8mb4`
- For Telegram: HTML parse mode, not Markdown
