import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_with_missing_names() -> list:
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


@pytest.fixture
def expected_restored_users() -> list:
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
    ]


def test_restore_names(users_with_missing_names: object,
                       expected_restored_users: object) -> None:
    restore_names(users_with_missing_names)
    assert users_with_missing_names == expected_restored_users
