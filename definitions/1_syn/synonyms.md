## Synonyms
### Definition
The query uses synonyms or alternative names for tables or columns that do not exist.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM clients;
```

### Explaination
The table `clients` does not exist in this schema. It is used as a synonym for `customer`, which is the correct table name.

### Correction
```sql
SELECT *
FROM customer;
```

