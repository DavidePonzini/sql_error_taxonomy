## Invalid schema cName
### Definition
The query references a schema that does not exist or is not defined.

### Example
```sql
SELECT *
FROM shop.customer;
```

### Explaination
The schema `shop` does not exist in the database. In this example, the customer table resides in the `public` schema.

### Correction
```sql
SELECT *
FROM public.customer;
```

