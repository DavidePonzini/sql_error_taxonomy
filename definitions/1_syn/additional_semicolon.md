## Additional semicolon
### Definition
An extra semicolon is present in the query, which can lead to syntax errors.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer;;
```

### Explanation
Ensure that there is only one semicolon at the end of the SQL statement.

### Correction
```sql
SELECT *
FROM customer;
```

