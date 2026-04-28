## Invalid schema cName
### Definition
The query references a schema that does not exist or is not defined.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM shop.customer;
```

### Explanation
The schema `shop` does not exist in the database. In this example, the customer table resides in the `public` schema.

### Correction
```sql
SELECT *
FROM public.customer;
```

