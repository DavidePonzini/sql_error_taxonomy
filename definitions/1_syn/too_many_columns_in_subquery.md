## Too many columns in subquery
### Definition
A subquery returns more columns than expected in the context where it is used.

### Example
```sql
SELECT * FROM students WHERE id IN (SELECT * FROM teachers);
```

### Explaination
The subquery in the WHERE clause is expected to return a single column of values to compare against the id column in the outer query. However, it returns all columns from the teachers table, leading to a mismatch.

### Correction
```sql
SELECT * FROM students WHERE id IN (SELECT id FROM teachers);
```

