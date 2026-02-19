## Expression on incorrect column
### Definition
A logical expression required by the data demand is present in the query, but on the wrong column.

### Data demand
List the IDs of all Coop stores.

### Example
```sql
SELECT sID
FROM store
WHERE street = 'Coop';
```

### Explaination
The condition `= 'Coop'` is correct, but it should be applied on the `sName` column, instead of the `street` column.

### Correction
```sql
SELECT sID
FROM store
WHERE sName = 'Coop';
```

