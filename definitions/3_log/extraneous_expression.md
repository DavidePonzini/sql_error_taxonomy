## Extraneous expression
### Definition
A logical expression not required by the data demand is present in the query.

### Data demand
List the IDs of all Coop stores.

### Example
```sql
SELECT sID
FROM store
WHERE
    sName = 'Coop'
    AND city = 'Genoa';
```

### Explaination
The query lists all Coop stores located in Genoa, which is not what the data demand required. The extraneous condition `city = 'Genoa'` should be removed.

### Correction
```sql
SELECT sID
FROM store
WHERE sName = 'Coop';
```

