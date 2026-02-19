## Unnecessarily complicated SELECT in EXISTS subquery
### Definition
The SELECT clause in an EXISTS subquery returns more than a single column, which is unnecessary since EXISTS only checks for the existence of rows.

### Example
```sql
SELECT name FROM students s WHERE EXISTS (SELECT id, name FROM teachers t WHERE t.name = s.name);
```

### Explaination
The EXISTS subquery is intended to find students who have the same name as any teacher. However, the SELECT clause in the subquery returns both id and name columns, which is unnecessary because EXISTS only checks for the existence of rows that meet the condition. Returning multiple columns adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT name FROM students s WHERE EXISTS (SELECT 1 FROM teachers t WHERE t.name = s.name);
```

