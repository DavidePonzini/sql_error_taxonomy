## Undefined column
### Definition
The query references a column that does not exist in the specified table(s).

### Example
```sql
SELECT credit_card
FROM customer;
```

### Explaination
The table customer does not contain a column named `credit_card`.

### Correction
```sql
SELECT cName
FROM customer;
```

