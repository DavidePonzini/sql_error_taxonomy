## Improper nesting of subqueries
### Definition
Subqueries are nested improperly, leading to a different evaluation order than intended.

### Example
```sql
SELECT * FROM students s WHERE id NOT EXISTS (SELECT * FROM graduates g WHERE g.student_id = s.id AND EXISTS (SELECT * FROM tutors t WHERE t.student_id = s.id));
```

### Explaination
This query is intended to find students who are not graduates and have tutors. However, the nesting of the EXISTS subquery within the NOT EXISTS subquery returns students who are not graduates or have tutors, but not both.

### Correction
```sql
SELECT * FROM students s WHERE NOT EXISTS (SELECT * FROM graduates g WHERE g.student_id = s.id) AND EXISTS (SELECT * FROM tutors t WHERE t.student_id = s.id);
```

