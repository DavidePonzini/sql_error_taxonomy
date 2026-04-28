## Incorrect function
### Definition
An incorrect function is used for the intended operation, leading to unexpected results.

### Data demand
Calculate the average age of customers.

### Example
```sql
SELECT SUM(age) FROM customer;
```

### Explanation
The exercise requires calculating the average age of customers, but the query uses the `SUM` function instead of `AVG`, resulting in the total age rather than the average age.

### Correction
```sql
SELECT AVG(age) FROM customer;
```

