import pytest
from app.restore_names import restore_names


@pytest.fixture
def base_users() -> list[dict]:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]


def test_restore_names_when_first_name_is_none(base_users: list[dict]) -> None:
    users = [user.copy() for user in base_users]

    users[0]["first_name"] = None
    users[1]["first_name"] = None

    restore_names(users)

    expected = [
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

    assert users == expected


def test_restore_names_when_first_name_missing(base_users: list[dict]) -> None:
    users = [user.copy() for user in base_users]
    restore_names(users)

    expected = [
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

    assert users == expected
