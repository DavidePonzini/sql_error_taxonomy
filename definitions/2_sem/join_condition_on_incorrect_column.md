## Join condition on incorrect column (matches impossible)
### Definition
A join is performed on columns that cannot logically match, resulting in an empty result set.

### Example
```sql
SELECT * FROM students JOIN teachers ON students.age = teachers.salary;
```

### Explaination
This query attempts to join the students and teachers tables based on the condition that a student's age equals a teacher's salary. Since age and salary are fundamentally different types of data, this join condition is illogical and will likely result in no matching rows.

### Correction
```sql
SELECT * FROM students JOIN teachers ON students.class_id = teachers.class_id;
```

