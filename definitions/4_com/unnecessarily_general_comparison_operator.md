## Unnecessarily general comparison operator
### Definition
An operator used for a comparison can be replaced by a more specific one without changing the logic.

### Example
```sql
SELECT * FROM students WHERE age >= (SELECT MAX(age) FROM students);
```

### Explaination
The query is intended to find the oldest students. However, the ">" part of the operator is unnecessary because no student can be older than the maximum age. Using the more specific "=" operator makes the query clearer and more efficient.

### Correction
```sql
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
```

