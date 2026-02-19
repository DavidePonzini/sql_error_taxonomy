## Condition in the subquery can be moved up
### Definition
A condition in the subquery refences only values from the outer query and can be moved to the outer WHERE clause.

### Example
```sql
SELECT name FROM students s WHERE EXISTS (SELECT 1 FROM teachers t WHERE t.name = s.name AND s.age > 18);
```

### Explaination
The condition 's.age > 18' in the subquery only references the outer query's table 'students'. Therefore, it can be moved to the outer WHERE clause, which can improve query readability and potentially performance.

### Correction
```sql
SELECT name FROM students s WHERE s.age > 18 AND EXISTS (SELECT 1 FROM teachers t WHERE t.name = s.name);
```

