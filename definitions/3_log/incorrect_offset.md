## Incorrect OFFSET
### Definition
The `OFFSET` clause is used with an incorrect value.

### Data demand
List customers ordered by their names, skipping the first 5 customers.

### Example
```sql
SELECT *
FROM customer
ORDER BY cName
OFFSET 10;
```

### Explaination
The query uses an incorrect offset value of 10, which skips more customers than intended. The data demand requires skipping only the first 5 customers.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName
OFFSET 5;
```

