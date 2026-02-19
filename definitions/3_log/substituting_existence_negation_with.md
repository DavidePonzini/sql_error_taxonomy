## Substituting existence negation with <>
### Definition
The query uses <> to check for non-existence instead of NOT IN or NOT EXISTS.

### Example
```sql
SELECT * FROM students WHERE id <> (SELECT student_id FROM graduates);
```

### Explaination
This query attempts to find students who are not graduates by using the <> operator. However, this query actually returns students whose id is not equal to the single value returned by the subquery, which is not the intended behavior. To correctly find students who are not graduates, use NOT IN or NOT EXISTS.

### Correction
```sql
SELECT * FROM students WHERE id NOT IN (SELECT student_id FROM graduates);
```

