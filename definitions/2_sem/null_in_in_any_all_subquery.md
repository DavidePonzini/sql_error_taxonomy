## NULL in IN/ANY/ALL subquery
### Definition
Using nullable values in `IN`, `ANY`, or `ALL` subqueries can lead to unexpected results due to the way NULLs are handled in SQL.

### Example
```sql
SELECT *
FROM customer
WHERE city IN (
    SELECT city
    FROM store
);
```

### Explaination
This query attempts to find customers whose city appears in the `store` table.
However, if the subquery returns `NULL` values, the `IN` condition can evaluate to `UNKNOWN`, causing matching rows to be excluded unexpectedly.

### Correction
```sql
SELECT *
FROM customer
WHERE city IN (
    SELECT city
    FROM store
    WHERE city IS NOT NULL
);
```

