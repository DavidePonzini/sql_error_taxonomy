## Undefined object
### Definition
The query references a table that does not exist or is not defined.

### Example
```sql
SELECT * FROM cats;
```

### Explaination
The table cats does not exist in the database.

### Correction
```sql
SELECT * FROM students;
```

