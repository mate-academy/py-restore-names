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
    ]


def test_restore_if_first_name_is_none(users: list) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_if_first_name_was_excluded(users: list) -> None:
    restore_names(users)
    assert users[1].get("first_name") == "Mike"
