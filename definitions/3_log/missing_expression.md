## Missing expression
### Definition
A logical expression required by the data demand is missing from the query.

### Data demand
List the names of all customers who are older than 18 years and live in Genoa.

### Example
```sql
SELECT cName
FROM customer
WHERE age > 18;
```

### Explaination
The query only checks for customers older than 18 but does not filter for customers living in Genoa.

### Correction
```sql
SELECT cName
FROM customer
WHERE 
    age > 18
    AND city = 'Genoa';
```

