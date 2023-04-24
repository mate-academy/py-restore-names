import pytest
from app.restore_names import restore_names


def test_should_check_function_with_users_first_name_equal_to_None():
    users = [
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
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_check_function_with_users_whose_first_name_is_missing():
    users = [
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
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
