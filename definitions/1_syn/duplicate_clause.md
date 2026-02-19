## Duplicate clause
### Definition
A clause is repeated in the query, such as multiple WHERE or ORDER BY clauses.

### Example
```sql
SELECT * FROM students ORDER BY age ORDER BY name;
```

### Explaination
This query is invalid because it contains two ORDER BY clauses. Each clause should only appear once in a query.

### Correction
```sql
SELECT * FROM students ORDER BY age, name;
```

