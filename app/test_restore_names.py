import pytest

from app.restore_names import restore_names


@pytest.fixture
def users() -> list[dict]:
    return [
        {
            "first_name": None,
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_name_is_none(users: list[dict]) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_name_is_missing(users: list[dict]) -> None:
    restore_names(users)
    assert users[1]["first_name"]
