## GROUP BY can be replaced with DISTINCT
### Definition
All GROUP BY columns are also in the SELECT clause without any aggregate functions, making DISTINCT a simpler alternative.

### Example
```sql
SELECT name, age FROM students GROUP BY name, age;
```

### Explaination
The query groups the students by their name and age, but does not use any aggregate functions. Since the SELECT clause only includes the grouped columns, using DISTINCT is a simpler and more efficient way to achieve the same result.

### Correction
```sql
SELECT DISTINCT name, age FROM students;
```

