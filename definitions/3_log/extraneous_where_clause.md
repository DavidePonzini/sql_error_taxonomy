## Extraneous WHERE clause
### Definition
A `WHERE` clause is included in the query when the data demand does not require any filtering of results.

### Data demand
List the names of all customers.

### Example
```sql
SELECT cName
FROM customer
WHERE city = 'Genoa';
```

### Explaination
The data demand is to list the names of all customers, regardless of their city. The inclusion of the `WHERE` clause filters the results to only include customers from Genoa, which is not what the data demand specifies. This results in an incomplete list of customer names.

### Correction
```sql
SELECT cName
FROM customer;
```

