## Data type mismatch
### Definition
The query uses incompatible data types in an operation or comparison.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE cName = 7;
```

### Explaination
The condition in the WHERE clause compares a string column (cName) with an integer value (7), which is not valid.

### Correction
```sql
SELECT *
FROM customer
WHERE cName = 'John';
```

