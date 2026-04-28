## Failure to specify column name twice
### Definition
When using multiple conditions on the same column, the column name is not specified for each condition.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE age > 18 AND < 25;
```

### Explanation
Each condition in the WHERE clause must explicitly specify the column cName it applies to.

### Correction
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND age < 25;
```

