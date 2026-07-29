import pytest
from app.restore_names import restore_names


@pytest.fixture()
def data_of_users_with_error() -> list[dict]:
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


def test_should_restore_names(data_of_users_with_error: list[dict]) -> None:
    except_users_with_none = [
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

    restore_names(data_of_users_with_error)

    assert data_of_users_with_error == except_users_with_none
