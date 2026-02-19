## Missing DISTINCT from function parameter
### Definition
DISTINCT is missing within a function where it is required to ensure unique values are considered.

### Example
```sql
SELECT COUNT(supervisor) FROM students;
```

### Explaination
The exercise requires counting the number of supervisors assigned to students, counting each supervisor only once, regardless of how many students they supervise. However, the query counts all supervisor entries, including duplicates.

### Correction
```sql
SELECT COUNT(DISTINCT supervisor) FROM students;
```

