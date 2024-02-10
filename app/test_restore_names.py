import pytest

from app.restore_names import restore_names


@pytest.fixture
def users() -> None:
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


def test_restore_names(users: list) -> None:
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
    ]


def test_restore_names_no_changes(users: list) -> None:
    original_users = users.copy()
    restore_names(users)
    assert users == original_users


def test_restore_names_with_existing_first_name(users: list) -> None:
    users.append({
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
    })
    original_users = users.copy()
    restore_names(users)
    assert users == original_users
