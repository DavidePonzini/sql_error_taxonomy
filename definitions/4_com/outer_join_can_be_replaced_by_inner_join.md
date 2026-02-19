## OUTER JOIN can be replaced by INNER JOIN
### Definition
Using a `WHERE` condition on the right table of a `LEFT OUTER JOIN` effectively turns it into an `INNER JOIN`.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT s.cName, t.sName
FROM
    customer c
    LEFT OUTER JOIN store s ON c.cID = s.sID
WHERE s.city = 'Genoa';
```

### Explaination
The query uses a `LEFT OUTER JOIN` to join the `customer` and `store` tables, but the `WHERE` clause removes any `NULL` values from the right table, which means that only matching rows will be returned. This effectively turns the `LEFT OUTER JOIN` into an `INNER JOIN`, making the use of `LEFT OUTER JOIN` unnecessary in this context.

### Correction
```sql
SELECT c.cName, s.sName
FROM
    customer c
    INNER JOIN store s ON c.cID = s.sID
WHERE s.city = 'Genoa';
```

