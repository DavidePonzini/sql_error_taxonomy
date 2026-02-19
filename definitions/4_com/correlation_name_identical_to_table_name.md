## Correlation name identical to table name
### Definition
The query defines a correlation name (alias) for a table that is the same as the original table name, making the alias redundant.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT *
FROM customer AS customer;
```

### Explaination
The query defines a correlation name (alias) `customer` for the `customer` table, which is identical to the original table name. This redundancy adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT *
FROM customer;
```

