## Extraneous column in SELECT
### Definition
A column is included in the `SELECT` clause that is not expected or needed for the intended result.

### Data demand
List IDs and named of all customers.

### Example
```sql
SELECT cID, cName, street
FROM customer;
```

### Explaination
The data demand requires only the IDs and names of customers, but the query also includes the `street` column in the SELECT clause. This adds unnecessary data to the result set.

### Correction
```sql
SELECT cID, cName
FROM customer;
```

