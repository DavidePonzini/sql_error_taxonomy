## Missing column from ORDER BY clause
### Definition
A required column is missing from the ORDER BY clause.

### Example
```sql
SELECT name, age FROM students ORDER BY name;
```

### Explaination
The exercise requires the results to be ordered by both name and age. However, the query only orders the results by name, omitting age from the ORDER BY clause.

### Correction
```sql
SELECT name, age FROM students ORDER BY name, age;
```

