## Confusing function with function parameter
### Definition
A function is confused with its parameter, leading to incorrect query syntax or logic.

### Example
```sql
SELECT (COUNT) pName
FROM customer;
```

### Explaination
The query incorrectly uses parentheses around the function name COUNT, which makes it look like a parameter rather than a function call. The correct syntax is to use COUNT without parentheses around it.

### Correction
```sql
SELECT COUNT(pName)
FROM customer;
```

