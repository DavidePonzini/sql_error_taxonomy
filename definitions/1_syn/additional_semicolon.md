## Additional semicolon
### Definition
An extra semicolon is present in the query, which can lead to syntax errors.

### Example
```sql
SELECT *
FROM customer;;
```

### Explaination
Ensure that there is only one semicolon at the end of the SQL statement.

### Correction
```sql
SELECT *
FROM customer;
```

