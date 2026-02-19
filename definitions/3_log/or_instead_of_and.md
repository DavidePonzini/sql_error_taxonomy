## OR instead of AND
### Definition
Query uses OR where AND is needed.

### Data demand
List of students older that 18 that have received an 'A' grade.

### Example
```sql
SELECT * FROM students WHERE age > 18 OR grade = 'A';
```

### Explaination
This query finds students who are older than 18, as well as those who have received an 'A' grade, regardless of age. However, this does not match the data demand. In this case, `AND` should have been used instead of `OR`.

### Correction
```sql
SELECT * FROM students WHERE age > 18 AND grade = 'A';
```

