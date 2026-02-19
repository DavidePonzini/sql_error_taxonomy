## Extraneous quotes
### Definition
A column name is enclosed in quotes, effectively turning it into a string literal.

### Example
```sql
SELECT * FROM students WHERE name = 'supervisor_name';
```

### Explaination
This query is intended to find students who have the same name as their supervisor. However, by enclosing supervisor_name in quotes, it returns students whose name is literally 'supervisor_name', rather than comparing it to the value in the supervisor_name column.

### Correction
```sql
SELECT * FROM students WHERE name = supervisor_name;
```

