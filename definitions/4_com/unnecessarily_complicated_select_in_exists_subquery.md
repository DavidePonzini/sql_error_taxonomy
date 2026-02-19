## Unnecessarily complicated SELECT in EXISTS subquery
### Definition
The `SELECT` clause in an `EXISTS` subquery returns more than a single column, which is unnecessary since `EXISTS` only checks for the existence of rows.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT cName
FROM customer c
WHERE EXISTS (
    SELECT s.sID, s.sName
    FROM store s
    WHERE c.cName = s.sName
);
```

### Explaination
The `EXISTS` subquery is intended to find customers who have the same name as a store. However, the `SELECT` clause returns multiple store columns, which is unnecessary because `EXISTS` only checks whether at least one row is returned.

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

