## Ambiguous column
### Definition
When using multiple tables in a query, a column present in more than one table is referenced without specifying which table it belongs to.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT city
FROM customer, store;
```

### Explaination
Both tables contain a column named `city`. Without qualifying the table, the database cannot determine which `city` column to use.

### Correction
```sql
SELECT customer.city
FROM customer, store;
```
