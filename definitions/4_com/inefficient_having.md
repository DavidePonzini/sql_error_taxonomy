## Inefficient HAVING
### Definition
A condition in the HAVING clause does not depend on aggregate functions and can be moved to the WHERE clause.

### Example
```sql
SELECT supervisor, COUNT(*) FROM students GROUP BY supervisor HAVING supervisor IS NOT NULL;
```

### Explaination
The HAVING clause is used to filter groups based on aggregate conditions. However, the condition 'supervisor IS NOT NULL' does not depend on any aggregate functions and can be applied before grouping. Moving this condition to the WHERE clause improves query efficiency by reducing the number of rows that need to be grouped.

### Correction
```sql
SELECT supervisor, COUNT(*) FROM students WHERE supervisor IS NOT NULL GROUP BY supervisor;
```

