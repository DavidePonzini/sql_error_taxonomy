## Unnecessary column in ORDER BY clause
### Definition
A column is included in the `ORDER BY` clause that does not affect the ordering of the results due to functional dependencies.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT cID, cName
FROM customer
ORDER BY cID, cName;
```

### Explaination
The query orders the results by both `cID` and `cName`. However, since `cID` is a primary key, it uniquely identifies each row. Therefore, ordering by `cName` after `cID` does not change the order of the results, making it unnecessary.

### Correction
```sql
SELECT cID, cName
FROM customer
ORDER BY cID;
```

