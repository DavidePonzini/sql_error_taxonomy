## Strange HAVING: HAVING without GROUP BY
### Definition
The query uses a `HAVING` clause without a corresponding `GROUP BY` clause.

### Example
```sql
SELECT *
FROM customer HAVING AVG(age) > 18;
```

### Explaination
The `HAVING` clause is used to filter grouped results and should always be used in conjunction with a `GROUP BY` clause.

### Correction
```sql
SELECT city, AVG(age)
FROM customer
GROUP BY city
HAVING AVG(age) > 18;
```

