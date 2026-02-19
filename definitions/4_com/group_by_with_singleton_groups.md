## GROUP BY with singleton groups
### Definition
`GROUP BY` is used on groups that each contain only a single row, making the grouping unnecessary.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT cID, AVG(age)
FROM customer
GROUP BY cID;
```

### Explaination
The query groups customers by their unique identifier `cID`, which means that each group will contain only one customer. Since there is only one row in each group, the `GROUP BY` clause does not serve any purpose, and the same result can be achieved without grouping.

### Correction
```sql
SELECT cID, age
FROM customer;
```

