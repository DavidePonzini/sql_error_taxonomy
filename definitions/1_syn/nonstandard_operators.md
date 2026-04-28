## Nonstandard operators (e.g., &&, \|\| or ==)
### Definition
The query uses operators that are not part of the standard SQL syntax, such as `&&`, `||`, or `==` instead of `AND`, `OR`, or `=`.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE
    cID == 18
    && city == 'A';
```

### Explanation
The operators `==` and `&&`, although common in programming languages, are not valid in SQL. Use `=` and `AND` instead.

### Correction
```sql
SELECT *
FROM customer
WHERE
    cID = 18
    AND city = 'A';
```

