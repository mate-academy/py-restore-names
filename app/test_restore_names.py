import pytest

from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> List[dict]:
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }, {
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    return users


def test_to_restore_names(users_template: List[dict]) -> None:
    restore_names(users_template)
    assert users_template == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }, {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
