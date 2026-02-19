## Omitting a join condition
### Definition
A query references multiple tables but does not include the necessary join conditions to connect them, leading to incomplete or incorrect results.

### Data demand
List the inventory of all stores in Genoa.

### Example
```sql
SELECT *
FROM
    store,
    inventory
WHERE
    city = 'Genoa';
```

### Explaination
This query does not include any join conditions to connect the `store` and `inventory` tables. As a result, it produces a Cartesian product of the two tables filtered only by the city condition on the `store` table. This means that it will return all combinations of stores in Genoa with all inventory items, regardless of whether those items are actually in those stores.

### Correction
```sql
SELECT *
FROM
    store
    NATURAL JOIN inventory
WHERE
    city = 'Genoa';
```

