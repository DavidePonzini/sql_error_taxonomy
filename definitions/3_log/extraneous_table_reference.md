## Extraneous table reference
### Definition
The query references more tables than necessary, leading to incorrect or unexpected results.

### Data demand
List the names of all customers.

### Example
```sql
SELECT cName
FROM customer, store;
```

### Explanation
The query references both the `customer` and `store` tables, but the data demand only requires information from the `customer` table. The inclusion of the `store` table creates a Cartesian product, resulting in multiple rows for each customer name, which is not the intended outcome.

### Correction
```sql
SELECT cName
FROM customer;
```

