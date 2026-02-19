## Join condition on incorrect column (matches possible)
### Definition
A join condition uses the wrong column, leading to incorrect or unexpected results.

### Data demand
List stores along with their inventory. 

### Example
```sql
SELECT *
FROM store s
JOIN inventory i ON s.sID = i.pID;
```

### Explaination
The query attempts to join the `store` and `inventory` tables using the condition `s.sID = i.pID`. However, `sID` is the store ID and `pID` is the product ID, so this condition does not correctly relate the two tables. As a result, the query will not return the intended results of listing stores along with their inventory.

### Correction
```sql
SELECT *
FROM store s
JOIN inventory i ON s.sID = i.sID;
```

