## Using WHERE twice
### Definition
The query contains multiple `WHERE` clauses, which is not allowed.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE age > 18
WHERE city = 'Genoa';
```

### Explanation
A query can only have one `WHERE` clause. Combine multiple conditions using logical operators like `AND` or `OR`.

### Correction
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```

