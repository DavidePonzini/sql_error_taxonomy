## Confusing table names with column names
### Definition
A table name is used where a column name is expected, or vice versa.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT city.customer
FROM customer;
```

### Explanation
This query tries to access a column called `customer` from the `city` table, which does not exist. The correct syntax is to specify the table name followed by the column name.

### Correction
```sql
SELECT customer.city
FROM customer;
```

