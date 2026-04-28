## Missing OFFSET clause
### Definition
The `OFFSET` clause is missing from the query when the data demand requires skipping a certain number of rows before starting to return results.

### Data demand
List the first the second, third and fourth customers in alphabetical order.

### Example
```sql
SELECT *
FROM customer
ORDER BY cName
LIMIT 3;
```

### Explanation
The query doesn't satisfy its data demand, since it lists the first three customers instead of the second, third and fourth customers. The `OFFSET` clause is needed to skip the first customer.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName
LIMIT 3
OFFSET 1;
```