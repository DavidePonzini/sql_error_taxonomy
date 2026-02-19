## Missing AS from SELECT
### Definition
A column presents a different name from what is required by the exercise, due to the absence of an AS alias.

### Example
```sql
SELECT name FROM students;
```

### Explaination
The exercise requires the output column to be labeled as 'student_name', but the query does not use an AS alias to rename the column.

### Correction
```sql
SELECT name AS student_name FROM students;
```

