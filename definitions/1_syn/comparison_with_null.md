## Comparison with NULL
### Definition
The query uses a comparison with NULL using operators like `=` or `!=` instead of `IS NULL` or `IS NOT NULL`.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE age = NULL;
```

### Explanation
When checking for NULL values, use `IS NULL` or `IS NOT NULL` instead of standard comparison operators.

### Correction
```sql
SELECT *
FROM customer
WHERE age IS NULL;
```

