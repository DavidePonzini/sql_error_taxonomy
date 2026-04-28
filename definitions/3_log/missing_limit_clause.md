## Missing LIMIT clause
### Definition
The `LIMIT` clause is missing from the query when the data demand requires limiting the number of rows returned in the result set.

### Data demand
List 10 customers from the database.

### Example
```sql
SELECT *
FROM customer;
```

### Explanation
The query retrieves all customers from the database, but it does not include a `LIMIT` clause to restrict the number of rows returned to 10, as required by the data demand.

### Correction
```sql
SELECT *
FROM customer
LIMIT 10;
```
