## GROUP BY with only a single group
### Definition
`GROUP BY` is used in a way that results in only a single group, making the grouping unnecessary.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT AVG(age)
FROM customer
WHERE city = 'Genoa'
GROUP BY city;
```

### Explaination
The query groups customers by city, but the `WHERE` clause filters the results to only include customers from Genoa. This means that there will be only one group (Genoa) in the result, making the `GROUP BY` clause unnecessary. The same result can be achieved without grouping, as we are only interested in the average age of customers from Genoa.

### Correction
```sql
SELECT AVG(age)
FROM customer
WHERE city = 'Genoa';
```

