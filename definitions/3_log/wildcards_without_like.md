## Wildcards without LIKE
### Definition
Wildcards such as % or _ are used with = instead of LIKE, resulting in a literal comparison rather than a pattern match.

### Example
```sql
SELECT * FROM students WHERE name = 'J%n';
```

### Explaination
This query selects all students whose name is exactly 'J%n', including the percent sign, rather than matching names that start with 'J' and end with 'n' with any characters in between.

### Correction
```sql
SELECT * FROM students WHERE name LIKE 'J%n';
```

