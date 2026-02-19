## Invalid wildcard
### Definition
Invalid wildcard characters are used in pattern matching instead of the standard SQL wildcards, such as using * instead of % or using ? instead of _.

### Data demand
List all customers whose names start with 'J' and end with 'n'.

### Example
```sql
SELECT *
FROM customer
WHERE cName LIKE 'J*n';
```

### Explaination
The query uses the `*` wildcard to match any sequence of characters, which is common in other programming languages but not in SQL. In SQL, the `%` wildcard is used for pattern matching. As a result, the query does not return any results because it is looking for names that literally contain 'J*n' instead of names that start with 'J' and end with 'n'.

### Correction
```sql
SELECT *
FROM customer
WHERE cName LIKE 'J%n';
```

