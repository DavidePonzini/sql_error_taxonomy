## Improper nesting of expressions
### Definition
Expressions are not properly nested with parentheses, leading to incorrect evaluation order.

### Data demand
List customers whose age plus 5, multiplied by 2, is greater than 30.

### Example
```sql
SELECT *
FROM customer
WHERE age + 5 * 2 > 30;
```

### Explanation
In this query, the multiplication operator has a higher precedence than the addition operator. As a result, `5 * 2` is evaluated first, giving 10, and then `age + 10` is evaluated. This is not the intended calculation. The correct evaluation should be `(age + 5) * 2`, which requires proper nesting with parentheses.

### Correction
```sql
SELECT *
FROM customer
WHERE (age + 5) * 2 > 30;
```

