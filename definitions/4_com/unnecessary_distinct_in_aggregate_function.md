## Unnecessary DISTINCT in aggregate function
### Definition
`DISTINCT` is used within an aggregate function where all values are already unique, making it redundant.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT COUNT(DISTINCT cID)
FROM customer;
```

### Explaination
The `cID` column is a primary key, meaning each value is unique. Therefore, using `DISTINCT` within the `COUNT` function doesn't change the result, as there cannot be any duplicate ids to count.

### Correction
```sql
SELECT COUNT(cID)
FROM customer;
```

