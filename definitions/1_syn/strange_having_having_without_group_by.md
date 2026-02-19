## Strange HAVING: HAVING without GROUP BY
### Definition
The query uses a HAVING clause without a corresponding GROUP BY clause.

### Example
```sql
SELECT * FROM students HAVING AVG(score) > 80;
```

### Explaination
The HAVING clause is used to filter grouped results and should always be used in conjunction with a GROUP BY clause.

### Correction
```sql
SELECT class, AVG(score) FROM students GROUP BY class HAVING AVG(score) > 80;
```

