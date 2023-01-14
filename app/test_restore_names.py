import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
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
        {
            "first_name": "John",
            "last_name": "Galt",
            "full_name": "John Galt"
        }
    ]


def test_restore_names(users_template) -> None:
    restore_names(users_template)
    assert users_template == [
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
        {
            "first_name": "John",
            "last_name": "Galt",
            "full_name": "John Galt"
        }
    ]
