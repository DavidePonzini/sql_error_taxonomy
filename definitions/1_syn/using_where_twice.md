## Using WHERE twice
### Definition
The query contains multiple `WHERE` clauses, which is not allowed.

### Example
```sql
SELECT *
FROM customer
WHERE age > 18
WHERE city = 'Genoa';
```

### Explaination
A query can only have one `WHERE` clause. Combine multiple conditions using logical operators like `AND` or `OR`.

### Correction
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```

