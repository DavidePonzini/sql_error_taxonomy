## UNION can be replaced by OR
### Definition
Two SELECT statements combined with UNION can be simplified to a single SELECT with an OR condition.

### Example
```sql
SELECT name FROM students WHERE age < 18 UNION SELECT name FROM students WHERE grade = 'A';
```

### Explaination
The query retrieves the names of students who are either younger than 18 or have received an 'A' grade. This can be simplified by using a single SELECT statement with an OR condition in the WHERE clause, which is more straightforward and efficient.

### Correction
```sql
SELECT name FROM students WHERE age < 18 OR grade = 'A';
```

