import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> List[dict]:
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


def test_should_check_function_with_users_whose_first_name_is_equal_to_none(
        user_template: List[dict]
) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_should_check_function_with_users_whose_first_name_is_missing(
        user_template: List[dict]
) -> None:
    restore_names(user_template)
    assert user_template[1]["first_name"] == "Mike"
