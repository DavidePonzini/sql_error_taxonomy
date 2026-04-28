## Missing GROUP BY clause
### Definition
A `GROUP BY` clause is missing from the query when the data demand requires aggregation of results based on one or more columns.

### Data demand
List the average age of customers for each city.

### Example
```sql
SELECT AVG(age)
FROM customer;
```

### Explanation
The query calculates the average age of all customers but does not group the results by city. As a result, it returns a single average age for all customers, not for each city.

### Correction
```sql
SELECT AVG(age)
FROM customer
GROUP BY city;
```