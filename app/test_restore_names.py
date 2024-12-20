import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_example() -> list[dict]:
    users = [
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

    return users


def test_restore_user_with_none(users_example: list[dict]) -> None:
    restore_names(users_example)
    assert users_example[0]["first_name"] == "Jack"


def test_restore_user_with_empty_name(users_example: list[dict]) -> None:
    restore_names(users_example)
    assert users_example[1]["first_name"] == "Mike"
