## Exraneous ORDER BY clause
### Definition
An ORDER BY clause is included in the query when the exercise does not require any specific ordering of the results.

### Example
```sql
SELECT name, age FROM students ORDER BY name;
```

### Explaination
The exercise does not specify any ordering for the results, so including an ORDER BY clause is unnecessary and adds complexity to the query.

### Correction
```sql
SELECT name, age FROM students;
```

