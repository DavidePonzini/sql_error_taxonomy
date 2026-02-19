## Constant column output
### Definition
A column in the output has the same constant value for all rows.

### Example
```sql
SELECT cName, city
WHERE city = 'Genoa'
FROM customer;
```

### Explaination
The `city` column does not provide any useful information because it has the same value (*'Genoa'*) for all customer in the result set. This redundancy can clutter the output and make it harder to focus on relevant data.

### Correction
```sql
SELECT cName
FROM customer
WHERE city = 'Genoa';
```

