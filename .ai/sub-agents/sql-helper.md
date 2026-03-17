---
name: sql-helper
description: MySQL query generation specialist. Delegate all complex SQL here.
---

# 🔧 SQL Helper Sub-Agent

## Input Required
1. Goal — what data do you need?
2. Tables involved — names + key columns
3. Filters — what conditions apply?
4. Output — what columns to return?

## Common Patterns

### Sales Report
```sql
SELECT DATE(created_at) as sale_date,
    COUNT(*) as total_invoices,
    SUM(total_amount) as revenue,
    SUM(profit) as profit
FROM invoices
WHERE created_at BETWEEN ? AND ?
    AND status = 'completed'
GROUP BY DATE(created_at)
ORDER BY sale_date DESC;
```

### Overstock Detection
```sql
SELECT d.nameeng, d.namear, i.quantity,
    i.avg_consumption,
    ROUND(i.quantity / NULLIF(i.avg_consumption,0), 1) as months_stock
FROM inventory i
JOIN drugs d ON d.id = i.drug_id
WHERE i.quantity > (i.avg_consumption * ?)
ORDER BY months_stock DESC;
```

### Top Sellers
```sql
SELECT d.nameeng,
    SUM(si.quantity) as total_sold,
    SUM(si.quantity * si.sell_price) as revenue
FROM sale_items si
JOIN drugs d ON d.id = si.drug_id
WHERE si.created_at >= DATE_SUB(NOW(), INTERVAL ? MONTH)
GROUP BY d.id
ORDER BY total_sold DESC
LIMIT ?;
```
