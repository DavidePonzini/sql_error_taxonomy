## Extraneous table reference
### Definition
The query references more tables than necessary, leading to incorrect or unexpected results.

### Example
```sql
SELECT name FROM students, teachers WHERE ...;
```

### Explaination
This query is intended to retrieve the names of students that meet certain criteria, but it unnecessarily joins the teachers table, which is not needed for this purpose. This can lead to incorrect results if there are multiple teachers associated with a student or if there are no matching teachers.

### Correction
```sql
SELECT name FROM students WHERE ...;
```

