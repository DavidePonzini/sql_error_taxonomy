## Missing DISTINCT from SELECT
### Definition
A `DISTINCT` keyword is missing from the `SELECT` clause, leading to duplicate rows in the result set where uniqueness is required by the exercise.

### Data demand
List the unique cities where customers live.

### Example
```sql
SELECT city
FROM customer;
```

### Explanation
The query retrieves the cities of all customers, but it does not use `DISTINCT`, which means that if multiple customers live in the same city, that city will appear multiple times in the result set. This does not meet the data demand for listing unique cities.

### Correction
```sql
SELECT DISTINCT city
FROM customer;
```

