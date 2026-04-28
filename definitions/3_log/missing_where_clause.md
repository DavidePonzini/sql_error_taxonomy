## Missing WHERE clause
### Definition
A `WHERE` clause is missing from the query when the data demand requires filtering of results based on specific conditions.

### Data demand
List the names of all customers older than 18 and living in the city of Genoa.

### Example
```sql
SELECT cName
FROM customer;
```

### Explanation
The query does not satisfy its data demand, since it does not include a `WHERE` clause to filter the results based on the specified conditions of age and city. As a result, it returns the names of all customers, regardless of their age or city of residence, which is not what the data demand specifies.

### Correction
```sql
SELECT cName
FROM customer
WHERE
    age > 18
    AND city = 'Genoa';
```
