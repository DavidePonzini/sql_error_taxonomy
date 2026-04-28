## GROUP BY can be replaced with DISTINCT
### Definition
All `GROUP BY` columns are also in the `SELECT` clause without any aggregate functions, making `DISTINCT` a simpler alternative.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT city, street
FROM customer
GROUP BY city, street;
```

### Explanation
The query groups customers by `city` and `street`, but it does not perform any aggregation. Since all `GROUP BY` columns are also in the `SELECT` clause without any aggregate functions, the same result can be achieved using `DISTINCT`, which is simpler and more efficient in this case.

### Correction
```sql
SELECT DISTINCT cName, cID FROM customer;
```

