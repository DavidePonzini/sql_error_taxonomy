## DISTINCT that might remove important duplicates
### Definition
Using `DISTINCT` removes duplicate rows from the result set, which may inadvertently exclude important data.

### Data demand
*(Not relevant, semantic errors do not depend on the data demand.)*

### Example
```sql
SELECT DISTINCT cName
from customer
WHERE city = 'Genoa';
```

### Explaination
If multiple customer share the same name and live in Genoa, using DISTINCT will return only one instance of that name, potentially omitting other customers with the same name who also live in the same city. This could lead to incomplete or misleading results.

### Correction
```sql
SELECT cName
from customer
WHERE city = 'Genoa';
```

