import pytest
from copy import deepcopy
from app.restore_names import restore_names


@pytest.fixture
def users_template() -> list:
    users = [
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
    return users


def test_first_name_is_none(users_template: list) -> None:
    new_users = deepcopy(users_template)
    new_users[0]["first_name"] = None

    assert restore_names(new_users) == users_template


def test_parameter_first_name_missing(users_template: list) -> None:
    new_users = deepcopy(users_template)
    new_users[0].pop("first_name")

    assert restore_names(new_users) == users_template
