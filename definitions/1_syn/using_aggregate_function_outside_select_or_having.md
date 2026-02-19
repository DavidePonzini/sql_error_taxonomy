## Using aggregate function outside SELECT or HAVING
### Definition
An aggregate function is used in a part of the query where it is not allowed, such as WHERE or GROUP BY.

### Example
```sql
SELECT * FROM students WHERE AVG(score) > 80;
```

### Explaination
Aggregate functions can only be used in the SELECT clause or the HAVING clause when grouping results. This query is attempting to use AVG in the WHERE clause, which is not allowed.

### Correction
```sql
SELECT * FROM students GROUP BY class HAVING AVG(score) > 80;
```

