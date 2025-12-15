import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list:
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
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]


def test_restore_names_for_missing_and_none_first_name(users: list) -> None:
    restore_names(users)
    assert users == [
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
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]


def test_no_change_for_users_with_existing_first_name(users: list) -> None:
    restore_names(users)
    original_users = users[:]
    restore_names(users)
    assert users == original_users


def test_function_does_not_return_value(users: list) -> None:
    result = restore_names(users)
    assert result is None
