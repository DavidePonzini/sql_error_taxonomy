## Missing NOT operator
### Definition
A logical condition is missing a `NOT` operator, leading to incorrect results.

### Data demand
List customers who are older than 18 and do not live in Genoa.

### Example
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```

### Explanation
This query is intended to find customers who are older than 18 and do not live in Genoa. However, without the `NOT` operator, it returns customers who are older than 18 and live in Genoa.

### Correction
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND NOT city = 'Genoa';
```