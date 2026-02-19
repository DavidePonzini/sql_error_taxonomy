## AND instead of OR
### Definition
Query uses `AND` where `OR` is needed.

### Data demand
List customers who are older that 18, as well as those who live in Genoa, regardless of their age.

### Example
```sql
SELECT *
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```


### Explaination
This query finds customers older than 18 who live in Genoa. However, this does not match the data demand. In this case, `OR` should have been used instead of `AND`.

### Correction
```sql
SELECT *
FROM customer
WHERE 
    age > 18
    OR city = 'Genoa';
```

