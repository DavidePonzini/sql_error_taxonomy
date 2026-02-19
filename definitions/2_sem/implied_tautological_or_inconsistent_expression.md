## Implied, tautological or inconsistent expression
### Definition
Query contains expressions that are always true, always false, or logically redundant.

### Example
```sql
SELECT * FROM students WHERE age > 10 AND age > 5 AND name = name;
```

### Explaination
The expression age > 10 AND age > 5 is redundant because if age is greater than 10, it is inherently greater than 5. Additionally, the condition name = name is always true for all rows. Simplifying the query to remove these redundancies will improve clarity and performance.

### Correction
```sql
SELECT * FROM students WHERE age > 10;
```

