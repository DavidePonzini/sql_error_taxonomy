## Constant column output
### Definition
A column in the output has the same constant value for all rows.

### Example
```sql
SELECT name, country WHERE country = 'IT' FROM students;
```

### Explaination
The country column does not provide any useful information because it has the same value ('IT') for all students in the result set. This redundancy can clutter the output and make it harder to focus on relevant data.

### Correction
```sql
SELECT name FROM students WHERE country = 'IT';
```

