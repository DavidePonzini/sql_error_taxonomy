## Confusing the order of keywords (e.g., FROM customer SELECT fee)
### Definition
Keywords in the SQL statement are in the wrong order.

### Example
```sql
FROM students SELECT name;
```

### Explaination
Ensure that SQL keywords are in the correct order: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, OFFSET.

### Correction
```sql
SELECT name FROM students;
```

