import pytest
from app.restore_names import restore_names


test_cases = [

    (
        [
            {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
            {"last_name": "Adams", "full_name": "Mike Adams"},
            {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        ],
        [
            {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
            {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
            {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        ]
    ),

    (
        [
            {"full_name": "Robert Downey"},
        ],
        [
            {"full_name": "Robert Downey", "first_name": "Robert"},
        ]
    ),

    (
        [
            {"first_name": None, "full_name": "Chris Evans"},
        ],
        [
            {"first_name": "Chris", "full_name": "Chris Evans"},
        ]
    ),

    (
        [],
        []
    ),

    (
        [
            {"first_name": None, "full_name": "Mary Jane Watson"},
        ],
        [
            {"first_name": "Mary", "full_name": "Mary Jane Watson"},
        ]
    ),
]


@pytest.mark.parametrize("input_users, expected_users", test_cases)
def test_restore_names_modifies_in_place(input_users, expected_users):
    restore_names(input_users)
    assert input_users == expected_users
