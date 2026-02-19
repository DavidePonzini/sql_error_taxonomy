## Omitting the FROM clause
### Definition
The query is missing the FROM clause and does not select a constant value.

### Example
```sql
SELECT name WHERE age > 18;
```

### Explaination
The FROM clause is required in a SELECT statement to specify the table from which to retrieve data.

### Correction
```sql
SELECT name FROM students WHERE age > 18;
```

