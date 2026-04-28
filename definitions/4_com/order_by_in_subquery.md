## ORDER BY in subquery
### Definition
An `ORDER BY` clause is used in a subquery where it does not affect the final result set.

### Example
```sql
SELECT city
FROM customer
WHERE city IN (
    SELECT city
    FROM store
    ORDER BY city
);
```

### Explanation
The main query retrieves cities from the `customer` table that are present in the list of cities returned by the subquery. The order of cities in the subquery's result does not affect which cities are included in the final output, making the `ORDER BY` clause unnecessary in this context.

### Correction
```sql
SELECT city
FROM customer
WHERE city IN (
    SELECT city
    FROM store
);
```

