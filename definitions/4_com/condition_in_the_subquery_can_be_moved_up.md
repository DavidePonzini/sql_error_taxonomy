## Condition in the subquery can be moved up
### Definition
A condition in a subquery references only values from the outer query and can be moved to the outer clause.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT cName
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM store s
    WHERE
        s.sName = c.cName
        AND c.age > 18
    );
```

### Explaination
The condition `c.age > 18` in the subquery only references the outer query's table `customer`. Therefore, it can be moved to the outer `WHERE` clause, which can improve query readability and potentially performance.

### Correction
```sql
SELECT cName
FROM customer c
WHERE
    c.age > 18
    AND EXISTS (
        SELECT 1
        FROM store s
        WHERE s.sName = c.cName
    );
```

