## Unused correlation name
### Definition
A correlation name (alias) is defined for a table but not used in the query.

### Example
```sql
SELECT name FROM students s;
```

### Explaination
The query defines a correlation name 's' for the students table but does not use it anywhere in the query. This adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT name FROM students;
```

