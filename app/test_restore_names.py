import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_after_template() -> list:
    users_after = [
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
    return users_after


@pytest.fixture()
def user_before_template() -> list:
    users_before = [
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
    return users_before


def test_restore_names(user_before_template: list,
                       user_after_template: list) -> None:
    restore_names(user_before_template)
    assert user_before_template == user_after_template
