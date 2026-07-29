import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        # Case 1: first_name is None
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
        ),
        # Case 2: first_name key is missing entirely
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
        ),
        # Case 3: first_name already exists (should not be changed)
        (
            [
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor",
                }
            ],
            [
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor",
                }
            ],
        ),
        # Case 4: Multiple users mixed together
        (
            [
                {"first_name": None, "full_name": "Alice Smith"},
                {"full_name": "Bob Jones"},
            ],
            [
                {"first_name": "Alice", "full_name": "Alice Smith"},
                {"first_name": "Bob", "full_name": "Bob Jones"},
            ],
        ),
    ],
)
def test_restore_names(users: list, expected_users: list) -> None:
    # Act: The function modifies the list in-place
    restore_names(users)

    # Assert: Verify the modified list matches our expectations
    assert users == expected_users
