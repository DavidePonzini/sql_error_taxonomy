## Incorrect ordering of rows
### Definition
The ORDER BY clause sorts the results in the wrong order (ascending instead of descending, or vice versa).

### Example
```sql
SELECT name, age FROM students ORDER BY age ASC;
```

### Explaination
The exercise requires the results to be ordered by age in descending order, but the query sorts the results in ascending order instead.

### Correction
```sql
SELECT name, age FROM students ORDER BY age DESC;
```

