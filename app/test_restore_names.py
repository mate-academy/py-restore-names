import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("input_users, expected_users", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ],
        [
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
    ),
    (
        [
            {
                "first_name": "Alice",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Bob",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ],
        [
            {
                "first_name": "Alice",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Bob",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
    ),
])
def test_restore_names_with_parameterization(input_users, expected_users):
    restore_names(input_users)
    assert input_users == expected_users
