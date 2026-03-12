## Implied, tautological or inconsistent expression
### Definition
Query contains expressions that are always true, always false, or logically redundant.

### Data demand
*(Not relevant, semantic errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE
    age > 30
    AND age > 25
    AND cName = cName;
```

### Explaination
The expression `age > 30 AND age > 25` is redundant because if `age` is greater than 30, it is inherently greater than 25. Additionally, the condition `cName = cName` is always true for all rows.

Simplifying the query to remove these redundancies will improve clarity and performance, without altering its logic.

### Correction
```sql
SELECT *
FROM customer
WHERE age > 25;
```

