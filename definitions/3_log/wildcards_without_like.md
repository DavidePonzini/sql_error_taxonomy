## Wildcards without LIKE
### Definition
Wildcards such as % or _ are used with `=` instead of `LIKE`, resulting in a literal comparison rather than a pattern match.

### Data demand
List all customers whose names start with 'J' and end with 'n'.

### Example
```sql
SELECT *
FROM customer
WHERE cName = 'J%n';
```

### Explaination
This query selects all customer whose name is exactly `J%n`, including the percent sign, rather than matching names that start with 'J' and end with 'n'.

### Correction
```sql
SELECT *
FROM customer
WHERE cName LIKE 'J%n';
```

