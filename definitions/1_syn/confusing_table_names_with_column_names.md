## Confusing table names with column names
### Definition
A table name is used where a column name is expected, or vice versa.

### Example
```sql
SELECT name.students FROM students, teachers;
```

### Explaination
This query tries the access a column called 'students' from the 'name' table, which does not exist. The correct syntax is to specify the table name followed by the column name.

### Correction
```sql
SELECT students.name FROM students, teachers;
```

