## Unmatched brackets
### Definition
Curly and square brackets are used instead of parentheses, or parentheses are unmatched.

### Example
```sql
SELECT * FROM students WHERE age > ((15 + 18) * 2) / (7 + 3;
```

### Explaination
Use only parentheses () for grouping expressions in SQL, and ensure that all opening parentheses have a corresponding closing parenthesis.

### Correction
```sql
SELECT * FROM students WHERE age > ((15 + 18) * 2) / (7 + 3);
```

