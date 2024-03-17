import pytest
from app.restore_names import restore_names
from typing import Callable


@pytest.fixture
def users_template() -> None:
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
    yield users


def test_restore_names(users_template: Callable) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"
    assert users_template[1]["first_name"] == "Mike"
