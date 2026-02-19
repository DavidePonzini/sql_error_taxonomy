## DISTINCT that might remove important duplicates
### Definition
Using DISTINCT removes duplicate rows from the result set, which may inadvertently exclude important data.

### Example
```sql
SELECT DISTINCT name from students WHERE grade = 'A';
```

### Explaination
If multiple students share the same name and have received an 'A' grade, using DISTINCT will return only one instance of that name, potentially omitting other students with the same name who also earned an 'A'. This could lead to incomplete or misleading results.

### Correction
```sql
SELECT name from students WHERE grade = 'A';
```

