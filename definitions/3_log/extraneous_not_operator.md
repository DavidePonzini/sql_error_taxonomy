## Extraneous NOT operator
### Definition
A condition uses NOT where it is not needed, leading to incorrect results.

### Example
```sql
SELECT * FROM students WHERE age > 18 AND NOT grade = 'A';
```

### Explaination
This query is intended to find students who are older than 18 and have received an 'A' grade. However, the NOT operator negates the grade condition, resulting in students who are older than 18 but have not received an 'A' grade.

### Correction
```sql
SELECT * FROM students WHERE age > 18 AND grade = 'A';
```

