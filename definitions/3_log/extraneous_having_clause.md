## Extraneous HAVING clause
### Definition
A `HAVING` clause is included in the query when the data demand does not require any filtering of grouped results.

### Data demand
List the average age of customers for each city.

### Example
```sql
SELECT city, AVG(age)
FROM customer
GROUP BY city
HAVING AVG(age) > 30;
```

### Explaination
The query uses a `HAVING` clause to filter groups of customers based on their average age. However, the data demand is to list the average age of all customers, not to filter groups. The `HAVING` clause is extraneous in this context.

### Correction
```sql
SELECT city, AVG(age)
FROM customer
GROUP BY city;
```

