## Unnecessary complication
### Definition
The query is more complex than necessary to achieve the intended result.

This is an umbrella category for various types of unnecessary complications in SQL queries that do not fit into more specific categories.

### Data demand
Select the names of customers who are at least 18 years old.

### Example
```sql
SELECT cName
FROM customer
WHERE
    age > 36 / 2
    OR age = 9 * (12 - 2);
```

### Explanation
The exercise requires selecting customer at least 18 years old. However, the query uses unnecessary arithmetic operations to express the age condition, making it more complicated than needed.

### Correction
```sql
SELECT cName
FROM customer
WHERE age >= 18;
```

