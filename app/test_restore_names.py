import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize("input_users, expected_users", [
    (
        [  # first_name empty
            {"last_name": "White", "full_name": "Alice White"},
            {"last_name": "Brown", "full_name": "Chris Brown"},
        ],
        [
            {"first_name": "Alice", "last_name": "White", "full_name": "Alice White"},
            {"first_name": "Chris", "last_name": "Brown", "full_name": "Chris Brown"},
        ]
    ),
])
def test_restore_only_missing_names(input_users, expected_users):
    restore_names(input_users)
    assert input_users == expected_users, "Tests should check function with users whose first_name is missing"


@pytest.mark.parametrize("input_users, expected_users", [
    (
        [  # first_name = None
            {"first_name": None, "last_name": "Green", "full_name": "Lana Green"},
            {"first_name": None, "last_name": "Black", "full_name": "Derek Black"},
        ],
        [
            {"first_name": "Lana", "last_name": "Green", "full_name": "Lana Green"},
            {"first_name": "Derek", "last_name": "Black", "full_name": "Derek Black"},
        ]
    ),
])
def test_restore_only_none_names(input_users, expected_users):
    restore_names(input_users)
    assert input_users == expected_users, "Tests should check function with users whose first_name is equal to None"
