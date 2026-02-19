## Wrong wildcard
### Definition
The wrong wildcard is used in a `LIKE` pattern. For example, using `%` instead of `_` to match a single character, or vice versa.

### Data demand
List all customers whose names start with 'J', followed by any single character, and then 'n'.

### Example
```sql
SELECT *
FROM customer
WHERE cName LIKE 'J%n';
```

### Explaination
This query uses the `%` wildcard, which matches any sequence of characters (including zero characters), instead of the `_` wildcard, which matches exactly one character. As a result, this query will return customers whose names start with 'J' and end with 'n', regardless of how many characters are in between, which does not satisfy the data demand.

### Correction
```sql
SELECT *
FROM customer
WHERE cName LIKE 'J_n';
```

