## Unmatched brackets
### Definition
Curly and square brackets are used instead of parentheses, or parentheses are unmatched.

### Example
```sql
SELECT *
FROM customer
WHERE cID > ((15 + 18) * 2) / (7 + 3;
```

### Explaination
All opening parentheses must have a corresponding closing parenthesis.

### Correction
```sql
SELECT *
FROM customer
WHERE cID > ((15 + 18) * 2) / (7 + 3);
```

