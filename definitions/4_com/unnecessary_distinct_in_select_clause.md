## Unnecessary DISTINCT in SELECT clause
### Definition
DISTINCT is used on a SELECT clause where duplicate values cannot occur, adding unnecessary complexity.

### Example
```sql
SELECT DISTINCT id, name FROM students;
```

### Explaination
The id column is a primary key, meaning each value is unique. Therefore, using DISTINCT is redundant since there cannot be any duplicate rows in the result set based on the id column.

### Correction
```sql
SELECT id, name FROM students;
```

