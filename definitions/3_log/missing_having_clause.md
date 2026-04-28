## Missing HAVING clause
### Definition
A `HAVING` clause is missing from the query when the data demand requires filtering of grouped results based on an aggregate condition.

### Data demand
List the average age of customers for each city where the average age is greater than 30.

### Example
```sql
SELECT city, AVG(age)
FROM customer
GROUP BY city;
```

### Explanation
The query calculates the average age of customers for each city but does not include a `HAVING` clause to filter the results based on the condition that the average age should be greater than 30. As a result, it returns the average age for all cities, not just those where the average age exceeds 30.

### Correction
```sql
SELECT city, AVG(age)
FROM customer
GROUP BY city
HAVING AVG(age) > 30;
```