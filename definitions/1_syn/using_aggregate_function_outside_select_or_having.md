## Using aggregate function outside SELECT or HAVING
### Definition
An aggregate function is used in a part of the query where it is not allowed, such as `WHERE` or `GROUP BY`.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT city
FROM customer
WHERE AVG(age) > 18;
```

### Explaination
Aggregate functions can only be used in the `SELECT` clause, or the `HAVING` clause when grouping results. This query is attempting to use `AVG` in the `WHERE` clause, which is not allowed.

### Correction
```sql
SELECT city
FROM customer
GROUP BY city
HAVING AVG(age) > 18;
```

