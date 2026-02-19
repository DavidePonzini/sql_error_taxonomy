## Undefined function
### Definition
The query references a function that does not exist or is not defined.

### Example
```sql
SELECT CAPSLOCK(name) FROM students;
```

### Explaination
The function CAPSLOCK does not exist in the database.

### Correction
```sql
SELECT UPPER(name) FROM students;
```

