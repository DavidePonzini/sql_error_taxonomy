from enum import IntEnum, StrEnum
from dataclasses import dataclass

VERSION: int = 1

class SqlErrorCategory(StrEnum):
    """Enumeration of SQL error categories."""
    SYNTAX = "SYN"
    SEMANTIC = "SEM"
    LOGICAL = "LOG"
    COMPLICATION = "COM"

@dataclass(frozen=True)
class SqlErrorDefinition:
    """Data class representing the definition of an SQL error."""
    name: str
    category: SqlErrorCategory

class SqlErrors(IntEnum):
    """Enumeration of SQL error types with unique identifiers."""

    # Syntax errors
    AMBIGUOUS_COLUMN = 1
    AMBIGUOUS_FUNCTION = 2
    UNDEFINED_COLUMN = 3
    UNDEFINED_FUNCTION = 4
    UNDEFINED_PARAMETER = 5
    UNDEFINED_OBJECT = 6
    INVALID_SCHEMA_NAME = 7
    MISSPELLINGS = 8
    SYNONYMS = 9
    OMITTING_QUOTES_AROUND_CHARACTER_DATA = 10
    FAILURE_TO_SPECIFY_COLUMN_NAME_TWICE = 11
    IS_WHERE_NOT_APPLICABLE = 12
    DATA_TYPE_MISMATCH = 13
    USING_AGGREGATE_FUNCTION_OUTSIDE_SELECT_OR_HAVING = 14
    AGGREGATE_FUNCTIONS_CANNOT_BE_NESTED = 15
    EXTRANEOUS_OR_OMITTED_GROUPING_COLUMN = 16
    STRANGE_HAVING_HAVING_WITHOUT_GROUP_BY = 17
    TOO_MANY_COLUMNS_IN_SUBQUERY = 18
    MISSING_QUANTIFIER = 19
    CONFUSING_FUNCTION_WITH_FUNCTION_PARAMETER = 20
    USING_WHERE_TWICE = 21
    OMITTING_THE_FROM_CLAUSE = 22
    COMPARISON_WITH_NULL = 23
    OMITTING_THE_SEMICOLON = 24
    DATE_TIME_FIELD_OVERFLOW = 25
    DUPLICATE_CLAUSE = 26
    USING_AN_UNDEFINED_CORRELATION_NAME = 27
    CONFUSING_TABLE_NAMES_WITH_COLUMN_NAMES = 28
    CONFUSING_THE_ORDER_OF_KEYWORDS = 29
    CONFUSING_THE_SYNTAX_OF_KEYWORDS = 30
    OMITTING_COMMAS = 31
    UNMATCHED_BRACKETS = 32
    CURLY_OR_SQUARE_BRACKETS = 33
    NONSTANDARD_KEYWORDS_OR_STANDARD_KEYWORDS_IN_WRONG_CONTEXT = 34
    NONSTANDARD_OPERATORS = 35
    ADDITIONAL_SEMICOLON = 36
    DIFFERENT_TUPLES_IN_SET_OPERATION = 37

    # Semantic errors
    IMPLIED_TAUTOLOGICAL_OR_INCONSISTENT_EXPRESSION = 38
    DISTINCT_IN_SUM_OR_AVG = 39
    DISTINCT_THAT_MIGHT_REMOVE_IMPORTANT_DUPLICATES = 40
    MIXING_A_GREATER_THAN_0_WITH_IS_NOT_NULL_OR_EMPTY_STRING_WITH_NULL = 41
    NULL_IN_IN_ANY_ALL_SUBQUERY = 42
    JOIN_CONDITION_ON_UNMATCHABLE_COLUMN = 43
    MANY_DUPLICATES = 44
    CONSTANT_COLUMN_OUTPUT = 45
    DUPLICATE_COLUMN_OUTPUT = 46

    # Logical errors
    AND_INSTEAD_OF_OR = 47
    OR_INSTEAD_OF_AND = 48
    EXTRANEOUS_NOT_OPERATOR = 49
    MISSING_NOT_OPERATOR = 50
    SUBSTITUTING_EXISTENCE_NEGATION_WITH_NOT_EQUAL_TO = 51
    INCORRECT_COMPARISON_OPERATOR_OR_INCORRECT_VALUE_COMPARED = 52
    INCORRECT_TABLE_REFERENCE = 53
    MISSING_TABLE_REFERENCE = 54
    EXTRANEOUS_TABLE_REFERENCE = 55
    JOIN_CONDITION_ON_INCORRECT_COLUMN = 56
    JOIN_CONDITION_WITH_INCORRECT_COMPARISON_OPERATOR = 57
    OMITTING_A_JOIN_CONDITION = 58
    CONDITION_ON_OUTER_JOIN = 59
    IMPROPER_NESTING_OF_EXPRESSIONS = 60
    IMPROPER_NESTING_OF_SUBQUERIES = 61
    EXTRANEOUS_QUOTES = 62
    MISSING_EXPRESSION = 63
    EXTRANEOUS_EXPRESSION = 64
    EXPRESSION_ON_INCORRECT_COLUMN = 65
    EXPRESSION_IN_INCORRECT_CLAUSE = 66
    WILDCARDS_WITHOUT_LIKE = 67
    WRONG_WILDCARD = 68
    INVALID_WILDCARD = 69
    EXTRANEOUS_COLUMN_IN_SELECT = 70
    MISSING_COLUMN_FROM_SELECT = 71
    MISSING_DISTINCT_FROM_SELECT = 72
    MISSING_AS_FROM_SELECT = 73
    MISSING_COLUMN_FROM_ORDER_BY_CLAUSE = 74
    INCORRECT_COLUMN_IN_ORDER_BY_CLAUSE = 75
    INCORRECT_ORDERING_OF_ROWS = 76
    MISSING_WHERE_CLAUSE = 77
    MISSING_GROUP_BY_CLAUSE = 78
    MISSING_HAVING_CLAUSE = 79
    MISSING_ORDER_BY_CLAUSE = 80
    MISSING_LIMIT_CLAUSE = 81
    MISSING_OFFSET_CLAUSE = 82
    EXTRANEOUS_WHERE_CLAUSE = 83
    EXTRANEOUS_GROUP_BY_CLAUSE = 84
    EXTRANEOUS_HAVING_CLAUSE = 85
    EXTRANEOUS_ORDER_BY_CLAUSE = 86
    EXTRANEOUS_LIMIT_CLAUSE = 87
    EXTRANEOUS_OFFSET_CLAUSE = 88
    INCORRECT_LIMIT = 89
    INCORRECT_OFFSET = 90
    INCORRECT_FUNCTION = 91
    DISTINCT_AS_FUNCTION_PARAMETER_WHERE_NOT_APPLICABLE = 92
    MISSING_DISTINCT_FROM_FUNCTION_PARAMETER = 93
    INCORRECT_COLUMN_AS_FUNCTION_PARAMETER = 94

    # Complication
    UNNECESSARY_COMPLICATION = 95
    UNNECESSARY_DISTINCT_IN_SELECT_CLAUSE = 96
    UNNECESSARY_TABLE_REFERENCE = 97
    UNUSED_CORRELATION_NAME = 98
    TABLES_HAVE_THE_SAME_DATA = 99
    CORRELATION_NAME_IDENTICAL_TO_TABLE_NAME = 100
    UNNECESSARILY_GENERAL_COMPARISON_OPERATOR = 101
    LIKE_WITHOUT_WILDCARDS = 102
    UNNECESSARILY_COMPLICATED_SELECT_IN_EXISTS_SUBQUERY = 103
    IN_EXISTS_CAN_BE_REPLACED_BY_COMPARISON = 104
    UNNECESSARY_AGGREGATE_FUNCTION = 105
    UNNECESSARY_DISTINCT_IN_AGGREGATE_FUNCTION = 106
    UNNECESSARY_ARGUMENT_OF_COUNT = 107
    UNNECESSARY_GROUP_BY_IN_EXISTS_SUBQUERY = 108
    GROUP_BY_WITH_SINGLETON_GROUPS = 109
    GROUP_BY_WITH_ONLY_A_SINGLE_GROUP = 110
    GROUP_BY_CAN_BE_REPLACED_WITH_DISTINCT = 111
    UNION_CAN_BE_REPLACED_BY_OR = 112
    UNNECESSARY_COLUMN_IN_ORDER_BY_CLAUSE = 113
    ORDER_BY_IN_SUBQUERY = 114
    INEFFICIENT_HAVING = 115
    INEFFICIENT_UNION = 116
    CONDITION_IN_THE_SUBQUERY_CAN_BE_MOVED_UP = 117
    OUTER_JOIN_CAN_BE_REPLACED_BY_INNER_JOIN = 118
    UNUSED_CTE = 119


    @property
    def definition(self) -> SqlErrorDefinition:
        """Returns the definition of the SQL error."""
        return _SQL_ERROR_DEFINITIONS[self]

    @property
    def category(self) -> SqlErrorCategory:
        """Returns the category of the SQL error."""
        return self.definition.category

    @property
    def name(self) -> str:
        """Returns the name of the SQL error."""
        return self.definition.name

    @property
    def error_id(self) -> int:
        """
            Returns the unique identifier of the SQL error.

            **NOTE:** IDs can change across versions, so they should be stored alongside the taxonomy version.
        """
        return self.value

_SQL_ERROR_DEFINITIONS: dict[SqlErrors, SqlErrorDefinition] = {
    SqlErrors.AMBIGUOUS_COLUMN: SqlErrorDefinition('Ambiguous column',                                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.AMBIGUOUS_FUNCTION: SqlErrorDefinition('Ambiguous function',                                                                                          SqlErrorCategory.SYNTAX),
    SqlErrors.UNDEFINED_COLUMN: SqlErrorDefinition('Undefined column',                                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.UNDEFINED_FUNCTION: SqlErrorDefinition('Undefined function',                                                                                          SqlErrorCategory.SYNTAX),
    SqlErrors.UNDEFINED_PARAMETER: SqlErrorDefinition('Undefined parameter',                                                                                        SqlErrorCategory.SYNTAX),
    SqlErrors.UNDEFINED_OBJECT: SqlErrorDefinition('Undefined object',                                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.INVALID_SCHEMA_NAME: SqlErrorDefinition('Invalid schema name',                                                                                        SqlErrorCategory.SYNTAX),
    SqlErrors.MISSPELLINGS: SqlErrorDefinition('Misspellings',                                                                                                      SqlErrorCategory.SYNTAX),
    SqlErrors.SYNONYMS: SqlErrorDefinition('Synonyms',                                                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.OMITTING_QUOTES_AROUND_CHARACTER_DATA: SqlErrorDefinition('Omitting quotes around character data',                                                    SqlErrorCategory.SYNTAX),
    SqlErrors.FAILURE_TO_SPECIFY_COLUMN_NAME_TWICE: SqlErrorDefinition('Failure to specify column name twice',                                                      SqlErrorCategory.SYNTAX),
    SqlErrors.IS_WHERE_NOT_APPLICABLE: SqlErrorDefinition('IS where not applicable',                                                                                SqlErrorCategory.SYNTAX),
    SqlErrors.DATA_TYPE_MISMATCH: SqlErrorDefinition('Data type mismatch',                                                                                          SqlErrorCategory.SYNTAX),
    SqlErrors.USING_AGGREGATE_FUNCTION_OUTSIDE_SELECT_OR_HAVING: SqlErrorDefinition('Using aggregate function outside SELECT or HAVING',                            SqlErrorCategory.SYNTAX),
    SqlErrors.AGGREGATE_FUNCTIONS_CANNOT_BE_NESTED: SqlErrorDefinition('Aggregate functions cannot be nested',                                                      SqlErrorCategory.SYNTAX),
    SqlErrors.EXTRANEOUS_OR_OMITTED_GROUPING_COLUMN: SqlErrorDefinition('Extraneous or omitted grouping column',                                                    SqlErrorCategory.SYNTAX),
    SqlErrors.STRANGE_HAVING_HAVING_WITHOUT_GROUP_BY: SqlErrorDefinition('Strange HAVING: HAVING without GROUP BY',                                                 SqlErrorCategory.SYNTAX),
    SqlErrors.TOO_MANY_COLUMNS_IN_SUBQUERY: SqlErrorDefinition('Too many columns in subquery',                                                                      SqlErrorCategory.SYNTAX),
    SqlErrors.MISSING_QUANTIFIER: SqlErrorDefinition('Missing quantifier',                                                                                          SqlErrorCategory.SYNTAX),
    SqlErrors.CONFUSING_FUNCTION_WITH_FUNCTION_PARAMETER: SqlErrorDefinition('Confusing function with function parameter',                                          SqlErrorCategory.SYNTAX),
    SqlErrors.USING_WHERE_TWICE: SqlErrorDefinition('Using WHERE twice',                                                                                            SqlErrorCategory.SYNTAX),
    SqlErrors.OMITTING_THE_FROM_CLAUSE: SqlErrorDefinition('Omitting the FROM clause',                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.COMPARISON_WITH_NULL: SqlErrorDefinition('Comparison with NULL',                                                                                      SqlErrorCategory.SYNTAX),
    SqlErrors.OMITTING_THE_SEMICOLON: SqlErrorDefinition('Omitting the semicolon',                                                                                  SqlErrorCategory.SYNTAX),
    SqlErrors.DATE_TIME_FIELD_OVERFLOW: SqlErrorDefinition('Date time field overflow',                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.DUPLICATE_CLAUSE: SqlErrorDefinition('Duplicate clause',                                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.USING_AN_UNDEFINED_CORRELATION_NAME: SqlErrorDefinition('Using an undefined correlation name',                                                        SqlErrorCategory.SYNTAX),
    SqlErrors.CONFUSING_TABLE_NAMES_WITH_COLUMN_NAMES: SqlErrorDefinition('Confusing table names with column names',                                                SqlErrorCategory.SYNTAX),
    SqlErrors.CONFUSING_THE_ORDER_OF_KEYWORDS: SqlErrorDefinition('Confusing the order of keywords (e.g., FROM customer SELECT fee)',                               SqlErrorCategory.SYNTAX),
    SqlErrors.CONFUSING_THE_SYNTAX_OF_KEYWORDS: SqlErrorDefinition("Confusing the syntax of keywords (e.g., LIKE ('A,' 'B'))",                                      SqlErrorCategory.SYNTAX),
    SqlErrors.OMITTING_COMMAS: SqlErrorDefinition('Omitting commas',                                                                                                SqlErrorCategory.SYNTAX),
    SqlErrors.UNMATCHED_BRACKETS: SqlErrorDefinition('Unmatched brackets',                                                                                          SqlErrorCategory.SYNTAX),
    SqlErrors.CURLY_OR_SQUARE_BRACKETS: SqlErrorDefinition('Curly or square brackets',                                                                              SqlErrorCategory.SYNTAX),
    SqlErrors.NONSTANDARD_KEYWORDS_OR_STANDARD_KEYWORDS_IN_WRONG_CONTEXT: SqlErrorDefinition('Nonstandard keywords or standard keywords in wrong context',          SqlErrorCategory.SYNTAX),
    SqlErrors.NONSTANDARD_OPERATORS: SqlErrorDefinition('Nonstandard operators (e.g., &&, || or ==)',                                                               SqlErrorCategory.SYNTAX),
    SqlErrors.ADDITIONAL_SEMICOLON: SqlErrorDefinition('Additional semicolon',                                                                                      SqlErrorCategory.SYNTAX),
    SqlErrors.DIFFERENT_TUPLES_IN_SET_OPERATION: SqlErrorDefinition('Different tuples in set operation',                                                            SqlErrorCategory.SYNTAX),
    SqlErrors.IMPLIED_TAUTOLOGICAL_OR_INCONSISTENT_EXPRESSION: SqlErrorDefinition('Implied, tautological or inconsistent expression',                               SqlErrorCategory.SEMANTIC),
    SqlErrors.DISTINCT_IN_SUM_OR_AVG: SqlErrorDefinition('DISTINCT in SUM or AVG',                                                                                  SqlErrorCategory.SEMANTIC),
    SqlErrors.DISTINCT_THAT_MIGHT_REMOVE_IMPORTANT_DUPLICATES: SqlErrorDefinition('DISTINCT that might remove important duplicates',                                SqlErrorCategory.SEMANTIC),
    SqlErrors.MIXING_A_GREATER_THAN_0_WITH_IS_NOT_NULL_OR_EMPTY_STRING_WITH_NULL: SqlErrorDefinition('Mixing a >0 with IS NOT NULL or empty string with NULL',      SqlErrorCategory.SEMANTIC),
    SqlErrors.NULL_IN_IN_ANY_ALL_SUBQUERY: SqlErrorDefinition('NULL in IN/ANY/ALL subquery',                                                                        SqlErrorCategory.SEMANTIC),
    SqlErrors.JOIN_CONDITION_ON_UNMATCHABLE_COLUMN: SqlErrorDefinition('Join condition on unmatchable column',                                                      SqlErrorCategory.SEMANTIC),
    SqlErrors.MANY_DUPLICATES: SqlErrorDefinition('Many duplicates',                                                                                                SqlErrorCategory.SEMANTIC),
    SqlErrors.CONSTANT_COLUMN_OUTPUT: SqlErrorDefinition('Constant column output',                                                                                  SqlErrorCategory.SEMANTIC),
    SqlErrors.DUPLICATE_COLUMN_OUTPUT: SqlErrorDefinition('Duplicate column output',                                                                                SqlErrorCategory.SEMANTIC),
    SqlErrors.AND_INSTEAD_OF_OR: SqlErrorDefinition('AND instead of OR',                                                                                            SqlErrorCategory.LOGICAL),
    SqlErrors.OR_INSTEAD_OF_AND: SqlErrorDefinition('OR instead of AND',                                                                                            SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_NOT_OPERATOR: SqlErrorDefinition('Extraneous NOT operator',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_NOT_OPERATOR: SqlErrorDefinition('Missing NOT operator',                                                                                      SqlErrorCategory.LOGICAL),
    SqlErrors.SUBSTITUTING_EXISTENCE_NEGATION_WITH_NOT_EQUAL_TO: SqlErrorDefinition('Substituting existence negation with <>',                                      SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_COMPARISON_OPERATOR_OR_INCORRECT_VALUE_COMPARED: SqlErrorDefinition('Incorrect comparison operator or incorrect value compared',            SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_TABLE_REFERENCE: SqlErrorDefinition('Incorrect table reference',                                                                            SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_TABLE_REFERENCE: SqlErrorDefinition('Missing table reference',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_TABLE_REFERENCE: SqlErrorDefinition('Extraneous table reference',                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.JOIN_CONDITION_ON_INCORRECT_COLUMN: SqlErrorDefinition('Join condition on incorrect column',                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.JOIN_CONDITION_WITH_INCORRECT_COMPARISON_OPERATOR: SqlErrorDefinition('Join condition with incorrect comparison operator',                            SqlErrorCategory.LOGICAL),
    SqlErrors.OMITTING_A_JOIN_CONDITION: SqlErrorDefinition('Omitting a join condition',                                                                            SqlErrorCategory.LOGICAL),
    SqlErrors.CONDITION_ON_OUTER_JOIN: SqlErrorDefinition('Condition on OUTER JOIN',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.IMPROPER_NESTING_OF_EXPRESSIONS: SqlErrorDefinition('Improper nesting of expressions',                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.IMPROPER_NESTING_OF_SUBQUERIES: SqlErrorDefinition('Improper nesting of subqueries',                                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_QUOTES: SqlErrorDefinition('Extraneous quotes',                                                                                            SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_EXPRESSION: SqlErrorDefinition('Missing expression',                                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_EXPRESSION: SqlErrorDefinition('Extraneous expression',                                                                                    SqlErrorCategory.LOGICAL),
    SqlErrors.EXPRESSION_ON_INCORRECT_COLUMN: SqlErrorDefinition('Expression on incorrect column',                                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.EXPRESSION_IN_INCORRECT_CLAUSE: SqlErrorDefinition('Expression in incorrect clause',                                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.WILDCARDS_WITHOUT_LIKE: SqlErrorDefinition('Wildcards without LIKE',                                                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.WRONG_WILDCARD: SqlErrorDefinition('Wrong wildcard',                                                                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.INVALID_WILDCARD: SqlErrorDefinition('Invalid wildcard',                                                                                              SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_COLUMN_IN_SELECT: SqlErrorDefinition('Extraneous column in SELECT',                                                                        SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_COLUMN_FROM_SELECT: SqlErrorDefinition('Missing column from SELECT',                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_DISTINCT_FROM_SELECT: SqlErrorDefinition('Missing DISTINCT from SELECT',                                                                      SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_AS_FROM_SELECT: SqlErrorDefinition('Missing AS from SELECT',                                                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_COLUMN_FROM_ORDER_BY_CLAUSE: SqlErrorDefinition('Missing column from ORDER BY clause',                                                        SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_COLUMN_IN_ORDER_BY_CLAUSE: SqlErrorDefinition('Incorrect column in ORDER BY clause',                                                        SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_ORDERING_OF_ROWS: SqlErrorDefinition('Incorrect ordering of rows',                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_WHERE_CLAUSE: SqlErrorDefinition('Missing WHERE clause',                                                                                      SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_GROUP_BY_CLAUSE: SqlErrorDefinition('Missing GROUP BY clause',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_HAVING_CLAUSE: SqlErrorDefinition('Missing HAVING clause',                                                                                    SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_ORDER_BY_CLAUSE: SqlErrorDefinition('Missing ORDER BY clause',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_LIMIT_CLAUSE: SqlErrorDefinition('Missing LIMIT clause',                                                                                      SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_OFFSET_CLAUSE: SqlErrorDefinition('Missing OFFSET clause',                                                                                    SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_WHERE_CLAUSE: SqlErrorDefinition('Extraneous WHERE clause',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_GROUP_BY_CLAUSE: SqlErrorDefinition('Extraneous GROUP BY clause',                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_HAVING_CLAUSE: SqlErrorDefinition('Extraneous HAVING clause',                                                                              SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_ORDER_BY_CLAUSE: SqlErrorDefinition('Extraneous ORDER BY clause',                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_LIMIT_CLAUSE: SqlErrorDefinition('Extraneous LIMIT clause',                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.EXTRANEOUS_OFFSET_CLAUSE: SqlErrorDefinition('Extraneous OFFSET clause',                                                                              SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_LIMIT: SqlErrorDefinition('Incorrect LIMIT',                                                                                                SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_OFFSET: SqlErrorDefinition('Incorrect OFFSET',                                                                                              SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_FUNCTION: SqlErrorDefinition('Incorrect function',                                                                                          SqlErrorCategory.LOGICAL),
    SqlErrors.DISTINCT_AS_FUNCTION_PARAMETER_WHERE_NOT_APPLICABLE: SqlErrorDefinition('DISTINCT as function parameter where not applicable',                        SqlErrorCategory.LOGICAL),
    SqlErrors.MISSING_DISTINCT_FROM_FUNCTION_PARAMETER: SqlErrorDefinition('Missing DISTINCT from function parameter',                                              SqlErrorCategory.LOGICAL),
    SqlErrors.INCORRECT_COLUMN_AS_FUNCTION_PARAMETER: SqlErrorDefinition('Incorrect column as function parameter',                                                  SqlErrorCategory.LOGICAL),
    SqlErrors.UNNECESSARY_COMPLICATION: SqlErrorDefinition('Unnecessary complication',                                                                              SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_DISTINCT_IN_SELECT_CLAUSE: SqlErrorDefinition('Unnecessary DISTINCT in SELECT clause',                                                    SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_TABLE_REFERENCE: SqlErrorDefinition('Unnecessary table reference',                                                                        SqlErrorCategory.COMPLICATION),
    SqlErrors.UNUSED_CORRELATION_NAME: SqlErrorDefinition('Unused correlation name',                                                                                SqlErrorCategory.COMPLICATION),
    SqlErrors.TABLES_HAVE_THE_SAME_DATA: SqlErrorDefinition('Tables have the same data',                                                                            SqlErrorCategory.COMPLICATION),
    SqlErrors.CORRELATION_NAME_IDENTICAL_TO_TABLE_NAME: SqlErrorDefinition('Correlation name identical to table name',                                              SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARILY_GENERAL_COMPARISON_OPERATOR: SqlErrorDefinition('Unnecessarily general comparison operator',                                            SqlErrorCategory.COMPLICATION),
    SqlErrors.LIKE_WITHOUT_WILDCARDS: SqlErrorDefinition('LIKE without wildcards',                                                                                  SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARILY_COMPLICATED_SELECT_IN_EXISTS_SUBQUERY: SqlErrorDefinition('Unnecessarily complicated SELECT in EXISTS subquery',                        SqlErrorCategory.COMPLICATION),
    SqlErrors.IN_EXISTS_CAN_BE_REPLACED_BY_COMPARISON: SqlErrorDefinition('IN/EXISTS can be replaced by comparison',                                                SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_AGGREGATE_FUNCTION: SqlErrorDefinition('Unnecessary aggregate function',                                                                  SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_DISTINCT_IN_AGGREGATE_FUNCTION: SqlErrorDefinition('Unnecessary DISTINCT in aggregate function',                                          SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_ARGUMENT_OF_COUNT: SqlErrorDefinition('Unnecessary argument of COUNT',                                                                    SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_GROUP_BY_IN_EXISTS_SUBQUERY: SqlErrorDefinition('Unnecessary GROUP BY in EXISTS subquery',                                                SqlErrorCategory.COMPLICATION),
    SqlErrors.GROUP_BY_WITH_SINGLETON_GROUPS: SqlErrorDefinition('GROUP BY with singleton groups',                                                                  SqlErrorCategory.COMPLICATION),
    SqlErrors.GROUP_BY_WITH_ONLY_A_SINGLE_GROUP: SqlErrorDefinition('GROUP BY with only a single group',                                                            SqlErrorCategory.COMPLICATION),
    SqlErrors.GROUP_BY_CAN_BE_REPLACED_WITH_DISTINCT: SqlErrorDefinition('GROUP BY can be replaced with DISTINCT',                                                  SqlErrorCategory.COMPLICATION),
    SqlErrors.UNION_CAN_BE_REPLACED_BY_OR: SqlErrorDefinition('UNION can be replaced by OR',                                                                        SqlErrorCategory.COMPLICATION),
    SqlErrors.UNNECESSARY_COLUMN_IN_ORDER_BY_CLAUSE: SqlErrorDefinition('Unnecessary column in ORDER BY clause',                                                    SqlErrorCategory.COMPLICATION),
    SqlErrors.ORDER_BY_IN_SUBQUERY: SqlErrorDefinition('ORDER BY in subquery',                                                                                      SqlErrorCategory.COMPLICATION),
    SqlErrors.INEFFICIENT_HAVING: SqlErrorDefinition('Inefficient HAVING',                                                                                          SqlErrorCategory.COMPLICATION),
    SqlErrors.INEFFICIENT_UNION: SqlErrorDefinition('Inefficient UNION',                                                                                            SqlErrorCategory.COMPLICATION),
    SqlErrors.CONDITION_IN_THE_SUBQUERY_CAN_BE_MOVED_UP: SqlErrorDefinition('Condition in the subquery can be moved up',                                            SqlErrorCategory.COMPLICATION),
    SqlErrors.OUTER_JOIN_CAN_BE_REPLACED_BY_INNER_JOIN: SqlErrorDefinition('OUTER JOIN can be replaced by INNER JOIN',                                              SqlErrorCategory.COMPLICATION),
    SqlErrors.UNUSED_CTE: SqlErrorDefinition('Unused CTE',                                                                                                          SqlErrorCategory.COMPLICATION),
}
