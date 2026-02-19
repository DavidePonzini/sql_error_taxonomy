## Undefined column
### Definition
The query references a column that does not exist in the specified table(s).

### Example
```sql
SELECT credit_card FROM students;
```

### Explaination
The table students does not contain a column named 'credit_card'.

### Correction
```sql
SELECT name FROM students;
```

