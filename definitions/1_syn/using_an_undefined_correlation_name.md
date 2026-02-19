## Using an undefined correlation name
### Definition
The query references a correlation name (alias) that has not been defined.

### Example
```sql
SELECT s2.name FROM students AS s;
```

### Explaination
This query renames the students table to 's' but then tries to reference it as 's2', which is not defined.

### Correction
```sql
SELECT s.name FROM students AS s;
```

