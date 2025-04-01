import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users,expected", [
    pytest.param(
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ], [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ],
        id="Add first name if it is None"
    ),
    pytest.param(
        [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ], [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ],
        id="Add first name if it is not there"
    ),
])
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected


def test_restore_names_return_none() -> None:
    assert (
        restore_names([
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]) is None
    ), "Should return None"
