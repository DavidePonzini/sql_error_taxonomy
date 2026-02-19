## Undefined object
### Definition
The query references a table that does not exist or is not defined.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM cats;
```

### Explaination
The table `cats` does not exist in the database.

### Correction
```sql
SELECT *
FROM customer;
```

