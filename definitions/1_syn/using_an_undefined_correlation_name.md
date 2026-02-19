## Using an undefined correlation cName
### Definition
The query references a correlation name (alias) that has not been defined.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT c2.cName
FROM customer AS c;
```

### Explaination
This query renames the customer table to `c` but then tries to reference it as `c2`, which is not defined.

### Correction
```sql
SELECT c.cName
FROM customer AS c;
```

