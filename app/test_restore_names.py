import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize(
    "list_users, expected_result",
    [
        (
            [{"first_name": None, "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "full_name": "Jack Holy"}]
        ),
        (
            [{"full_name": "Mike Adams"}],
            [{"first_name": "Mike", "full_name": "Mike Adams"}]
        )
    ]
)
def test_restore_names(
        list_users: List[Dict[str, str]],
        expected_result: List[Dict[str, str]]
) -> None:
    # Make a copy of the input list for testing
    users_copy = [user.copy() for user in list_users]

    # Call the function that modifies the list in place
    restore_names(users_copy)

    # Check if the modified list matches the expected result
    assert users_copy == expected_result
