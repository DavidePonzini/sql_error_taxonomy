## Duplicate clause
### Definition
A clause is repeated in the query, such as multiple `WHERE` or `ORDER BY` clauses.

### Example
```sql
SELECT *
FROM customer
ORDER BY cName
ORDER BY cID;
```

### Explaination
This query is invalid because it contains two `ORDER BY` clauses. Each clause should only appear once in a query.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName, cID;
```

