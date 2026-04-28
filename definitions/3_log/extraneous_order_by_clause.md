## Extraneous ORDER BY clause
### Definition
An `ORDER BY` clause is included in the query when the data demand does not require any specific ordering of the results.

### Data demand
List all customers.

### Example
```sql
SELECT *
FROM customer
ORDER BY cName;
```

### Explanation
The data demand does not specify any ordering for the results, so including an `ORDER BY` clause is unnecessary and adds complexity to the query.

### Correction
```sql
SELECT *
FROM customer;
```

