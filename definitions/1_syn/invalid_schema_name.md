## Invalid schema name
### Definition
The query references a schema that does not exist or is not defined.

### Example
```sql
SELECT * FROM school.students;
```

### Explaination
The schema school does not exist in the database. In this example, the students table resides in the public schema.

### Correction
```sql
SELECT * FROM public.students;
```

