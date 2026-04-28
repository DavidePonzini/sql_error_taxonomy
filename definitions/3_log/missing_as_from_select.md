## Missing AS from SELECT
### Definition
A column presents a different name from what is required by the exercise, due to the absence of an `AS` alias.

### Data demand
List the names of all customers, labeling the output column as `name`.

### Example
```sql
SELECT cName
FROM customer;
```

### Explanation
The query retrieves the names of all customers, but it does not label the output column as `name`, which is required by the data demand.

### Correction
```sql
SELECT cName AS name
FROM customer;
```

