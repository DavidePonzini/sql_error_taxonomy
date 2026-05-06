import pytest

from sql_error_taxonomy import SqlErrors

def test_sql_error_ids_are_contiguous() -> None:
    assert sorted(error.value for error in SqlErrors) == list(range(1, len(SqlErrors) + 1))
