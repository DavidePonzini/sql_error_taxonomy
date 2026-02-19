## AND instead of OR
### Definition
Query uses AND where OR is needed.

### Data demand
List of students who are older that 18, as well as those have received an 'A' grade, regardless of age.

### Example
```sql
SELECT * FROM students WHERE age > 18 AND grade = 'A';
```


### Explaination
This query finds students older than 18 that have received an 'A' grade. However, this does not match the data demand. In this case, `OR` should have been used instead of `AND`.

### Correction
```sql
SELECT * FROM students WHERE age > 18 OR grade = 'A';
```

