## Curly or square brackets
### Definition
Curly and square brackets are used instead of parentheses.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE age > [(15 + 18) * 2] / (7 + 3);
```

### Explaination
Only parentheses ( "`(`" and "`)`" ) are allowed for grouping expressions in SQL.

### Correction
```sql
SELECT *
FROM customer
WHERE age > ((15 + 18) * 2) / (7 + 3);
```

