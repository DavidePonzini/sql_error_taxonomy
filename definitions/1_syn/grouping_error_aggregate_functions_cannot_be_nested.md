## Grouping error: aggregate functions cannot be nested
### Definition
Aggregate functions cannot be nested within each other in a query.

### Example
```sql
SELECT SUM(AVG(score)) FROM students GROUP BY class;
```

### Explaination
This query attempts to nest the AVG function inside the SUM function, which is not allowed. Instead, you can use a subquery to first calculate the average scores per group and then sum those averages.

### Correction
```sql
SELECT SUM(score) FROM (SELECT AVG(score) AS score FROM students GROUP BY class) AS avg_scores;
```

