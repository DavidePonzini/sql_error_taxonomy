## Unused CTE
### Definition
A Common Table Expression (CTE) is defined in the query but not referenced or used in the main query or any subqueries.

### Data demand
*(Not relevant)*

### Example
```sql
WITH cte AS (
    SELECT cID, cName
    FROM customer
)

SELECT cName
FROM customer;
```

### Explanation
The CTE named `cte` is defined but never used in the main query. This adds unnecessary complexity to the query without providing any benefit.

### Correction
```sql
SELECT cName
FROM customer;
```

