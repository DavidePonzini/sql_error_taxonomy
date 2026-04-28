## Unnecessarily general comparison operator
### Definition
An operator used for a comparison can be replaced by a more specific one without changing the logic.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT *
FROM customer
WHERE age >= (
    SELECT MAX(age)
    FROM customer
);
```

### Explanation
The query is intended to find the oldest customer. However, the `>=` part of the operator is unnecessary because no customer can be older than the maximum age. Using the more specific `=` operator makes the query clearer and more efficient.

### Correction
```sql
SELECT *
FROM customer
WHERE age = (
    SELECT MAX(age)
    FROM customer
);
```

