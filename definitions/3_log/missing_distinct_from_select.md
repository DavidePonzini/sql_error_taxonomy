## Missing DISTINCT from SELECT
### Definition
A DISTINCT keyword is missing from the SELECT clause, leading to duplicate rows in the result set where uniqueness is required by the exercise.

### Example
```sql
SELECT city FROM students;
```

### Explaination
The exercise requires a list of unique cities where students live. However, the query does not include the DISTINCT keyword, resulting in duplicate city names in the output.

### Correction
```sql
SELECT DISTINCT city FROM students;
```

