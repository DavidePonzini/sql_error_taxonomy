from enum import IntEnum, StrEnum, unique
from dataclasses import dataclass

@unique
class SqlErrorCategory(StrEnum):
    '''Enumeration of SQL error categories.'''
    SYNTAX = 'SYN'
    SEMANTIC = 'SEM'
    LOGICAL = 'LOG'
    COMPLICATION = 'COM'

@dataclass(frozen=True)
class SqlErrorDefinition:
    '''Data class representing the definition of an SQL error.'''
    _name: str
    category: SqlErrorCategory
    is_deprecated: bool = False
    deprecation_message: str = ''

    @property
    def name(self):
        '''Returns the name of the SQL error.'''
        if self.is_deprecated:
            return f'[DEPRECATED] {self._name}'
        return self._name

@unique
class SqlErrors(IntEnum):
    '''
        Enumeration of SQL error types with unique identifiers.

        **NOTE:** The unique identifiers assigned to each error type will never be changed or removed, but new IDs may be added in the future.
    '''

    # Syntax errors
    AMBIGUOUS_COLUMN = 2
    AMBIGUOUS_FUNCTION = 3
    UNDEFINED_COLUMN = 4
    UNDEFINED_FUNCTION = 5
    UNDEFINED_PARAMETER = 6
    UNDEFINED_OBJECT = 7
    INVALID_SCHEMA_NAME = 8
    MISSPELLINGS = 9
    SYNONYMS = 10
    OMITTED_QUOTES = 11
    FAILURE_TO_SPECIFY_COLUMN_NAME_TWICE = 12
    IS_WHERE_NOT_APPLICABLE = 35
    DATA_TYPE_MISMATCH = 13
    AGGREGATE_FUNCTION_OUTSIDE_SELECT_OR_HAVING = 14
    AGGREGATE_FUNCTIONS_CANNOT_BE_NESTED = 15
    EXTRANEOUS_OR_OMITTED_GROUPING_COLUMN = 16
    HAVING_WITHOUT_GROUP_BY = 17
    TOO_MANY_COLUMNS_IN_SUBQUERY = 106
    MISSING_QUANTIFIER = 107
    CONFUSING_FUNCTION_WITH_FUNCTION_PARAMETER = 18
    USING_WHERE_TWICE = 19
    OMITTED_FROM_CLAUSE = 20
    COMPARISON_WITH_NULL = 21
    OMITTED_SEMICOLON = 22
    ADDITIONAL_SEMICOLON = 38
    DATE_TIME_FIELD_OVERFLOW = 23
    DUPLICATE_CLAUSE = 24
    UNDEFINED_CORRELATION_NAME = 25
    CONFUSED_TABLE_NAMES_WITH_COLUMN_NAMES = 27
    CONFUSED_ORDER_OF_KEYWORDS = 30
    CONFUSED_SYNTAX_OF_KEYWORDS = 32
    OMITTED_COMMAS = 33
    UNMATCHED_BRACKETS = 108
    CURLY_OR_SQUARE_BRACKETS = 109
    NONSTANDARD_KEYWORDS_OR_STANDARD_KEYWORDS_IN_WRONG_CONTEXT = 36
    NONSTANDARD_OPERATORS = 37
    DIFFERENT_TUPLES_IN_SET_OPERATION = 110

    # Semantic errors
    IMPLIED_TAUTOLOGICAL_OR_INCONSISTENT_EXPRESSION = 40
    DISTINCT_IN_SUM_OR_AVG = 41
    DISTINCT_THAT_MIGHT_REMOVE_IMPORTANT_DUPLICATES = 42
    MIXED_A_GREATER_THAN_0_WITH_IS_NOT_NULL_OR_EMPTY_STRING_WITH_NULL = 45
    NULL_IN_IN_ANY_ALL_SUBQUERY = 46
    JOIN_CONDITION_ON_UNMATCHABLE_COLUMN = 47
    MANY_DUPLICATES = 49
    CONSTANT_COLUMN_OUTPUT = 50
    DUPLICATE_COLUMN_OUTPUT = 51

    # Logical errors
    AND_INSTEAD_OF_OR = 39
    OR_INSTEAD_OF_AND = 52
    EXTRANEOUS_NOT_OPERATOR = 53
    MISSING_NOT_OPERATOR = 54
    SUBSTITUTED_EXISTENCE_NEGATION_WITH_NOT_EQUAL_TO = 55
    INCORRECT_COMPARISON_OPERATOR_OR_INCORRECT_VALUE_COMPARED = 57
    INCORRECT_TABLE_REFERENCE = 58
    MISSING_TABLE_REFERENCE = 62
    EXTRANEOUS_TABLE_REFERENCE = 59
    JOIN_CONDITION_ON_INCORRECT_COLUMN = 60
    JOIN_CONDITION_WITH_INCORRECT_COMPARISON_OPERATOR = 61
    MISSING_JOIN_CONDITION = 48
    CONDITION_ON_OUTER_JOIN = 104
    IMPROPER_NESTING_OF_EXPRESSIONS = 63
    IMPROPER_NESTING_OF_SUBQUERIES = 64
    EXTRANEOUS_QUOTES = 65
    MISSING_EXPRESSION = 66
    EXTRANEOUS_EXPRESSION = 68
    EXPRESSION_ON_INCORRECT_COLUMN = 67
    EXPRESSION_IN_INCORRECT_CLAUSE = 69
    WILDCARDS_WITHOUT_LIKE = 43
    WRONG_WILDCARD = 112
    INVALID_WILDCARD = 113
    EXTRANEOUS_COLUMN_IN_SELECT = 70
    MISSING_COLUMN_FROM_SELECT = 71
    MISSING_DISTINCT_FROM_SELECT = 72
    MISSING_AS_FROM_SELECT = 73
    MISSING_COLUMN_FROM_ORDER_BY_CLAUSE = 74
    INCORRECT_COLUMN_IN_ORDER_BY_CLAUSE = 75
    INCORRECT_ORDERING_OF_ROWS = 77
    MISSING_WHERE_CLAUSE = 114
    MISSING_GROUP_BY_CLAUSE = 115
    MISSING_HAVING_CLAUSE = 116
    MISSING_ORDER_BY_CLAUSE = 117
    MISSING_LIMIT_CLAUSE = 118
    MISSING_OFFSET_CLAUSE = 119
    EXTRANEOUS_WHERE_CLAUSE = 120
    EXTRANEOUS_GROUP_BY_CLAUSE = 121
    EXTRANEOUS_HAVING_CLAUSE = 122
    EXTRANEOUS_ORDER_BY_CLAUSE = 76
    EXTRANEOUS_LIMIT_CLAUSE = 123
    EXTRANEOUS_OFFSET_CLAUSE = 124
    INCORRECT_LIMIT = 125
    INCORRECT_OFFSET = 126
    INCORRECT_FUNCTION = 80
    DISTINCT_AS_FUNCTION_PARAMETER_WHERE_NOT_APPLICABLE = 78
    MISSING_DISTINCT_FROM_FUNCTION_PARAMETER = 79
    INCORRECT_COLUMN_AS_FUNCTION_PARAMETER = 81

    # Complication
    UNNECESSARY_COMPLICATION = 82
    UNNECESSARY_DISTINCT_IN_SELECT_CLAUSE = 83
    UNNECESSARY_TABLE_REFERENCE = 84
    UNUSED_CORRELATION_NAME = 85
    TABLES_HAVE_SAME_DATA = 86
    CORRELATION_NAME_IDENTICAL_TO_TABLE_NAME = 127
    UNNECESSARILY_GENERAL_COMPARISON_OPERATOR = 87
    LIKE_WITHOUT_WILDCARDS = 88
    UNNECESSARILY_COMPLICATED_SELECT_IN_EXISTS_SUBQUERY = 89
    IN_EXISTS_CAN_BE_REPLACED_BY_COMPARISON = 90
    UNNECESSARY_AGGREGATE_FUNCTION = 91
    UNNECESSARY_DISTINCT_IN_AGGREGATE_FUNCTION = 92
    UNNECESSARY_ARGUMENT_OF_COUNT = 93
    UNNECESSARY_GROUP_BY_IN_EXISTS_SUBQUERY = 94
    GROUP_BY_WITH_SINGLETON_GROUPS = 95
    GROUP_BY_WITH_ONLY_A_SINGLE_GROUP = 96
    GROUP_BY_CAN_BE_REPLACED_WITH_DISTINCT = 97
    UNION_CAN_BE_REPLACED_BY_OR = 98
    UNNECESSARY_COLUMN_IN_ORDER_BY_CLAUSE = 99
    ORDER_BY_IN_SUBQUERY = 100
    INEFFICIENT_HAVING = 101
    INEFFICIENT_UNION = 102
    CONDITION_IN_SUBQUERY_CAN_BE_MOVED_UP = 103
    OUTER_JOIN_CAN_BE_REPLACED_BY_INNER_JOIN = 105
    UNUSED_CTE = 128

    # DEPRECATED
    OMITTING_CORRELATION_NAMES = 1
    RESTRICTION_IN_SELECT_CLAUSE = 28
    PROJECTION_IN_WHERE_CLAUSE = 29
    CONFUSED_LOGIC_OF_KEYWORDS = 31
    CURLY_SQUARE_UNMATCHED_BRACKETS = 34
    INCORRECT_WILDCARD = 44
    PUTTING_NOT_IN_FRONT_OF_INCORRECT_IN_EXISTS = 56

    @property
    def definition(self) -> SqlErrorDefinition:
        '''Returns the definition of the SQL error.'''
        return _SQL_ERROR_DEFINITIONS[self]

    @property
    def category(self) -> SqlErrorCategory:
        '''Returns the category of the SQL error.'''
        return self.definition.category

    @property
    def error_id(self) -> int:
        '''Returns the unique identifier of the SQL error.'''
        return self.value

_SQL_ERROR_DEFINITIONS: dict[SqlErrors, SqlErrorDefinition] = {
    SqlErrors.OMITTING_CORRELATION_NAMES: SqlErrorDefinition(
        'Omitting correlation names',
        SqlErrorCategory.SYNTAX,
        is_deprecated=True,
        deprecation_message='Use #2 AMBIGUOUS_COLUMN instead, which is more specific and covers the same cases.'
    ),

    SqlErrors.AMBIGUOUS_COLUMN: SqlErrorDefinition(
        'Ambiguous column',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.AMBIGUOUS_FUNCTION: SqlErrorDefinition(
        'Ambiguous function',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.UNDEFINED_COLUMN: SqlErrorDefinition(
        'Undefined column',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.UNDEFINED_FUNCTION: SqlErrorDefinition(
        'Undefined function',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.UNDEFINED_PARAMETER: SqlErrorDefinition(
        'Undefined parameter',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.UNDEFINED_OBJECT: SqlErrorDefinition(
        'Undefined object',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.INVALID_SCHEMA_NAME: SqlErrorDefinition(
        'Invalid schema name',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.MISSPELLINGS: SqlErrorDefinition(
        'Misspellings',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.SYNONYMS: SqlErrorDefinition(
        'Synonyms',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.OMITTED_QUOTES: SqlErrorDefinition(
        'Omitting quotes around character data',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.FAILURE_TO_SPECIFY_COLUMN_NAME_TWICE: SqlErrorDefinition(
        'Failure to specify column name twice',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.IS_WHERE_NOT_APPLICABLE: SqlErrorDefinition(
        'IS where not applicable',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.DATA_TYPE_MISMATCH: SqlErrorDefinition(
        'Data type mismatch',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.AGGREGATE_FUNCTION_OUTSIDE_SELECT_OR_HAVING: SqlErrorDefinition(
        'Using aggregate function outside SELECT or HAVING',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.AGGREGATE_FUNCTIONS_CANNOT_BE_NESTED: SqlErrorDefinition(
        'Aggregate functions cannot be nested',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.EXTRANEOUS_OR_OMITTED_GROUPING_COLUMN: SqlErrorDefinition(
        'Extraneous or omitted grouping column',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.HAVING_WITHOUT_GROUP_BY: SqlErrorDefinition(
        'Strange HAVING: HAVING without GROUP BY',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.TOO_MANY_COLUMNS_IN_SUBQUERY: SqlErrorDefinition(
        'Too many columns in subquery',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.MISSING_QUANTIFIER: SqlErrorDefinition(
        'Missing quantifier',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.CONFUSING_FUNCTION_WITH_FUNCTION_PARAMETER: SqlErrorDefinition(
        'Confusing function with function parameter',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.USING_WHERE_TWICE: SqlErrorDefinition(
        'Using WHERE twice',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.OMITTED_FROM_CLAUSE: SqlErrorDefinition(
        'Omitting the FROM clause',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.COMPARISON_WITH_NULL: SqlErrorDefinition(
        'Comparison with NULL',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.OMITTED_SEMICOLON: SqlErrorDefinition(
        'Omitting the semicolon',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.DATE_TIME_FIELD_OVERFLOW: SqlErrorDefinition(
        'Date time field overflow',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.DUPLICATE_CLAUSE: SqlErrorDefinition(
        'Duplicate clause',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.UNDEFINED_CORRELATION_NAME: SqlErrorDefinition(
        'Using an undefined correlation name',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.CONFUSED_TABLE_NAMES_WITH_COLUMN_NAMES: SqlErrorDefinition(
        'Confusing table names with column names',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.RESTRICTION_IN_SELECT_CLAUSE: SqlErrorDefinition(
        'Restriction in SELECT clause (e.g., SELECT fee > 100)',
        SqlErrorCategory.SYNTAX,
        is_deprecated=True,
        deprecation_message='Not an error per se, use more specific errors, such as #70 EXTRANEOUS_COLUMN_IN_SELECT, or #66 MISSING_EXPRESSION instead, based on the actual request'
    ),
    SqlErrors.PROJECTION_IN_WHERE_CLAUSE: SqlErrorDefinition(
        'Projection in WHERE clause (e.g., WHERE firstname, surname)',
        SqlErrorCategory.SYNTAX,
        is_deprecated=True,
        deprecation_message='Based on student\'s intent. Use error #32 CONFUSED_SYNTAX_OF_KEYWORDS or a more appropriate error instead.'
    ),
    SqlErrors.CONFUSED_ORDER_OF_KEYWORDS: SqlErrorDefinition(
        'Confusing the order of keywords (e.g., FROM customer SELECT fee)',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.CONFUSED_LOGIC_OF_KEYWORDS: SqlErrorDefinition(
        'Confused logic of keywords',
        SqlErrorCategory.SYNTAX,
        is_deprecated=True,
        deprecation_message='Undetectable without knowing the student\'s intent. Use other errors instead.'
    ),
    SqlErrors.CONFUSED_SYNTAX_OF_KEYWORDS: SqlErrorDefinition(
        "Confusing the syntax of keywords (e.g., LIKE ('A,' 'B'))",
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.OMITTED_COMMAS: SqlErrorDefinition(
        'Omitting commas',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.CURLY_SQUARE_UNMATCHED_BRACKETS: SqlErrorDefinition(
        'Curly, square, or unmatched brackets',
        SqlErrorCategory.SYNTAX,
        is_deprecated=True,
        deprecation_message='Use #108 UNMATCHED_BRACKETS or #109 CURLY_OR_SQUARE_BRACKETS instead.'
    ),
    SqlErrors.UNMATCHED_BRACKETS: SqlErrorDefinition(
        'Unmatched brackets',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.CURLY_OR_SQUARE_BRACKETS: SqlErrorDefinition(
        'Curly or square brackets',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.NONSTANDARD_KEYWORDS_OR_STANDARD_KEYWORDS_IN_WRONG_CONTEXT: SqlErrorDefinition(
        'Nonstandard keywords or standard keywords in wrong context',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.NONSTANDARD_OPERATORS: SqlErrorDefinition(
        'Nonstandard operators (e.g., &&, || or ==)',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.ADDITIONAL_SEMICOLON: SqlErrorDefinition(
        'Additional semicolon',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.DIFFERENT_TUPLES_IN_SET_OPERATION: SqlErrorDefinition(
        'Different tuples in set operation',
        SqlErrorCategory.SYNTAX
    ),
    SqlErrors.IMPLIED_TAUTOLOGICAL_OR_INCONSISTENT_EXPRESSION: SqlErrorDefinition(
        'Implied, tautological or inconsistent expression',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.DISTINCT_IN_SUM_OR_AVG: SqlErrorDefinition(
        'DISTINCT in SUM or AVG',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.DISTINCT_THAT_MIGHT_REMOVE_IMPORTANT_DUPLICATES: SqlErrorDefinition(
        'DISTINCT that might remove important duplicates',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.MIXED_A_GREATER_THAN_0_WITH_IS_NOT_NULL_OR_EMPTY_STRING_WITH_NULL: SqlErrorDefinition(
        'Mixing a >0 with IS NOT NULL or empty string with NULL',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.NULL_IN_IN_ANY_ALL_SUBQUERY: SqlErrorDefinition(
        'NULL in IN/ANY/ALL subquery',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.JOIN_CONDITION_ON_UNMATCHABLE_COLUMN: SqlErrorDefinition(
        'Join condition on unmatchable column',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.MANY_DUPLICATES: SqlErrorDefinition(
        'Many duplicates',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.CONSTANT_COLUMN_OUTPUT: SqlErrorDefinition(
        'Constant column output',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.DUPLICATE_COLUMN_OUTPUT: SqlErrorDefinition(
        'Duplicate column output',
        SqlErrorCategory.SEMANTIC
    ),
    SqlErrors.AND_INSTEAD_OF_OR: SqlErrorDefinition(
        'AND instead of OR',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.OR_INSTEAD_OF_AND: SqlErrorDefinition(
        'OR instead of AND',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_NOT_OPERATOR: SqlErrorDefinition(
        'Extraneous NOT operator',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_NOT_OPERATOR: SqlErrorDefinition(
        'Missing NOT operator',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.SUBSTITUTED_EXISTENCE_NEGATION_WITH_NOT_EQUAL_TO: SqlErrorDefinition(
        'Substituting existence negation with <>',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.PUTTING_NOT_IN_FRONT_OF_INCORRECT_IN_EXISTS: SqlErrorDefinition(
        'Putting NOT in front of incorrect IN/EXISTS',
        SqlErrorCategory.LOGICAL,
        is_deprecated=True,
        deprecation_message='Use #53 EXTRANEOUS_NOT_OPERATOR or #54 MISSING_NOT_OPERATOR instead.'
    ),
    SqlErrors.INCORRECT_COMPARISON_OPERATOR_OR_INCORRECT_VALUE_COMPARED: SqlErrorDefinition(
        'Incorrect comparison operator or incorrect value compared',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_TABLE_REFERENCE: SqlErrorDefinition(
        'Incorrect table reference',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_TABLE_REFERENCE: SqlErrorDefinition(
        'Missing table reference',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_TABLE_REFERENCE: SqlErrorDefinition(
        'Extraneous table reference',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.JOIN_CONDITION_ON_INCORRECT_COLUMN: SqlErrorDefinition(
        'Join condition on incorrect column',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.JOIN_CONDITION_WITH_INCORRECT_COMPARISON_OPERATOR: SqlErrorDefinition(
        'Join condition with incorrect comparison operator',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_JOIN_CONDITION: SqlErrorDefinition(
        'Missing join condition',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.CONDITION_ON_OUTER_JOIN: SqlErrorDefinition(
        'Condition on OUTER JOIN',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.IMPROPER_NESTING_OF_EXPRESSIONS: SqlErrorDefinition(
        'Improper nesting of expressions',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.IMPROPER_NESTING_OF_SUBQUERIES: SqlErrorDefinition(
        'Improper nesting of subqueries',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_QUOTES: SqlErrorDefinition(
        'Extraneous quotes',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_EXPRESSION: SqlErrorDefinition(
        'Missing expression',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_EXPRESSION: SqlErrorDefinition(
        'Extraneous expression',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXPRESSION_ON_INCORRECT_COLUMN: SqlErrorDefinition(
        'Expression on incorrect column',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXPRESSION_IN_INCORRECT_CLAUSE: SqlErrorDefinition(
        'Expression in incorrect clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.WILDCARDS_WITHOUT_LIKE: SqlErrorDefinition(
        'Wildcards without LIKE',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_WILDCARD: SqlErrorDefinition(
        'Incorrect wildcard',
        SqlErrorCategory.LOGICAL,
        is_deprecated=True,
        deprecation_message='Use #112 WRONG_WILDCARD or #113 INVALID_WILDCARD instead.'
    ),
    SqlErrors.WRONG_WILDCARD: SqlErrorDefinition(
        'Wrong wildcard',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INVALID_WILDCARD: SqlErrorDefinition(
        'Invalid wildcard',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_COLUMN_IN_SELECT: SqlErrorDefinition(
        'Extraneous column in SELECT',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_COLUMN_FROM_SELECT: SqlErrorDefinition(
        'Missing column from SELECT',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_DISTINCT_FROM_SELECT: SqlErrorDefinition(
        'Missing DISTINCT from SELECT',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_AS_FROM_SELECT: SqlErrorDefinition(
        'Missing AS from SELECT',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_COLUMN_FROM_ORDER_BY_CLAUSE: SqlErrorDefinition(
        'Missing column from ORDER BY clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_COLUMN_IN_ORDER_BY_CLAUSE: SqlErrorDefinition(
        'Incorrect column in ORDER BY clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_ORDERING_OF_ROWS: SqlErrorDefinition(
        'Incorrect ordering of rows',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_WHERE_CLAUSE: SqlErrorDefinition(
        'Missing WHERE clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_GROUP_BY_CLAUSE: SqlErrorDefinition(
        'Missing GROUP BY clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_HAVING_CLAUSE: SqlErrorDefinition(
        'Missing HAVING clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_ORDER_BY_CLAUSE: SqlErrorDefinition(
        'Missing ORDER BY clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_LIMIT_CLAUSE: SqlErrorDefinition(
        'Missing LIMIT clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_OFFSET_CLAUSE: SqlErrorDefinition(
        'Missing OFFSET clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_WHERE_CLAUSE: SqlErrorDefinition(
        'Extraneous WHERE clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_GROUP_BY_CLAUSE: SqlErrorDefinition(
        'Extraneous GROUP BY clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_HAVING_CLAUSE: SqlErrorDefinition(
        'Extraneous HAVING clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_ORDER_BY_CLAUSE: SqlErrorDefinition(
        'Extraneous ORDER BY clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_LIMIT_CLAUSE: SqlErrorDefinition(
        'Extraneous LIMIT clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.EXTRANEOUS_OFFSET_CLAUSE: SqlErrorDefinition(
        'Extraneous OFFSET clause',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_LIMIT: SqlErrorDefinition(
        'Incorrect LIMIT',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_OFFSET: SqlErrorDefinition(
        'Incorrect OFFSET',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_FUNCTION: SqlErrorDefinition(
        'Incorrect function',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.DISTINCT_AS_FUNCTION_PARAMETER_WHERE_NOT_APPLICABLE: SqlErrorDefinition(
        'DISTINCT as function parameter where not applicable',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.MISSING_DISTINCT_FROM_FUNCTION_PARAMETER: SqlErrorDefinition(
        'Missing DISTINCT from function parameter',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.INCORRECT_COLUMN_AS_FUNCTION_PARAMETER: SqlErrorDefinition(
        'Incorrect column as function parameter',
        SqlErrorCategory.LOGICAL
    ),
    SqlErrors.UNNECESSARY_COMPLICATION: SqlErrorDefinition(
        'Unnecessary complication',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_DISTINCT_IN_SELECT_CLAUSE: SqlErrorDefinition(
        'Unnecessary DISTINCT in SELECT clause',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_TABLE_REFERENCE: SqlErrorDefinition(
        'Unnecessary table reference',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNUSED_CORRELATION_NAME: SqlErrorDefinition(
        'Unused correlation name',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.TABLES_HAVE_SAME_DATA: SqlErrorDefinition(
        'Tables have the same data',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.CORRELATION_NAME_IDENTICAL_TO_TABLE_NAME: SqlErrorDefinition(
        'Correlation name identical to table name',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARILY_GENERAL_COMPARISON_OPERATOR: SqlErrorDefinition(
        'Unnecessarily general comparison operator',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.LIKE_WITHOUT_WILDCARDS: SqlErrorDefinition(
        'LIKE without wildcards',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARILY_COMPLICATED_SELECT_IN_EXISTS_SUBQUERY: SqlErrorDefinition(
        'Unnecessarily complicated SELECT in EXISTS subquery',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.IN_EXISTS_CAN_BE_REPLACED_BY_COMPARISON: SqlErrorDefinition(
        'IN/EXISTS can be replaced by comparison',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_AGGREGATE_FUNCTION: SqlErrorDefinition(
        'Unnecessary aggregate function',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_DISTINCT_IN_AGGREGATE_FUNCTION: SqlErrorDefinition(
        'Unnecessary DISTINCT in aggregate function',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_ARGUMENT_OF_COUNT: SqlErrorDefinition(
        'Unnecessary argument of COUNT',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_GROUP_BY_IN_EXISTS_SUBQUERY: SqlErrorDefinition(
        'Unnecessary GROUP BY in EXISTS subquery',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.GROUP_BY_WITH_SINGLETON_GROUPS: SqlErrorDefinition(
        'GROUP BY with singleton groups',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.GROUP_BY_WITH_ONLY_A_SINGLE_GROUP: SqlErrorDefinition(
        'GROUP BY with only a single group',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.GROUP_BY_CAN_BE_REPLACED_WITH_DISTINCT: SqlErrorDefinition(
        'GROUP BY can be replaced with DISTINCT',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNION_CAN_BE_REPLACED_BY_OR: SqlErrorDefinition(
        'UNION can be replaced by OR',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNNECESSARY_COLUMN_IN_ORDER_BY_CLAUSE: SqlErrorDefinition(
        'Unnecessary column in ORDER BY clause',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.ORDER_BY_IN_SUBQUERY: SqlErrorDefinition(
        'ORDER BY in subquery',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.INEFFICIENT_HAVING: SqlErrorDefinition(
        'Inefficient HAVING',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.INEFFICIENT_UNION: SqlErrorDefinition(
        'Inefficient UNION',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.CONDITION_IN_SUBQUERY_CAN_BE_MOVED_UP: SqlErrorDefinition(
        'Condition in the subquery can be moved up',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.OUTER_JOIN_CAN_BE_REPLACED_BY_INNER_JOIN: SqlErrorDefinition(
        'OUTER JOIN can be replaced by INNER JOIN',
        SqlErrorCategory.COMPLICATION
    ),
    SqlErrors.UNUSED_CTE: SqlErrorDefinition(
        'Unused CTE',
        SqlErrorCategory.COMPLICATION
    ),
}
