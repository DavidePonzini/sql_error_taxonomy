## Incorrect LIMIT
### Definition
The `LIMIT` clause is used with an incorrect value.

### Data demand
List the first 3 customers ordered by their names.

### Example
```sql
SELECT *
FROM customer
ORDER BY cName
LIMIT 10;
```

### Explanation
The query doesn't satisfy its data demand, since it lists the first 10 customers instead of the first 3 customers.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName
LIMIT 3;
```

