## Omitting the semicolon
### Definition
The query is missing the terminating semicolon at the end of the statement.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
```

### Explanation
SQL standard requires each statement to end with a semicolon (`;`). Make sure to include it at the end of your queries.

### Correction
```sql
SELECT *
FROM customer;
```

