import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
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


@pytest.fixture()
def user_restored_template() -> list:
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


def test_restore_name(
        user_template: list,
        user_restored_template: list) -> None:
    restore_names(user_template)
    assert user_template == user_restored_template
