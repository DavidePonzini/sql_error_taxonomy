## Table reference can be omitted
### Definition
A table is joined just to access a value which is already available as a foreign key.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT i.sID, p.pID
FROM inventory i
JOIN product p ON i.pID = p.pID;
```

### Explaination
In this query, the `product` table is joined to access the `pID` column, which is already available in the `inventory` table as a foreign key. The join is unnecessary and can be omitted without affecting the result of the query.

### Correction
```sql
SELECT i.sID, i.pID
FROM inventory i;
```

