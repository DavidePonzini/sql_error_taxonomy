## Mixing a >0 with IS NOT NULL or empty string with NULL
### Definition
Using > 0 or = '' to check for non-null values instead of IS NOT NULL or IS NULL.

### Example
```sql
SELECT * FROM students WHERE test_score = '';
```

### Explaination
This query erroneously attempts to find students who haven't taken the test by checking for an empty string in the test_score column. However, this query actually selects students who have taken the test and have been assigned a score of '' (empty string).

### Correction
```sql
SELECT * FROM students WHERE test_score IS NULL;
```

