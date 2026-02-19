## Undefined function
### Definition
The query references a function that does not exist or is not defined.

### Example
```sql
SELECT CAPSLOCK(cName)
FROM customer;
```

### Explaination
The function `CAPSLOCK` does not exist in the database.

### Correction
```sql
SELECT UPPER(cName)
FROM customer;
```

