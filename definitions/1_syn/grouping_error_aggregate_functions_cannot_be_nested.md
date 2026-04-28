## Grouping error: aggregate functions cannot be nested
### Definition
Aggregate functions cannot be nested within each other in a query.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT SUM(AVG(age))
FROM customer
GROUP BY city;
```

### Explanation
This query attempts to nest the AVG function inside the SUM function, which is not allowed. Instead, you can use a subquery to first calculate the average scores per group and then sum those averages.

### Correction
```sql
SELECT SUM(age)
FROM (
    SELECT AVG(age) AS age
    FROM customer
    GROUP BY city
) AS avg_ages;
```

