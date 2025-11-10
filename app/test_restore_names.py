import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def users_creator() -> list:
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
            "first_name": "Olha",
            "last_name": "Polzunkowa",
            "full_name": "Olha Polzunkowa",
        },
    ]


def test_if_user_name_is_none(users_creator: list) -> None:
    restore_names(users_creator)
    assert users_creator[0]["first_name"] == "Jack"


def test_if_user_name_not_exist(users_creator: list) -> None:
    restore_names(users_creator)
    assert users_creator[1]["first_name"] == "Mike"


def test_if_first_name_exist(users_creator: list) -> None:
    restore_names(users_creator)
    assert users_creator[2]["first_name"] == "Olha"
