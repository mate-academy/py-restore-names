import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_results",
    [
        [
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
                }
            ]
        ],
        [
            [
                {
                    "last_name": "Adams",
                    "full_name": "Jane Adams",
                },
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
            ],
            [
                {
                    "first_name": "Jane",
                    "last_name": "Adams",
                    "full_name": "Jane Adams",
                },
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
            ]
        ]
    ]
)
def test_restore_names(users: list, expected_results: list) -> None:
    restore_names(users)
    assert users == expected_results
