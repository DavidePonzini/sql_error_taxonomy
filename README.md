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

| Table name | Attributes                                      
| :--------- | :----------------------------------------------------------- |
| customer   | <ins>cID</ins>, cName, street, city, age        
| store      | <ins>sID</ins>, sName, street, city             
| product    | <ins>pID</ins>, pName, suffix                   
| inventory  | <ins>sID</ins>, <ins>pID</ins>, date, quantity, unit_price   |

## Updates and maintenance
Each error type is assigned a unique identifier which is will never be changed or removed, but new IDs may be added in the future.

Existing taxonomies can be updated by running again the [error categorization module](https://github.com/DavidePonzini/sql_error_categorizer) on the same set of queries, and reclassifying any errors that have changed category or type.


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


### Ambiguous database object
| ID  | Name | Discussed in
| :-- | :--- | :---
|   2 | [Ambiguous column](definitions/1_syn/ambiguous_column.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
|   3 | [Ambiguous function](definitions/1_syn/ambiguous_function.md) | [^taipalus_errors2018]
### Undefined database object
| ID  | Name | Discussed in
| :-- | :--- | :---
|   4 | [Undefined column](definitions/1_syn/undefined_column.md) | [^taipalus_errors2018]
|   5 | [Undefined function](definitions/1_syn/undefined_function.md) | [^taipalus_errors2018]
|   6 | [Undefined parameter](definitions/1_syn/undefined_parameter.md) | [^taipalus_errors2018]
|   7 | [Undefined object](definitions/1_syn/undefined_object.md) | [^taipalus_errors2018]
|   8 | [Invalid schema name](definitions/1_syn/invalid_schema_name.md) | [^taipalus_errors2018]
|   9 | [Misspellings](definitions/1_syn/misspellings.md) | [^taipalus_errors2018]
|  10 | [Synonyms](definitions/1_syn/synonyms.md) | [^taipalus_errors2018]
|  11 | [Omitting quotes around character data](definitions/1_syn/omitting_quotes_around_character_data.md) | [^taipalus_errors2018]
### Data type mismatch
| ID  | Name | Discussed in
| :-- | :--- | :---
|  12 | [Failure to specify column name twice](definitions/1_syn/failure_to_specify_column_name_twice.md) | [^taipalus_errors2018]
|  35 | [IS where not applicable](definitions/1_syn/is_where_not_applicable.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
|  13 | [Data type mismatch](definitions/1_syn/data_type_mismatch.md) | [^taipalus_errors2018]
### Illegal aggregate function placement
| ID  | Name | Discussed in
| :-- | :--- | :---
|  14 | [Using aggregate function outside SELECT or HAVING](definitions/1_syn/using_aggregate_function_outside_select_or_having.md) | [^taipalus_errors2018]
|  15 | [Aggregate functions cannot be nested](definitions/1_syn/aggregate_functions_cannot_be_nested.md) | [^taipalus_errors2018]
### Illegal or insufficient grouping
| ID  | Name | Discussed in
| :-- | :--- | :---
|  16 | [Extraneous or omitted grouping column](definitions/1_syn/extraneous_or_omitted_grouping_column.md) | [^taipalus_errors2018]
|  17 | [HAVING without GROUP BY](definitions/1_syn/having_without_group_by.md) | [^taipalus_errors2018]
### Invalid subqueries
| ID  | Name | Discussed in
| :-- | :--- | :---
|  26 | [Too many columns in subquery](definitions/1_syn/too_many_columns_in_subquery.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
| 106 | [Missing quantifier](definitions/1_syn/missing_quantifier.md) | [^ponzini_proposal2026]
### Common syntax error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  18 | [Confusing function with function parameter](definitions/1_syn/confusing_function_with_function_parameter.md) | [^taipalus_errors2018]
|  19 | [Using WHERE twice](definitions/1_syn/using_where_twice.md) | [^taipalus_errors2018]
|  20 | [Omitting the FROM clause](definitions/1_syn/omitting_the_from_clause.md) | [^taipalus_errors2018]
|  21 | [Comparison with NULL](definitions/1_syn/comparison_with_null.md) | [^taipalus_errors2018]
|  22 | [Omitted semicolon](definitions/1_syn/omitting_the_semicolon.md) | [^taipalus_errors2018]
|  38 | [Additional semicolon](definitions/1_syn/additional_semicolon.md) | [^taipalus_errors2018]
|  23 | [Date time field overflow](definitions/1_syn/date_time_field_overflow.md) | [^taipalus_errors2018]
|  24 | [Duplicate clause](definitions/1_syn/duplicate_clause.md) | [^taipalus_errors2018]
|  25 | [Undefined correlation name](definitions/1_syn/using_an_undefined_correlation_name.md) | [^taipalus_errors2018]
|  27 | [Confused table names with column names](definitions/1_syn/confusing_table_names_with_column_names.md) | [^taipalus_errors2018]
|  30 | [Confused the order of keywords (e.g., FROM customer SELECT fee)](definitions/1_syn/confusing_the_order_of_keywords.md) | [^taipalus_errors2018]
|  32 | [Confused the syntax of keywords (e.g., LIKE ('A,' 'B'))](definitions/1_syn/confusing_the_syntax_of_keywords.md) | [^taipalus_errors2018]
|  33 | [Omitting commas](definitions/1_syn/omitting_commas.md) | [^taipalus_errors2018]
| 107 | [Unmatched brackets](definitions/1_syn/unmatched_brackets.md) | [^ponzini_proposal2026]
| 108 | [Curly or square brackets](definitions/1_syn/curly_or_square_brackets.md) | [^ponzini_proposal2026]
|  36 | [Nonstandard keywords or standard keywords in wrong context](definitions/1_syn/nonstandard_keywords_or_standard_keywords_in_wrong_context.md) | [^taipalus_errors2018]
|  37 | [Nonstandard operators (e.g., &&, \|\| or ==)](definitions/1_syn/nonstandard_operators.md) | [^taipalus_errors2018]
| 109 | [Different tuples in set operation](definitions/1_syn/different_tuples_in_set_operation.md) | [^ponzini_proposal2026]


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

### Inconsistent expression
| ID  | Name | Discussed in
| :-- | :--- | :---
|  40 | [Implied, tautological or inconsistent expression](definitions/2_sem/implied_tautological_or_inconsistent_expression.md) | [^taipalus_errors2018] 
|  41 | [DISTINCT in SUM or AVG](definitions/2_sem/distinct_in_sum_or_avg.md) | [^taipalus_errors2018]
|  42 | [DISTINCT that might remove important duplicates](definitions/2_sem/distinct_that_might_remove_important_duplicates.md) | [^taipalus_errors2018]
|  45 | [Mixed a >0 with IS NOT NULL or empty string with NULL](definitions/2_sem/mixing_a_0_with_is_not_null_or_empty_string_with_null.md) | [^taipalus_errors2018]
### Inconsistent join
| ID  | Name | Discussed in
| :-- | :--- | :---
|  46 | [NULL in IN/ANY/ALL subquery](definitions/2_sem/null_in_in_any_all_subquery.md) | [^taipalus_errors2018]
|  47 | [Join condition on unmatchable column](definitions/2_sem/join_condition_on_unmatchable_column.md) | [^taipalus_errors2018]
### Duplicate rows
| ID  | Name | Discussed in
| :-- | :--- | :---
|  49 | [Many duplicates](definitions/2_sem/many_duplicates.md) | [^taipalus_errors2018]
### Redundant column output
| ID  | Name | Discussed in
| :-- | :--- | :---
|  50 | [Constant column output](definitions/2_sem/constant_column_output.md) | [^taipalus_errors2018]
|  51 | [Duplicate column output](definitions/2_sem/duplicate_column_output.md) | [^taipalus_errors2018]

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

### Operator error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  39 | [AND instead of OR](definitions/3_log/and_instead_of_or.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
|  52 | [OR instead of AND](definitions/3_log/or_instead_of_and.md) | [^taipalus_errors2018]
|  53 | [Extraneous NOT operator](definitions/3_log/extraneous_not_operator.md) | [^taipalus_errors2018]
|  54 | [Missing NOT operator](definitions/3_log/missing_not_operator.md) | [^taipalus_errors2018]
|  55 | [Substituting existence negation with <>](definitions/3_log/substituting_existence_negation_with.md) | [^taipalus_errors2018]
|  57 | [Incorrect comparison operator or incorrect value compared](definitions/3_log/incorrect_comparison_operator_or_incorrect_value_compared.md) | [^taipalus_errors2018]
### Join error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  58 | [Incorrect table reference](definitions/3_log/incorrect_table_reference.md) | [^taipalus_errors2018]
|  62 | [Missing table reference](definitions/3_log/missing_table_reference.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
|  59 | [Extraneous table reference](definitions/3_log/extraneous_table_reference.md) | [^taipalus_errors2018]
|  60 | [Join condition on incorrect column](definitions/3_log/join_condition_on_incorrect_column.md) | [^taipalus_errors2018]
|  61 | [Join condition with incorrect comparison operator](definitions/3_log/join_condition_with_incorrect_comparison_operator.md) | [^taipalus_errors2018]
|  48 | [Missing join condition](definitions/3_log/omitting_a_join_condition.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
| 104 | [Condition on OUTER JOIN](definitions/3_log/condition_on_outer_join.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
### Nesting error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  63 | [Improper nesting of expressions](definitions/3_log/improper_nesting_of_expressions.md) | [^taipalus_errors2018]
|  64 | [Improper nesting of subqueries](definitions/3_log/improper_nesting_of_subqueries.md) | [^taipalus_errors2018]
### Expression error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  65 | [Extraneous quotes](definitions/3_log/extraneous_quotes.md) | [^taipalus_errors2018]
|  66 | [Missing expression](definitions/3_log/missing_expression.md) | [^taipalus_errors2018]
|  68 | [Extraneous expression](definitions/3_log/extraneous_expression.md) | [^taipalus_errors2018]
|  67 | [Expression on incorrect column](definitions/3_log/expression_on_incorrect_column.md) | [^taipalus_errors2018]
|  69 | [Expression in incorrect clause](definitions/3_log/expression_in_incorrect_clause.md) | [^taipalus_errors2018]
|  43 | [Wildcards without LIKE](definitions/3_log/wildcards_without_like.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
| 110 | [Wrong wildcard](definitions/3_log/wrong_wildcard.md) | [^ponzini_proposal2026]
| 111 | [Invalid wildcard](definitions/3_log/invalid_wildcard.md) | [^ponzini_proposal2026]
### Projection error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  70 | [Extraneous column in SELECT](definitions/3_log/extraneous_column_in_select.md) | [^taipalus_errors2018]
|  71 | [Missing column from SELECT](definitions/3_log/missing_column_from_select.md) | [^taipalus_errors2018]
|  72 | [Missing DISTINCT from SELECT](definitions/3_log/missing_distinct_from_select.md) | [^taipalus_errors2018]
|  73 | [Missing AS from SELECT](definitions/3_log/missing_as_from_select.md) | [^taipalus_errors2018]
|  74 | [Missing column from ORDER BY clause](definitions/3_log/missing_column_from_order_by_clause.md) | [^taipalus_errors2018]
|  75 | [Incorrect column in ORDER BY clause](definitions/3_log/incorrect_column_in_order_by_clause.md) | [^taipalus_errors2018]
|  77 | [Incorrect ordering of rows](definitions/3_log/incorrect_ordering_of_rows.md) | [^taipalus_errors2018]
### Clause error
| ID  | Name | Discussed in
| :-- | :--- | :---
| 112 | [Missing WHERE clause](definitions/3_log/missing_where_clause.md) | [^ponzini_proposal2026]
| 113 | [Missing GROUP BY clause](definitions/3_log/missing_group_by_clause.md) | [^ponzini_proposal2026]
| 114 | [Missing HAVING clause](definitions/3_log/missing_having_clause.md) | [^ponzini_proposal2026]
| 115 | [Missing ORDER BY clause](definitions/3_log/missing_order_by_clause.md) | [^ponzini_proposal2026]
| 116 | [Missing LIMIT clause](definitions/3_log/missing_limit_clause.md) | [^ponzini_proposal2026]
| 117 | [Missing OFFSET clause](definitions/3_log/missing_offset_clause.md) | [^ponzini_proposal2026]
| 118 | [Extraneous WHERE clause](definitions/3_log/extraneous_where_clause.md) | [^ponzini_proposal2026]
| 119 | [Extraneous GROUP BY clause](definitions/3_log/extraneous_group_by_clause.md) | [^ponzini_proposal2026]
| 120 | [Extraneous HAVING clause](definitions/3_log/extraneous_having_clause.md) | [^ponzini_proposal2026]
|  76 | [Extraneous ORDER BY clause](definitions/3_log/extraneous_order_by_clause.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
| 121 | [Extraneous LIMIT clause](definitions/3_log/extraneous_limit_clause.md) | [^ponzini_proposal2026]
| 122 | [Extraneous OFFSET clause](definitions/3_log/extraneous_offset_clause.md) | [^ponzini_proposal2026]
| 123 | [Incorrect LIMIT](definitions/3_log/incorrect_limit.md) | [^ponzini_proposal2026]
| 124 | [Incorrect OFFSET](definitions/3_log/incorrect_offset.md) | [^ponzini_proposal2026]
### Function error
| ID  | Name | Discussed in
| :-- | :--- | :---
|  80 | [Incorrect function](definitions/3_log/incorrect_function.md) | [^taipalus_errors2018]
|  78 | [DISTINCT as function parameter where not applicable](definitions/3_log/distinct_as_function_parameter_where_not_applicable.md) | [^taipalus_errors2018]
|  79 | [Missing DISTINCT from function parameter](definitions/3_log/missing_distinct_from_function_parameter.md) | [^taipalus_errors2018]
|  81 | [Incorrect column as function parameter](definitions/3_log/incorrect_column_as_function_parameter.md) | [^taipalus_errors2018]

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

### Complication
| ID  | Name | Discussed in
| :-- | :--- | :---
|  82 | [Unnecessary complication](definitions/4_com/unnecessary_complication.md) | [^taipalus_errors2018]
|  83 | [Unnecessary DISTINCT in SELECT clause](definitions/4_com/unnecessary_distinct_in_select_clause.md) | [^taipalus_errors2018]
|  84 | [Unnecessary table reference](definitions/4_com/unnecessary_table_reference.md) | [^taipalus_errors2018]
|  85 | [Unused correlation name](definitions/4_com/unused_correlation_name.md) | [^taipalus_errors2018]
|  86 | [Tables have the same data](definitions/4_com/tables_have_the_same_data.md) | [^taipalus_errors2018] [^ponzini_proposal2026]
| 125 | [Correlation name identical to table name](definitions/4_com/correlation_name_identical_to_table_name.md) | [^ponzini_proposal2026]
|  87 | [Unnecessarily general comparison operator](definitions/4_com/unnecessarily_general_comparison_operator.md) | [^taipalus_errors2018]
|  88 | [LIKE without wildcards](definitions/4_com/like_without_wildcards.md) | [^taipalus_errors2018]
|  89 | [Unnecessarily complicated SELECT in EXISTS subquery](definitions/4_com/unnecessarily_complicated_select_in_exists_subquery.md) | [^taipalus_errors2018]
|  90 | [IN/EXISTS can be replaced by comparison](definitions/4_com/in_exists_can_be_replaced_by_comparison.md) | [^taipalus_errors2018]
|  91 | [Unnecessary aggregate function](definitions/4_com/unnecessary_aggregate_function.md) | [^taipalus_errors2018]
|  92 | [Unnecessary DISTINCT in aggregate function](definitions/4_com/unnecessary_distinct_in_aggregate_function.md) | [^taipalus_errors2018]
|  93 | [Unnecessary argument of COUNT](definitions/4_com/unnecessary_argument_of_count.md) | [^taipalus_errors2018]
|  94 | [Unnecessary GROUP BY in EXISTS subquery](definitions/4_com/unnecessary_group_by_in_exists_subquery.md) | [^taipalus_errors2018]
|  95 | [GROUP BY with singleton groups](definitions/4_com/group_by_with_singleton_groups.md) | [^taipalus_errors2018]
|  96 | [GROUP BY with only a single group](definitions/4_com/group_by_with_only_a_single_group.md) | [^taipalus_errors2018]
|  97 | [GROUP BY can be replaced with DISTINCT](definitions/4_com/group_by_can_be_replaced_with_distinct.md) | [^taipalus_errors2018]
|  98 | [UNION can be replaced by OR](definitions/4_com/union_can_be_replaced_by_or.md) | [^taipalus_errors2018]
|  99 | [Unnecessary column in ORDER BY clause](definitions/4_com/unnecessary_column_in_order_by_clause.md) | [^taipalus_errors2018]
| 100 | [ORDER BY in subquery](definitions/4_com/order_by_in_subquery.md) | [^taipalus_errors2018]
| 101 | [Inefficient HAVING](definitions/4_com/inefficient_having.md) | [^taipalus_errors2018]
| 102 | [Inefficient UNION](definitions/4_com/inefficient_union.md) | [^taipalus_errors2018]
| 103 | [Condition in the subquery can be moved up](definitions/4_com/condition_in_the_subquery_can_be_moved_up.md) | [^taipalus_errors2018]
| 105 | [OUTER JOIN can be replaced by INNER JOIN](definitions/4_com/outer_join_can_be_replaced_by_inner_join.md) | [^taipalus_errors2018]
| 126 | [Unused CTE](definitions/4_com/unused_cte.md) | [^ponzini_proposal2026]

## Deprecated error types
The following error types have been deprecated and should not be used for new classifications. They are retained in the taxonomy for backward compatibility and historical reference.

| ID  | Name | Discussed in | Deprecated in 
| :-- | :--- | :--- | :---
|   1 | Omitting correlation names | [^taipalus_errors2018] | [^ponzini_proposal2026]
|  28 | Restriction in SELECT clause | [^taipalus_errors2018] | [^ponzini_proposal2026]
|  29 | Projection in WHERE clause | [^taipalus_errors2018] | [^ponzini_proposal2026]
|  31 | Confusing the logic of keywords | [^taipalus_errors2018] | [^ponzini_proposal2026]
|  34 | Curly, square or unmatched brackets | [^taipalus_errors2018] | [^ponzini_proposal2026]
|  44 | Incorrect wildcard | [^taipalus_errors2018] | [^ponzini_proposal2026]
|  56 | Putting NOT in front of incorrect IN/EXISTS | [^taipalus_errors2018] | [^ponzini_proposal2026]
# Notes

### Classification principles

- The four top-level categories are **mutually exclusive as primary labels**, although a single query may exhibit **multiple issues**.
- Classification prioritizes **observable query behavior** over inferred intent.

# References
[^taipalus_errors2018]: Taipalus, Toni, Mikko Siponen, and Tero Vartiainen. "Errors and complications in SQL query formulation." *ACM Transactions on Computing Education (TOCE)* 18.3 (2018): 1-29. https://doi.org/10.1145/3231712

[^miedema_identifying2022]: Miedema, Daphne, Efthimia Aivaloglou, and George Fletcher. "Identifying SQL misconceptions of novices: Findings from a think-aloud study." *ACM Inroads* 13.1 (2022): 52-65. https://dx.doi.org/10.1145/3514214

[^ponzini_proposal2026]: Ponzini, Davide, Giovanna Guerrini, and Barbara Catania. "A Proposal for Revising SQL Error Taxonomies Based on Automated Detection." (2026). *DataEd 2026*. https://ceur-ws.org/Vol-4192/DataEd-paper9.pdf
