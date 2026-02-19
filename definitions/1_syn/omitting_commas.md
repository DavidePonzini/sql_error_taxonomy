## Omitting commas
### Definition
When listing multiple columns or values, commas are missing between them.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT cID city street
FROM customer;
```

### Explaination
This query is missing commas between the column names in the `SELECT` clause. Ensure that each column name is separated by a comma.

### Correction
```sql
SELECT cID, city, street
FROM customer;
```

