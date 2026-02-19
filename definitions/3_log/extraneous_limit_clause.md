## Extraneous LIMIT clause
### Definition
The `LIMIT` clause is included in the query when the data demand does not require restricting the number of results returned.

### Data demand
List all customers.

### Example
```sql
SELECT *
FROM customer
LIMIT 10;
```

### Explaination
The query doesn't satisfy its data demand, since it lists only 10 customers instead of all those present in the database.

### Correction
```sql
SELECT *
FROM customer;
```

