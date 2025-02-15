import pytest
from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_restore_names_multiple_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_empty_list() -> None:
    users = []

    restore_names(users)

    assert users == []


@pytest.mark.parametrize(
    "users,expected_first_names",
    [
        (
            [{"first_name": None, "full_name": "Jack Holy"}],
            ["Jack"]
        ),
        (
            [{"full_name": "Mike Adams"}],
            ["Mike"]
        ),
        (
            [
                {"first_name": None, "full_name": "Jack Holy"},
                {"full_name": "Mike Adams"},
                {"first_name": "John", "full_name": "John Doe"}
            ],
            ["Jack", "Mike", "John"]
        ),
    ]
)
def test_restore_names_parametrized(
        users: list,
        expected_first_names: list
) -> None:
    restore_names(users)

    for user, expected_name in zip(users, expected_first_names):
        assert user["first_name"] == expected_name
