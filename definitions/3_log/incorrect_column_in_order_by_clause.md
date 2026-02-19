## Incorrect column in ORDER BY clause
### Definition
An incorrect column is used in the ORDER BY clause, leading to results being sorted in an unintended manner.

### Example
```sql
SELECT name, age FROM students ORDER BY city;
```

### Explaination
The exercise requires the results to be ordered by name, but the query incorrectly orders the results by city instead.

### Correction
```sql
SELECT name, age FROM students ORDER BY name;
```

