## Using WHERE twice
### Definition
The query contains multiple WHERE clauses, which is not allowed.

### Example
```sql
SELECT * FROM students WHERE age > 18 WHERE grade = 'A';
```

### Explaination
A query can only have one WHERE clause. Combine multiple conditions using logical operators like AND or OR.

### Correction
```sql
SELECT * FROM students WHERE age > 18 AND grade = 'A';
```

