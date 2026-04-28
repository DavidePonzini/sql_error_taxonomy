## Inefficient UNION
### Definition
A `UNION` operation can be replaced by `UNION ALL` without changing the result set, improving performance.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT city 
FROM customer
WHERE city < 'M'
UNION
SELECT city
FROM store
WHERE city > 'M';
```

### Explanation
The query combines cities from the `customer` and `store` tables using `UNION`, which eliminates duplicate rows. However, the conditions in the `WHERE` clauses ensure that there will be no overlapping cities between the two sets (cities less than 'M' from `customer` and cities greater than 'M' from `store`). Therefore, there are no duplicates to eliminate, and using `UNION ALL` would yield the same result more efficiently.

### Correction
```sql
SELECT city 
FROM customer
WHERE city < 'M'
UNION ALL
SELECT city
FROM store
WHERE city > 'M';
```

