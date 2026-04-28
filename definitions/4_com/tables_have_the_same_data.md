## Tables have the same data
### Definition
The query references two tables that always contain the same data.

### Data demand
*(Not relevant)*

### Example
```sql
SELECT *
FROM
    customer a
    JOIN customer b ON a.cID = b.cID;
```

### Explanation
The query joins the customer table with itself on the `cID` column, which is a primary key. Since each `cID` is unique, the join will always pair each customer with themselves, resulting in identical data from both tables. This redundancy adds unnecessary complexity without any benefit.

### Correction
```sql
SELECT *
FROM customer;
```

