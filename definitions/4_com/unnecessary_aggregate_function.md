## Unnecessary aggregate function
### Definition
An aggregate function is used on a single value.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT MAX(age) FROM customer WHERE cID = 123;
```

### Explaination
The query retrieves the age of a specific customer with `cID = 123`. Since the `WHERE` clause filters the results to a single row, using the `MAX` aggregate function is unnecessary, as there will only be one value to return.

### Correction
```sql
SELECT age
FROM customer
WHERE cID = 123;
```

