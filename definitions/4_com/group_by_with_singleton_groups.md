## GROUP BY with singleton groups
### Definition
GROUP BY is used on groups that each contain only a single row, making the grouping unnecessary.

### Example
```sql
SELECT id, AVG(age) FROM students GROUP BY id;
```

### Explaination
The query groups the students by their id, which is a primary key. Since each id is unique, each group will contain only a single row. Therefore, using GROUP BY is unnecessary, as it does not change the result set.

### Correction
```sql
SELECT id, age FROM students;
```

