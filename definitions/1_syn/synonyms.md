## Synonyms
### Definition
The query uses synonyms or alternative names for tables or columns that do not exist.

### Example
```sql
SELECT * FROM pupils;
```

### Explaination
The table pupils does not exist in the database. It is a synonym for 'students', which is the correct table name.

### Correction
```sql
SELECT * FROM students;
```

