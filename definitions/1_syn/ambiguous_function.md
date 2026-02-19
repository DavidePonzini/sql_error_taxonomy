## Ambiguous function
### Definition
Multiple functions with the same name exist, and the query does not specify which one to use.

### Example
```sql
CREATE FUNCTION my_function(interval) RETURNS text AS $$
    SELECT 'Interval';
$$ LANGUAGE sql;

CREATE FUNCTION my_function(time) RETURNS text AS $$
    SELECT 'Time';
$$ LANGUAGE sql;

SELECT my_function(NULL);
```

### Explaination
There are two functions named `my_function`, one that takes an interval and another that takes a time. The query does not specify which function to use, leading to ambiguity.

### Correction
```sql
SELECT my_function(NULL::interval);
```

### Note
This error is very complex to trigger, since most DBMSs automatically convert data types to the most suitable one.