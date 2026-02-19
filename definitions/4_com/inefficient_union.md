## Inefficient UNION
### Definition
A UNION operation can be replaced by UNION ALL without changing the result set, improving performance.

### Example
```sql
SELECT name FROM students WHERE age < 18 UNION SELECT name FROM students WHERE age > 30;
```

### Explaination
The two queries retrieve names of students from disjoint age groups (younger than 18 and older than 30). Since there is no overlap between these two groups, using UNION ALL is more efficient as it does not perform the additional step of removing duplicates, which is unnecessary in this case.

### Correction
```sql
SELECT name FROM students WHERE age < 18 UNION ALL SELECT name FROM students WHERE age > 30;
```

