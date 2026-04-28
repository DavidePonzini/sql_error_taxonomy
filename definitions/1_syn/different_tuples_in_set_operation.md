## Different tuples in set operation
### Definition
Two queries combined with a set operation (`UNION`/`INTERSECT`/`EXCEPT`) return tuples with different cardinalities.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT city
FROM customer
UNION
SELECT city, street
FROM store;
```

### Explanation
The former SELECT returns a single column (`city`), while the latter returns two columns (`city` and `street`).
Set operations require both results to have the same number of columns.

### Correction
```sql
SELECT city
FROM customer
UNION
SELECT city
FROM store;
```

