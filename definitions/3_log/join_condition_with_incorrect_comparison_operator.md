## Join condition with incorrect comparison operator
### Definition
A join condition uses the wrong comparison operator, leading to incorrect or unexpected results.

### Data demand
List the IDs of pairs of customers who live in the same city.

### Example
```sql
SELECT c1.cID, c2.cID
FROM customer c1
JOIN customer c2 ON c1.city <> c2.city;
```

### Explaination
The query attempts to find pairs of customers who live in the same city, but it uses the `<>` operator, which means "not equal". As a result, it retrieves pairs of customers who live in different cities instead of those who live in the same city.

### Correction
```sql
SELECT c1.cID, c2.cID
FROM customer c1
JOIN customer c2 ON c1.city = c2.city;
```

