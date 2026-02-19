## Unnecessary GROUP BY in EXISTS subquery
### Definition
A GROUP BY clause is used in an EXISTS subquery where it is not needed, as EXISTS only checks for the existence of rows.

### Example
```sql
SELECT name FROM students s WHERE EXISTS (SELECT 1 FROM teachers t GROUP BY t.name HAVING t.name = s.name);
```

### Explaination
The EXISTS subquery is intended to find students who have the same name as any teacher. However, the GROUP BY clause is unnecessary because EXISTS only checks for the existence of rows that meet the condition. Using GROUP BY adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT name FROM students s WHERE EXISTS (SELECT 1 FROM teachers t WHERE t.name = s.name);
```

