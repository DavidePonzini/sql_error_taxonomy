## OUTER JOIN can be replaced by INNER JOIN
### Definition
Using a WHERE condition on the right table of a LEFT OUTER JOIN effectively turns it into an INNER JOIN.

### Example
```sql
SELECT s.name, t.name FROM students s LEFT OUTER JOIN teachers t ON s.supervisor_id = t.id WHERE t.department = 'Math';
```

### Explaination
The WHERE condition 't.department = 'Math'' filters out any rows where there is no matching teacher, which negates the purpose of the LEFT OUTER JOIN. In this case, an INNER JOIN is more appropriate and efficient.

### Correction
```sql
SELECT s.name, t.name FROM students s INNER JOIN teachers t ON s.supervisor_id = t.id WHERE t.department = 'Math';
```

