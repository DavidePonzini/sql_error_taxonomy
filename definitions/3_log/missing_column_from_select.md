## Missing column from SELECT
### Definition
A required column is missing from the SELECT clause.

### Example
```sql
SELECT name FROM students;
```

### Explaination
The exercise requires both the names and ages of students, but the query only selects the name column, omitting the age column.

### Correction
```sql
SELECT name, age FROM students;
```

