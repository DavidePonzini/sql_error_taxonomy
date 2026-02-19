## IN/EXISTS can be replaced by comparison
### Definition
A subuery using `IN` or `EXISTS` can be simplified to a direct comparison.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT *
FROM customer
WHERE cID IN (SELECT cID FROM customer WHERE age < 18);
```

### Explaination
The query is intended to find customers who are younger than 18. However, it uses a subquery with `IN`, which can be simplified to a direct comparison. Since `cID` is a unique identifier, we can directly compare the age without needing a subquery.

### Correction
```sql
SELECT * FROM customer WHERE age < 18;
```

