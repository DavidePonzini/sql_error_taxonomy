# SQL Error Taxonomy

This repository provides a lightweight SQL error taxonomy aimed at supporting uniform error classification in educational and automated settings.

It is based on the taxonomy proposed by Taipalus et al. [^taipalus_errors2018], with revisions introduced in our work to address ambiguities and limitations encountered when applying the taxonomy in automated SQL error-detection pipelines. The revised taxonomy refines error definitions, clarifies labels, and improves suitability for algorithmic classification.

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

**Error definitions:** see [`ERROR_DEFINITIONS.md`](ERROR_DEFINITIONS.md) for detailed information on each error.
You can also use the links in the table below.


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
|             | 8   | [Misspellings](ERROR_DEFINITIONS.md)
|             | 9   | [Synonyms](ERROR_DEFINITIONS.md)
|             | 10  | [Omitting quotes around character data](ERROR_DEFINITIONS.md)
| **Data type mismatch**
|             | 11  | [Failure to specify column name twice](ERROR_DEFINITIONS.md)
|             | 12  | [IS where not applicable](ERROR_DEFINITIONS.md)
|             | 13  | [Data type mismatch](ERROR_DEFINITIONS.md)
| **Illegal aggregate function placement**
|             | 14  | [Using aggregate function outside SELECT or HAVING](ERROR_DEFINITIONS.md)
|             | 15  | [Grouping error: aggregate functions cannot be nested](ERROR_DEFINITIONS.md)
| **Illegal or insufficient grouping**
|             | 16  | [Grouping error: extraneous or omitted grouping column](ERROR_DEFINITIONS.md)
|             | 17  | [Strange HAVING: HAVING without GROUP BY](ERROR_DEFINITIONS.md)
| **Illegal or insufficient grouping**
|             | 18  | [Too many columns in subquery](ERROR_DEFINITIONS.md)
|             | 19  | [Missing quantifier](ERROR_DEFINITIONS.md)
| **Common syntax error**
|             | 20  | [Confusing function with function parameter](ERROR_DEFINITIONS.md)
|             | 21  | [Using WHERE twice](ERROR_DEFINITIONS.md)
|             | 22  | [Omitting the FROM clause](ERROR_DEFINITIONS.md)
|             | 23  | [Comparison with NULL](ERROR_DEFINITIONS.md)
|             | 24  | [Omitting the semicolon](ERROR_DEFINITIONS.md)
|             | 25  | [Date time field overflow](ERROR_DEFINITIONS.md)
|             | 26  | [Duplicate clause](ERROR_DEFINITIONS.md)
|             | 27  | [Using an undefined correlation name](ERROR_DEFINITIONS.md)
|             | 28  | [Confusing table names with column names](ERROR_DEFINITIONS.md)
|             | 29  | [Confusing the order of keywords (e.g., FROM customer SELECT fee)](ERROR_DEFINITIONS.md)
|             | 30  | [Confusing the syntax of keywords (e.g., LIKE ('A,' 'B'))](ERROR_DEFINITIONS.md)
|             | 31  | [Omitting commas](ERROR_DEFINITIONS.md)
|             | 32  | [Unmatched brackets](ERROR_DEFINITIONS.md)
|             | 33  | [Curly or square brackets](ERROR_DEFINITIONS.md)
|             | 34  | [Nonstandard keywords or standard keywords in wrong context](ERROR_DEFINITIONS.md)
|             | 35  | [Nonstandard operators (e.g., &&, \|\| or ==)](ERROR_DEFINITIONS.md)
|             | 36  | [Additional semicolon](ERROR_DEFINITIONS.md)
|             | 37  | [Different tuples in set operation](ERROR_DEFINITIONS.md)


### Semantic errors
| Subcategory | ID  | Name
| :---------- | :-: | :---
| **Inconsistent expression**
|             | 38  | [Implied, tautological or inconsistent expression](ERROR_DEFINITIONS.md)
|             | 39  | [DISTINCT in SUM or AVG](ERROR_DEFINITIONS.md)
|             | 40  | [DISTINCT that might remove important duplicates](ERROR_DEFINITIONS.md)
|             | 41  | [Mixing a >0 with IS NOT NULL or empty string with NULL](ERROR_DEFINITIONS.md)
| **Inconsistent join**
|             | 42  | [NULL in IN/ANY/ALL subquery](ERROR_DEFINITIONS.md)
|             | 43  | [Join condition on incorrect column (matches impossible)](ERROR_DEFINITIONS.md)
| **Duplicate rows**
|             | 44  | [Many duplicates](ERROR_DEFINITIONS.md)
| **Redundant column output**
|             | 45  | [Constant column output](ERROR_DEFINITIONS.md)
|             | 46  | [Duplicate column output](ERROR_DEFINITIONS.md)

### Logic errors
| Subcategory | ID  | Name
| :---------- | :-: | :---
**Operator error**
|             | 47  | [AND instead of OR](ERROR_DEFINITIONS.md)
|             | 48  | [OR instead of AND](ERROR_DEFINITIONS.md)
|             | 49  | [Extraneous NOT operator](ERROR_DEFINITIONS.md)
|             | 50  | [Missing NOT operator](ERROR_DEFINITIONS.md)
|             | 51  | [Substituting existence negation with <>](ERROR_DEFINITIONS.md)
|             | 52  | [Incorrect comparison operator or incorrect value compared](ERROR_DEFINITIONS.md)
**Join error**
|             | 53  | [Incorrect table reference](ERROR_DEFINITIONS.md)
|             | 54  | [Missing table reference](ERROR_DEFINITIONS.md)
|             | 55  | [Extraneous table reference](ERROR_DEFINITIONS.md)
|             | 56  | [Join condition on incorrect column (matches possible)](ERROR_DEFINITIONS.md)
|             | 57  | [Join condition with incorrect comparison operator](ERROR_DEFINITIONS.md)
|             | 58  | [Omitting a join condition](ERROR_DEFINITIONS.md)
|             | 59  | [Condition on OUTER JOIN](ERROR_DEFINITIONS.md)
**Nesting error**
|             | 60  | [Improper nesting of expressions](ERROR_DEFINITIONS.md)
|             | 61  | [Improper nesting of subqueries](ERROR_DEFINITIONS.md)
**Expression error**
|             | 62  | [Extraneous quotes](ERROR_DEFINITIONS.md)
|             | 63  | [Missing expression](ERROR_DEFINITIONS.md)
|             | 64  | [Expression on incorrect column](ERROR_DEFINITIONS.md)
|             | 65  | [Extraneous expression](ERROR_DEFINITIONS.md)
|             | 66  | [Expression in incorrect clause](ERROR_DEFINITIONS.md)
|             | 67  | [Wildcards without LIKE](ERROR_DEFINITIONS.md)
|             | 68  | [Wrong wildcard](ERROR_DEFINITIONS.md)
|             | 69  | [Invalid wildcard](ERROR_DEFINITIONS.md)
**Projection error**
|             | 70  | [Extraneous column in SELECT](ERROR_DEFINITIONS.md)
|             | 71  | [Missing column from SELECT](ERROR_DEFINITIONS.md)
|             | 72  | [Missing DISTINCT from SELECT](ERROR_DEFINITIONS.md)
|             | 73  | [Missing AS from SELECT](ERROR_DEFINITIONS.md)
|             | 74  | [Missing column from ORDER BY clause](ERROR_DEFINITIONS.md)
|             | 75  | [Incorrect column in ORDER BY clause](ERROR_DEFINITIONS.md)
|             | 76  | [Incorrect ordering of rows](ERROR_DEFINITIONS.md)
**Clause error**
|             | 77  | [Missing WHERE clause](ERROR_DEFINITIONS.md)
|             | 78  | [Extraneous WHERE clause](ERROR_DEFINITIONS.md)
|             | 79  | [Missing GROUP BY clause](ERROR_DEFINITIONS.md)
|             | 80  | [Extraneous GROUP BY clause](ERROR_DEFINITIONS.md)
|             | 81  | [Missing HAVING clause](ERROR_DEFINITIONS.md)
|             | 82  | [Extraneous HAVING clause](ERROR_DEFINITIONS.md)
|             | 83  | [Missing ORDER BY clause](ERROR_DEFINITIONS.md)
|             | 84  | [Exraneous ORDER BY clause](ERROR_DEFINITIONS.md)
|             | 85  | [Missing LIMIT clause](ERROR_DEFINITIONS.md)
|             | 86  | [Exraneous LIMIT clause](ERROR_DEFINITIONS.md)
|             | 87  | [Incorrect LIMIT](ERROR_DEFINITIONS.md)
|             | 88  | [Missing OFFSET clause](ERROR_DEFINITIONS.md)
|             | 89  | [Exraneous OFFSET clause](ERROR_DEFINITIONS.md)
|             | 90  | [Incorrect OFFSET](ERROR_DEFINITIONS.md)
**Function error**
|             | 91  | [DISTINCT as function parameter where not applicable](ERROR_DEFINITIONS.md)
|             | 92  | [Missing DISTINCT from function parameter](ERROR_DEFINITIONS.md)
|             | 93  | [Incorrect function](ERROR_DEFINITIONS.md)
|             | 94  | [Incorrect column as function parameter](ERROR_DEFINITIONS.md)

### Complications
| Subcategory | ID  | Name
| :---------- | :-: | :---
|             | 95  | [Unnecessary complication](ERROR_DEFINITIONS.md)
|             | 96  | [Unnecessary DISTINCT in SELECT clause](ERROR_DEFINITIONS.md)
|             | 97  | [Table reference can be omitted](ERROR_DEFINITIONS.md)
|             | 98  | [Unnecessary join](ERROR_DEFINITIONS.md)
|             | 99  | [Unused correlation name](ERROR_DEFINITIONS.md)
|             | 100 | [Tables have the same data](ERROR_DEFINITIONS.md)
|             | 101 | [Correlation name identical to table name](ERROR_DEFINITIONS.md)
|             | 102 | [Unnecessarily general comparison operator](ERROR_DEFINITIONS.md)
|             | 103 | [LIKE without wildcards](ERROR_DEFINITIONS.md)
|             | 104 | [Unnecessarily complicated SELECT in EXISTS subquery](ERROR_DEFINITIONS.md)
|             | 105 | [IN/EXISTS can be replaced by comparison](ERROR_DEFINITIONS.md)
|             | 106 | [Unnecessary aggregate function](ERROR_DEFINITIONS.md)
|             | 107 | [Unnecessary DISTINCT in aggregate function](ERROR_DEFINITIONS.md)
|             | 108 | [Unnecessary argument of COUNT](ERROR_DEFINITIONS.md)
|             | 109 | [Unnecessary GROUP BY in EXISTS subquery](ERROR_DEFINITIONS.md)
|             | 110 | [GROUP BY with singleton groups](ERROR_DEFINITIONS.md)
|             | 111 | [GROUP BY with only a single group](ERROR_DEFINITIONS.md)
|             | 112 | [GROUP BY can be replaced with DISTINCT](ERROR_DEFINITIONS.md)
|             | 113 | [UNION can be replaced by OR](ERROR_DEFINITIONS.md)
|             | 114 | [Unnecessary column in ORDER BY clause](ERROR_DEFINITIONS.md)
|             | 115 | [ORDER BY in subquery](ERROR_DEFINITIONS.md)
|             | 116 | [Inefficient HAVING](ERROR_DEFINITIONS.md)
|             | 117 | [Inefficient UNION](ERROR_DEFINITIONS.md)
|             | 118 | [Condition in the subquery can be moved up](ERROR_DEFINITIONS.md)
|             | 119 | [OUTER JOIN can be replaced by INNER JOIN](ERROR_DEFINITIONS.md)
|             | 120 | [Unused CTE](ERROR_DEFINITIONS.md)

## References

[^taipalus_errors2018]: Toni Taipalus, Mikko Siponen, and Tero Vartiainen. 2018. *Errors and Complications in SQL Query Formulation.* ACM Trans. Comput. Educ. 18, 3, Article 15 (September 2018), 29 pages. https://doi.org/10.1145/3231712
