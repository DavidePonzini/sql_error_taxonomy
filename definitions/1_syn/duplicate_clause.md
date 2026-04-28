## Duplicate clause
### Definition
A clause is repeated in the query, such as multiple `WHERE` or `ORDER BY` clauses.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
ORDER BY cName
ORDER BY cID;
```

### Explanation
This query is invalid because it contains two `ORDER BY` clauses. Each clause should only appear once in a query.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName, cID;
```

