import pytest

from app.restore_names import restore_names


@pytest.fixture
def users_with_missing_first_name() -> list[dict]:
    return [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"
         },
        {"last_name": "Adams",
         "full_name": "Mike Adams"
         }
    ]


@pytest.fixture
def users_with_first_name() -> list[dict]:
    return [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"
         }
    ]


@pytest.fixture
def empty_users() -> list:
    return []


def test_restore_names_with_missing_first_name(
        users_with_missing_first_name: list[dict]
) -> None:
    restore_names(users_with_missing_first_name)
    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]

    assert users_with_missing_first_name == expected


def test_restore_names_with_existing_first_name(
        users_with_first_name: list[dict]
) -> None:
    original = users_with_first_name.copy()
    restore_names(users_with_first_name)
    assert users_with_first_name == original


def test_restore_empty_users(empty_users: list) -> None:
    restore_names(empty_users)
    assert empty_users == []
