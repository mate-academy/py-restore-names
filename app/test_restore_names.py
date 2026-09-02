import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user() -> list:
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
            "first_name": "Tom",
            "last_name": "Black",
            "full_name": "Bob Black",
        }
    ]


def test_restore_names_if_first_name_equal_none(user: list[dict]) -> None:
    restore_names(user)
    assert user[0]["first_name"] == "Jack"


def test_restore_names_if_first_name_not_in_dict(user: list[dict]) -> None:
    restore_names(user)
    assert user[1]["first_name"] == "Mike"


def test_restore_names_if_name_in_dict(user: list[dict]) -> None:
    restore_names(user)
    assert user[2]["first_name"] == "Tom"


def test_should_return_none(user: list[dict]) -> None:
    assert restore_names(user) is None
