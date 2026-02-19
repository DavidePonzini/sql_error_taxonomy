## GROUP BY with only a single group
### Definition
GROUP BY is used in a way that results in only a single group, making the grouping unnecessary.

### Example
```sql
SELECT AVG(age) FROM students WHERE country = 'IT' GROUP BY country;
```

### Explaination
The query groups the students by country after filtering for those in 'IT'. Since all remaining rows belong to the same country, there is only a single group. Therefore, using GROUP BY is unnecessary, as it does not change the result set.

### Correction
```sql
SELECT AVG(age) FROM students WHERE country = 'IT';
```

