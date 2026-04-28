## Date time field overflow
### Definition
An invalid date or time value is used in the query.

### Data demand
*(Not relevant, syntax errors do not depend on the data demand.)*

### Example
```sql
SELECT *
FROM events
WHERE date = '2024-02-33';
```

### Explanation
The date '2024-02-33' is invalid because a month cannot have 33 days.

### Correction
```sql
SELECT *
FROM events
WHERE date = '2024-02-28';
```

