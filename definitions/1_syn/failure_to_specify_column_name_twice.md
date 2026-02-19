## Failure to specify column name twice
### Definition
When using multiple conditions on the same column, the column name is not specified for each condition.

### Example
```sql
SELECT * FROM students WHERE age > 18 AND < 25;
```

### Explaination
Each condition in the WHERE clause must explicitly specify the column name it applies to.

### Correction
```sql
SELECT * FROM students WHERE age > 18 AND age < 25;
```

