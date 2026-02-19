## ORDER BY in subquery
### Definition
An ORDER BY clause is used in a subquery where it does not affect the final result set.

### Example
```sql
SELECT name FROM students WHERE name IN (SELECT name FROM teachers ORDER BY name);
```

### Explaination
The query retrieves the names of students who have the same name as any teacher. However, the ORDER BY clause in the subquery is unnecessary, as the order of rows in a subquery does not impact the final result set of the outer query.

### Correction
```sql
SELECT name FROM students WHERE name IN (SELECT name FROM teachers);
```

