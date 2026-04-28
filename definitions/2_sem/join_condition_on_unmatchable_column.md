## Join condition on unmatchable column
### Definition
A join condition is performed on columns that cannot logically match, resulting in an empty result set.

### Data demand
*(Not relevant, semantic errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM
    store s
    JOIN inventory i ON s.sID = i.unit_price;
```

### Explanation
This query attempts to join the `store` and `inventory` tables based on the condition that a stores's `sID` equals the inventory's `unit_price`. Since `sID` and `unit_price` are fundamentally different types of data, this join condition is illogical and will likely result in no matching rows.

### Correction
```sql
SELECT *
FROM
    store s
    JOIN inventory i ON s.sID = i.sID;
```

