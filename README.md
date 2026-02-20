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
| :---------- | :-- | :---
| **Ambiguous database object**
|             | SYN_AMBIGUOUS_COLUMN | [Ambiguous column](definitions/1_syn/ambiguous_column.md)
|             | SYN_AMBIGUOUS_FUNCTION | [Ambiguous function](definitions/1_syn/ambiguous_function.md)
| **Undefined database object**
|             | SYN_UNDEFINED_COLUMN | [Undefined column](definitions/1_syn/undefined_column.md)
|             | SYN_UNDEFINED_FUNCTION | [Undefined function](definitions/1_syn/undefined_function.md)
|             | SYN_UNDEFINED_PARAMETER | [Undefined parameter](definitions/1_syn/undefined_parameter.md)
|             | SYN_UNDEFINED_OBJECT | [Undefined object](definitions/1_syn/undefined_object.md)
|             | SYN_INVALID_SCHEMA | [Invalid schema name](definitions/1_syn/invalid_schema_name.md)
|             | SYN_MISSPELLING | [Misspellings](definitions/1_syn/misspellings.md)
|             | SYN_SYNONYM | [Synonyms](definitions/1_syn/synonyms.md)
|             | SYN_OMIT_QUOTES | [Omitting quotes around character data](definitions/1_syn/omitting_quotes_around_character_data.md)
| **Data type mismatch**
|             | SYN_FAILURE_TO_SPECIFY_COLUMN_NAME_TWICE | [Failure to specify column name twice](definitions/1_syn/failure_to_specify_column_name_twice.md)
|             | SYN_IS_WHERE_NOT_APPLICABLE | [IS where not applicable](definitions/1_syn/is_where_not_applicable.md)
|             | SYN_DATA_TYPE_MISMATCH | [Data type mismatch](definitions/1_syn/data_type_mismatch.md)
| **Illegal aggregate function placement**
|             | SYN_AGGREGATE_FUNCTION_OUTSIDE_SELECT_OR_HAVING | [Using aggregate function outside SELECT or HAVING](definitions/1_syn/using_aggregate_function_outside_select_or_having.md)
|             | SYN_AGGREGATE_FUNCTION_NESTED | [Grouping error: aggregate functions cannot be nested](definitions/1_syn/grouping_error_aggregate_functions_cannot_be_nested.md)
| **Illegal or insufficient grouping**
|             | SYN_EXTRANEOUS_OR_OMITTED_GROUPING_COLUMN | [Grouping error: extraneous or omitted grouping column](definitions/1_syn/grouping_error_extraneous_or_omitted_grouping_column.md)
|             | SYN_HAVING_WITHOUT_GROUP_BY | [Strange HAVING: HAVING without GROUP BY](definitions/1_syn/strange_having_having_without_group_by.md)
| **Illegal or insufficient grouping**
|             | SYN_TOO_MANY_COLUMNS_IN_SUBQUERY | [Too many columns in subquery](definitions/1_syn/too_many_columns_in_subquery.md)
|             | SYN_MISSING_QUANTIFIER | [Missing quantifier](definitions/1_syn/missing_quantifier.md)
| **Common syntax error**
|             | SYN_CONFUSING_FUNCTION_WITH_FUNCTION_PARAMETER | [Confusing function with function parameter](definitions/1_syn/confusing_function_with_function_parameter.md)
|             | SYN_USING_WHERE_TWICE | [Using WHERE twice](definitions/1_syn/using_where_twice.md)
|             | SYN_OMITTED_FROM_CLAUSE | [Omitting the FROM clause](definitions/1_syn/omitting_the_from_clause.md)
|             | SYN_COMPARISON_WITH_NULL | [Comparison with NULL](definitions/1_syn/comparison_with_null.md)
|             | SYN_OMITTED_SEMICOLON | [Omitting the semicolon](definitions/1_syn/omitting_the_semicolon.md)
|             | SYN_DATE_TIME_FIELD_OVERFLOW | [Date time field overflow](definitions/1_syn/date_time_field_overflow.md)
|             | SYN_DUPLICATE_CLAUSE | [Duplicate clause](definitions/1_syn/duplicate_clause.md)
|             | SYN_UNDEFINED_CORRELATION_NAME | [Using an undefined correlation name](definitions/1_syn/using_an_undefined_correlation_name.md)
|             | SYN_CONFUSING_TABLE_NAMES_WITH_COLUMN_NAMES | [Confusing table names with column names](definitions/1_syn/confusing_table_names_with_column_names.md)
|             | SYN_KEYWORDS_ORDER | [Confusing the order of keywords (e.g., FROM customer SELECT fee)](definitions/1_syn/confusing_the_order_of_keywords.md)
|             | SYN_KEYWORDS_SYNTAX | [Confusing the syntax of keywords (e.g., LIKE ('A,' 'B'))](definitions/1_syn/confusing_the_syntax_of_keywords.md)
|             | SYN_OMITTED_COMMAS | [Omitting commas](definitions/1_syn/omitting_commas.md)
|             | SYN_UNMATCHED_BRACKETS | [Unmatched brackets](definitions/1_syn/unmatched_brackets.md)
|             | SYN_CURLY_OR_SQUARE_BRACKETS | [Curly or square brackets](definitions/1_syn/curly_or_square_brackets.md)
|             | SYN_NONSTANDARD_KEYWORDS | [Nonstandard keywords or standard keywords in wrong context](definitions/1_syn/nonstandard_keywords_or_standard_keywords_in_wrong_context.md)
|             | SYN_NONSTANDARD_OPERATORS | [Nonstandard operators (e.g., &&, \|\| or ==)](definitions/1_syn/nonstandard_operators.md)
|             | SYN_ADDITIONAL_SEMICOLON | [Additional semicolon](definitions/1_syn/additional_semicolon.md)
|             | SYN_DIFFERENT_TUPLES_IN_SET_OPERATION | [Different tuples in set operation](definitions/1_syn/different_tuples_in_set_operation.md)


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
| :---------- | :-- | :---
| **Inconsistent expression**
|             | SEM_IMPLIED_TAUTOLOGICAL_OR_INCONSISTENT_EXPRESSION | [Implied, tautological or inconsistent expression](definitions/2_sem/implied_tautological_or_inconsistent_expression.md)
|             | SEM_DISTINCT_SUM_AVG | [DISTINCT in SUM or AVG](definitions/2_sem/distinct_in_sum_or_avg.md)
|             | SEM_DISTINCT_REMOVE_IMPORTANT_DUPLICATES | [DISTINCT that might remove important duplicates](definitions/2_sem/distinct_that_might_remove_important_duplicates.md)
|             | SEM_MIXING_GT0_WITH_IS_NOT_NULL_OR_EMPTY_STRING_WITH_NULL | [Mixing a >0 with IS NOT NULL or empty string with NULL](definitions/2_sem/mixing_a_0_with_is_not_null_or_empty_string_with_null.md)
| **Inconsistent join**
|             | SEM_NULL_IN_IN_ANY_ALL_SUBQUERY | [NULL in IN/ANY/ALL subquery](definitions/2_sem/null_in_in_any_all_subquery.md)
|             | SEM_JOIN_CONDITION_ON_INCORRECT_COLUMN | [Join condition on incorrect column (matches impossible)](definitions/2_sem/join_condition_on_incorrect_column.md)
| **Duplicate rows**
|             | SEM_MANY_DUPLICATES | [Many duplicates](definitions/2_sem/many_duplicates.md)
| **Redundant column output**
|             | SEM_CONSTANT_COLUMN_OUTPUT | [Constant column output](definitions/2_sem/constant_column_output.md)
|             | SEM_DUPLICATE_COLUMN_OUTPUT | [Duplicate column output](definitions/2_sem/duplicate_column_output.md)

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
| :---------- | :-- | :---
**Operator error**
|             | LOG_AND_INSTEAD_OF_OR | [AND instead of OR](definitions/3_log/and_instead_of_or.md)
|             | LOG_OR_INSTEAD_OF_AND | [OR instead of AND](definitions/3_log/or_instead_of_and.md)
|             | LOG_EXTRANEOUS_NOT_OPERATOR | [Extraneous NOT operator](definitions/3_log/extraneous_not_operator.md)
|             | LOG_MISSING_NOT_OPERATOR | [Missing NOT operator](definitions/3_log/missing_not_operator.md)
|             | LOG_SUBSTITUTING_EXISTENCE_NEGATION_WITH_NEQ | [Substituting existence negation with <>](definitions/3_log/substituting_existence_negation_with.md)
|             | LOG_INCORRECT_COMPARISON_OPERATOR_OR_INCORRECT_VALUE_COMPARED | [Incorrect comparison operator or incorrect value compared](definitions/3_log/incorrect_comparison_operator_or_incorrect_value_compared.md)
**Join error**
|             | LOG_INCORRECT_TABLE_REFERENCE | [Incorrect table reference](definitions/3_log/incorrect_table_reference.md)
|             | LOG_MISSING_TABLE_REFERENCE | [Missing table reference](definitions/3_log/missing_table_reference.md)
|             | LOG_EXTRANEOUS_TABLE_REFERENCE | [Extraneous table reference](definitions/3_log/extraneous_table_reference.md)
|             | LOG_JOIN_CONDITION_ON_INCORRECT_COLUMN | [Join condition on incorrect column (matches possible)](definitions/3_log/join_condition_on_incorrect_column.md)
|             | LOG_JOIN_CONDITION_WITH_INCORRECT_COMPARISON_OPERATOR | [Join condition with incorrect comparison operator](definitions/3_log/join_condition_with_incorrect_comparison_operator.md)
|             | LOG_OMITTING_A_JOIN_CONDITION | [Omitting a join condition](definitions/3_log/omitting_a_join_condition.md)
|             | LOG_CONDITION_ON_OUTER_JOIN | [Condition on OUTER JOIN](definitions/3_log/condition_on_outer_join.md)
**Nesting error**
|             | LOG_IMPROPER_NESTING_OF_EXPRESSIONS | [Improper nesting of expressions](definitions/3_log/improper_nesting_of_expressions.md)
|             | LOG_IMPROPER_NESTING_OF_SUBQUERIES | [Improper nesting of subqueries](definitions/3_log/improper_nesting_of_subqueries.md)
**Expression error**
|             | LOG_EXTRANEOUS_QUOTES | [Extraneous quotes](definitions/3_log/extraneous_quotes.md)
|             | LOG_MISSING_EXPRESSION | [Missing expression](definitions/3_log/missing_expression.md)
|             | LOG_EXPRESSION_ON_INCORRECT_COLUMN | [Expression on incorrect column](definitions/3_log/expression_on_incorrect_column.md)
|             | LOG_EXTRANEOUS_EXPRESSION | [Extraneous expression](definitions/3_log/extraneous_expression.md)
|             | LOG_EXPRESSION_IN_INCORRECT_CLAUSE | [Expression in incorrect clause](definitions/3_log/expression_in_incorrect_clause.md)
|             | LOG_WILDCARDS_WITHOUT_LIKE | [Wildcards without LIKE](definitions/3_log/wildcards_without_like.md)
|             | LOG_WRONG_WILDCARD | [Wrong wildcard](definitions/3_log/wrong_wildcard.md)
|             | LOG_INVALID_WILDCARD | [Invalid wildcard](definitions/3_log/invalid_wildcard.md)
**Projection error**
|             | LOG_EXTRANEOUS_COLUMN_IN_SELECT | [Extraneous column in SELECT](definitions/3_log/extraneous_column_in_select.md)
|             | LOG_MISSING_COLUMN_FROM_SELECT | [Missing column from SELECT](definitions/3_log/missing_column_from_select.md)
|             | LOG_MISSING_DISTINCT_FROM_SELECT | [Missing DISTINCT from SELECT](definitions/3_log/missing_distinct_from_select.md)
|             | LOG_MISSING_AS_FROM_SELECT | [Missing AS from SELECT](definitions/3_log/missing_as_from_select.md)
|             | LOG_MISSING_COLUMN_FROM_ORDER_BY_CLAUSE | [Missing column from ORDER BY clause](definitions/3_log/missing_column_from_order_by_clause.md)
|             | LOG_INCORRECT_COLUMN_IN_ORDER_BY_CLAUSE | [Incorrect column in ORDER BY clause](definitions/3_log/incorrect_column_in_order_by_clause.md)
|             | LOG_INCORRECT_ORDERING_OF_ROWS | [Incorrect ordering of rows](definitions/3_log/incorrect_ordering_of_rows.md)
**Clause error**
|             | LOG_MISSING_CLAUSE_WHERE | [Missing WHERE clause](definitions/3_log/missing_where_clause.md)
|             | LOG_MISSING_CLAUSE_GROUP_BY | [Missing GROUP BY clause](definitions/3_log/missing_group_by_clause.md)
|             | LOG_MISSING_CLAUSE_HAVING | [Missing HAVING clause](definitions/3_log/missing_having_clause.md)
|             | LOG_MISSING_CLAUSE_ORDER_BY | [Missing ORDER BY clause](definitions/3_log/missing_order_by_clause.md)
|             | LOG_MISSING_CLAUSE_LIMIT | [Missing LIMIT clause](definitions/3_log/missing_limit_clause.md)
|             | LOG_MISSING_CLAUSE_OFFSET | [Missing OFFSET clause](definitions/3_log/missing_offset_clause.md)
|             | LOG_EXTRANEOUS_CLAUSE_WHERE | [Extraneous WHERE clause](definitions/3_log/extraneous_where_clause.md)
|             | LOG_EXTRANEOUS_CLAUSE_GROUP_BY | [Extraneous GROUP BY clause](definitions/3_log/extraneous_group_by_clause.md)
|             | LOG_EXTRANEOUS_CLAUSE_HAVING | [Extraneous HAVING clause](definitions/3_log/extraneous_having_clause.md)
|             | LOG_EXTRANEOUS_CLAUSE_ORDER_BY | [Extraneous ORDER BY clause](definitions/3_log/extraneous_order_by_clause.md)
|             | LOG_EXTRANEOUS_CLAUSE_LIMIT | [Extraneous LIMIT clause](definitions/3_log/extraneous_limit_clause.md)
|             | LOG_EXTRANEOUS_CLAUSE_OFFSET | [Extraneous OFFSET clause](definitions/3_log/extraneous_offset_clause.md)
|             | LOG_INCORRECT_LIMIT | [Incorrect LIMIT](definitions/3_log/incorrect_limit.md)
|             | LOG_INCORRECT_OFFSET | [Incorrect OFFSET](definitions/3_log/incorrect_offset.md)
**Function error**
|             | LOG_INCORRECT_FUNCTION | [Incorrect function](definitions/3_log/incorrect_function.md)
|             | LOG_FUNCTION_PARAMETER_EXTRANEOUS_DISTINCT | [DISTINCT as function parameter where not applicable](definitions/3_log/distinct_as_function_parameter_where_not_applicable.md)
|             | LOG_FUNCTION_PARAMETER_MISSING_DISTINCT | [Missing DISTINCT from function parameter](definitions/3_log/missing_distinct_from_function_parameter.md)
|             | LOG_FUNCTION_PARAMETER_INCORRECT_COLUMN | [Incorrect column as function parameter](definitions/3_log/incorrect_column_as_function_parameter.md)

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
| :---------- | :-- | :---
|             | COM_COMPLICATION | [Unnecessary complication](definitions/4_com/unnecessary_complication.md)
|             | COM_UNNECESSARY_DISTINCT_IN_SELECT | [Unnecessary DISTINCT in SELECT clause](definitions/4_com/unnecessary_distinct_in_select_clause.md)
|             | COM_UNNECESSARY_TABLE_REFERENCE | [Unnecessary table reference](definitions/4_com/unnecessary_table_reference.md)
|             | COM_UNUSED_CORRELATION_NAME | [Unused correlation name](definitions/4_com/unused_correlation_name.md)
|             | COM_TABLES_HAVE_SAME_DATA | [Tables have the same data](definitions/4_com/tables_have_the_same_data.md)
|             | COM_CORRELATION_NAME_IDENTICAL_TO_TABLE_NAME | [Correlation name identical to table name](definitions/4_com/correlation_name_identical_to_table_name.md)
|             | COM_UNNECESSARILY_GENERAL_COMPARISON_OPERATOR | [Unnecessarily general comparison operator](definitions/4_com/unnecessarily_general_comparison_operator.md)
|             | COM_LIKE_WITHOUT_WILDCARDS | [LIKE without wildcards](definitions/4_com/like_without_wildcards.md)
|             | COM_UNNECESSARILY_COMPLICATED_SELECT_IN_EXISTS_SUBQUERY | [Unnecessarily complicated SELECT in EXISTS subquery](definitions/4_com/unnecessarily_complicated_select_in_exists_subquery.md)
|             | COM_IN_EXISTS_CAN_BE_REPLACED_BY_COMPARISON | [IN/EXISTS can be replaced by comparison](definitions/4_com/in_exists_can_be_replaced_by_comparison.md)
|             | COM_UNNECESSARY_AGGREGATE_FUNCTION | [Unnecessary aggregate function](definitions/4_com/unnecessary_aggregate_function.md)
|             | COM_UNNECESSARY_DISTINCT_IN_AGGREGATE_FUNCTION | [Unnecessary DISTINCT in aggregate function](definitions/4_com/unnecessary_distinct_in_aggregate_function.md)
|             | COM_UNNECESSARY_ARGUMENT_OF_COUNT | [Unnecessary argument of COUNT](definitions/4_com/unnecessary_argument_of_count.md)
|             | COM_UNNECESSARY_GROUP_BY_IN_EXISTS_SUBQUERY | [Unnecessary GROUP BY in EXISTS subquery](definitions/4_com/unnecessary_group_by_in_exists_subquery.md)
|             | COM_GROUP_BY_WITH_SINGLETON_GROUPS | [GROUP BY with singleton groups](definitions/4_com/group_by_with_singleton_groups.md)
|             | COM_GROUP_BY_WITH_ONLY_A_SINGLE_GROUP | [GROUP BY with only a single group](definitions/4_com/group_by_with_only_a_single_group.md)
|             | COM_GROUP_BY_CAN_BE_REPLACED_WITH_DISTINCT | [GROUP BY can be replaced with DISTINCT](definitions/4_com/group_by_can_be_replaced_with_distinct.md)
|             | COM_UNION_CAN_BE_REPLACED_BY_OR | [UNION can be replaced by OR](definitions/4_com/union_can_be_replaced_by_or.md)
|             | COM_UNNECESSARY_COLUMN_IN_ORDER_BY_CLAUSE | [Unnecessary column in ORDER BY clause](definitions/4_com/unnecessary_column_in_order_by_clause.md)
|             | COM_ORDER_BY_IN_SUBQUERY | [ORDER BY in subquery](definitions/4_com/order_by_in_subquery.md)
|             | COM_INEFFICIENT_HAVING | [Inefficient HAVING](definitions/4_com/inefficient_having.md)
|             | COM_INEFFICIENT_UNION | [Inefficient UNION](definitions/4_com/inefficient_union.md)
|             | COM_CONDITION_IN_THE_SUBQUERY_CAN_BE_MOVED_UP | [Condition in the subquery can be moved up](definitions/4_com/condition_in_the_subquery_can_be_moved_up.md)
|             | COM_OUTER_JOIN_CAN_BE_REPLACED_BY_INNER_JOIN | [OUTER JOIN can be replaced by INNER JOIN](definitions/4_com/outer_join_can_be_replaced_by_inner_join.md)
|             | COM_UNUSED_CTE | [Unused CTE](definitions/4_com/unused_cte.md)

# Notes

### Classification principles

- The four top-level categories are **mutually exclusive as primary labels**, although a single query may exhibit **multiple issues**.
- Classification prioritizes **observable query behavior** over inferred intent.

### Identifier design

- Error identifiers are symbolic rather than numeric to avoid implying a fixed ordering.
- This design choice increases robustness to future revisions, additions, or reclassification, without requiring systematic renumbering.

# References
[^taipalus_errors2018]: Toni Taipalus, Mikko Siponen, and Tero Vartiainen. 2018. *Errors and Complications in SQL Query Formulation.* ACM Trans. Comput. Educ. 18, 3, Article 15 (September 2018), 29 pages. https://doi.org/10.1145/3231712

[^miedema_identifying2022]: Daphne Miedema, Efthimia Aivaloglou, and George Fletcher. *Identifying SQL misconceptions of novices: Findings from a think-aloud study.* ACM Inroads 13.1 (2022): 52-65. https://dx.doi.org/10.1145/3514214
