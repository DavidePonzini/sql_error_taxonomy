## Comparison with NULL
### Definition
The query uses a comparison with NULL using operators like = or != instead of IS NULL or IS NOT NULL.

### Example
```sql
SELECT * FROM students WHERE name = NULL;
```

### Explaination
When checking for NULL values, use IS NULL or IS NOT NULL instead of standard comparison operators.

### Correction
```sql
SELECT * FROM students WHERE name IS NULL;
```

