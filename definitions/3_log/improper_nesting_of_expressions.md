## Improper nesting of expressions
### Definition
Expressions are not properly nested with parentheses, leading to incorrect evaluation order.

### Example
```sql
SELECT * FROM students WHERE age + 5 * 2 > 30;
```

### Explaination
This query is intended to find students whose age plus 5, multiplied by 2, is greater than 30. However, without proper parentheses, the multiplication operator (*) has a higher precedence than addition (+), leading to an incorrect evaluation order.

### Correction
```sql
SELECT * FROM students WHERE (age + 5) * 2 > 30;
```

