## Missing column from ORDER BY clause
### Definition
A required column is missing from the `ORDER BY` clause.

### Data demand
List the names and ages of all customers, ordered by their names and then by their ages.

### Example
```sql
SELECT cName, age
FROM customer
ORDER BY cName;
```

### Explanation
The query retrieves the names and ages of all customers but only orders the results by `cName`. 
Customers with the same name are unsorted within their group.

### Correction
```sql
SELECT cName, age
FROM customer
ORDER BY cName, age;
```

