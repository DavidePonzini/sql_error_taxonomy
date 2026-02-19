## Omitting commas
### Definition
When listing multiple columns or values, commas are missing between them.

### Example
```sql
SELECT firstname lastname age FROM students;
```

### Explaination
This query is missing commas between the column names in the SELECT clause. Ensure that each column name is separated by a comma.

### Correction
```sql
SELECT firstname, lastname, age FROM students;
```

