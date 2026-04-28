## DISTINCT as function parameter where not applicable
### Definition
DISTINCT is used within a function where it is not appropriate or necessary.

### Data demand
Count the number of customers whose age is known.

### Example
```sql
SELECT COUNT(DISTINCT age)
FROM customer;
```

### Explanation
`DISTINCT` causes `COUNT` to count unique ages only. Multiple customers with the same age are counted as one.

### Correction
```sql
SELECT COUNT(age)
FROM customer;
```

