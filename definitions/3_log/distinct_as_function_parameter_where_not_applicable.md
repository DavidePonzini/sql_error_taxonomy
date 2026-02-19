## DISTINCT as function parameter where not applicable
### Definition
DISTINCT is used within a function where it is not appropriate or necessary.

### Example
```sql
SELECT COUNT(DISTINCT supervisor) FROM students;
```

### Explaination
The exercise expects the total number of students who have a supervisor assigned, but the DISTICT keyword causes the COUNT function to count only unique supervisors, which is not the intended behavior.

### Correction
```sql
SELECT COUNT(supervisor) FROM students;
```

