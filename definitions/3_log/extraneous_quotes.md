## Extraneous quotes
### Definition
A column name is enclosed in quotes, effectively turning it into a string literal.

### Data demand
List all customers who live in a city where there is a store.

### Example
```sql
SELECT *
FROM customer c, store s
WHERE c.city = 's.city';
```

### Explanation
In this query, the condition `c.city = 's.city'` compares the `city` column of the `customer` table to the string literal `'s.city'`, which is not correct.
To compare the `city` column of both tables, the quotes around `s.city` must be removed.

### Correction
```sql
SELECT *
FROM customer c, store s
WHERE c.city = s.city;
```

