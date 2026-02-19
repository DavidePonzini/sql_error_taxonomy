## Missing ORDER BY clause
### Definition
An `ORDER BY` clause is missing from the query when the data demand requires the results to be sorted in a specific order.

### Data demand
List all customers in alphabetical order.

### Example
```sql
SELECT *
FROM customer;
```

### Explaination
The query does not satisfy its data demand, since it does not include an `ORDER BY` clause to sort the results in alphabetical order by customer name.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName;
```