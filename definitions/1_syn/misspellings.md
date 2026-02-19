## Misspellings
### Definition
The query contains misspelled table names, column names, or other identifiers.

### Example
```sql
SELECT *
FROM costumer;
```

### Explaination
The table `costumer` does not exist in the database. It is a misspelling of `customer`.

### Correction
```sql
SELECT *
FROM customer;
```

