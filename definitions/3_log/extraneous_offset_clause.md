## Extraneous OFFSET clause
### Definition
The `OFFSET` clause is included in the query when the data demand does not require skipping any rows in the result set.

### Data demand
List the first three customers in alphabetical order.

### Example
```sql
SELECT *
FROM customer
ORDER BY cName
LIMIT 3
OFFSET 1;
```

### Explanation
The query doesn't satisfy its data demand, since it lists customers the second, third and fourth customers, instead of the first three.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName
LIMIT 3;