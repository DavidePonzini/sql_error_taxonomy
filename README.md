# SQL Error Taxonomy

This repository provides a lightweight SQL error taxonomy aimed at supporting uniform error classification in educational and automated settings.

It is based on the taxonomy proposed by Taipalus et al. [^taipalus_errors_complication_2018], with revisions introduced in our work to address ambiguities and limitations encountered when applying the taxonomy in automated SQL error-detection pipelines. The revised taxonomy refines error definitions, clarifies labels, and improves suitability for algorithmic classification.

## Top-level categories

SQL errors can be organized into four categories:

1. **Syntax errors:** the query contains invalid SQL syntax and cannot be executed. No result set is produced.  
   - *Example:* `SELECT WHERE *;`  
   - This query is invalid since it's missing which columns to select, the entire `FROM` clause, and it has an invalid condition in the `WHERE` clause.

2. **Semantic errors:** the query produces a result set which is always useless, regardless of the data present in the database, and regardless of its data demand.  
   - *Example:* `SELECT * FROM table WHERE 1=0;`  
   - Regardless of the data demand, this query will always return an empty set, since the condition is always false.

3. **Logic errors:** the query produces a valid set, but it does not satisfy its data demand.  
   - *Example:* `SELECT cID FROM customer WHERE city = 'Turin';`  
   - *Data demand:* Select the IDs of customers who live in Genoa  
   - This query is valid, but it does not satisfy the data demand, since it lists the IDs of customers who live in Turin, instead of those who live in Genoa.

4. **Complications:** the query satisfies its data demand, but in an overly complex way.  
   - *Example:* `SELECT city FROM store GROUP BY city;`  
   - *Data demand:* List all cities in which stores are located, without repetitions.  
   - Even though the query returns the correct result, using `GROUP BY` (instead of `SELECT DISTINCT`) just to remove duplicate values is both less efficient and harder to read.

## Taxonomy

**Error definitions:** see [`ERROR_DEFINITIONS.md`](ERROR_DEFINITIONS.md)


### Syntax errors
| Subcategory | ID  | Name
| :---------- | :-: | :---
| **Ambiguous database object**
|             | 1   | [Ambiguous column](ERROR_DEFINITIONS.md#ambiguous-column)
|             | 2   | [Ambiguous function](ERROR_DEFINITIONS.md#ambiguous-function)
| **Undefined database object**
|             | 3   | [Undefined column](ERROR_DEFINITIONS.md)
|             | 4   | [Undefined function](ERROR_DEFINITIONS.md)
|             | 5   | [Undefined parameter](ERROR_DEFINITIONS.md)
|             | 6   | [Undefined object](ERROR_DEFINITIONS.md)
|             | 7   | [Invalid schema name](ERROR_DEFINITIONS.md)
|             |     | [Misspellings](ERROR_DEFINITIONS.md)
|             |     | [Synonyms](ERROR_DEFINITIONS.md)
|             |     | [Omitting quotes around character data](ERROR_DEFINITIONS.md)
| **Data type mismatch**
|             |     | [Failure to specify column name twice](ERROR_DEFINITIONS.md)
|             |     | [Data type mismatch](ERROR_DEFINITIONS.md)
| **Illegal aggregate function placement**
|             |     | [Using aggregate function outside SELECT or HAVING](ERROR_DEFINITIONS.md)
|             |     | [Grouping error: aggregate functions cannot be nested](ERROR_DEFINITIONS.md)
| **Illegal or insufficient grouping**
|             |     | [Grouping error: extraneous or omitted grouping column](ERROR_DEFINITIONS.md)
|             |     | [Strange HAVING: HAVING without GROUP BY](ERROR_DEFINITIONS.md)
| **Common syntax error**
|             |     | [Confusing function with function parameter](ERROR_DEFINITIONS.md)
|             |     | [Using WHERE twice](ERROR_DEFINITIONS.md)
|             |     | [Omitting the FROM clause](ERROR_DEFINITIONS.md)
|             |     | [Comparison with NULL](ERROR_DEFINITIONS.md)
|             |     | [Omitting the semicolon](ERROR_DEFINITIONS.md)
|             |     | [Date time field overflow](ERROR_DEFINITIONS.md)
|             |     | [Duplicate clause](ERROR_DEFINITIONS.md)
|             |     | [Using an undefined correlation name](ERROR_DEFINITIONS.md)
|             |     | [Too many columns in subquery](ERROR_DEFINITIONS.md)
|             |     | [Confusing table names with column names](ERROR_DEFINITIONS.md)
|             |     | [Restriction in SELECT clause (e.g., SELECT fee >10)](ERROR_DEFINITIONS.md)
|             |     | [Projection in WHERE clause (e.g., WHERE firstname, surname)](ERROR_DEFINITIONS.md)
|             |     | [Confusing the order of keywords (e.g., FROM customer SELECT fee)](ERROR_DEFINITIONS.md)
|             |     | [Confusing the logic of keywords (e.g. grouping instead of ordering)](ERROR_DEFINITIONS.md)
|             |     | [Confusing the syntax of keywords (e.g., LIKE ('A,' 'B'))](ERROR_DEFINITIONS.md)
|             |     | [Omitting commas](ERROR_DEFINITIONS.md)
|             |     | [Curly, square or unmatched brackets](ERROR_DEFINITIONS.md)
|             |     | [IS where not applicable](ERROR_DEFINITIONS.md)
|             |     | [Nonstandard keywords or standard keywords in wrong context](ERROR_DEFINITIONS.md)
|             |     | [Nonstandard operators (e.g., &&, \|\| or ==)](ERROR_DEFINITIONS.md)
|             |     | [Additional semicolon](ERROR_DEFINITIONS.md)


### Semantic errors
| Subcategory | ID  | Name
| :---------- | :-: | :---
|             |     | 

### Logic errors
| Subcategory | ID  | Name
| :---------- | :-: | :---
|             |     | 

### Complications
| Subcategory | ID  | Name
| :---------- | :-: | :---
|             |     | 


## References

[^taipalus_errors_complication_2018]: Toni Taipalus, Mikko Siponen, and Tero Vartiainen. 2018. *Errors and Complications in SQL Query Formulation.* ACM Trans. Comput. Educ. 18, 3, Article 15 (September 2018), 29 pages. https://doi.org/10.1145/3231712
