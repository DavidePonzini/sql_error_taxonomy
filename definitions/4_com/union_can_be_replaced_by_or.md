## UNION can be replaced by OR
### Definition
Two `SELECT` statements combined with `UNION` select the same data from the same table and have mutually exclusive conditions. In such cases, the `UNION` can be replaced by a single `SELECT` statement with an `OR` condition.

### Data demand
List the IDs and names of customers who are either younger than 18 or older than 30.

### Example
```sql
SELECT cID, cName
FROM customer
WHERE age < 18
UNION
SELECT cID, cName
FROM customer
WHERE age > 30;
```

### Explanation
The two queries retrieve names of customer from disjoint age groups (younger than 18 and older than 30). Since there is no overlap between these two groups, the same result can be achieved with a single query using an `OR` condition, which is more efficient and easier to read.

### Correction
```sql
SELECT cID, cName
FROM customer
WHERE
    age < 18
    OR age > 30;
```
