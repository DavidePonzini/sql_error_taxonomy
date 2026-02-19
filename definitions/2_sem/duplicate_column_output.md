## Duplicate column output
### Definition
Multiple columns in the output always contain identical values.

### Example
```sql
SELECT first_name, last_name, first_name FROM students;
```

### Explaination
The query selects the first_name column twice, resulting in duplicate data in the output. This redundancy can confuse users and make it harder to interpret the results.

### Correction
```sql
SELECT first_name, last_name FROM students;
```

