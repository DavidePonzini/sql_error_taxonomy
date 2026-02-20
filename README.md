# SQL Error Taxonomy

This repository provides a SQL error taxonomy aimed at supporting uniform error classification in educational and automated settings.

It is based on the taxonomy proposed by Taipalus et al. [^taipalus_errors2018], with revisions introduced in our work to address ambiguities and limitations encountered when applying the taxonomy in automated SQL error-detection pipelines. The revised taxonomy refines error definitions, clarifies labels, and improves suitability for algorithmic classification.

Definitions are grounded in **observable properties of queries**, with criteria chosen to remain suitable for **automated detection** while preserving **pedagogical interpretability**.
No assumptions about student intent are made at this level.

# Top-level categories

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

# Taxonomy

You can use the links in the tables below to see detailed information on each error.

For each query, we will be referencing the following schema, adapted from Miedema et Al. [^miedema_identifying2022].
Underlined attributes collectively form the primary key for each table.

| Table name | Attributes                                                   |
| :--------- | :----------------------------------------------------------- |
| customer   | <ins>cID</ins>, cName, street, city, age                     |
| store      | <ins>sID</ins>, sName, street, city                          |
| product    | <ins>pID</ins>, pName, suffix                                |
| inventory  | <ins>sID</ins>, <ins>pID</ins>, date, quantity, unit_price   |

## Syntax errors
**Definition**  
A *syntax error* occurs when a SQL query violates the syntactic or typing rules of the SQL language and **cannot be executed by the DBMS**.

**Key properties**
- The DBMS rejects the query at parse time or during static validation.
- No result set is produced.
- The error can be detected without knowledge of the data demand.
- The error is independent of the database instance contents.

**Pedagogical interpretation**  
Syntax errors typically reflect difficulties with SQL grammar, clause structure, or expression formation, and often arise in early stages of learning.

| Subcategory | ID  | Name
| :---------- | :-: | :---
| **Ambiguous database object**
|             | 1   | [Ambiguous column](definitions/1_syn/ambiguous_column.md)
|             | 2   | [Ambiguous function](definitions/1_syn/ambiguous_function.md)
| **Undefined database object**
|             | 3   | [Undefined column](definitions/1_syn/undefined_column.md)
|             | 4   | [Undefined function](definitions/1_syn/undefined_function.md)
|             | 5   | [Undefined parameter](definitions/1_syn/undefined_parameter.md)
|             | 6   | [Undefined object](definitions/1_syn/undefined_object.md)
|             | 7   | [Invalid schema name](definitions/1_syn/invalid_schema_name.md)
|             | 8   | [Misspellings](definitions/1_syn/misspellings.md)
|             | 9   | [Synonyms](definitions/1_syn/synonyms.md)
|             | 10  | [Omitting quotes around character data](definitions/1_syn/omitting_quotes_around_character_data.md)
| **Data type mismatch**
|             | 11  | [Failure to specify column name twice](definitions/1_syn/failure_to_specify_column_name_twice.md)
|             | 12  | [IS where not applicable](definitions/1_syn/is_where_not_applicable.md)
|             | 13  | [Data type mismatch](definitions/1_syn/data_type_mismatch.md)
| **Illegal aggregate function placement**
|             | 14  | [Using aggregate function outside SELECT or HAVING](definitions/1_syn/using_aggregate_function_outside_select_or_having.md)
|             | 15  | [Grouping error: aggregate functions cannot be nested](definitions/1_syn/grouping_error_aggregate_functions_cannot_be_nested.md)
| **Illegal or insufficient grouping**
|             | 16  | [Grouping error: extraneous or omitted grouping column](definitions/1_syn/grouping_error_extraneous_or_omitted_grouping_column.md)
|             | 17  | [Strange HAVING: HAVING without GROUP BY](definitions/1_syn/strange_having_having_without_group_by.md)
| **Illegal or insufficient grouping**
|             | 18  | [Too many columns in subquery](definitions/1_syn/too_many_columns_in_subquery.md)
|             | 19  | [Missing quantifier](definitions/1_syn/missing_quantifier.md)
| **Common syntax error**
|             | 20  | [Confusing function with function parameter](definitions/1_syn/confusing_function_with_function_parameter.md)
|             | 21  | [Using WHERE twice](definitions/1_syn/using_where_twice.md)
|             | 22  | [Omitting the FROM clause](definitions/1_syn/omitting_the_from_clause.md)
|             | 23  | [Comparison with NULL](definitions/1_syn/comparison_with_null.md)
|             | 24  | [Omitting the semicolon](definitions/1_syn/omitting_the_semicolon.md)
|             | 25  | [Date time field overflow](definitions/1_syn/date_time_field_overflow.md)
|             | 26  | [Duplicate clause](definitions/1_syn/duplicate_clause.md)
|             | 27  | [Using an undefined correlation name](definitions/1_syn/using_an_undefined_correlation_name.md)
|             | 28  | [Confusing table names with column names](definitions/1_syn/confusing_table_names_with_column_names.md)
|             | 29  | [Confusing the order of keywords (e.g., FROM customer SELECT fee)](definitions/1_syn/confusing_the_order_of_keywords.md)
|             | 30  | [Confusing the syntax of keywords (e.g., LIKE ('A,' 'B'))](definitions/1_syn/confusing_the_syntax_of_keywords.md)
|             | 31  | [Omitting commas](definitions/1_syn/omitting_commas.md)
|             | 32  | [Unmatched brackets](definitions/1_syn/unmatched_brackets.md)
|             | 33  | [Curly or square brackets](definitions/1_syn/curly_or_square_brackets.md)
|             | 34  | [Nonstandard keywords or standard keywords in wrong context](definitions/1_syn/nonstandard_keywords_or_standard_keywords_in_wrong_context.md)
|             | 35  | [Nonstandard operators (e.g., &&, \|\| or ==)](definitions/1_syn/nonstandard_operators.md)
|             | 36  | [Additional semicolon](definitions/1_syn/additional_semicolon.md)
|             | 37  | [Different tuples in set operation](definitions/1_syn/different_tuples_in_set_operation.md)


## Semantic errors
**Definition**  
A *semantic error* occurs when a SQL query is syntactically valid and executable, but its evaluation is **semantically flawed regardless of the data demand**, producing a result that is always meaningless.

**Key properties**
- The query executes successfully.
- The result set is intrinsically invalid (e.g., always empty or logically inconsistent).
- The error can be detected without reference to the intended task.
- The behavior holds for any possible database instance.

**Pedagogical interpretation**  
These errors often signal misconceptions about logical conditions, boolean reasoning, or the meaning of operators in SQL.

| Subcategory | ID  | Name
| :---------- | :-: | :---
| **Inconsistent expression**
|             | 38  | [Implied, tautological or inconsistent expression](definitions/2_sem/implied_tautological_or_inconsistent_expression.md)
|             | 39  | [DISTINCT in SUM or AVG](definitions/2_sem/distinct_in_sum_or_avg.md)
|             | 40  | [DISTINCT that might remove important duplicates](definitions/2_sem/distinct_that_might_remove_important_duplicates.md)
|             | 41  | [Mixing a >0 with IS NOT NULL or empty string with NULL](definitions/2_sem/mixing_a_0_with_is_not_null_or_empty_string_with_null.md)
| **Inconsistent join**
|             | 42  | [NULL in IN/ANY/ALL subquery](definitions/2_sem/null_in_in_any_all_subquery.md)
|             | 43  | [Join condition on incorrect column (matches impossible)](definitions/2_sem/join_condition_on_incorrect_column.md)
| **Duplicate rows**
|             | 44  | [Many duplicates](definitions/2_sem/many_duplicates.md)
| **Redundant column output**
|             | 45  | [Constant column output](definitions/2_sem/constant_column_output.md)
|             | 46  | [Duplicate column output](definitions/2_sem/duplicate_column_output.md)

## Logic errors
**Definition**  
A *logic error* occurs when a SQL query is syntactically and semantically valid, but **does not satisfy the given data demand**.

**Key properties**
- The query executes successfully.
- A result set is produced.
- The result does not match the expected outcome defined by the data demand.
- Detection requires comparison with at least one correct reference query or specification.

**Pedagogical interpretation**  
Logic errors reflect misunderstandings of the problem requirements, relational reasoning, or the mapping between natural language requests and SQL constructs.

| Subcategory | ID  | Name
| :---------- | :-: | :---
**Operator error**
|             | 47  | [AND instead of OR](definitions/3_log/and_instead_of_or.md)
|             | 48  | [OR instead of AND](definitions/3_log/or_instead_of_and.md)
|             | 49  | [Extraneous NOT operator](definitions/3_log/extraneous_not_operator.md)
|             | 50  | [Missing NOT operator](definitions/3_log/missing_not_operator.md)
|             | 51  | [Substituting existence negation with <>](definitions/3_log/substituting_existence_negation_with.md)
|             | 52  | [Incorrect comparison operator or incorrect value compared](definitions/3_log/incorrect_comparison_operator_or_incorrect_value_compared.md)
**Join error**
|             | 53  | [Incorrect table reference](definitions/3_log/incorrect_table_reference.md)
|             | 54  | [Missing table reference](definitions/3_log/missing_table_reference.md)
|             | 55  | [Extraneous table reference](definitions/3_log/extraneous_table_reference.md)
|             | 56  | [Join condition on incorrect column (matches possible)](definitions/3_log/join_condition_on_incorrect_column.md)
|             | 57  | [Join condition with incorrect comparison operator](definitions/3_log/join_condition_with_incorrect_comparison_operator.md)
|             | 58  | [Omitting a join condition](definitions/3_log/omitting_a_join_condition.md)
|             | 59  | [Condition on OUTER JOIN](definitions/3_log/condition_on_outer_join.md)
**Nesting error**
|             | 60  | [Improper nesting of expressions](definitions/3_log/improper_nesting_of_expressions.md)
|             | 61  | [Improper nesting of subqueries](definitions/3_log/improper_nesting_of_subqueries.md)
**Expression error**
|             | 62  | [Extraneous quotes](definitions/3_log/extraneous_quotes.md)
|             | 63  | [Missing expression](definitions/3_log/missing_expression.md)
|             | 64  | [Expression on incorrect column](definitions/3_log/expression_on_incorrect_column.md)
|             | 65  | [Extraneous expression](definitions/3_log/extraneous_expression.md)
|             | 66  | [Expression in incorrect clause](definitions/3_log/expression_in_incorrect_clause.md)
|             | 67  | [Wildcards without LIKE](definitions/3_log/wildcards_without_like.md)
|             | 68  | [Wrong wildcard](definitions/3_log/wrong_wildcard.md)
|             | 69  | [Invalid wildcard](definitions/3_log/invalid_wildcard.md)
**Projection error**
|             | 70  | [Extraneous column in SELECT](definitions/3_log/extraneous_column_in_select.md)
|             | 71  | [Missing column from SELECT](definitions/3_log/missing_column_from_select.md)
|             | 72  | [Missing DISTINCT from SELECT](definitions/3_log/missing_distinct_from_select.md)
|             | 73  | [Missing AS from SELECT](definitions/3_log/missing_as_from_select.md)
|             | 74  | [Missing column from ORDER BY clause](definitions/3_log/missing_column_from_order_by_clause.md)
|             | 75  | [Incorrect column in ORDER BY clause](definitions/3_log/incorrect_column_in_order_by_clause.md)
|             | 76  | [Incorrect ordering of rows](definitions/3_log/incorrect_ordering_of_rows.md)
**Clause error**
|             | 77  | [Missing WHERE clause](definitions/3_log/missing_where_clause.md)
|             | 78  | [Extraneous WHERE clause](definitions/3_log/extraneous_where_clause.md)
|             | 79  | [Missing GROUP BY clause](definitions/3_log/missing_group_by_clause.md)
|             | 80  | [Extraneous GROUP BY clause](definitions/3_log/extraneous_group_by_clause.md)
|             | 81  | [Missing HAVING clause](definitions/3_log/missing_having_clause.md)
|             | 82  | [Extraneous HAVING clause](definitions/3_log/extraneous_having_clause.md)
|             | 83  | [Missing ORDER BY clause](definitions/3_log/missing_order_by_clause.md)
|             | 84  | [Extraneous ORDER BY clause](definitions/3_log/extraneous_order_by_clause.md)
|             | 85  | [Missing LIMIT clause](definitions/3_log/missing_limit_clause.md)
|             | 86  | [Extraneous LIMIT clause](definitions/3_log/extraneous_limit_clause.md)
|             | 87  | [Incorrect LIMIT](definitions/3_log/incorrect_limit.md)
|             | 88  | [Missing OFFSET clause](definitions/3_log/missing_offset_clause.md)
|             | 89  | [Extraneous OFFSET clause](definitions/3_log/extraneous_offset_clause.md)
|             | 90  | [Incorrect OFFSET](definitions/3_log/incorrect_offset.md)
**Function error**
|             | 91  | [DISTINCT as function parameter where not applicable](definitions/3_log/distinct_as_function_parameter_where_not_applicable.md)
|             | 92  | [Missing DISTINCT from function parameter](definitions/3_log/missing_distinct_from_function_parameter.md)
|             | 93  | [Incorrect function](definitions/3_log/incorrect_function.md)
|             | 94  | [Incorrect column as function parameter](definitions/3_log/incorrect_column_as_function_parameter.md)

## Complications
**Definition**  
A *complication* occurs when a SQL query **satisfies the data demand**, but does so in an **unnecessarily complex, redundant, or non-idiomatic way**.

**Key properties**
- The query returns a correct result set.
- One or more components are redundant, superfluous, or replaceable by simpler constructs.
- Removing or simplifying these components does not change the result.
- Detection requires knowledge of the data demand.

**Pedagogical interpretation**  
Complications often indicate partial understanding or overgeneralization of SQL constructs, and provide opportunities for feedback focused on readability, efficiency, and idiomatic query formulation.

| Subcategory | ID  | Name
| :---------- | :-: | :---
|             | 95  | [Unnecessary complication](definitions/4_com/unnecessary_complication.md)
|             | 96  | [Unnecessary DISTINCT in SELECT clause](definitions/4_com/unnecessary_distinct_in_select_clause.md)
|             | 97  | [Unnecessary table reference](definitions/4_com/unnecessary_table_reference.md)
|             | 98  | [Unused correlation name](definitions/4_com/unused_correlation_name.md)
|             | 99  | [Tables have the same data](definitions/4_com/tables_have_the_same_data.md)
|             | 100 | [Correlation name identical to table name](definitions/4_com/correlation_name_identical_to_table_name.md)
|             | 101 | [Unnecessarily general comparison operator](definitions/4_com/unnecessarily_general_comparison_operator.md)
|             | 102 | [LIKE without wildcards](definitions/4_com/like_without_wildcards.md)
|             | 103 | [Unnecessarily complicated SELECT in EXISTS subquery](definitions/4_com/unnecessarily_complicated_select_in_exists_subquery.md)
|             | 104 | [IN/EXISTS can be replaced by comparison](definitions/4_com/in_exists_can_be_replaced_by_comparison.md)
|             | 105 | [Unnecessary aggregate function](definitions/4_com/unnecessary_aggregate_function.md)
|             | 106 | [Unnecessary DISTINCT in aggregate function](definitions/4_com/unnecessary_distinct_in_aggregate_function.md)
|             | 107 | [Unnecessary argument of COUNT](definitions/4_com/unnecessary_argument_of_count.md)
|             | 108 | [Unnecessary GROUP BY in EXISTS subquery](definitions/4_com/unnecessary_group_by_in_exists_subquery.md)
|             | 109 | [GROUP BY with singleton groups](definitions/4_com/group_by_with_singleton_groups.md)
|             | 110 | [GROUP BY with only a single group](definitions/4_com/group_by_with_only_a_single_group.md)
|             | 111 | [GROUP BY can be replaced with DISTINCT](definitions/4_com/group_by_can_be_replaced_with_distinct.md)
|             | 112 | [UNION can be replaced by OR](definitions/4_com/union_can_be_replaced_by_or.md)
|             | 113 | [Unnecessary column in ORDER BY clause](definitions/4_com/unnecessary_column_in_order_by_clause.md)
|             | 114 | [ORDER BY in subquery](definitions/4_com/order_by_in_subquery.md)
|             | 115 | [Inefficient HAVING](definitions/4_com/inefficient_having.md)
|             | 116 | [Inefficient UNION](definitions/4_com/inefficient_union.md)
|             | 117 | [Condition in the subquery can be moved up](definitions/4_com/condition_in_the_subquery_can_be_moved_up.md)
|             | 118 | [OUTER JOIN can be replaced by INNER JOIN](definitions/4_com/outer_join_can_be_replaced_by_inner_join.md)
|             | 119 | [Unused CTE](definitions/4_com/unused_cte.md)

# Notes on Category Boundaries

- The four top-level categories are **mutually exclusive as primary labels**, but a single query may exhibit **multiple issues**.
- Classification prioritizes **observable query behavior** over inferred intent.
- The distinction between *semantic* and *logic* errors hinges on whether the data demand is required for detection.

# References
[^taipalus_errors2018]: Toni Taipalus, Mikko Siponen, and Tero Vartiainen. 2018. *Errors and Complications in SQL Query Formulation.* ACM Trans. Comput. Educ. 18, 3, Article 15 (September 2018), 29 pages. https://doi.org/10.1145/3231712

[^miedema_identifying2022]: Daphne Miedema, Efthimia Aivaloglou, and George Fletcher. *Identifying SQL misconceptions of novices: Findings from a think-aloud study.* ACM Inroads 13.1 (2022): 52-65. https://dx.doi.org/10.1145/3514214
