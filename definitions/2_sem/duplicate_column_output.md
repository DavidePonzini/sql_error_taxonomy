## Duplicate column output
### Definition
Multiple columns in the output always contain identical values.

### Data demand
*(Not relevant, semantic errors do not depend on the data demand.)*

### Example
```sql
SELECT cID, cName, cName
FROM customer;
```

### Explanation
The query selects the `cName` column twice, resulting in duplicate data in the output. This redundancy can confuse users and make it harder to interpret the results.

### Correction
```sql
SELECT cID, cName
FROM customer;
```

