## Incorrect table reference
### Definition
The query references the wrong table, leading to incorrect or unexpected results.

### Data demand
List the cities where customers are located.

### Example
```sql
SELECT DISTINCT city
FROM store;
```

### Explanation
The query references the `store` table instead of the `customer` table, which is where the city information for customers is stored. As a result, it retrieves cities from the `store` table rather than from the `customer` table, which does not meet the data demand.

### Correction
```sql
SELECT DISTINCT city
FROM customer;
```

