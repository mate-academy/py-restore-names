import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture
def users_template() -> List[dict]:
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
    ]


def test_users_not_list() -> None:
    with pytest.raises(TypeError):
        restore_names(None)


def test_users_is_not_none(users_template: List[dict]) -> None:
    users = users_template
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_users_is_not_empty(users_template: List[dict]) -> None:
    assert any(users.get("first_name") is None for users in users_template)
