## Unnecessary column in ORDER BY clause
### Definition
A column is included in the ORDER BY clause that does not affect the ordering of the results due to functional dependencies.

### Example
```sql
SELECT id, name FROM students ORDER BY id, name;
```

### Explaination
The query orders the results by both id and name. However, since id is a primary key, it uniquely identifies each row. Therefore, ordering by name after id does not change the order of the results, making it unnecessary.

### Correction
```sql
SELECT id, name FROM students ORDER BY id;
```

