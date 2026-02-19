## Incorrect ordering of rows
### Definition
The `ORDER BY` clause sorts the results in the wrong order (ascending instead of descending, or vice versa).

### Data demand
List customers names in reverse alphabetical order.

### Example
```sql
SELECT cName
FROM customer
ORDER BY cID;
```

### Explaination
The exercise requires the results to be ordered by `cName` in descending order, but the query sorts the results in ascending order instead.

### Correction
```sql
SELECT cName
FROM customer
ORDER BY cName DESC;
```

