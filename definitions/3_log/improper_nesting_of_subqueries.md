## Improper nesting of subqueries
### Definition
Subqueries are nested improperly, leading to a different evaluation order than intended.

### Data demand
List all stores that have items in inventory but none of those items have suffix `XL`.

### Example
```sql
SELECT *
FROM store s
WHERE NOT EXISTS (
  SELECT 1
  FROM inventory i
  WHERE i.sID = s.sID
    AND EXISTS (
      SELECT 1
      FROM product p
      WHERE p.pID = i.pID
        AND p.suffix = 'XL'
    )
);
```

### Explaination
This query is intended to enforce two separate conditions: the store has inventory rows, and none of those rows refers to a product with suffix `XL`. Nesting `EXISTS` inside `NOT EXISTS` leads to selecting stores that do not have any inventory rows at all, which is not the intended outcome. The correct approach is to use two separate `EXISTS` conditions at the same level.

### Correction
```sql
SELECT *
FROM store s
WHERE EXISTS (
  SELECT 1
  FROM inventory i
  WHERE i.sID = s.sID
)
AND NOT EXISTS (
  SELECT 1
  FROM inventory i
  JOIN product p ON p.pID = i.pID
  WHERE i.sID = s.sID
    AND p.suffix = 'XL'
);
```

