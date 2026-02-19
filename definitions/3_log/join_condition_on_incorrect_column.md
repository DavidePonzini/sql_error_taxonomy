## Join condition on incorrect column (matches possible)
### Definition
A join condition uses the wrong column, leading to incorrect or unexpected results.

### Example
```sql
SELECT students.name FROM students JOIN teachers ON students.class_id = teachers.favourite_number;
```

### Explaination
This query is intended to retrieve the names of students who are associated with specific teachers. However, the join condition uses the favourite_number column from the teachers table, which is not logically related to the class_id column from the students table. This can lead to incorrect or unexpected results, as the join may match students with unrelated teachers based on arbitrary favourite numbers.

### Correction
```sql
SELECT students.name FROM students JOIN teachers ON students.class_id = teachers.class_id;
```

