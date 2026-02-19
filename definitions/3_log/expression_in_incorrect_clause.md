## Expression in incorrect clause
### Definition
A correct logical expression is present in the WRONG clause (i.e. `WHERE` instead of `HAVING`, or vice versa).

### Data demand
List the average age of customers for each city.
Show only cities in which the average age is less than 30.

### Example
```sql
SELECT city, AVG(age)
FROM customer
WHERE age < 30
GROUP BY city;
```

### Explaination
This query answers the following data demand: *List the average age of customers for each city. Consider only customers younger than 30.*

To correctly satisfy the data demand, the condition `age < 30` must be moved to the `HAVING` clause, since it must apply on the grouping result instead of individual rows.

### Correction
```sql
SELECT city, AVG(age)
FROM customer
GROUP BY city
HAVING AVG(age) < 30;
```

