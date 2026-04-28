## Undefined parameter
### Definition
The query references a parameter that does not exist or is not defined. Also, placeholder parameters are used incorrectly.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT ?
FROM customer
WHERE cID = :param;
```

### Explanation
The query uses placeholder parameters instead of actual values.
Even though this can be valid syntax in prepared statements, it is not in regular queries.

### Correction
```sql
SELECT cName
FROM customer
WHERE cID = 1;
```

