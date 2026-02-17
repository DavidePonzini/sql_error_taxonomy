# Lightweight SQL Error Taxonomy

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

## Documentation

- **Error definitions:** see [`ERROR_DEFINITIONS.md`](ERROR_DEFINITIONS.md)

## References

[^taipalus_errors_complication_2018]: Toni Taipalus, Mikko Siponen, and Tero Vartiainen. 2018. *Errors and Complications in SQL Query Formulation.* ACM Trans. Comput. Educ. 18, 3, Article 15 (September 2018), 29 pages. https://doi.org/10.1145/3231712
