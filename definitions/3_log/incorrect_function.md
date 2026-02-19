## Incorrect function
### Definition
An incorrect function is used for the intended operation, leading to unexpected results.

### Example
```sql
SELECT SUM(age) FROM students;
```

### Explaination
The exercise requires calculating the average age of students, but the query uses the SUM function instead of AVG, resulting in the total age rather than the average.

### Correction
```sql
SELECT AVG(age) FROM students;
```

