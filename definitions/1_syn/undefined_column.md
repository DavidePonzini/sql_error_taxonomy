## Undefined column
### Definition
The query references a column that does not exist in the specified table(s).

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT credit_card
FROM customer;
```

### Explanation
The table customer does not contain a column named `credit_card`.

### Correction
```sql
SELECT cName
FROM customer;
```

