## Unnecessary argument of COUNT
### Definition
`COUNT` is used with a specific column name instead of using `COUNT(*)` or `COUNT(1)` when counting non-nullable columns.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT COUNT(cID)
FROM customer;
```

### Explanation
The `cID` column is the primary key of the `customer` table and as such it cannot contain any `NULL` values. Therefore, using `COUNT(cID)` is equivalent to `COUNT(*)`, as all rows will be counted. Using `COUNT(*)` is more straightforward and efficient in this case.

### Correction
```sql
SELECT COUNT(*)
FROM customer;
```

