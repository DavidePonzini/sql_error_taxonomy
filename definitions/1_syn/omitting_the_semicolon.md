## Omitting the semicolon
### Definition
The query is missing the terminating semicolon at the end of the statement.

### Example
```sql
SELECT *
FROM customer
```

### Explaination
SQL standard requires each statement to end with a semicolon (`;`). Make sure to include it at the end of your queries.

### Correction
```sql
SELECT *
FROM customer;
```

