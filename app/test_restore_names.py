import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_data() -> list:
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
        {
            "first_name": "Sam",
            "last_name": "Smith",
            "full_name": "Sam Smith",
        }
    ]


@pytest.fixture()
def expected_users_data() -> list:
    return [
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
        {
            "first_name": "Sam",
            "last_name": "Smith",
            "full_name": "Sam Smith",
        }
    ]


def test_restore_names(users_data: list, expected_users_data: list) -> None:
    restore_names(users_data)
    assert users_data == expected_users_data
