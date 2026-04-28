## Missing DISTINCT from function parameter
### Definition
`DISTINCT` is missing within a function where it is required to ensure repeated values are not counted multiple times.

### Data demand
Count the number of unique cities in the customer table.

### Example
```sql
SELECT COUNT(city)
FROM customer;
```

### Explanation
The query counts all entries in the `city` column, including duplicates. If multiple customers are from the same city, they will be counted multiple times, which does not meet the data demand for counting unique cities.

### Correction
```sql
SELECT COUNT(DISTINCT city)
FROM customer;
```

