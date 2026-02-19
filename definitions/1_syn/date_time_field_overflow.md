## Date time field overflow
### Definition
An invalid date or time value is used in the query.

### Example
```sql
SELECT *
FROM events
WHERE date = '2024-02-33';
```

### Explaination
The date '2024-02-33' is invalid because a month cannot have 33 days.

### Correction
```sql
SELECT *
FROM events
WHERE date = '2024-02-28';
```

