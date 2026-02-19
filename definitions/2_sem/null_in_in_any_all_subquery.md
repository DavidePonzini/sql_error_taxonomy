## NULL in IN/ANY/ALL subquery
### Definition
Using nullable values in IN, ANY, or ALL subqueries can lead to unexpected results due to the way NULLs are handled in SQL.

### Example
```sql
SELECT * FROM students WHERE age IN (SELECT age FROM teachers);
```

### Explaination
This query attempts to find students who have the same age as any teacher. However, if the subquery returns any NULL values, the entire IN condition evaluates to UNKNOWN for those rows, which means they will not be included in the result set. This can lead to missing data if there are NULL ages in the teachers table.

### Correction
```sql
SELECT * FROM students WHERE age IN (SELECT age FROM teachers WHERE age IS NOT NULL);
```

