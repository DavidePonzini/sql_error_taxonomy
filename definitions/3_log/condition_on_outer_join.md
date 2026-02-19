## Condition on OUTER JOIN
### Definition
Using a JOIN ON condition on the left table of a LEFT OUTER JOIN affects only the right table, which can lead to unexpected results.

### Example
```sql
SELECT s.name, t.name FROM students s LEFT OUTER JOIN teachers t ON s.supervisor_id = t.id AND s.age > 18;
```

### Explaination
The condition 's.age > 18' is applied only on the right table. If a student is younger than 18, the join will still include that student with NULL values for the teacher columns, which is not the internted behavior. To filter students based on age, the condition should be placed in the WHERE clause instead.

### Correction
```sql
SELECT s.name, t.name FROM students s LEFT OUTER JOIN teachers t ON s.supervisor_id = t.id WHERE s.age > 18;
```

