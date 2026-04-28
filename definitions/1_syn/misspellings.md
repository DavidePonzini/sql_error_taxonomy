## Misspellings
### Definition
The query contains misspelled table names, column names, or other identifiers.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM costumer;
```

### Explanation
The table `costumer` does not exist in the database. It is a misspelling of `customer`.

### Correction
```sql
SELECT *
FROM customer;
```

