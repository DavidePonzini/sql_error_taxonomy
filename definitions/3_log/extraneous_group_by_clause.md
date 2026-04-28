## Extraneous GROUP BY clause
### Definition
A `GROUP BY` clause is included in the query when the data demand does not require any aggregation or grouping of the results.

### Data demand
List the average age of customers.

### Example
```sql
SELECT AVG(age)
FROM customer
GROUP BY city;
```

### Explanation
The query groups customers by city and calculates the average age for each city. However, the data demand is to list the average age of all customers, not grouped by city.

### Correction
```sql
SELECT AVG(age)
FROM customer;
```

