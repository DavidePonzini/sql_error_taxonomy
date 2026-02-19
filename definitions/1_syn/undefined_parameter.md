## Undefined parameter
### Definition
The query references a parameter that does not exist or is not defined. Also, placeholder parameters are used incorrectly.

### Example
```sql
SELECT ? FROM students WHERE id = :param;
```

### Explaination
The query uses placeholder parameters instead of actual values. This is valid syntax in prepared statements, but not in regular queries.

### Correction
```sql
SELECT name FROM students WHERE id = 1;
```

