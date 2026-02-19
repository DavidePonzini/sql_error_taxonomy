## Unnecessary argument of COUNT
### Definition
COUNT is used with a specific column name instead of using COUNT(*) or COUNT(1) when counting non-nullable columns.

### Example
```sql
SELECT COUNT(name) FROM students;
```

### Explaination
The name column is defined as NOT NULL, meaning it cannot contain any NULL values. Therefore, using COUNT(name) is equivalent to COUNT(*), as all rows will be counted. Using COUNT(*) is more straightforward and efficient in this case.

### Correction
```sql
SELECT COUNT(*) FROM students;
```

