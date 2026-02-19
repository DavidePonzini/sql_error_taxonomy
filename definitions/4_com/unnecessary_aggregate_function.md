## Unnecessary aggregate function
### Definition
An aggregate function is used on a single value.

### Example
```sql
SELECT MAX(age) FROM students WHERE id = 123;
```

### Explaination
The query retrieves the age of a specific student with id 123. Since the WHERE clause filters the results to a single row, using the MAX aggregate function is unnecessary, as there is only one value to return.

### Correction
```sql
SELECT age FROM students WHERE id = 123;
```

