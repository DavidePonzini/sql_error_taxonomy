import pytest

from sql_error_taxonomy import SqlErrors

DEPRECATED_ERROR_IDS = {
    1,
    28,
    29,
    31,
    34,
    44,
    56,
}


@pytest.mark.parametrize(
    'error',
    [error for error in SqlErrors],
    ids=[repr(error) for error in SqlErrors],
)
def test_sql_error_id_is_deprecated(error: SqlErrors) -> None:
    if error.value in DEPRECATED_ERROR_IDS:
        assert SqlErrors(error).definition.is_deprecated
    else:
        assert not SqlErrors(error).definition.is_deprecated
