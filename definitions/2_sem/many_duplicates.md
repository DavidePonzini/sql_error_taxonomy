## Many duplicates
### Definition
The query returns many times the same values, making the results difficult to interpret.

### Example
```sql
SELECT city
FROM customer;
```

### Explaination
This query aims to find all the cities where customers live. However, if multiple customers live in the same city, that city will appear multiple times in the result set, leading to redundancy and making it harder to analyze the data.

### Correction
```sql
SELECT DISTINCT city
FROM customer;
```

