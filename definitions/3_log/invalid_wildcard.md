## Invalid wildcard
### Definition
Wildcards are used incorrectly in pattern matching, such as using _ when % is needed, or using non-standard wildcards like *.

### Example
```sql
SELECT * FROM students WHERE name LIKE 'J*n';
```

### Explaination
The query uses the non-standard wildcard * instead of the SQL standard wildcard %. The * character is not recognized by LIKE for pattern matching in SQL and is instead treated as a literal character.

### Correction
```sql
SELECT * FROM students WHERE name LIKE 'J%n';
```

