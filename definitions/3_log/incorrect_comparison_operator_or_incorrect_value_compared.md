## Incorrect comparison operator or incorrect value compared
### Definition
A condition uses the wrong comparison operator or compares against an incorrect value, leading to unintended results.

### Data demand
List customers who are older than 18 years old.

### Example
```sql
SELECT *
FROM customer
WHERE age < 18;
```

### Explaination
The query uses the `<` operator instead of `>`, which results in listing customers who are younger than 18 instead of those who are older.

### Correction
```sql
SELECT *
FROM customer
WHERE age > 18;
```

