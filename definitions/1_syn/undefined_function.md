## Undefined function
### Definition
The query references a function that does not exist or is not defined.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT CAPSLOCK(cName)
FROM customer;
```

### Explanation
The function `CAPSLOCK` does not exist in the database.

### Correction
```sql
SELECT UPPER(cName)
FROM customer;
```

