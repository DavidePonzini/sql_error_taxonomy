## IS where not applicable
### Definition
The `IS` operator is used for comparisons on values other than `NULL` or boolean expressions.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT * FROM
customer
WHERE age IS 18;
```

### Explanation
The IS operator should only be used for checking `NULL` values or boolean expressions (e.g., `IS TRUE`, `IS FALSE`). For other comparisons, use standard comparison operators like `=`, `<>`, `>`, `<`, `>=`, `<=`.

### Correction
```sql
SELECT *
FROM customer
WHERE age = 18;
```

