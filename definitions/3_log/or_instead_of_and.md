## OR instead of AND
### Definition
Query uses `OR` where `AND` is needed.

### Data demand
List customers older that 18 who live in Genoa.

### Example
```sql
SELECT *
FROM customer
WHERE
    age > 18
    OR city = 'Genoa';
```

### Explanation
This query finds customers who are older than 18, as well as those who live in Genoa, regardless of their age.
However, this does not match the data demand. In this case, `AND` should have been used instead of `OR`.

### Correction
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```

