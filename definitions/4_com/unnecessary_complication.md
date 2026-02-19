## Unnecessary complication
### Definition
The query is more complex than necessary to achieve the intended result.

### Example
```sql
SELECT name FROM students WHERE age > 36 / 2 OR age = 9 * (12 - 2);
```

### Explaination
The exercise requires selecting students at least 18 years old. However, the query uses unnecessary arithmetic operations to express the age condition, making it more complicated than needed.

### Correction
```sql
SELECT name FROM students WHERE age >= 18;
```

