## Data type mismatch
### Definition
The query uses incompatible data types in an operation or comparison.

### Example
```sql
SELECT * FROM students WHERE name = 7;
```

### Explaination
The condition in the WHERE clause compares a string column (name) with an integer value (7), which is not valid.

### Correction
```sql
SELECT * FROM students WHERE name = 'John';
```

