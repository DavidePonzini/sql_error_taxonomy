## Omitting quotes around character data
### Definition
Character data values are not enclosed in quotes, which is required for string literals.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE cName = John;
```

### Explaination
Character data values must be enclosed in single quotes (`'`) to be recognized as string literals.

### Correction
```sql
SELECT *
FROM customer
WHERE cName = 'John';
```

