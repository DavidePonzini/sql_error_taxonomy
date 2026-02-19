## Confusing the order of keywords (e.g., FROM customer SELECT fee)
### Definition
Keywords in the SQL statement are in the wrong order.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
FROM customer
SELECT cName;
```

### Explaination
Ensure that SQL keywords are in the correct order: `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, `OFFSET`.

### Correction
```sql
SELECT cName
FROM customer;
```

