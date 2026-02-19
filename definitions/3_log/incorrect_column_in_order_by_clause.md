## Incorrect column in ORDER BY clause
### Definition
An incorrect column is used in the `ORDER BY` clause, leading to results being sorted in an unintended manner.

### Data demand
List all customers ordered alphabetically by their names.

### Example
```sql
SELECT *
FROM customer
ORDER BY city;
```

### Explaination
The query orders the results by the `city` column instead of the `cName` column, which is not what the data demand specifies. This results in customers being sorted by their city rather than their names.

### Correction
```sql
SELECT *
FROM customer
ORDER BY cName;
```

