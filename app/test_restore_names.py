import pytest

from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def return_users() -> List[dict]:
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
            "first_name": "Alias",
            "last_name": "Black",
            "full_name": "Alias Black"
        }
    ]


def test_should_replace_first_name_if_it_none(
        return_users: List[dict]
) -> None:
    restore_names(return_users)
    assert return_users[0]["first_name"] == "Jack"


def test_should_add_first_name_if_it_not_exist(
        return_users: List[dict]
) -> None:
    restore_names(return_users)
    assert return_users[1]["first_name"] == "Mike"


def test_should_doing_nothing_when_first_name_correctly_exist(
        return_users: List[dict]
) -> None:
    restore_names(return_users)
    assert return_users[2]["first_name"] == "Alias"
