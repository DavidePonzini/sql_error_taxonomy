## Condition on OUTER JOIN
### Definition
Using a JOIN ON condition on the left table of a LEFT OUTER JOIN affects only the right table, which can lead to unexpected results.

### Data demand
List all customer and store data for customers who live in a city where a Coop is located.

### Example
```sql
SELECT *
FROM
    customer c
    LEFT OUTER JOIN store s ON s.city = c.city AND s.sName = 'Coop';
```

### Explanation
The condition `s.sName = 'Coop'` is applied in the `ON` clause and affects how rows match on the right side. If a store's name does not satisfy the condition, the row can still appear with `NULL` values, which is not the intended behavior. To filter rows, the condition should be placed in the `WHERE` clause.

### Correction
```sql
SELECT *
FROM
    customer c
    LEFT OUTER JOIN store s ON s.city = c.city
WHERE s.sName = 'Coop';
```

