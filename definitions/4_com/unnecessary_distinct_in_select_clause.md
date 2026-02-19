## Unnecessary DISTINCT in SELECT clause
### Definition
`DISTINCT` is used on a `SELECT` clause where duplicate values cannot occur, adding unnecessary complexity.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT DISTINCT cID, cName
FROM customer;
```

### Explaination
The `cID` column is a primary key, meaning each value is unique. Therefore, using `DISTINCT` is redundant since there cannot be any duplicate rows in the result set.

### Correction
```sql
SELECT cID, cName
FROM customer;
```

