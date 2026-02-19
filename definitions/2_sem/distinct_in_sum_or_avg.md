## DISTINCT in SUM or AVG
### Definition
Using `DISTINCT` within `SUM` or `AVG` means that only unique values are summed or averaged, which is almost never the intended behavior.

### Example
```sql
SELECT AVG(DISTINCT age)
FROM customer;
```

### Explaination
This query first considers all the unique customer ages (each value is counted only once) and then calculates the average of those unique ages.
If there are 200 customer aged 20 and 1 customer aged 30, the average will be `(20 + 30) / 2 = 25`, which does not accurately reflect the average age of all customers.

### Correction
```sql
SELECT AVG(age)
FROM customer;
```

