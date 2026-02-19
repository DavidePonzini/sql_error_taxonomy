## Nonstandard keywords or standard keywords in wrong context
### Definition
The query uses invalid keywords or standard keywords in inappropriate contexts.

### Example
```sql
SELECT *
FROM customer
SORT BY cName;
```

### Explaination
The correct keyword for sorting results in SQL is `ORDER BY`, not `SORT BY`.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName;
```

