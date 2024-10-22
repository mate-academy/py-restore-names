import pytest
from app.restore_names import restore_names


@pytest.fixture()
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
        }
    ]


def test_when_first_name_is_none(users: list) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_when_no_first_name_in_dict(users: list) -> None:
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
