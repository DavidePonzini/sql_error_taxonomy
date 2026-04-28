## Missing quantifier
### Definition
A comparison is performed with a subquery that can possibly return multiple values, regardless of the data currently present in the database.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM inventory
WHERE unit_price >= (
    SELECT unit_price
    FROM product
    NATURAL JOIN inventory
    WHERE pName = 'Banana'
);
```

### Explanation
The value of `unit_price` is directly compared to the result of the subquery.

This works fine only if the subquery returns a single value (i.e. the `product` table contains only one entry whose cName is *'Banana'*).
However, if the table is later updated, and a new product with the same cName is added, the query becomes invalid.

This problem can be solved by using a quantifier in the comparison (ANY/ALL).

### Correction
```sql
SELECT *
FROM inventory
WHERE unit_price >= ANY(
    SELECT unit_price
    FROM product
    NATURAL JOIN inventory
    WHERE pName = 'Banana'
);
```

