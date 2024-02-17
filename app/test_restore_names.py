import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_templates() -> list:
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


def test_when_name_is_none(users_templates: pytest.fixture) -> None:
    restore_names(users_templates)
    assert users_templates[0] == {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }


def test_when_first_name_not_exist(users_templates: pytest.fixture) -> None:
    restore_names(users_templates)
    assert users_templates[1] == {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }
