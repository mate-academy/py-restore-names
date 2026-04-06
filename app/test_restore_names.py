import pytest
from app.restore_names import restore_names


users_case_1 = [
    {
        "first_name": None,
        "last_name": "Doe",
        "full_name": "John Doe"
    }
]

expected_case_1 = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe"
    }
]

users_case_2 = [
    {
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }
]

expected_case_2 = [
    {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }
]


@pytest.mark.parametrize(
    "users, expected_users",
    [
        (users_case_1, expected_case_1),
        (users_case_2, expected_case_2),
    ]
)
def test_restore_names(users: list, expected_users: list) -> None:
    restore_names(users)
    assert users == expected_users
