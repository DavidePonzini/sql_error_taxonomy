## Omitting the FROM clause
### Definition
The query is missing the `FROM` clause and does not select a constant value.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT cName
WHERE age > 18;
```

### Explaination
The `FROM` clause is required in a SELECT statement to specify the table from which to retrieve data.

### Correction
```sql
SELECT cName
FROM customer
WHERE age > 18;
```

