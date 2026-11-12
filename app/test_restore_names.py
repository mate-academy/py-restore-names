import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        pytest.param(
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holly"},
                {"last_name": "Adams",
                 "full_name": "Mike Adams"},
                {"first_name": "Derek",
                 "last_name": "Bishop",
                 "full_name": "Derek Bishop"},
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holly"},
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"},
                {"first_name": "Derek",
                 "last_name": "Bishop",
                 "full_name": "Derek Bishop"},
            ],
        ),
    ],
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    assert restore_names(users) is None
    assert restore_names(users) == expected
