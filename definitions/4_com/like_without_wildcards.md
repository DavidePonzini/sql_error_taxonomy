## LIKE without wildcards
### Definition
The LIKE operator is used without any wildcard characters, making it equivalent to a simple equality comparison.

### Example
```sql
SELECT * FROM students WHERE name LIKE 'John';
```

### Explaination
The query uses the LIKE operator to compare the name column to 'John' without any wildcard characters. This makes the LIKE operator unnecessary, as it behaves the same way as the = operator in this case.

### Correction
```sql
SELECT * FROM students WHERE name = 'John';
```

