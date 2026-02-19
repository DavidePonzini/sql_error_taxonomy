## Unnecessary DISTINCT in aggregate function
### Definition
DISTINCT is used within an aggregate function where all values are already unique, making it redundant.

### Example
```sql
SELECT COUNT(DISTINCT id) FROM students;
```

### Explaination
The id column is a primary key, meaning each value is unique. Therefore, using DISTINCT within the COUNT function doesn't change the result, as there cannot be any duplicate ids to count.

### Correction
```sql
SELECT COUNT(id) FROM students;
```

