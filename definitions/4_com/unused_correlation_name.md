## Unused correlation name
### Definition
A correlation name (alias) is defined for a table but not used in the query.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT cName
FROM customer AS c;
```

### Explaination
The query defines a correlation name `c` for the `customer` table but does not use it anywhere in the query. This adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT cName
FROM customer;
```

