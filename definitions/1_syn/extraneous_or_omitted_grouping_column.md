## Extraneous or omitted grouping column
### Definition
When using GROUP BY, all non-aggregated columns in the SELECT clause must be included in the GROUP BY clause. Only aggregated columns or columns included in the GROUP BY clause can be referenced in the HAVING clause.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT cName, AVG(unit_price)
FROM customer
GROUP BY city;
```

### Explanation
The query selects the column `cName` which is neither aggregated nor included in the `GROUP BY` clause. This leads to ambiguity about which `cName` to return for each group. To fix this, either include `cName` in the`GROUP BY` clause or remove it from the `SELECT` clause.

### Correction
```sql
SELECT city, AVG(unit_price)
FROM customer
GROUP BY city;
```

