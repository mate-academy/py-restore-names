import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]


def test_restore_users(user_template: callable) -> None:
    result = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]

    restore_names(user_template)
    assert user_template == result
