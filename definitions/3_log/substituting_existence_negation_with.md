## Substituting existence negation with <>
### Definition
The query uses `<>` to check for non-existence instead of `NOT IN` or `NOT EXISTS`.

### Data demand
List all stores that do not have any inventory items that cost 5.

### Example
```sql
SELECT *
FROM store s
WHERE EXISTS (
    SELECT 1
    FROM inventory i
    WHERE
        i.sID = s.sID
        AND i.unit_price <> 5
);
```

### Explaination
This query uses `<>` to check for inventory items that do not cost 5, but it does not correctly enforce the condition that there should be no inventory items that cost 5. Instead, it checks if there exists at least one inventory item that does not cost 5, which is not the intended logic. The correct approach is to use `NOT EXISTS` to ensure that there are no inventory items with a unit price of 5 for each store.


### Correction
```sql
SELECT *
FROM store s
WHERE NOT EXISTS (
    SELECT 1
    FROM inventory i
    WHERE
        i.sID = s.sID
        AND i.unit_price = 5
);
```

