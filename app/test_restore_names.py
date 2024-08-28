import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list[dict]:
    users_template = [
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
    return users_template


@pytest.fixture()
def fixed_users() -> list[dict]:
    fixed_users = [
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
    return fixed_users


def test_restore_names(users_template: list[dict],
                       fixed_users: list[dict]) -> None:
    restore_names(users_template)
    assert users_template == fixed_users
