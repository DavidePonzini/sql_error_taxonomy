## Incorrect column as function parameter
### Definition
An incorrect column is used as a parameter for a function, leading to unintended results.

### Example
```sql
SELECT EXTRACT(month FROM birthdate) FROM students;
```

### Explaination
The exercise asks for the month the students graduated, but the query extracts the month of their birthdate instead.

### Correction
```sql
SELECT EXTRACT(month FROM graduation_date) FROM students;
```

