## Unnecessary join
### Definition
A table is joined just to access a value which is already available as a foreign key.

### Example
```sql
SELECT s.id, t.id FROM students s JOIN teachers t ON s.supervisor_id = t.id;
```

### Explaination
The exercise requires selecting the student IDs along with their supervisor IDs. However, the query unnecessarily joins the teachers table to retrieve the supervisor IDs, which are already available in the students table as foreign keys.

### Correction
```sql
SELECT id, supervisor_id FROM students;
```

