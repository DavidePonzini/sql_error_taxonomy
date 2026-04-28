## Unnecessary GROUP BY in EXISTS subquery
### Definition
A `GROUP BY` clause is used in an `EXISTS` subquery where it is not needed, as `EXISTS` only checks for the existence of rows.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT cName
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM store s
    WHERE c.cName = s.sName
    GROUP BY s.city
);
```

### Explanation
The `GROUP BY` clause in the `EXISTS` subquery is unnecessary because `EXISTS` only checks whether at least one row is returned by the subquery. The grouping does not affect the existence check and adds unnecessary complexity to the query.

### Correction
```sql
SELECT cName
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM store s
    WHERE c.cName = s.sName
);
```

