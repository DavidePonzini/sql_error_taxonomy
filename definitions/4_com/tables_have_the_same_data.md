## Tables have the same data
### Definition
The query references two tables that always contain the same data.

### Example
```sql
SELECT a.name, b.name FROM students a JOIN students b ON a.id = b.id;
```

### Explaination
The query joins the students table with itself on the id column, which is a primary key. Since each id is unique, the join will always pair each student with themselves, resulting in identical data from both tables. This redundancy adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT name FROM students;
```

