## Too many columns in subquery
### Definition
A subquery returns more columns than expected in the context where it is used.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM inventory
WHERE sID IN (
    SELECT *
    FROM store
    WHERE sName = 'Coop'
);
```

### Explanation
The subquery in the WHERE clause must return exactly one column to compare with `inventory.sID`. Returning all store columns causes a column-count mismatch.

### Correction
```sql
SELECT *
FROM inventory
WHERE sID IN (
    SELECT sID
    FROM store
    WHERE sName = 'Coop'
);```

