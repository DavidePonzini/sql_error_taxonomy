## Mixing a >0 with IS NOT NULL or empty string with NULL
### Definition
Using `> 0` or `= ''` to check for non-null values instead of `IS NOT NULL` or `IS NULL`.

### Data demand
*(Not relevant, semantic errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM customer
WHERE street = '';
```

### Explanation
This query erroneously attempts to find customers for whom we don't know in which street they live, by checking for an empty string in the `street` column.
However, this query actually selects customers who live in a street named `''` *(empty string)*.

### Correction
```sql
SELECT *
FROM customer
WHERE street IS NULL;
```

