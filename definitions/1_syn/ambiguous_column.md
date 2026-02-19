## Ambiguous column
### Definition
When using multiple tables in a query, a column present in more than one table is referenced without specifying which table it belongs to.

### Example
```sql
SELECT id FROM students, teachers;
```

### Explaination
Both tables contain a column named 'id'. Without specifying the table, the database cannot determine which 'id' to use.

### Correction
```sql
SELECT students.id FROM students, teachers;
```

