## IN/EXISTS can be replaced by comparison
### Definition
A subuery using IN or EXISTS can be simplified to a direct comparison.

### Example
```sql
SELECT * FROM students WHERE id NOT IN (SELECT id FROM students WHERE age < 18);
```

### Explaination
The query finds students who are 18 years old or older by selecting those whose IDs are not in the set of IDs of students younger than 18. This can be simplified by checking the age directly, which is more straightforward and efficient.

### Correction
```sql
SELECT * FROM students WHERE age >= 18;
```

