## LIKE without wildcards
### Definition
The `LIKE` operator is used without any wildcard characters, making it equivalent to a simple equality comparison.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT *
FROM customer
WHERE cName LIKE 'John';
```

### Explanation
The query uses the `LIKE` operator to compare the `cName` column to the string 'John' without any wildcard characters (such as `%` or `_`). This means that the `LIKE` operator is functioning as a simple equality comparison, and there is no need for it in this context.

### Correction
```sql
SELECT *
FROM customer
WHERE cName = 'John';
```

