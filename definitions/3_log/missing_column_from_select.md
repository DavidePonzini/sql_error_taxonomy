## Missing column from SELECT
### Definition
A required column is missing from the `SELECT` clause.

### Data demand
List the names and ages of all customers.

### Example
```sql
SELECT cName
FROM customer;
```

### Explaination
The exercise requires both the names and ages of customer, but the query only selects the former.

### Correction
```sql
SELECT cName, age
FROM customer;
```

