import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize(
    "users,expected_result",
    [
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
                }
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
        ),
        (
            [
                {
                    "last_name": "Smith",
                    "full_name": "Adam Smith",
                },
                {
                    "first_name": None,
                    "last_name": "Bond",
                    "full_name": "James Bond"
                },
                {
                    "last_name": "Holmes",
                    "full_name": "Sherlock Holmes",
                }
            ],
            [
                {
                    "first_name": "Adam",
                    "last_name": "Smith",
                    "full_name": "Adam Smith",
                },
                {
                    "first_name": "James",
                    "last_name": "Bond",
                    "full_name": "James Bond"
                },
                {
                    "first_name": "Sherlock",
                    "last_name": "Holmes",
                    "full_name": "Sherlock Holmes",
                }
            ]
        )
    ]
)
def test_restore_names(users: list, expected_result: list) -> None:
    restore_names(users)
    assert (
        users == expected_result
    ), f"restore_names returned {users} but {expected_result} was expected"
