## Grouping error: extraneous or omitted grouping column
### Definition
When using GROUP BY, all non-aggregated columns in the SELECT clause must be included in the GROUP BY clause. Only aggregated columns or columns included in the GROUP BY clause can be referenced in the HAVING clause.

### Example
```sql
SELECT name, AVG(score) FROM students GROUP BY class;
```

### Explaination
The query selects the column 'name' which is neither aggregated nor included in the GROUP BY clause. This leads to ambiguity about which 'name' to return for each group. To fix this, either include 'name' in the GROUP BY clause or remove it from the SELECT clause.

### Correction
```sql
SELECT class, AVG(score) FROM students GROUP BY class;
```

