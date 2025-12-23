import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Black",
            "last_name": "Adam",
            "full_name": "Black Adam",
        }
    ]


def test_restore_names_when_correct_user(users: list[dict]) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Black"


def test_restore_names_when_first_name_is_missing(users: list[dict]) -> None:
    for user in users:
        del user["first_name"]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Black"


def test_restore_names_when_first_name_is_none(users: list[dict]) -> None:
    for user in users:
        user["first_name"] = None
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Black"
