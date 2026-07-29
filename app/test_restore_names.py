import pytest
from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> List[dict]:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Adam Smith",
        },
        {
            "last_name": "Rockefeller",
            "full_name": "John Rockefeller",
        },
    ]
    return users


def test_restore_first_name_when_is_none(
        users_template: List[dict]
) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Adam"


def test_restore_first_name_when_does_not_exist(
        users_template: List[dict]
) -> None:
    restore_names(users_template)
    assert users_template[1]["first_name"] == "John"
