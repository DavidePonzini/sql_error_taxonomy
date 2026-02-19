## Extraneous column in SELECT
### Definition
A column is included in the SELECT clause that is not expected or needed for the intended result.

### Example
```sql
SELECT name, age, address FROM students;
```

### Explaination
The exercise requires only the names and ages of students, but the query also includes the address column in the SELECT clause. This adds unnecessary data to the result set.

### Correction
```sql
SELECT name, age FROM students;
```

