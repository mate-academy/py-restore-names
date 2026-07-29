import pytest
from app.restore_names import restore_names
from typing import List, Dict, Any


@pytest.fixture
def sample_users_data() -> List[Dict[str, Any]]:
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
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "",
            "last_name": "Smith",
            "full_name": "Sara Smith",
        }
    ]


def test_restoration_is_applied_correctly(sample_users_data:
                                          List[Dict[str, Any]]) -> None:

    restore_names(sample_users_data)

    expected_results = [
        {"first_name": "Jack", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "John", "last_name": "Doe",
         "full_name": "John Doe"},
        {"first_name": "", "last_name": "Smith",
         "full_name": "Sara Smith"},
    ]

    assert sample_users_data == expected_results


def test_unchanged_names_remain_unchanged() -> None:

    users = [
        {"first_name": "Existing", "last_name": "User",
         "full_name": "New Name User"},
        {"first_name": "Valid", "last_name": "One",
         "full_name": "Different Valid One"},
    ]
    original_users = users.copy()

    restore_names(users)

    assert users == original_users


def test_function_returns_nothing() -> None:

    users = []
    assert restore_names(users) is None


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([], []),
    ]
)
def test_empty_list_handling(input_list: List[Dict[str, Any]],
                             expected_output: List[Dict[str, Any]]) -> None:

    users_copy = input_list.copy()

    restore_names(users_copy)

    assert users_copy == expected_output
