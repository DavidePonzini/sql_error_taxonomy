## Extraneous NOT operator
### Definition
A logical condition uses `NOT` where it is not needed, leading to incorrect results.

### Data demand
List customers who are older than 18 and live in Genoa.

### Example
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND NOT city = 'Genoa';
```

### Explaination
This query is intended to find customers who are older than 18 and live in Genoa. However, the `NOT` operator negates the city condition, resulting in customers who are older than 18 but do not live in Genoa.

### Correction
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```

