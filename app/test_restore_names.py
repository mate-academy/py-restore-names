import pytest
from app.restore_names import restore_names


@pytest.fixture
def user() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_missing_and_none_first_names(user: list) -> None:
    restore_names(user)
    assert user == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_empty_users() -> None:
    users = []

    result = restore_names(users)

    assert result is None
    assert users == []
