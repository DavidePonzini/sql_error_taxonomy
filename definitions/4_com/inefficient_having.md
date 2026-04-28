## Inefficient HAVING
### Definition
A condition in the `HAVING` clause does not depend on aggregate functions and can be moved to the `WHERE` clause.

### Example
```sql
SELECT age, COUNT(*)
FROM customer
GROUP BY age
HAVING age IS NOT NULL;
```

### Explanation
The HAVING clause is used to filter groups based on aggregate conditions. However, the condition `age IS NOT NULL` does not depend on aggregation and can be applied before grouping, which is more efficient.

### Correction
```sql
SELECT age, COUNT(*)
FROM customer
WHERE age IS NOT NULL
GROUP BY age;
```

